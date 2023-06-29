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
    slug = models.CharField(max_length=30, db_index=True, null=True, blank=True, verbose_name='اسلاگ محصول')

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
    price1 = models.PositiveIntegerField(verbose_name='قیمت۱', null=True)
    price2 = models.PositiveIntegerField(verbose_name='قیمت۲', null=True)
    image1 = models.CharField(max_length=100, verbose_name='۱تصویر محصول', null=True, blank=True)
    image2 = models.CharField(max_length=100, verbose_name='۲تصویر محصول', null=True, blank=True)
    color1 = models.CharField(max_length=30, verbose_name='۱رنگ محصول', null=True, blank=True)
    color2 = models.CharField(max_length=30, verbose_name='۲رنگ محصول', null=True, blank=True)
    brand1 = models.CharField(max_length=30, verbose_name='۱برند محصول', null=True, blank=True)
    brand2 = models.CharField(max_length=30, verbose_name='۲برند محصول', null=True, blank=True)
    color_quantity1 = models.PositiveIntegerField(verbose_name='۱تعداد رنگ بندی موجود', null=True)
    color_quantity2 = models.PositiveIntegerField(verbose_name='۲تعداد رنگ بندی موجود', null=True)
    product_type1 = models.CharField(max_length=30, db_index=True, null=True, blank=True, verbose_name='نوع محصول۱')
    product_type2 = models.CharField(max_length=30, db_index=True, null=True, blank=True, verbose_name='نوع محصول۲')
    product_jense1 = models.CharField(max_length=30, db_index=True, null=True, blank=True, verbose_name='جنس محصول۱')
    product_jense2 = models.CharField(max_length=30, db_index=True, null=True, blank=True, verbose_name='جنس محصول۲')
    product_wight1 = models.CharField(max_length=30, db_index=True, null=True, blank=True, verbose_name='وزن محصول۱')
    product_wight2 = models.CharField(max_length=30, db_index=True, null=True, blank=True, verbose_name='وزن محصول۲')
    product_abad1 = models.CharField(max_length=30, db_index=True, null=True, blank=True, verbose_name='ابعاد خارجی محصول۱')
    product_abad2 = models.CharField(max_length=30, db_index=True, null=True, blank=True, verbose_name='ابعاد خارجی محصول۲')
    product_size1 = models.CharField(max_length=30, db_index=True, null=True, blank=True, verbose_name='سایز محصول۱')
    product_size2 = models.CharField(max_length=30, db_index=True, null=True, blank=True, verbose_name='سایز محصول۲')
    product_garr1 = models.CharField(max_length=30, db_index=True, null=True, blank=True, verbose_name='گارانتی محصول۱')
    product_garr2 = models.CharField(max_length=30, db_index=True, null=True, blank=True, verbose_name='گارانتی محصول۲')
    slug1 = models.CharField(max_length=30, db_index=True, null=True, blank=True, verbose_name='اسلاگ محصول اول')
    slug2 = models.CharField(max_length=30, db_index=True, null=True, blank=True, verbose_name='اسلاگ محصول دوم')
    
    class Meta:
        verbose_name = 'مقایسه محصول'
        verbose_name_plural = 'مقایسات محصولات'


