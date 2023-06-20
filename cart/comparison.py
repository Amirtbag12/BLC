from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpRequest, JsonResponse
from django.shortcuts import render, redirect
from product.models import InventoryItem
from django.contrib import messages
from .models import Comparison 


@login_required
def comparison_view(request):
    return render(request, 'products/comparison/comparison.html')

@login_required
@csrf_exempt
def add_comparison(request):
    if request.method == 'POST':
        if request.user.is_authenticade:
            try:
                product_id = request.POST.get('product_id')
                if product_id:
                    product_id  = int(product_id)
                    if (Comparison.objects.filter(user=request.user.phoneNumber, product_id1=product_id)) or (Comparison.objects.filter(user=request.user.phoneNumber, product_id2=product_id)):
                        return JsonResponse({'status':"کالا هم اکنون در لیست مقایسه محصولات شما موجود است", 'success': False})
                    else:
                        product = InventoryItem.objects.get(pk=product_id)
                        add_cart_date = int(request.POST.get('add_cart_date'))
                        product_color_quantity = int(request.POST.get('product_color_quantity'))
                        product_slug = request.POST.get('product_slug')
                        for i in range(2):
                            if i == 0:
                                if add_cart_date > 0:
                                    Comparison.objects.create(
                                        user = request.user.phoneNumber,
                                        product_id1 = product_id,
                                        product_title1 = product.product_title,
                                        quantity1 = product.quantity,
                                        price1 = add_cart_date,
                                        image1 = product.image,
                                        color_quantity1 = product_color_quantity,
                                        brand1 = product.brand,
                                        product_type1 = product.product_type,
                                        product_jense1 = product.product_jense,
                                        product_wight1 = product.product_wight,
                                        product_abad1 = product.product_abad,
                                        product_size1 = product.product_size,
                                        product_garr1 = product.product_garr,
                                        slug1= product_slug,)
                                    i = i + 1
                                    return JsonResponse({'status':f"محصول {product.product_title} با موفقیت برای مقایسه اضافه شد. لطفا یک محصول دیگر نیز اضافه کنید.", 'success': True})
                                else:
                                    Comparison.objects.create(
                                        user = request.user.phoneNumber,
                                        product_id1 = product_id,
                                        product_title1 = product.product_title,
                                        quantity1 = product.quantity,
                                        price1 = product.price,
                                        image1 = product.image,
                                        color_quantity1 = product_color_quantity,
                                        brand1 = product.brand,
                                        product_type1 = product.product_type,
                                        product_jense1 = product.product_jense,
                                        product_wight1 = product.product_wight,
                                        product_abad1 = product.product_abad,
                                        product_size1 = product.product_size,
                                        product_garr1 = product.product_garr,
                                        slug1= product_slug,)
                                    i = i + 1
                                    return JsonResponse({'status':f"محصول {product.product_title} با موفقیت برای مقایسه اضافه شد. لطفا یک محصول دیگر نیز اضافه کنید.", 'success': True})
                            elif i ==1:
                                if add_cart_date > 0:
                                    Comparison.objects.create(
                                        user = request.user.phoneNumber,
                                        product_id2 = product_id,
                                        product_title2 = product.product_title,
                                        quantity2 = product.quantity,
                                        price2 = add_cart_date,
                                        image2 = product.image,
                                        color_quantity2 = product_color_quantity,
                                        brand2 = product.brand,
                                        product_type2 = product.product_type,
                                        product_jense2 = product.product_jense,
                                        product_wight2 = product.product_wight,
                                        product_abad2 = product.product_abad,
                                        product_size2 = product.product_size,
                                        product_garr2 = product.product_garr,
                                        slug2= product_slug,)
                                    i = i + 1
                                    return JsonResponse({'status':f"محصول {product.product_title} نیز با موفقیت به مقایسه محصولات اضافه شده. اکنون میتوانید مقایسه دو محصول را مشاهده کنید", 'success': True})
                                else:
                                    Comparison.objects.create(
                                        user = request.user.phoneNumber,
                                        product_id2 = product_id,
                                        product_title2 = product.product_title,
                                        quantity2 = product.quantity,
                                        price2 = product.price,
                                        image2 = product.image,
                                        color_quantity2 = product_color_quantity,
                                        brand2 = product.brand,
                                        product_type2 = product.product_type,
                                        product_jense2 = product.product_jense,
                                        product_wight2 = product.product_wight,
                                        product_abad2 = product.product_abad,
                                        product_size2 = product.product_size,
                                        product_garr2 = product.product_garr,
                                        slug2= product_slug,)
                                    i = i + 1
                                    return JsonResponse({'status':f"محصول {product.product_title} نیز با موفقیت به مقایسه محصولات اضافه شده. اکنون میتوانید مقایسه دو محصول را مشاهده کنید", 'success': True})
                            elif i ==2:
                                Comparison.objects.filter(user=request.user.phoneNumber).delete()
                                if add_cart_date > 0:
                                    Comparison.objects.create(
                                        user = request.user.phoneNumber,
                                        product_id1 = product_id,
                                        product_title1 = product.product_title,
                                        quantity1 = product.quantity,
                                        price1 = add_cart_date,
                                        image1 = product.image,
                                        color_quantity1 = product_color_quantity,
                                        brand1 = product.brand,
                                        product_type1 = product.product_type,
                                        product_jense1 = product.product_jense,
                                        product_wight1 = product.product_wight,
                                        product_abad1 = product.product_abad,
                                        product_size1 = product.product_size,
                                        product_garr1 = product.product_garr,
                                        slug1= product_slug,)
                                    i = 0
                                    return JsonResponse({'status':f"محصول {product.product_title} با موفقیت برای مقایسه اضافه شد. لطفا یک محصول دیگر نیز اضافه کنید.", 'success': True})
                                else:
                                    Comparison.objects.create(
                                        user = request.user.phoneNumber,
                                        product_id1 = product_id,
                                        product_title1 = product.product_title,
                                        quantity1 = product.quantity,
                                        price1 = product.price,
                                        image1 = product.image,
                                        color_quantity1 = product_color_quantity,
                                        brand1 = product.brand,
                                        product_type1 = product.product_type,
                                        product_jense1 = product.product_jense,
                                        product_wight1 = product.product_wight,
                                        product_abad1 = product.product_abad,
                                        product_size1 = product.product_size,
                                        product_garr1 = product.product_garr,
                                        slug1= product_slug,)
                                    i = 0
                                    return JsonResponse({'status':f"محصول {product.product_title} با موفقیت برای مقایسه اضافه شد. لطفا یک محصول دیگر نیز اضافه کنید.", 'success': True})        
            except InventoryItem.DoesNotExist:
                return JsonResponse({'status':"محصول مورد نظر پیدا نشد.", 'success': False})
    else:
        return JsonResponse({'status':"درخواست معتبر نیست", 'success': False})


@login_required
@csrf_exempt
def clear_comparison(request):
    if request.method == 'POST':
        product_title = request.POST.get('product_title')
        if product_title:
            try:
                Comparison.objects.filter(user=request.user.phoneNumber).delete()
                return JsonResponse({'status':"محصول از مقایسه محصولات حذف شد.", 'success': True})
            except:
                return JsonResponse({'status':"محصول مورد پیدا نشد.", 'success': False})
        else:
            return JsonResponse({'status':"محصول مورد پیدا نشد.", 'success': False})
    return render(request, 'products/cart/cart.html',{'discount': discount})