from django.shortcuts import render
from abc import ABC, abstractmethod

# Create your views here.


''' ProductDisplay class is an abstract class which is inherited inorder to display the products.
every product must implement view function of this class inorder to get displayed in the html view'''


class ProductDisplay(ABC):# polymorphism

    def __init__(self,cards_per_row,display_file):
        self.cards_per_row  =cards_per_row
        self.display_file  = display_file

    @abstractmethod
    def view(self):
        pass

def home(request):
    return render(request,'home.html') #returns home page