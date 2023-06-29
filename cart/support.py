from django.views.decorators.csrf import csrf_exempt
from django.http import HttpRequest, JsonResponse
from django.shortcuts import render, redirect
from .serializers import CartSerializer #support_serialize
from .models import Support


def message(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            if(request.user.is_supporter):
                try:
                    supporter = request.POST.get('supporter')
                    supported_user = request.POST.get('supported_user')
                    support_message = request.POST.get('sopport_message')
                    if(Support.objects.filter(supporter=supporter, support_user=supported_user, support_message__isnull=False).exists()):
                        pass
                    elif(Support.objects.filter(support_user=supported_user)):
                        Support.objects.filter(support_user=supported_user).update(
                            supporter = supporter,
                            support_message = support_message,
                        )
                    else:
                        return JsonResponse({'status':"پشتیبانی کاربر توسط اپراتور پشتیبان دیگری رزرو شده", 'success': False})
                except:
                    return JsonResponse({'status':"مشکل غیر منتظره ای رخ داده - پشتیبان گرامی لطفا با توسعه دهنده تماس حاصل فرمایید", 'success': False})
            else:
                # if user not sopporter:
                if (Support.objects.filter(user=request.user.phoneNumber)):
                    pass
                else:
                    pass
        else:
            return JsonResponse({'status':"برای ارسال پیام پشتیبانی ابتدا وارد سایت شوید یا ثبت نام کنید", 'success': False})
    else:
        return JsonResponse({'status':"درخواست معتبر نیست", 'success': False})