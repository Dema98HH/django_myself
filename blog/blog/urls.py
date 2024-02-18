
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('departments/', include('department.urls')),
    path('products/', include('product.urls')),

]
