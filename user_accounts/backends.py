"""
Custom backend for users authentication.
developer : #ABS
"""

# Import all requirements  
from .forms import UserForm, change_pass_users, UserEmailForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import check_password
from django.contrib.auth.backends import ModelBackend
from django.http import HttpRequest, JsonResponse
from django.core.validators import validate_email
from django.shortcuts import redirect, reverse
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate
from .models import user_accounts, Customer
from django.db.models import Q
from typing import Optional


# CustomBackend class
class CustomBackend(ModelBackend):
    # function authenticate
    def authenticate(self, request, username=None, password=None,has_new_password = None, WPOPass = None, **kwargs) -> Optional[get_user_model()]:
        UserModel = get_user_model()
        try:
            user = UserModel.objects.get(Q(username=username) | Q(email=username))| Q(phoneNember=username)
        except UserModel.DoesNotExist:
            return None
        else:
            # Check if the provided password is valid for the user
            if user.check_password(password):
                return user
        return None


@login_required
def update_user(request):
    if request.method == 'POST':
        frist_name = request.POST.get('frist_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        old_pass = request.POST.get('old_password')
        pass1 = request.POST.get('new_password')
        pass2 = request.POST.get('confirm_password')
        if frist_name and last_name:
            if frist_name and last_name and not email:
                user_accounts.objects.filter(phoneNumber=request.user.phoneNumber).update(
                    first_name = frist_name,
                    last_name = last_name,)
                return JsonResponse({'status':"نام و نام خانوادگی با موفقیت به روز شد", 'success': True})
            elif email and frist_name and last_name:
                try: 
                    validate_email(email)
                    user_accounts.objects.filter(phoneNumber=request.user.phoneNumber).update(
                            first_name = frist_name,
                            last_name = last_name,
                            email = email,)
                    return JsonResponse({'status':"نام و نام خانوادگی و ایمیل با موفقیت به روز شد", 'success': True})
                except:
                    return JsonResponse({'status':"ایمل وارد شده معتبر نیست", 'success': False})
            else:
                return JsonResponse({'status':"خطایی رخ داده - دوباره تلاش کنید", 'success': False})
        elif old_pass and pass1 and pass2:
            if old_pass and pass1:
                if old_pass != pass1:
                    if check_password(old_pass, request.user.password):
                        if pass1 == pass2:
                            user = request.user
                            user.set_password(pass1)
                            user.save()
                            return JsonResponse({'status':"رمز عبور با موفقیت تغییر کرد", 'success': True})
                        else:
                            return JsonResponse({'status': "رمز جدید و تکرار آن باید برابر باشند", 'success': False})
                    else:
                        return JsonResponse({'status':"رمز عبور قدیمی اشتباه است", 'success': False})
                else:
                    return JsonResponse({'status':'رمز عبور جدید نمی‌تواند با رمز عبور قدیمی برابر باشد.', 'success': False})
                    
            else:
                return JsonResponse({'status':"برای تغییر رمز عبور خود باید هر سه فیلد رمز عبور قدیمی - رمز جدید و تکرار رمز جدید را پر کنید", 'success': False})

        else:
            return JsonResponse({'status':"فیلد های نام و نام خانوادگی باید پر شوند", 'success': False})
    else:
        return JsonResponse({'status':"درخواست نا معتبر", 'success': False})

def costomer_detail(request):
    if request.method =='POST':
        phoneNumber = request.user.phoneNumber
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        address = request.POST.get('address')
        pelak = request.POST.get('pelak')
        ostan = request.POST.get('ostan')
        city = request.POST.get('city')
        zip_code = request.POST.get('zip_code')
        if first_name and last_name and address and ostan and city and zip_code:
            if len(zip_code) < 10 or len(zip_code) > 10 :
                return JsonResponse({'status':"کد پستی وارد شده معتبر نیست", 'success': False})
            else:
                user_accounts.objects.filter(phoneNumber=request.user.phoneNumber).update(first_name = first_name, last_name = last_name,)
                if Customer.objects.filter(customer=request.user.phoneNumber).exists():
                    Customer.objects.filter(customer = request.user.phoneNumber).update(
                        first_name = first_name,
                        last_name = last_name,
                        address = address,
                        pelak = pelak,
                        ostan = ostan,
                        city = city,
                        zip_zode = zip_code,
                    )
                    return JsonResponse({'status':"با تشکر ! اطلاعات آدرس شما به روز شد", 'success': True})
                else:
                    Customer.objects.create(
                        customer = request.user.phoneNumber,
                        first_name = first_name,
                        last_name = last_name,
                        address = address,
                        pelak = pelak,
                        ostan = ostan,
                        city = city,
                        zip_zode = zip_code,
                    )
                    return JsonResponse({'status':"با تشکر ! اطلاعات آدرس شما ایجاد شد", 'success': True})
        else:
            return JsonResponse({'status':"لطفا فیلد های درخواستی را کامل کرده و مجددا تلاش کنید", 'success': False})
    else:
        return JsonResponse({'status':"درخواست نا معتبر", 'success': False})
