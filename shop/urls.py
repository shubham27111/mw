from django.urls import path
from .import views

urlpatterns = [
    path('',views.index,name="ShopHome"),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('checkout/',views.checkout,name='checkout'),
    path('product/<int:myid>',views.product,name='product'),
    path('tracker/',views.tracker,name='tracker'),
    path('handlerequest/',views.handlerequest,name='handleRequest'),
    # path('search/',views.search,name='Search')
]