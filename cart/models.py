from user_accounts.models import user_accounts as User
from product.models import InventoryItem
from django.db import models


class Cart(models.Model):
    user = models.CharField(max_length=100, verbose_name='کاربر', null=True, blank=True)
    product_id = models.CharField(max_length=100, verbose_name='شناسه محصول', null=True, blank=True)
    product_title = models.CharField(max_length=100, verbose_name='نام محصول', null=True, blank=True)
    product_collection = models.CharField(max_length=100, verbose_name='شناسه دسته بندی محصول', null=True, blank=True)
    quantity = models.PositiveIntegerField(verbose_name='تعداد محصول', null=True)
    price = models.PositiveIntegerField(verbose_name='قیمت', blank=False, null=False)
    image = models.CharField(max_length=100, verbose_name='تصویر محصول', null=True, blank=True)
    color = models.CharField(max_length=30, verbose_name='رنگ محصول', null=True, blank=True)
    color_quantity = models.PositiveIntegerField(verbose_name='تعداد رنگ بندی موجود', null=True)
    
    def calculate_item_price(self):
        item_price = 0
        if self.quantity and self.price:
            item_price = self.quantity * self.price
        return item_price

    @classmethod
    def calculate_total_price(cls, user):
        total_price = 0
        cart_items = Cart.objects.filter(user=user)
        for cart_item in cart_items:
            total_price += cart_item.calculate_item_price()
        return total_price

    class Meta:
        verbose_name = 'آیتم سبد خرید'
        verbose_name_plural = 'آیتم‌های سبد خرید'


class Favourite(models.Model):
    user = models.CharField(max_length=100, verbose_name='کاربر', null=True, blank=True)
    product_id = models.CharField(max_length=100, verbose_name='شناسه محصول', null=True, blank=True)
    product_title = models.CharField(max_length=100, verbose_name='نام محصول', null=True, blank=True)
    product_collection = models.CharField(max_length=100, verbose_name='شناسه دسته بندی محصول', null=True, blank=True)
    quantity = models.PositiveIntegerField(verbose_name='تعداد محصول', null=True)
    price = models.PositiveIntegerField(verbose_name='قیمت', blank=False, null=False)
    image = models.CharField(max_length=100, verbose_name='تصویر محصول', null=True, blank=True)
    color = models.CharField(max_length=30, verbose_name='رنگ محصول', null=True, blank=True)
    color_quantity = models.PositiveIntegerField(verbose_name='تعداد رنگ بندی موجود', null=True)
    
    def calculate_item_price(self):
        item_price = 0
        if self.quantity and self.price:
            item_price = self.quantity * self.price
        return item_price

    @classmethod
    def calculate_total_price(cls, user):
        total_price = 0
        fev_items = Favourite.objects.filter(user=user)
        for fev_item in fev_items:
            total_price += fev_item.calculate_item_price()
        return total_price

    class Meta:
        verbose_name = 'علاقه مندی کاربر '
        verbose_name_plural = 'علاقه مندی های کاربران'


class Comparison(models.Model):
    user = models.CharField(max_length=100, verbose_name='کاربر', null=True, blank=True)
    product_id1 = models.CharField(max_length=100, verbose_name='۱شناسه محصول', null=True, blank=True)
    product_id2 = models.CharField(max_length=100, verbose_name='۲شناسه محصول', null=True, blank=True)
    product_title1 = models.CharField(max_length=100, verbose_name='۱نام محصول', null=True, blank=True)
    product_title2 = models.CharField(max_length=100, verbose_name='۲نام محصول', null=True, blank=True)
    product_collection1 = models.CharField(max_length=100, verbose_name='۱شناسه دسته بندی محصول', null=True, blank=True)
    product_collection2 = models.CharField(max_length=100, verbose_name='۲شناسه دسته بندی محصول', null=True, blank=True)
    quantity1 = models.PositiveIntegerField(verbose_name='تعداد محصول۱', null=True)
    quantity2 = models.PositiveIntegerField(verbose_name='تعداد محصول۲', null=True)
    price1 = models.PositiveIntegerField(verbose_name='قیمت۱', blank=False, null=False)
    price2 = models.PositiveIntegerField(verbose_name='قیمت۲', blank=False, null=False)
    image1 = models.CharField(max_length=100, verbose_name='۱تصویر محصول', null=True, blank=True)
    image2 = models.CharField(max_length=100, verbose_name='۲تصویر محصول', null=True, blank=True)
    color1 = models.CharField(max_length=30, verbose_name='۱رنگ محصول', null=True, blank=True)
    color2 = models.CharField(max_length=30, verbose_name='۲رنگ محصول', null=True, blank=True)
    color_quantity1 = models.PositiveIntegerField(verbose_name='۱تعداد رنگ بندی موجود', null=True)
    color_quantity2 = models.PositiveIntegerField(verbose_name='۲تعداد رنگ بندی موجود', null=True)
    

    class Meta:
        verbose_name = 'مقایسه محصول'
        verbose_name_plural = 'مقایسات محصولات'