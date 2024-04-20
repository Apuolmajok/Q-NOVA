from django.contrib import admin
from .models import Category, Customer, Product, Order, banner, Profile, ShippingAddress, OrderItem, Product_feature, NewArrival,Trending,TopRated,BestSells,Testimonials,Blog,Blogcategory, Cta, Produk
from django.contrib.auth.models import User

# Register your models here.
admin.site.register(Category)
admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Product_feature)
admin.site.register(Order)
admin.site.register(banner)
admin.site.register(Profile)
admin.site.register(ShippingAddress)
admin.site.register(OrderItem)
admin.site.register(NewArrival)
admin.site.register(Trending)
admin.site.register(TopRated)
admin.site.register(BestSells)
admin.site.register(Testimonials)
admin.site.register(Blog)
admin.site.register(Cta)
admin.site.register(Blogcategory)
admin.site.register(Produk)


#mix profile info and user info 
class ProfileInline(admin.StackedInline):
    model=Profile

class UserAdmin(admin.ModelAdmin):
    model=User
    field=["username", "first_name", "last_name", "email", ]
    inlines=[ProfileInline]

#Unregister the old way
admin.site.unregister(User)

#Reregister thr new way
admin.site.register(User, UserAdmin)