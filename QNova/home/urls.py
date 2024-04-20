from django.urls import path
from . import views

urlpatterns = [
        path('', views.Home, name='Home'),
        path('search/', views.search, name='search'),
        path('about/', views.about, name='about'),
        path('checkout/', views.checkout, name='checkout'),
        path('update_item/', views.updateItem, name='update_item'),
        path('cart/', views.cart, name='cart'),
        path('zzTandC/', views.zzTandC, name='zzTandC'),
        path('login/', views.login_user, name='login'),
        path('logout/', views.logout_user, name='logout'),
        path('register/', views.register_user, name='register'),
        path('update_password/', views.update_password, name='update_password'),
        path('update_user/', views.update_user, name='update_user'),
        path('update_info/', views.update_info, name='update_info'),
        path('business/', views.business, name='business'),
        path('product/<int:pk>', views.product, name='product'),
        path('produk/<int:pk>', views.produk, name='produk'),
        path('category/<str:category_name>', views.category, name='category'),
        path('blogcategory/<str:foo>', views.blogcategory, name='blogcategory'),
        # path('newarrival/', views.newarrival, name='newarrival'),
        # path('trending/', views.trending, name='trending'),
        # path('toprated/', views.toprated, name='toprated'),
        # path('bestsells/', views.bestsells, name='bestsells'),
        # path('testimonials/', views.testimonials, name='testimonials'),
        path('blog/', views.blog, name='blog'),
        path('dashboard/', views.dashboard, name='dashboard'),  
        path('vendorprof/', views.vendorprof, name='vendorprof'),
        path('vendorsignup/',views.vendorsignup, name='vendorsignup'),
        path('vendorlogin/',views.vendorlogin, name='vendorlogin'),
        

]