from tkinter import Variable
from urllib import request
from django.shortcuts import render

# Create your views here.
def example_view(request):
    # my_app/templates/my_app/example.html
    return render(request,'my_app/example.html')

def variable_view(request):
    my_var={'first_name':'rAm','last_name':'Singh','some_list':[1,2,3,4],
            'some_dict':{'inside_key':'inside_value'},'user_logged_in':False
    }

    return render(request,'my_app/variable.html',context=my_var)

