

from django.urls import path

from .import views

urlpatterns = [
    path('',views.home,name='home'),
    path('cart',views.cart,name='cart'),
    path('addcart/<int:id>',views.addcart,name='addcart'),
    path('remove/<int:id>',views.remove,name='remove'),
    path('checkout',views.checkout,name='checkout'),
    path('profile',views.profile,name='profile'),
    path('eprofile/<int:id>',views.eprofile,name='eprofile'),
    path('upassword/<int:id>',views.upassword,name='upassword'),
    path('dprofile',views.dprofile,name='dprofile'),
    path('ddelete/<int:id>',views.ddelete,name='ddelete'),
    path('aboutus',views.aboutus,name='aboutus'),
    path('contactus',views.contactus,name='contactus'),
]