class Support(models.Model):
    supporter = models.CharField(max_length=100, verbose_name='اپراتور پشتیبانی', null=True, blank=True)
    support_user = models.CharField(max_length=100, verbose_name='کاربر پشتیبانی گیرنده', null=True, blank=True)
    user_message0 = models.TextField(verbose_name='۱پیام کاربر به پشتیبان', null=True, blank=True)
    supporter_message0 = models.TextField(verbose_name='۱پیام پشتیبان به کاربر', null=True, blank=True)
    user_message1 = models.TextField(verbose_name='۲پیام کاربر به پشتیبان', null=True, blank=True)
    supporter_message1 = models.TextField(verbose_name='۲پیام پشتیبان به کاربر', null=True, blank=True)
    user_message2 = models.TextField(verbose_name='۳پیام کاربر به پشتیبان', null=True, blank=True)
    supporter_message2 = models.TextField(verbose_name='۳پیام پشتیبان به کاربر', null=True, blank=True)
    user_message3 = models.TextField(verbose_name='۴پیام کاربر به پشتیبان', null=True, blank=True)
    supporter_message3 = models.TextField(verbose_name='۴پیام پشتیبان به کاربر', null=True, blank=True)
    user_message4 = models.TextField(verbose_name='۵پیام کاربر به پشتیبان', null=True, blank=True)
    supporter_message4 = models.TextField(verbose_name='۵پیام پشتیبان به کاربر', null=True, blank=True)
    user_message5 = models.TextField(verbose_name='۶پیام کاربر به پشتیبان', null=True, blank=True)
    supporter_message5 = models.TextField(verbose_name='۶پیام پشتیبان به کاربر', null=True, blank=True)
    user_message6 = models.TextField(verbose_name='۷پیام کاربر به پشتیبان', null=True, blank=True)
    supporter_message6 = models.TextField(verbose_name='۷پیام پشتیبان به کاربر', null=True, blank=True)
    user_message7 = models.TextField(verbose_name='۸پیام کاربر به پشتیبان', null=True, blank=True)
    supporter_message7 = models.TextField(verbose_name='۸پیام پشتیبان به کاربر', null=True, blank=True)
    user_message8 = models.TextField(verbose_name='۹پیام کاربر به پشتیبان', null=True, blank=True)
    supporter_message8 = models.TextField(verbose_name='۹پیام پشتیبان به کاربر', null=True, blank=True)
    user_message9 = models.TextField(verbose_name='۱۰پیام کاربر به پشتیبان', null=True, blank=True)
    supporter_message9 = models.TextField(verbose_name='۱۰پیام پشتیبان به کاربر', null=True, blank=True)
    user_message10 = models.TextField(verbose_name='۱۱پیام کاربر به پشتیبان', null=True, blank=True)
    supporter_message10 = models.TextField(verbose_name='۱۱پیام پشتیبان به کاربر', null=True, blank=True)
    user_message11 = models.TextField(verbose_name='۱۲پیام کاربر به پشتیبان', null=True, blank=True)
    supporter_message11 = models.TextField(verbose_name='۱۲پیام پشتیبان به کاربر', null=True, blank=True)
    user_message12 = models.TextField(verbose_name='۱۳پیام کاربر به پشتیبان', null=True, blank=True)
    supporter_message12 = models.TextField(verbose_name='۱۳پیام پشتیبان به کاربر', null=True, blank=True)
    user_message13 = models.TextField(verbose_name='۱۴پیام کاربر به پشتیبان', null=True, blank=True)
    supporter_message13 = models.TextField(verbose_name='۱۴پیام پشتیبان به کاربر', null=True, blank=True)
    user_message14 = models.TextField(verbose_name='۱۵پیام کاربر به پشتیبان', null=True, blank=True)
    supporter_message14 = models.TextField(verbose_name='۱۵پیام پشتیبان به کاربر', null=True, blank=True)
    user_message15 = models.TextField(verbose_name='۱۶پیام کاربر به پشتیبان', null=True, blank=True)
    supporter_message15 = models.TextField(verbose_name='۱۶پیام پشتیبان به کاربر', null=True, blank=True)
    user_message16 = models.TextField(verbose_name='۱۷پیام کاربر به پشتیبان', null=True, blank=True)
    supporter_message16 = models.TextField(verbose_name='۱۷پیام پشتیبان به کاربر', null=True, blank=True)
    user_message17 = models.TextField(verbose_name='۱۸پیام کاربر به پشتیبان', null=True, blank=True)
    supporter_message17 = models.TextField(verbose_name='۱۸پیام پشتیبان به کاربر', null=True, blank=True)
    user_message18 = models.TextField(verbose_name='۱۹پیام کاربر به پشتیبان', null=True, blank=True)
    supporter_message18 = models.TextField(verbose_name='۱۹پیام پشتیبان به کاربر', null=True, blank=True)
    user_message19 = models.TextField(verbose_name='۲۰پیام کاربر به پشتیبان', null=True, blank=True)
    supporter_message19 = models.TextField(verbose_name='۲۰پیام پشتیبان به کاربر', null=True, blank=True)
    support_status = models.CharField(max_length=100, verbose_name='وضعیت پشتیبانی', null=True, blank=True)
    
    class Meta:
        verbose_name = 'پشتیبانی کاربر'
        verbose_name_plural = 'پشتیبانی کاربران'