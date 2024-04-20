from django.db import models
import datetime
from django.contrib.auth.models import User
from django.conf import settings
from django.db.models.signals import post_save


#VENDOR 

class Vendor(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
    store_name = models.CharField(max_length=255)
    username = models.CharField(max_length=255, blank=True, unique=True)
    email = models.EmailField(max_length=255, blank=True)
    store_description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    logo=models.ImageField(upload_to='uploads/cta/')
    password=models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.store_name








#create customer profile
class Profile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    date_modified=models.DateTimeField(User, auto_now=True)
    phone=models.CharField(max_length=20, blank=True)
    address1=models.CharField(max_length=200, blank=True)
    address2=models.CharField(max_length=200, blank=True)
    city=models.CharField(max_length=200, blank=True)
    state=models.CharField(max_length=200, blank=True)
    zipcode=models.CharField(max_length=200, blank=True)
    country=models.CharField(max_length=200, blank=True)


    def __str__(self):
        return self.user.username

#create a user profile by default when users sign up
def create_profile(sender, instance, created, **kwargs):
    if created:
        user_profile=Profile(user=instance)
        user_profile.save()

#Automating the saved profile
post_save.connect(create_profile, sender=User)

  








#Categories of products
class Category(models.Model):
    name=models.CharField(max_length=50)

    def __str__(self):
        return self.name
    

    class Meta:
        verbose_name_plural = 'categories'
        
# class Category(models.Model):
#     name = models.CharField(max_length=50)
#     slug = models.SlugField(max_length=50, unique=True, blank=True)  

#     def save(self, *args, **kwargs):
#         # Automatically generate the slug from the name if it's not set
#         if not self.slug:
#             self.slug = slugify(self.name)
#         super().save(*args, **kwargs)

#     def __str__(self):
#         return self.name

#     class Meta:
#         verbose_name_plural = 'categories'
        
        
        
        
        


#Customers
class Customer(models.Model):
    user=models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    first_name=models.CharField(max_length=50, blank=True)
    last_name=models.CharField(max_length=50, blank=True)
    phone=models.CharField(max_length=10, null=True, blank=True)
    email=models.EmailField(max_length=100, null=True)
    password=models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


#All products
class Product(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE, null=True, blank=True)
    name=models.CharField(max_length=200)
    price=models.DecimalField(default=0,decimal_places=2, max_digits=16)
    Category=models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    description=models.TextField( max_length=500, default='', blank=True, null=True)
    image1=models.ImageField(upload_to='uploads/products/')
    image2=models.ImageField(upload_to='uploads/products/', blank=True, null=True)
    #Add sales
    is_sale = models.BooleanField(default=False)
    sale_price = models.DecimalField(default=0,decimal_places=2, max_digits=16)
    digital=models.BooleanField(default=False, null=True, blank=False)

    def __str__(self):
        return self.name
    
    
    
class Produk(models.Model):
    # vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE, related_name='products')
    name=models.CharField(max_length=200)
    price=models.DecimalField(default=0,decimal_places=2, max_digits=16)
    Category=models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    description=models.CharField(max_length=500, default='', blank=True, null=True)
    image1=models.ImageField(upload_to='uploads/produks/')
    image2=models.ImageField(upload_to='uploads/produks/', blank=True, null=True)
   
    #Add sales
    is_sale = models.BooleanField(default=False)
    sale_price = models.DecimalField(default=0,decimal_places=2, max_digits=16)
   
    def __str__(self):
        return self.name
    
    
    
class Product_feature(models.Model):
    name=models.CharField(max_length=200)
    price=models.DecimalField(default=0,decimal_places=2, max_digits=16)
    description=models.CharField(max_length=1000, default='', blank=True, null=True)
    image=models.ImageField(upload_to='uploads/product_features/')
    #Add sales
    is_sale = models.BooleanField(default=False)
    sale_price = models.DecimalField(default=0,decimal_places=2, max_digits=16)
    digital=models.BooleanField(default=False, null=True, blank=False)

    def __str__(self):
        return self.name

#Orders
class Order(models.Model):
    product=models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True)
    customer=models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
    quantity=models.IntegerField(default=1)
    address=models.CharField(max_length=200, default='', blank=True)
    phone=models.CharField(max_length=20, default='', blank=True)
    date_Ordered=models.DateField(default=datetime.datetime.today)
    status=models.BooleanField(default=False, null=True, blank=False)
    transaction_id=models.CharField(max_length=200,null=True)
   

    def __str__(self):
        return str(self.id)
    
    @property
    def get_cart_total(self):
        orderitems=self.orderitem_set.all()
        total=sum([item.get_total for item in orderitems])
        return total
    
    @property
    def get_cart_items(self):
        orderitems=self.orderitem_set.all()
        total=sum([item.quantity for item in orderitems])
        return total


    @property
    def shipping(self):
        shipping=False
        orderitems=self.orderitem_set.all()
        for i in orderitems:
            if i.product.digital==False:
                shipping=True

        return shipping
    
    

    
