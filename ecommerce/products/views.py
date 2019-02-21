# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import product
from django.shortcuts import render , HttpResponse

# Create your views here.


def home(request):
    products = product.objects.all()

    context = {
        "products": products
    }

    return render(request, 'products/home.html', context)


def search(request):
    try:
        q = request.GET.get('Keyword')
        print (q)
        #return HttpResponse(q)
        products = product.objects.filter(title__icontains=q)
        #print products
        #return HttpResponse(products)
        if products:
            context = {"products": products, "query": q}
        else:
            message = "Somethings wents wrong! please try something new"
            context = {"empty": True, 'message': message, "query": q}
        return render(request, 'products/searchresult.html', context)
    except:
        return HttpResponse("hey")


def detail(request, slug):
    #try:
        details = product.objects.get(slug=slug)
        context = {
            'details': details
        }
        return render(request, 'products/detail.html', context)
