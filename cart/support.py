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
                    support_message = request.POST.get('sopport_message')

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