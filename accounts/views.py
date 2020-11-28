from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from price.models import Indices
from price.models import Traders
from price.models import Holdings
from price.models import Scripts

from django.contrib.auth import get_user_model
# Create your views here.
def login(request):
    
    if request.method == "POST":
        username = request.POST['username'] 
        password = request.POST['password']


        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            all_users= get_user_model().objects.all()
            indcs = Indices.objects.all()
            

            for x in all_users:
                if x.username == username:
                    for y in Traders.objects.all():
                        if y.name == x.username:
                            wallet = y.price 
                            logger=y.name
                            
                    


                   
                            
                            return redirect ('/')
            return redirect ('/')
        else:
             messages.info(request,'Username invalid')
             
             return redirect('login')

    else:
        return render(request,'login.html')

def register(request):
    
    if request.method =='POST':
        first_name = request.POST.get('first_name',False)
        last_name = request.POST.get('last_name')     
        username = request.POST.get('username')    
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        if(User.objects.filter(username=username).exists()):

            messages.info(request,'Username Taken')
            return redirect('register')

            print("username taken")

        else:
            trader1=Traders(name=username, price=5000)
            trader1.save()
            user = User.objects.create_user(username=username,password=password1,email=email,first_name=first_name,last_name=last_name)
            user.save();
            
           
            print('user resgistered')
            
            

    
            
            return redirect('/')
    else:
        return render(request,'register.html')
def trade(request):
    
    
    if request.method =='POST':
        quantity = int(request.POST.get('quantity')) 
        script = request.POST.get('wanted')
        oper= request.POST.get('oper')
        
        current_user=request.user
        
        
        traders = Traders.objects.all()
        incs=Indices.objects.all()
        hold=Holdings.objects.all()
        j=1
        for y in incs:
            if script == y.name :
                if oper=="buy":
                    priceafterthis = y.price + quantity*0.1
                    if priceafterthis > y.high:
                        newhigh = priceafterthis
                    else:
                        newhigh = y.high
                    if priceafterthis > y.dayhigh:
                        newdayhigh = priceafterthis
                    else:
                        newdayhigh = y.high
                    if priceafterthis < y.low:
                        newlow = priceafterthis
                    else:
                        newlow = y.low
                    if priceafterthis < y.daylow:
                        newdaylow = priceafterthis
                    else:
                        newdaylow = y.low
                    netchange = y.price - priceafterthis
                    percentchange = netchange * 0.1
                    indice1=Indices(id=j,name= y.name,price=priceafterthis,volume = y.volume-quantity,high = newhigh,dayhigh = newdayhigh,low = newlow,daylow=newdaylow,nch=netchange,pch=percentchange,fact=y.fact)
                    indice1.save()
                   # print('changed indice')    
                

                        
                else: 
                        priceafterthis = y.price - quantity*0.1
                        if priceafterthis > y.high:
                            newhigh = priceafterthis
                        else:
                            newhigh = y.high
                        if priceafterthis > y.dayhigh:
                            newdayhigh = priceafterthis
                        else:
                            newdayhigh = y.high
                        if priceafterthis < y.low:
                                newlow = priceafterthis
                        else:
                            newlow = y.low
                        if priceafterthis < y.daylow:
                            newdaylow = priceafterthis
                        else:
                            newdaylow = y.low
                        netchange = y.price - priceafterthis
                        percentchange = netchange/100
                        indice1=Indices(id=j,name= y.name,price=priceafterthis,volume = y.volume+quantity,high = newhigh,dayhigh = newdayhigh,low = newlow,daylow=newdaylow,nch=netchange,pch=percentchange,fact=y.fact)
                        indice1.save()
            
                         
                    
                   

                i=2
                for x in traders:
                           
                        
                        if x.name == str(current_user):


                            if oper=="buy":
                            
                                    trader1=Traders(id=i,name=x.name ,price = (x.price - y.price*quantity))
                                    trader1.save()
                            else:
                                
                                    trader1=Traders(id=i,name=x.name ,price = (x.price + y.price*quantity))
                                    trader1.save()
                            k=1
                            button=0
                            for z in hold:
                                print("holding id",z.id)
                                
                                if z.holder == x and z.hold1 == y.name:
                                    print(z.holder)
                                    if oper== "sell":
                                        quantity =( -1 * quantity)
                                     #   print(quantity)
                                    
                                    holder1 = Holdings(id=k,holder=x,hold1=y.name,quantity=z.quantity+quantity)
                                    holder1.save()
                                    button=1

                                k=k+1
                                
                            if button != 1:
                                if oper=="sell":
                                        quantity =  quantity

                                print(button)
                                Holdings.objects.create(holder=x,hold1=y.name,quantity=quantity)
                                



                            
                            i=i+1
            j=j+1

                    
                    
                
                
           
                
                    


                    
        return redirect('/')


    else :
        return render(request,'trade.html')

