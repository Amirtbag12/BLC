from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView
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
                    Cart.objects.filter(user=request.user.phoneNumber).delete()
                    return JsonResponse({'status':"", 'success': True})
                else:
                    return JsonResponse({'status':"مقایسه محصولات هم اکنون خالی است.", 'success': False}):
                        product = InventoryItem.objects.get(pk=product_id)
                        add_cart_date = int(request.POST.get('add_cart_date'))
                        if(Favourite.objects.filter(user=request.user.phoneNumber, product_title=product.product_title,)):
                            return JsonResponse({'status':"کالا هم اکنون در علاقه مندی های شما موجود است", 'success': False})
                        else:
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
                                            color_quantity1 = product_color_quantity,)
                                        i++
                                        return JsonResponse({'status':f"محصول {product.product_title} با موفقیت برای مقایسه اضافه شد. لطفا یک محصول دیگر نیز اضافه کنید.", 'success': True})
                                    else:
                                        Comparison.objects.create(
                                            user = request.user.phoneNumber,
                                            product_id1 = product_id,
                                            product_title1 = product.product_title,
                                            quantity1 = product.quantity,
                                            price1 = product.price,
                                            image1 = product.image,
                                            color_quantity1 = product_color_quantity,)
                                        i++
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
                                            color_quantity2 = product_color_quantity)
                                        i++
                                        return JsonResponse({'status':f"محصول {product.product_title} نیز با موفقیت به مقایسه محصولات اضافه شده. اکنون میتوانید مقایسه دو محصول را مشاهده کنید", 'success': True})
                                    else:
                                        Comparison.objects.create(
                                            user = request.user.phoneNumber,
                                            product_id2 = product_id,
                                            product_title2 = product.product_title,
                                            quantity2 = product.quantity,
                                            price2 = product.price,
                                            image2 = product.image,
                                            color_quantity2 = product_color_quantity,)
                                        i++
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
                                            color_quantity1 = product_color_quantity,)
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
                                            color_quantity1 = product_color_quantity,)
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