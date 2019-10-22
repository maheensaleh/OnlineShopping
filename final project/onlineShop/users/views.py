from django.views.generic import TemplateView
from .forms import CustomerForm
from django.shortcuts import render,redirect
from .forms import PasswordMismatch, InvalidUsername, InvalidEmail, PasswordLength
from mobile.models import Mobile

# global variables:
user_data = []
purchase = False

''' this class displays the user form on html page'''
class FormDisplay(TemplateView):

    user_data = []  # global variable is restated here to refresh it each time the form is displayed
    template_name = 'users/register.html'

    # builtin method of templateView class to render form
    def get(self,request):
        form = CustomerForm()
        return render(request, self.template_name, {'form':form})

    # builtin method of TemplateView to submit form
    @staticmethod
    def post(request):
        error, ne, ee, pe, pl= False, False, False, False, False # html checks to display errors are initially false

        if request.method == 'POST':
            form = CustomerForm(request.POST) # create object of form

            if form.is_valid() and PasswordMismatch.value==False and PasswordLength.value==False  :
                form.save()
                global user_data
                user_data = [] # temp save info of new user
                user_data .append(form.cleaned_data.get('username'))
                user_data.append (form.cleaned_data.get( 'email'))

                return redirect('done/')

            else:

                error=True
                username_e, password_e, email_e,pl_e = None, None, None, None # error messages are initially none

                if InvalidUsername.value:
                    ne = True
                    username_e = InvalidUsername.message

                if PasswordMismatch.value:
                    pe = True
                    password_e = PasswordMismatch.message

                if InvalidEmail.value:
                    ee = True
                    email_e = InvalidEmail.message

                if PasswordLength.value:
                    pl = True
                    pl_e = PasswordLength.message

                form=CustomerForm()

                para={'form': form, 'username_e': username_e, 'password_e': password_e,
                      'email_e': email_e,'pl_e': pl_e, 'error': error, 'ne': ne, 'pe': pe,
                      'ee': ee,'pl': pl}

                PasswordMismatch.value,InvalidUsername.value,InvalidEmail.value, PasswordLength.value=False,False,False,False

                return render(request, 'users/register.html', para)


class NewAccount:  # content( composition )
    def __init__(self):
        global user_data
        self.info = user_data  # to save the information of new account


class ConfirmAccount:   # container ( composition )

    @staticmethod
    def ok(request):
        display = NewAccount()  # composition
        args = {'name': display.info[0], 'email': display.info[1]}
        return render(request, 'users/acc_confirm.html', args)


'''the class "cart" displays the selected items by the customer 
and calculates its bill and gives an option to purchase those items'''

class Cart:
    price_list = []
    model_list = []
    bill = 0
    data_list = []

    # to fetch the selected products and display them in cart
    def my_cart(request):
        global purchase

        #getting model and price of clicked itrm
        model = request.GET.get('model', '')
        price = request.GET.get('price', '')

        #append the model and price of selected items if it is not empty or not already present in cart
        if model!="":
            if model not in Cart.model_list:
                Cart.model_list.append(model)
                Cart.price_list.append(price)
                Cart.bill = 0

                #calculates bill
                for x in Cart.price_list:
                    Cart.bill=Cart.bill + int(x)

        #to prevent repeataion of items in cart
        Cart.data_list=[]

        #if customer has not purchased the items present in his cart then data of items is again entered in the data_list
        if purchase==False:
            for x in Cart.model_list:
                data_tmp = Mobile.objects.filter(product_model=x)  # fetch data from database
                Cart.data_list.append(data_tmp)

        # when the product is purchased i.e purchase=True, then the cart becomes empty.
        else:
            Cart.data_list = []
            Cart.model_list = []
            Cart.price_list = []
            Cart.bill = 0
            purchase = False

        # to remove a product selected by customer from his cart
        if len(Cart.model_list) != 0:
            #just to know that when and whose remove button is clicked
            remove = request.GET.get('remove', '')
            if remove == "remove":
                for x in Cart.model_list:
                    if x == request.GET.get('model', ''):
                        #gets index of the product clicked to remove and pops the item at same index from other lists as well
                        ind = Cart.model_list.index(x)
                        Cart.model_list.pop(ind)
                        Cart.price_list.pop(ind)
                        Cart.data_list.pop(ind)
                        break
                    else:
                        continue

        parameter = {"model": Cart.model_list, "price": Cart.price_list, "bill": Cart.bill, 'data': Cart.data_list}
        return render(request, "users/cart.html", parameter)


'''this class inherits a class "cart" and updates the stock after any purchase'''

class Stock(Cart):

    # updates stock after every purchase
    def update_stock(request):

        #to know when the purchase button is clicked
        extra = request.GET.get('extra', '')
        if extra == "none":

            # getting the product by its model and updating its quantity in admin stock
            for x in Cart.model_list:
                obj = Mobile.objects.get(product_model=x)
                obj.product_quantity -= 1
                obj.save()

        #refreshes the value of bill
        bill = 0

        # bill calculation
        for x in Cart.price_list:
            bill += int(x)

        #bill becomes zero if there is no item in cart
        if Cart.model_list == []:
            Cart.bill = 0

        param = {"model": Cart.model_list, "price": Cart.price_list, "bill":bill,'data':Cart.data_list}

        #if bill is zero the purchase button doesn't work
        if bill == 0:
            return render(request, "users/cart.html", param)

        elif bill != 0:
            return render(request, "users/payment.html", param)


'''this class deals with delivery of products'''

class Delivery:

    @staticmethod
    def deli(request):
        global purchase
        address = request.GET.get('address', '')
        #if the address is empty; submit button wont work
        if address != "":
            # when the products are purchased the cart will be refreshed
            purchase = True
            return render(request, "users/congrats.html")
        else:
            return render(request, "users/delivery.html")



# feedback by user
def render_feedback(request):
    return render(request, "users/feedback.html")

# content (aggregation)
class BasicFeedback:
    def feedback_check(self, a=''):
        if a=='':
            self.a = 'please enter a feedback '
            self.empty=True
        else:
            self.a=a
            self.empty=False

# container (aggregation)
class Feedback:
    def __init__(self, obj,comm):
        self.obj = obj
        self.obj.feedback_check(comm)

    def display(self):
        return self.obj.a, self.obj.empty
# calling the aggreagated classes and displaying the feedback

def feedback_display(request):
    #gets comment from user
    comment = request.GET.get('comment', '')
    obj1 = BasicFeedback()
    obj2 = Feedback(obj1,comment)
    value, chk=obj2.display()
    dictionary = {"feedback": value, "chk":chk}
    return render(request, "users/feedback_view.html", dictionary)
