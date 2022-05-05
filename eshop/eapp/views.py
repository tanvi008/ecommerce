
from .serializer import CustomerSerializer, OrdersSerializer, ProductSerializer
from rest_framework import generics
from rest_framework.views import APIView
from .models import Product,Customer,Orders
from rest_framework.response import Response
from rest_framework import status
# Create your views here.

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated 
from django.contrib.auth import get_user_model

from .serializer import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = UserSerializer
    queryset = get_user_model().objects.all()


class ProductView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class CustomerView(generics.ListCreateAPIView):
    def post(self, request):
        # print('entered')
        # a = request.POST.dict()
        # print(a.get('product'))
        # print(a['product'])
        product=Product.objects.filter(productname = 'clothes').first()
        print('exit')
        print(product)
        customer=Customer.objects.filter(name = 'tanvi').first()
        print(customer)
        order = Orders.objects.create(product=product, customer=customer)
        order.save()
        print(order)

        return order


    # queryset = Customer.objects.all()
    # serializer_class = CustomerSerializer

class OrdersView(APIView):
    def get(self, request):
        orders = Orders.objects.all()
        serializer = OrdersSerializer(orders, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = OrdersSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.error, status = status.HTTP_400_BAD_REQUEST)