def scripttrade(request):
    
    if request.method =='POST':
        quantity = int(request.POST.get('quantity')) 
        script = str(request.POST.get('wanted'))
        oper= request.POST.get('oper')
        current_user=str(request.user)
        traders = Traders.objects.all()
        scr=Scripts.objects.all()
        hold=Holdings.objects.all()
        j=1        
        for y in scr:
            print(j)  
                
            if script == y.name :
                    print(j, "is matched" )
                    
                    if oper=="buy":
                        priceafterthis = y.price + quantity*0.1
                        if priceafterthis > y.high:
                            newhigh = priceafterthis
                        else:
                            newhigh = y.high
                        if priceafterthis > y.dayhigh:
                            newdayhigh = priceafterthis
                        else:
                            newdayhigh = y.high
                        if priceafterthis < y.low:
                            newlow = priceafterthis
                        else:
                            newlow = y.low
                        if priceafterthis < y.daylow:
                            newdaylow = priceafterthis
                        else:
                            newdaylow = y.low
                        netchange = y.price - priceafterthis
                        percentchange = netchange * 0.1
                        script1=Scripts(id=j,name= y.name,price=priceafterthis,volume = y.volume-quantity,high = newhigh,dayhigh = newdayhigh,low = newlow,daylow=newdaylow,nch=netchange,pch=percentchange,fact=y.fact)
                        script1.save()
                        print('changed script')    

                        
                    else: 
                        priceafterthis = y.price - quantity*0.1
                        if priceafterthis > y.high:
                            newhigh = priceafterthis
                        else:
                            newhigh = y.high
                        if priceafterthis > y.dayhigh:
                            newdayhigh = priceafterthis
                        else:
                            newdayhigh = y.high
                        if priceafterthis < y.low:
                                newlow = priceafterthis
                        else:
                            newlow = y.low
                        if priceafterthis < y.daylow:
                            newdaylow = priceafterthis
                        else:
                            newdaylow = y.low
                        netchange = y.price - priceafterthis
                        percentchange = netchange/100
                        script1=Scripts(id=j,name= y.name,price=priceafterthis,volume = y.volume+quantity,high = newhigh,dayhigh = newdayhigh,low = newlow,daylow=newdaylow,nch=netchange,pch=percentchange,fact=y.fact)
                        script1.save()
                         
                    
                            

                    i=2
                    for x in traders:
                        
                        if x.name == str(current_user):
                            


                            if oper=="buy":
                            
                                trader1=Traders(id=i,name=x.name ,price = (x.price - y.price*quantity))
                                trader1.save()
                            else:
                                
                                trader1=Traders(id=i,name=x.name ,price = (x.price + y.price*quantity))
                                trader1.save()
                            k=1
                            button=0
                            for z in hold:
                                
                                
                                if z.holder == x and z.hold1 == y.name:
                                    print(z.holder,"is holding previusly ",y.name)
                                    if oper== "sell":
                                        quantity =( -1 * quantity)
                                        print(quantity)
                                    
                                    holder1 = Holdings(id=k,holder=x,hold1=y.name,quantity=z.quantity+quantity)
                                    holder1.save()
                                    button=1
                                k=k+1
                                
                            if button != 1:
                                if oper=="sell":
                                        quantity =  quantity

                                print("creating a new ",y.name)
                                Holdings.objects.create(holder=x,hold1=y.name,quantity=quantity)
                                


                            print('changed trader')
                        i=i+1
                
                    
                    print('gotit')
            j=j+1
                
           
                
                    


                    
        return redirect('scripts')


    else :
        return render(request,'trade.html')



