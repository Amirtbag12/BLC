from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView
from django.http import HttpRequest, JsonResponse
from django.shortcuts import render, redirect
from product.models import InventoryItem
from django.contrib import messages
from .models import Favourite 


@login_required
def add_favourite(request):
    if request.method == 'POST':
        if request.user.is_authenticated :
            try:
                product_id = int(request.POST.get('product_id'))
                product = InventoryItem.objects.get(pk=product_id)
                add_cart_date = int(request.POST.get('add_cart_date'))
                if(Favourite.objects.filter(user=request.user.phoneNumber, product_title=product.product_title,)):
                    return JsonResponse({'status':"کالا هم اکنون در علاقه مندی های شما موجود است", 'success': False})
                else:
                    if add_cart_date > 0:
                        Favourite.objects.create(
                            user = request.user.phoneNumber,
                            product_id = product_id,
                            product_title = product.product_title,
                            quantity = product.quantity,
                            price = add_cart_date,
                            image = product.image,
                            color_quantity = product_color_quantity,
                        )
                        return JsonResponse({'status':f"محصول {product.product_title} با موفقیت به علاقه مندی ها اضافه شد.", 'success': True})
                    else:
                        Cart.objects.create(
                            user = request.user.phoneNumber,
                            product_id = product_id,
                            product_title = product.product_title,
                            quantity = product.quantity,
                            price = product.price,
                            image = product.image,
                            color_quantity = product_color_quantity,
                        )
                        return JsonResponse({'status':f"محصول {product.product_title} با موفقیت به علاقه مندی ها اضافه شد.", 'success': True})
                            
            except InventoryItem.DoesNotExist:
                return JsonResponse({'status':"محصول مورد نظر پیدا نشد.", 'success': False})
        else:
            return JsonResponse({'status':"برای افزودن کالا به علاقه مندی ها ابتدا باید ثبت نام کنید یا وارد حساب خود شوید", 'success': False})

    return render(request, 'products/cart/cart.html',{'discount': discount})

@login_required
def update_cart(request):
    if request.method == 'POST':
        product_title = request.POST.get('product_title')
        quantity = int(request.POST.get('quantity'))
        color_quantity = product_color_quantity = int(request.POST.get('product_color_quantity'))
        if quantity > 0:
            product = InventoryItem.objects.get(product_title=product_title)
            if quantity <= product.quantity and quantity <= color_quantity:
                try:
                    user_cart = Cart.objects.get(user=request.user.phoneNumber, product_title=product_title)
                    user_cart.quantity = quantity
                    user_cart.save()
                    return JsonResponse({'status': "تعداد درخواستی با موفقیت به روز شد", 'success': True})
                except Cart.DoesNotExist:
                    return JsonResponse({'status': "محصول مورد پیدا نشد.", 'success': False})
            else:
                return JsonResponse({'status': "تعداد درخواستی بالاتر از موجودی محصول است.", 'success': False})
        else:
            try:
                Cart.objects.filter(user=request.user.phoneNumber, product_title=product_title).delete()
                return JsonResponse({'status':"محصول از سبد خرید حذف شد.", 'success': True})
            except Cart.DoesNotExist:
                return JsonResponse({'status': "محصول مورد پیدا نشد.", 'success': False})
    else:
        return render(request, 'products/cart/cart.html',{'discount': discount})

@login_required
@csrf_exempt
def remove_from_cart(request):
    if request.method == 'POST':
        product_title = request.POST.get('product_title')
        if product_title:
            try:
                Cart.objects.filter(user=request.user.phoneNumber, product_title=product_title).delete()
                return JsonResponse({'status':"محصول از سبد خرید حذف شد.", 'success': True})
            except:
                return JsonResponse({'status':"محصول مورد پیدا نشد.", 'success': False})
        else:
            return JsonResponse({'status':"محصول مورد پیدا نشد.", 'success': False})
    return render(request, 'products/cart/cart.html',{'discount': discount})

@login_required
@csrf_exempt
def apply_discount(request):
    if request.method == 'POST':
        product_title = request.POST.get('product_title')
        if product_title:
            price = int(request.POST.get('product_price'))
            category_id = int(request.POST.get('product_collection'))
            form = DiscountForm(request.POST)
            if form.is_valid():
                discount = Discount.objects.get(code=form.cleaned_data['code'])
                try:
                    if discount.product == product_id or discount.collection == category_id:
                        code = form.cleaned_data['code']
                        discounted_price = InventoryItem.apply_discount(discount_code=code, price=price)
                        Cart.objects.filter(user=request.user.phoneNumber, product_title=product_title).update(price=int(discounted_price))
                        return JsonResponse({'status':"کد تخفیف با موفقیت اعمال شد.", 'success': True})
                    else:
                        return JsonResponse({'status':"کد تخفیف معتبر نیست", 'success': False})
                except:
                    return JsonResponse({'status':"محصول مورد پیدا نشد.", 'success': False})
        else:
            return JsonResponse({'status':"محصول مورد پیدا نشد.", 'success': False})

    else:
        return render(request, 'products/cart/cart.html',{'discount': discount})

@login_required
def clear_cart(request):
    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        if product_id:
            Cart.objects.filter(user=request.user.phoneNumber).delete()
            return JsonResponse({'status':"سبد خرید خالی شد.", 'success': True})
        else:
            return JsonResponse({'status':"سبد خرید هم اکنون خالی است.", 'success': False})
    else:
        return render(request, 'products/cart/cart.html',{'discount': discount})

def checkout(request):
    return render(request,'products/checkout/checkout.html')
