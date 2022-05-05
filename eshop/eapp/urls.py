from django.urls import path
from eapp.views import CustomerView, OrdersView, ProductView

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework.routers import DefaultRouter
from eapp.views import UserViewSet

urlpatterns=[
    path('product/',ProductView.as_view(), name = 'product'),
    path('api/token/',TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name= 'token_refresh'),
    path('customer/', CustomerView.as_view(), name='customer'),
    path('orders/', OrdersView.as_view(), name='orders'),
]

router = DefaultRouter()
router.register('user',UserViewSet, basename='user')

urlpatterns +=router.urls