class OrderItem(models.Model):
    product=models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=True)
    order=models.ForeignKey(Order, on_delete=models.SET_NULL, null=True, blank=True)
    quantity=models.IntegerField(default=1,  null=True, blank=True)
    date_added=models.DateField(default=datetime.datetime.today)

    @property
    def get_total(self):
        total=self.product.price*self.quantity
        return total


class ShippingAddress(models.Model):
    customer=models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
    order=models.ForeignKey(Order, on_delete=models.SET_NULL, null=True, blank=True)
    address1=models.CharField(max_length=200, blank=True)
    address2=models.CharField(max_length=200, blank=True)
    city=models.CharField(max_length=200, blank=True)
    state=models.CharField(max_length=200, blank=True)
    zipcode=models.CharField(max_length=200, blank=True)
    country=models.CharField(max_length=200, blank=True)
    date_added=models.DateField(default=datetime.datetime.today)

    def __str__(self):
        return f'{self.address1} {self.address2}'




    
class banner(models.Model):
    img=models.CharField(max_length=200)
    alt_text=models.CharField(max_length=300)









class NewArrival(models.Model):
    name=models.CharField(max_length=200)
    price=models.DecimalField(default=0,decimal_places=2, max_digits=16)
    Category=models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    image=models.ImageField(upload_to='uploads/newArrivals/')
    #Add sales
    is_sale = models.BooleanField(default=False)
    sale_price = models.DecimalField(default=0,decimal_places=2, max_digits=16)

    def __str__(self):
        return self.name




class Trending(models.Model):
    name=models.CharField(max_length=200)
    price=models.DecimalField(default=0,decimal_places=2, max_digits=16)
    Category=models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    image=models.ImageField(upload_to='uploads/trendings/')
    #Add sales
    is_sale = models.BooleanField(default=False)
    sale_price = models.DecimalField(default=0,decimal_places=2, max_digits=16)

    def __str__(self):
        return self.name




class TopRated(models.Model):
    name=models.CharField(max_length=200)
    price=models.DecimalField(default=0,decimal_places=2, max_digits=16)
    Category=models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    image=models.ImageField(upload_to='uploads/topRateds/')
    #Add sales
    is_sale = models.BooleanField(default=False)
    sale_price = models.DecimalField(default=0,decimal_places=2, max_digits=16)

    def __str__(self):
        return self.name




class BestSells(models.Model):
    name=models.CharField(max_length=200)
    price=models.DecimalField(default=0,decimal_places=2, max_digits=16)
    Category=models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    image=models.ImageField(upload_to='uploads/bestSells/')
    #Add sales
    is_sale = models.BooleanField(default=False)
    sale_price = models.DecimalField(default=0,decimal_places=2, max_digits=16)

    def __str__(self):
        return self.name



class Testimonials(models.Model):
    name=models.CharField(max_length=200)
    title=models.CharField(max_length=200)
    image=models.ImageField(upload_to='uploads/testimonials/')
    description1=models.CharField(max_length=1000, default='', blank=True, null=True)
    description2=models.CharField(max_length=1000, default='', blank=True, null=True,)

    def __str__(self):
        return self.name
    

class Cta(models.Model):
    seasonname=models.CharField(max_length=200)
    startingprice=models.DecimalField(default=0,decimal_places=2, max_digits=16)
    image=models.ImageField(upload_to='uploads/cta/')
    discount=models.DecimalField(default=0,decimal_places=0, max_digits=3)
    

    def __str__(self):
        return self.seasonname
    


class Blog(models.Model):
    title=models.CharField(max_length=200,blank=True )
    name=models.CharField(max_length=200)
    blogcategory=models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    image=models.ImageField(upload_to='uploads/blogs/')
    blogtitle=models.CharField(max_length=1000, default='', blank=True, null=True)
    date=models.DateField(default=datetime.datetime.today)

    def __str__(self):
        return self.name

class Blogcategory(models.Model):
    name=models.CharField(max_length=50)

    def __str__(self):
        return self.name
    

    class Meta:
        verbose_name_plural = 'Blogcategories'
