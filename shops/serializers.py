from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import Shop, Section
from users.serializers import TinyUserSerializer
from products.models import Product
from favorites.models import FavoriteShop


class TinyShopSerializer(ModelSerializer):
    # 추가: 4개까지의 썸네일을 가져올 필드 정의
    thumbnails = serializers.SerializerMethodField()

    class Meta:
        model = Shop
        fields = (
            "pk",
            "shop_name",
            "avatar",
            "background_pic",
            "is_star_seller",
            "thumbnails",  # thumbnails 필드 추가
        )

    # 추가: 썸네일 정보 가져오는 메서드 정의
    def get_thumbnails(self, obj):
        # 샵에 해당하는 최대 4개의 상품 썸네일을 가져옵니다.
        products = Product.objects.filter(shop=obj)[:4]
        thumbnail_list = []

        for product in products:
            if product.thumbnail:
                thumbnail_list.append(product.thumbnail)

        return thumbnail_list


class ShopSerializer(ModelSerializer):
    is_liked = serializers.SerializerMethodField()

    class Meta:
        model = Shop
        fields = (
            "pk",
            "shop_name",
            "avatar",
            "background_pic",
            "is_liked",
            "is_star_seller",
        )

    def get_is_liked(self, shop):
        request = self.context.get("request")
        if request:
            if request.user.is_authenticated:
                return FavoriteShop.objects.filter(
                    user=request.user,
                    shops__pk=shop.pk,
                ).exists()
        return False


class ShopDetailSerializer(ModelSerializer):
    is_liked = serializers.SerializerMethodField()
    image_urls = serializers.SerializerMethodField()
    user = TinyUserSerializer(read_only=True)

    class Meta:
        model = Shop
        fields = (
            "pk",
            "user",
            "shop_name",
            "avatar",
            "description_title",
            "description",
            "background_pic",
            "description",
            "announcement",
            "expiration",
            "cancellation",
            "shop_policy_updated_at",
            "is_liked",
            "is_star_seller",
            "image_urls",
        )

    def get_is_liked(self, shop):
        request = self.context.get("request")
        if request:
            if request.user.is_authenticated:
                return FavoriteShop.objects.filter(
                    user=request.user,
                    shops__pk=shop.pk,
                ).exists()
        return False

    def get_image_urls(self, shop):
        image_fields = ["image_1", "image_2", "image_3", "image_4", "image_5"]
        image_urls = [
            getattr(shop, field) for field in image_fields if getattr(shop, field)
        ]
        return image_urls


class ShopCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = "__all__"


class SectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Section
        fields = ["id", "title", "rank", "shop"]
