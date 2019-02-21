# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from products.models import product
from cart.models import carttotal, cartitem
from django.shortcuts import render, HttpResponseRedirect, reverse, HttpResponse

# Create your views here.
def view(request):
        print ("view")
        try:
            the_id = request.session['cart_id']
        except:
            the_id = None
            print ("hey1222")
            print (the_id)
            products = product.objects.all()
            message = "Please do shoping, you have nothing in your cart"
            context = {"empty": True, "message": message, "products": products}
            return render(request, 'carts/view.html', context)

        if the_id:
            print ("hey2")
            products = product.objects.all()
            cart = carttotal.objects.get(id=the_id)
            context = {"cart":cart, "products": products}    
        else:
            print ("hey3")
            products = product.objects.all()
            message = "Please do shoping, you have nothing in your cart"
            context = {"empty": True, "message": message, "products": products}
        #template = "cart/view.html"
        return render(request, 'carts/view.html', context) 
    



def cart_update(request, slug):
    #return HttpResponse(slug)
    request.session.set_expiry(300)
    print ("hey")
    
    try:
        qty = request.GET.get('carth')
        print (qty)
        if qty is not None: 
            update_qty = True
            print ("hey u r in try block")
            print (qty)
        else:
            qty = None
            update_qty = False
            print ("none hai")
    except:
        print ("hey none")

    try:
        the_id = request.session['cart_id']
    except:
        print ("going for carttotal")
        ID = carttotal()
        print (ID)
        print ('hey')
        ID.save()
        print (ID)
        request.session['cart_id'] = ID.id
        print ("rS is")
        print (request.session['cart_id'])
        print ("upr hai")
        the_id = ID.id
        print (the_id)
        #itemm = carttotal()
        #itemm.save()
        #print item
        #request.session['cart_Id'] = new_item.id
        #the_id = new_item.id
        #print the_id

    cart = carttotal.objects.get(id=the_id)
    print (cart)
    #return render(request, 'cart/result.html', context)
    #print "hello"
    #context = {"cart":cart }
    try:
        prod = product.objects.get(slug=slug)
        print (prod)

        price = prod.product_price_set.all()
        
        for i in price:
            product_price = i.price

        print ("price:")
        print (product_price)
        #return HttpResponse(products)
    except:
        pass


    aa = cartitem.objects.all()
    print (aa)



    cart_item, created = cartitem.objects.get_or_create(Cart=cart, product=prod)
    print (cart_item)

#    if not cart_item in cart.item.all():
#        cart.item.add(cart_item)
#    else:
#          cart.item.remove(cart_item)    

    if update_qty and qty:
        if int(qty) == 0:
            cart_item.delete()
        else:
            cart_item.quantity = qty
            cart_item.price = product_price
            cart_item.save()
    else:
        pass
        
    #item_sub_price = item.product.price
  
    new_item = 0.00
    for item in cart.cartitem_set.all():
        print (item.price)
        totalitem = float(item.price) * item.quantity
        new_item += totalitem
        print (new_item)

    request.session['item_total'] = cart.cartitem_set.count()
    #print cart.products.count()
    cart.Total = new_item
    cart.save()    

    print ("the_id is: ")
    print (the_id)
    #return HttpResponseRedirect(reverse("home")) 

    return HttpResponseRedirect(reverse("view"))


'''
    if not prod in cart.products.all():
        cart.products.add(prod)
    else:
        cart.products.remove(prod)  
'''