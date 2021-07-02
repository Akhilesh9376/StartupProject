from django.urls import path
from .import views
urlpatterns = [
    path('',views.Home,name="Home"),
    path('team',views.Team,name='Team'),
    path('contact',views.Contact,name='Contact'),
    path('pricing',views.Price,name="Price"),
    path('blog',views.Blog,name='Blog'),
]
