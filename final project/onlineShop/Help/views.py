from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def Help(request):
    return render(request,"Help.html")

def Help_confrm(request):
    username = request.GET.get('username', '')
    dictionary={"username":username}
    return render(request, "query_confrm.html" , dictionary )
