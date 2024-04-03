from django.shortcuts import render, redirect
from .models import Product, Category, Profile, Product_feature, Order, OrderItem, NewArrival, Trending, TopRated, BestSells, Testimonials, Blog, Blogcategory, Cta
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm, UpdateUserForm, ChangePasswordForm, UserInfoForm
from django import forms
from django.db.models import Q
from django.http import JsonResponse
import json


# Create your views here.

#Seach  

def search(request):
#Determine if they filled out the form
      if request.method=='POST':
            searched=request.POST['searched']
            #Querry the products db model
            searched=Product.objects.filter(Q(name__icontains=searched) | Q(description__icontains=searched) |Q(price__icontains=searched))
            #Test for Null
            if not searched:
                  messages.success(request, "The product doesn't exist")
                  return render(request, "search.html", {})
            else:
                  return render(request, "search.html", {'searched':searched})
      else:
            return render(request, "search.html", {})







def update_info(request):
      if request.user.is_authenticated:
            current_user=Profile.objects.get(user__id=request.user.id)
            form=UserInfoForm(request.POST or None, instance=current_user)

            if form.is_valid():
                  form.save
                  messages.success(request, "Your Info Has Been Updated!!")
                  return redirect('Home')
            return render(request, "update_info.html", {'form':form})
      else:
            messages.success(request, "You must be logged In to Access this page!!")
            return redirect('Home')







def update_password(request):
       if request.user.is_authenticated:
            current_user=request.user
            #Did the user fill out the form
            if request.method=="POST":
                  form=ChangePasswordForm(current_user, request.POST)
                  #is the form valid
                  if form.is_valid():
                        form.save()
                        messages.success(request, "Your Password has been updated!!... ")
                        login(request,current_user)
                        return redirect('update_user')
                  else:
                        for error in list(form.errors.values()):
                              messages.error(request, error)
                              return redirect('update_password')
                                    
            else:
                  form=ChangePasswordForm(current_user)
                  return render(request, "update_password.html", {'form':form})
       else:
             messages.success(request, "You must be logged In to use this form")
             return redirect('Home')
             




def update_user(request):
      if request.user.is_authenticated:
            current_user=User.objects.get(id=request.user.id)
            user_form=UpdateUserForm(request.POST or None, instance=current_user)

            if user_form.is_valid():
                  user_form.save
                  login(request, current_user)
                  messages.success(request, "User Has Been Updated!!")
                  return redirect('Home')
            return render(request, "update_user.html", {'user_form':user_form})
      else:
            messages.success(request, "You must be logged In to Access this page!!")
            return redirect('Home')
     


def category(request,foo):
      #Replace hyphens with Spaces instead
      foo=foo.replace('-', ' ')
      #Grabbing the category from the url
      try:
          #Look up the Category 
          category=Category.objects.get(name=foo)
          products=Product.objects.filter(category=category)
          return render(request, 'category.html', {'products':products, 'category':category})
            
      except:
             messages.success(request, ("That Category Doesn't Exist as per now"))
             return redirect('Home')
            
      
def product(request,pk):
      product = Product.objects.get(id=pk)
      product = Product.objects.all()
      return render(request, 'product.html',{'product':product})

def product_feature(request):
      # product_feature = Product_feature.objects.get(id=pk)
      product_features = Product_feature.objects.all()
      return render(request, 'home.html', {'product_features': product_features})


def newarrival(request):
      # product_feature = Product_feature.objects.get(id=pk)
      newarrivals = NewArrival.objects.all()
      return render(request, 'home.html', {'newarrivals': newarrivals})


def trending(request):
      trendings = Trending.objects.all()
      return render(request, 'home.html', {'trendings': trendings})


def toprated(request):
      toprateds = TopRated.objects.all()
      return render(request, 'home.html', {'toprateds': toprateds})

def bestsells(request):
      bestsells = BestSells.objects.all()
      return render(request, 'home.html', {'bestsells': bestsells})

def testimonials(request):
      testimonials = Testimonials.objects.all()
      return render(request, 'home.html', {'testimonials': testimonials})


def cta(request):
      cta = Cta.objects.all()
      return render(request, 'home.html', {'cta': cta})

def blog(request):
      blog = Blog.objects.all()
      return render(request, 'home.html', {'blog': blog})






