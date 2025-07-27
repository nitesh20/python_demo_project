"""
URL configuration for demoproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))

    user credentials:
    admin
    admin admin123

    managers
    nitesh nit@1234
    vivek  viv@1234

    users
    amit ami@1234
    rahul rah@1234
    ashish ash@1234
    ajit aji@1234
    adarsh ada@1234
    muskan mus@1234
    aditya adi@1234
    Sumit  sum@1234
"""
from django.contrib import admin
from django.urls import path, include
from rolebase import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/register/', views.register_view, name='register'),
    # path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/', views.custome_login_view, name='customtoken_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/user/', views.user_list_view, name='user_list'),
    path('api/', include('task.urls')),
]
