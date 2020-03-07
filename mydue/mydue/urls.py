from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('api/paytm/', include('drf_paytm.urls')),
    path('', include('user.urls'), name = 'home'),
        
]
