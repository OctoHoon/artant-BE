from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.exceptions import (
    NotFound,
    ParseError,
    PermissionDenied,
)
from products.models import Product
from shops.models import Shop
from .models import FavoriteProduct, FavoriteShop
from .serializer import (
    FavoriteProductSerializer,
    TinyFavoriteProductSerializer,
    TinyFavoriteShopSerializer,
    FavoriteShopSerializer,
)
from django.conf import settings
from products.serializers import ProductListSerializer

# Create your views here.


# get specific user's favorite products
class UserFavoriteProducts(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_object(self, user_pk):
        try:
            return FavoriteProduct.objects.get(user_id=user_pk)
        except FavoriteProduct.DoesNotExist:
            raise NotFound

    def get(self, request, user_pk):
        try:
            page = request.query_params.get("page", 1)
            page = int(page)
        except ValueError:
            page = 1

        page_size = settings.FAVORITE_PRODUCT_PAGE_SIZE
        start = (page - 1) * page_size
        end = page * page_size

        favorite_product = self.get_object(user_pk)
        products = favorite_product.products.all()  # 해당 사용자가 좋아하는 모든 Product 객체 가져오기

        products_on_page = products[start:end]  # 페이지 범위에 해당하는 Product 객체 가져오기

        serializer = ProductListSerializer(  # ProductSerializer는 실제로 사용하는 Product Serializer로 바꿔야 합니다.
            products_on_page,
            many=True,
            context={"request": request},
        )
        return Response(serializer.data)


class FavoriteProductToggle(APIView):
    # get user's favorite product
    def get_favoriteProduct(self, user):
        favorite_product, _ = FavoriteProduct.objects.get_or_create(user=user)
        return favorite_product

    def get_product(self, product_pk):
        try:
            return Product.objects.get(pk=product_pk)
        except Product.DoesNotExist:
            raise NotFound

    def put(self, request, product_pk):
        favorite_product_list = self.get_favoriteProduct(request.user)
        product = self.get_product(product_pk)
        if favorite_product_list.products.filter(pk=product_pk).exists():
            favorite_product_list.products.remove(product)
        else:
            favorite_product_list.products.add(product)
        return Response(status=HTTP_200_OK)


class UserFavoriteShops(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_object(self, user_pk):
        try:
            return FavoriteShop.objects.get(user_id=user_pk)
        except FavoriteShop.DoesNotExist:
            raise NotFound

    def get(self, request, user_pk):
        favorite_shops = self.get_object(user_pk)
        serializer = FavoriteShopSerializer(
            favorite_shops,
            context={"request": request},
        )
        return Response(serializer.data)


class FavoriteShopToggle(APIView):
    def get_favoriteShops(self, user):
        try:
            return FavoriteShop.objects.get(user=user)
        except FavoriteShop.DoesNotExist:
            raise NotFound

    def get_shop(self, shop_pk):
        try:
            return Shop.objects.get(pk=shop_pk)
        except Shop.DoesNotExist:
            raise NotFound

    def put(self, request, shop_pk):
        favorite_shop_list = self.get_favoriteShops(request.user)
        shop = self.get_shop(shop_pk)
        if favorite_shop_list.shops.filter(pk=shop_pk).exists():
            favorite_shop_list.shops.remove(shop)
        else:
            favorite_shop_list.shops.add(shop)
        return Response(status=HTTP_200_OK)
