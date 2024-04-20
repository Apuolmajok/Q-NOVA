from django.shortcuts import render, redirect
from .models import Product, Category, Profile, Product_feature, Order, OrderItem, NewArrival, Trending, TopRated, BestSells, Testimonials, Blog, Blogcategory, Cta,  Produk, Customer, Vendor
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm, UpdateUserForm, ChangePasswordForm, UserInfoForm, VendorSignUpForm, ProductForm
from django import forms
from django.db.models import Q
from django.http import JsonResponse, HttpResponse
import json
from django.contrib.auth.decorators import login_required


# Create your views here.



# def add_product(request):
#     if request.method == 'POST':
#         form1 = ProductForm(request.POST, request.FILES)
#         if form1.is_valid():
#             form1.save()
#             return redirect('successfully added')  # Redirect to a new URL or show success message
#     else:
#         form1 = ProductForm()
#     return render(request, 'Dashboard.html', {'form1': form1})








@login_required
def vendorsignup(request):
        if request.method == 'POST':
            form2 = VendorSignUpForm(request.POST)
            if form2.is_valid():
                  form2.save()
                  vendor = Vendor.objects.filter(username=form2.cleaned_data.get("username")).first()
                  vendor.password = request.user.password
                  vendor.user = request.user
                  vendor.save()
                  messages.success(request, "Vendor registered successfully!")
                  return redirect('dashboard')  # Redirect to vendor dashboard or another appropriate page
        else:
          form2 = VendorSignUpForm()
        return render(request, 'vendorsignup.html', {'form2': form2})



def vendorlogin(request):
   if request.method == "POST":
               username=request.POST['username']
               password=request.POST['password']
               vendor = authenticate(request, username=username, password=password)
               if vendor is not None:
                      login(request, vendor)
                      messages.success(request,("You Have Been Logged In Successfully!!"))
                      return redirect('Home')
               else:
                      messages.success(request,("Incorrect password or username, please try again"))
                      return redirect('vendorlogin')
                      
   else:
       return render(request, 'vendorlogin.html',{})
      













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







# def update_info(request):
#       if request.user.is_authenticated:
#             current_user=Profile.objects.get(user__id=request.user.id)
#             form=UserInfoForm(request.POST or None, instance=current_user)

#             if form.is_valid():
#                   form.save
#                   messages.success(request, "Your Info Has Been Updated!!")
#                   return redirect('Home')
#             return render(request, "update_info.html", {'form':form})
#       else:
#             messages.success(request, "You must be logged In to Access this page!!")
#             return redirect('Home')


@login_required
def update_info(request):
    try:
        current_user = Profile.objects.get(user__id=request.user.id)
        form = UserInfoForm(request.POST or None, instance=current_user)
    except Profile.DoesNotExist:
        # If no profile exists, redirect to create a new profile or handle differently
        messages.error(request, "No profile found. Please create your profile.")
        return redirect('update_info')  # Assume 'create_profile' is a view that handles profile creation

    if request.method == 'POST':
        if form.is_valid():
            form.save()  # Make sure to call the method with ()
            messages.success(request, "Your Info Has Been Updated!!")
            return redirect('Home')

    # Display the form for GET requests or if form is not valid
    return render(request, "update_info.html", {'form': form})















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
     


def category(request, category_name):
      #Replace hyphens with Spaces instead
      category_name=category_name.replace('-', ' ')
      #Grabbing the category from the url
      try:
          #Look up the Category 
      #     category=Category.objects.get(name=category_name)
          category = Category.objects.get(name__iexact=category_name)
          products=Product.objects.filter(category=category)
          return render(request, 'category.html', {'products':products, 'category':category})
            
      except:
             messages.error(request, ("That Category Doesn't Exist as per now"))
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
      blogs = Blog.objects.all()
      return render(request, 'blog.html', {'blogs': blogs})

def blog(request):
      blogs = Blog.objects.all()
      return render(request, 'home.html', {'blogs': blogs})






def Home(request):
    if request.user.is_authenticated:
      #   if hasattr(request.user, 'customer'):
            customer = request.user.customer
            order, created = Order.objects.get_or_create(customer=customer, status=False)
            items = order.orderitem_set.all()
            cartItems = order.get_cart_items
            
      #   else:
      #         return redirect('Home')

      # # Check if the user has an associated customer
      #         try:
      #             customer = request.user.customer
      #         except User.customer.RelatedObjectDoesNotExist:
      #             # Here, handle the case where the customer does not exist.
      #             # For example, redirect to a profile creation page or return an error message.
      #             # return HttpResponse("You do not have a customer profile associated. Please create one.", status=404)
      # #             return redirect('login') 

      #       order, created = Order.objects.get_or_create(customer=customer, status=False)
      #       items = order.orderitem_set.all()
      #       cartItems = order.get_cart_items


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
        produks = Produk.objects.all()
        return render(request, 'business.html',{'produks': produks,})

def vendorprof(request):
        return render(request, 'vendorprof.html',{})

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
        if hasattr(request.user, 'customer'):
            customer = request.user.customer
            order, created = Order.objects.get_or_create(customer=customer, status=False)
            items = order.orderitem_set.all()
            cartItems = order.get_cart_items
        else:
        # Handle scenario where customer does not exist
        # Perhaps redirect to a profile completion page
           return redirect('update_info')
        
         

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
                      first_name=form.cleaned_data['first_name']
                      last_name=form.cleaned_data['last_name']
                      #login user
                      user=authenticate(username=username, password=password)
                      
                      login(request, user)
                      Customer.objects.create(user=request.user, first_name=first_name, last_name=last_name, password=password)

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
      # produkId=data['produkId']
      action=data['action']

      print('Action:', action)
      print('ProductId:', productId)
      # print('ProdukId:', produkId)


      customer=request.user.customer
      product=Product.objects.get(id=productId)
      # produk=Produk.objects.get(id=produkId)
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
      



def dashboard(request):
      vendor = Vendor.objects.filter(user=request.user).first()
      orders = Order.objects.filter(product__vendor=vendor).count()
      if request.method == 'POST':
            form1 = ProductForm(request.POST, request.FILES)
            if form1.is_valid():
                  form1.save()
                  return redirect('business')  # Redirect to a new URL or show success message
      else:
            form1 = ProductForm()
      return render(request, 'Dashboard.html', {'form1': form1, 'vendor':vendor, "orders": orders})





def produk(request,pk):
      produk = Produk.objects.get(id=pk)
      produk = Produk.objects.all()
      return render(request, 'bproduks.html',{'produk':produk})



def create_user_and_customer(username, password):
    user = User.objects.create_user(username=username, password=password)
    customer = Customer.objects.create(user=user)
    # Set up any additional customer-specific settings
    return user