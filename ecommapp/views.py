from django.shortcuts import render,redirect
from ecommapp.models import Contact,product
from django.contrib import messages
from math import ceil
from django.conf import settings
# import json

# # Create your views here.
def index(request):
    allproducts=[]
    catproducts= product.objects.values('category','id')
    cats={item['category'] for item in catproducts}
    for cat in cats:
        prods=product.objects.filter(category=cat)
        n=len(prods)
        nSlides= n // 4+ ceil((n/4) - (n//4))
        allproducts.append([prods,range(1, nSlides), nSlides])

    params= {'allproducts':allproducts}

    return render(request,"index.html",params)

def contact(request):
    if request.method=="POST":
        name=request.POST.get("name")
        email=request.POST.get("email")
        desc=request.POST.get("desc")
        pnumber=request.POST.get("pnumber")
        myquery=Contact(name=name,email=email,desc=desc,phonenumber=pnumber)
        myquery.save()
        messages.info(request,"we will get back to you")
        return render(request,"contact.html")
    
    return render(request,"contact.html")

def about(request):
    return render(request,"about.html")




   