def Home(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, status=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0, 'shipping':False}
        cartItems = order['get_cart_items']

    products = Product.objects.all()
    product_features = Product_feature.objects.all()
    newarrivals = NewArrival.objects.all()
    trendings = Trending.objects.all()
    toprateds = TopRated.objects.all()
    bestsells = BestSells.objects.all()
    testimonials = Testimonials.objects.all()
    cta = Cta.objects.all()
    blog = Blog.objects.all()
    return render(request, 'Home.html', {'products': products,'blog': blog, 'testimonials': testimonials, 'toprateds': toprateds,'bestsells': bestsells, 'product_features': product_features, 'trendings': trendings, 'newarrivals': newarrivals, 'cta': cta, 'cartItems': cartItems})


def about(request):
        return render(request, 'about.html',{})

def zzTandC(request):
        return render(request, 'zzTandC.html',{})

def business(request):
        return render(request, 'business.html',{})

def login_user(request):
        if request.method == "POST":
               username=request.POST['username']
               password=request.POST['password']
               user = authenticate(request, username=username, password=password)
               if user is not None:
                      login(request, user)
                      messages.success(request,("You Have Been Logged In Successfully!!"))
                      return redirect('Home')
               else:
                      messages.success(request,("Incorrect password or username, please try again"))
                      return redirect('login')
                      
        else:
            return render(request, 'login.html',{})

def logout_user(request):
       logout(request)
       messages.success(request, ("You have been logged out successfully!"))
       return redirect('Home')

def register_user(request):
      if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, status=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items

        
         

      else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0, 'shipping':False}
        cartItems = order['get_cart_items']

        form=SignUpForm()
        if request.method=="POST":
               form=SignUpForm(request.POST)
               if form.is_valid():
                      form.save()
                      username=form.cleaned_data['username']
                      password=form.cleaned_data['password1']
                      #login user
                      user=authenticate(username=username, password=password)
                      
                      login(request, user)
                      messages.success(request, ("User created successfully, Please fill out Your User info below!!"))
                      return redirect('update_info')
                   
               else:
                   messages.success(request, ("Oops! Registration unsuccessful, please try again"))
                   return redirect('register')
        else:
            return render(request, 'register.html',{'form':form, 'cartItems':cartItems})


#cart
        
def cart(request):
      if request.user.is_authenticated:
        customer=request.user.customer
        order, created=Order.objects.get_or_create(customer=customer, status=False)
        items=order.orderitem_set.all()
        cartItems = order.get_cart_items
      else:
        items=[]
        order={'get_cart_total':0, 'get_cart_items':0, 'shipping':False}
        cartItems = order['get_cart_items']

      return render(request, 'cart.html',{'items':items, 'order':order, 'cartItems': cartItems})


#checkout
def checkout(request):
      if request.user.is_authenticated:
        customer=request.user.customer
        order, created=Order.objects.get_or_create(customer=customer, status=False)
        items=order.orderitem_set.all()
        cartItems = order.get_cart_items
      else:
        items=[]
        order={'get_cart_total':0, 'get_cart_items':0, 'shipping':False}
        cartItems = order['get_cart_items']

      return render(request, 'checkout.html',{'items':items, 'order':order, 'cartItems': cartItems})

def updateItem(request):
      data=json.loads(request.body)
      productId=data['productId']
      action=data['action']

      print('Action:', action)
      print('ProductId:', productId)


      customer=request.user.customer
      product=Product.objects.get(id=productId)
      order, created=Order.objects.get_or_create(customer=customer, status=False)

      orderItem, created=OrderItem.objects.get_or_create(order=order, product=product)

      if action=='add':
            orderItem.quantity=(orderItem.quantity + 1)
      elif action=='remove':
            orderItem.quantity=(orderItem.quantity - 1)

      orderItem.save()


      if orderItem.quantity <= 0:
            orderItem.delete()

      

      return JsonResponse('Item was added', safe=False)














def blogcategory(request,foo):
      #Replace hyphens with Spaces instead
      foo=foo.replace('-', ' ')
      #Grabbing the category from the url
      try:
          #Look up the Category 
          blogcategory=Blogcategory.objects.get(name=foo)
          blogs=Blog.objects.filter(blogcategory=blogcategory)
          return render(request, 'blogcategory.html', {'blogs':blogs, 'blogcategory':blogcategory})
            
      except:
             messages.success(request, ("That Blog Category Doesn't Exist"))
             return redirect('Home')