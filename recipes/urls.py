from django.urls import path
from recipes.views import home, aboutus, contactus

urlpatterns = [
    path('', home), # Home
    path('aboutus/', aboutus), # /sobre/ 
    path('contactus/', contactus), # /about/
]
