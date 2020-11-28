from django.shortcuts import render
from .models import Indices
from .models import Traders
from .models import Scripts
from .models import GlobalIndices
from .models import Researches
from .models import Holdings
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
import random

def index(request):
    indcs = Indices.objects.all()
    all_users= get_user_model().objects.all()
    randu=random.randint(-25,25)
    traders=Traders.objects.all()
    current_user=request.user
    for y in indcs:
                    
                    priceafterthis = y.price + (randu* y.fact)
                    if priceafterthis > y.high:
                        newhigh = priceafterthis
                    else:
                        newhigh = y.high
                 
                    if priceafterthis > y.dayhigh:
                        newdayhigh = priceafterthis
                       
                    else:
                        newdayhigh = y.dayhigh
                        
                    
                    if priceafterthis < y.low:
                        newlow = priceafterthis
                    else:
                        newlow = y.low
                    if priceafterthis < y.daylow:
                        newdaylow = priceafterthis
                    else:
                        newdaylow = y.daylow
                    tochange = y.price + randu * y.fact
                    netchange = y.price - tochange
                    percentchange = netchange * 100 / y.price
                    indice1=Indices(id=y.id,name= y.name,price=tochange,volume = y.volume,high = newhigh,dayhigh = newdayhigh,low = newlow,daylow=newdaylow,nch=netchange,pch=percentchange,fact=y.fact)
                    indice1.save()
        
    wallet = 0
    k=1    
    for c in traders:
        
        if str(current_user) == c.name :
            wallet = c.price
           
           
        

    
    
    
        
    return render(request, 'index.html',{'all_users': all_users , 'indcs':indcs,'randu':randu,'wallet':wallet})


def scripts(request):
    scripts = Scripts.objects.all()
    all_users= get_user_model().objects.all()
    randu=random.randint(-3,3)
    traders=Traders.objects.all()
    current_user=request.user
    for y in scripts:
                    
                    priceafterthis = y.price + (randu* y.fact)
                    if priceafterthis > y.high:
                        newhigh = priceafterthis
                    else:
                        newhigh = y.high
                    print(newhigh,y.name)
                    if priceafterthis > y.dayhigh:
                        newdayhigh = priceafterthis
                       
                    else:
                        newdayhigh = y.dayhigh
                        
                    print(newdayhigh,y.name)
                    if priceafterthis < y.low:
                        newlow = priceafterthis
                    else:
                        newlow = y.low
                    if priceafterthis < y.daylow:
                        newdaylow = priceafterthis
                    else:
                        newdaylow = y.daylow
                    
                    tochange = y.price + randu * y.fact
                    netchange = y.price - tochange
                    percentchange = (netchange * 100 / y.price)
                    print(percentchange)
                    indice1=Scripts(id=y.id,name= y.name,price=tochange,volume = y.volume,high = newhigh,dayhigh = newdayhigh,low = newlow,daylow=newdaylow,nch=netchange,pch=percentchange,fact=y.fact)
                    indice1.save()
    wallet = 0
    k=1    
    for c in traders:
        
        if str(current_user) == c.name :
            wallet = c.price
           
           
    return render(request,'scripts.html',{'scripts':scripts})

    #return render(request,"index.html",{'indcs': indcs })


def globalindices(request):
    indcs = GlobalIndices.objects.all()
    all_users= get_user_model().objects.all()
    randu=random.randint(-10,10)
    traders=Traders.objects.all()
    current_user=request.user
    for y in indcs:
                    
                    priceafterthis = y.price + (randu* y.fact)
                    if priceafterthis > y.high:
                        newhigh = priceafterthis
                    else:
                        newhigh = y.high
                    
                    if priceafterthis > y.dayhigh:
                        newdayhigh = priceafterthis
                       
                    else:
                        newdayhigh = y.dayhigh
                        
                  
                    if priceafterthis < y.low:
                        newlow = priceafterthis
                    else:
                        newlow = y.low
                    if priceafterthis < y.daylow:
                        newdaylow = priceafterthis
                    else:
                        newdaylow = y.daylow
                    tochange = y.price + randu * y.fact
                    netchange = (y.price - tochange)

                    percentchange = (netchange * 100 / y.price)
                    print(percentchange)
                    
                    indice1=GlobalIndices(id=y.id,name= y.name,price=tochange,volume = y.volume,high = newhigh,dayhigh = newdayhigh,low = newlow,daylow=newdaylow,nch=netchange,pch=percentchange,fact=y.fact)
                    indice1.save()
    
    
        
        
    wallet = 0
    k=1    
    for c in traders:
        
        if str(current_user) == c.name :
            wallet = c.price   
    return render(request, 'globalindices.html',{'all_users': all_users , 'indcs':indcs,'randu':randu,'wallet':wallet})

def research(request):
    res = Researches.objects.all()

    return render(request,'research.html',{'res':res})
def contact(request):

    return render(request,'contact.html')
def app(request):
    
    return render(request,'app.html')
def profile(request):
    current_user=str(request.user)
    
    for x in User.objects.all():
        if current_user == x.username:
            username = x.username
            first_name = x.first_name
            email = x.email
            print(email)
            last_name = x.last_name



    return render(request,'profile.html',{'username':username,'first_name':first_name,'email': email,'last_name':last_name})

def holdings(request):
    current_user = str(request.user)
    traders = Traders.objects.all()
    hold=Holdings.objects.all()
    indc = Indices.objects.all()
    scripts = Scripts.objects.all()
    lst=[]
    a=0
    for y in traders:
        print(current_user,y.name)
        
        
        if y.name == current_user:
            print(y.name)
            print(y.id)
            a = y
    
    for x in  hold:
        b=1
        c=1

        for ind in indc:
            if ind.name == x.hold1:
                b = ind.price 
        for scr in scripts:
            if scr.name == x.hold1:
                c = scr.price


        if a == x.holder:
            total= x.quantity * b *c
            tup1=(x.hold1,x.quantity,total)
            

            lst.append(tup1) 

    
            
            
    
    return render(request,'holdings.html',{'lst':lst})
   