from django.shortcuts import render
from .models import Mobile
from home.views import ProductDisplay
from django.contrib.auth.decorators import login_required
from django.core.files import File

from django.http import HttpResponse


class MobileDisplay(ProductDisplay): ##inheritance

    def __init__(self,cards_per_row,brand,display_file):   ##overloading
        ProductDisplay.__init__(self,cards_per_row,display_file)
        self.brand  = brand

    def view(self): #overriding
        num = self.cards_per_row
        data = Mobile.objects.filter(product_brand=self.brand )  # fetch data from database
        n = (len(data) // (num)) + 1  # no. of rows
        print(data)
        temp = data
        send_list = []

        ##to divide the products into groups/rows
        while temp:
         send_list.append(temp[0:num])
         print(temp[0:num])
         if len(temp) >= num:
             temp = temp[num:]
         else:
             temp = ''
        print(send_list)

        para = { 'data': send_list}  # no. of rows
        return para,self.display_file


def mobile(request):

    n_data=Mobile.objects.filter(product_brand='Nokia')
    a_data=Mobile.objects.filter(product_brand='Apple')
    s_data=Mobile.objects.filter(product_brand='Samsung')
    para={'ndata':n_data,'adata':a_data,'sdata':s_data,'range':range(6),}
    return  render(request,"mobile.html",para)

@login_required
def Samsung(request):
    samsung=MobileDisplay(6,'Samsung','Samsung.html')
    parameters,d_file= samsung.view()
    return render(request,d_file,parameters)

@login_required
def Nokia(request):
    nokia=MobileDisplay(6,'Nokia','Nokia.html')
    parameters,d_file= nokia.view()
    return render(request,d_file,parameters)

@login_required
def Apple(request):
    apple=MobileDisplay(6,'Apple','Apple.html')
    parameters,d_file= apple.view()
    return render(request,d_file,parameters)

