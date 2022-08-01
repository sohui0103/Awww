from django.urls import path,include
from . import views

urlpatterns = [
   path('admin/', admin.site.urls),
   path('', include('socialShare.urls')) #this is my app urls
]