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
                    if(Support.objects.filter(supporter=supporter, support_user=supported_user, supporter_message0__isnull=False).exists()):
                        if(Support.objects.filter(supporter=supporter, support_user=supported_user, supporter_message1__isnull=False).exists()):
                            if(Support.objects.filter(supporter=supporter, support_user=supported_user, supporter_message2__isnull=False).exists()):
                                if(Support.objects.filter(supporter=supporter, support_user=supported_user, supporter_message3__isnull=False).exists()):
                                    if(Support.objects.filter(supporter=supporter, support_user=supported_user, supporter_message4__isnull=False).exists()):
                                        if(Support.objects.filter(supporter=supporter, support_user=supported_user, supporter_message5__isnull=False).exists()):
                                            if(Support.objects.filter(supporter=supporter, support_user=supported_user, supporter_message6__isnull=False).exists()):
                                                if(Support.objects.filter(supporter=supporter, support_user=supported_user, supporter_message7__isnull=False).exists()):
                                                    if(Support.objects.filter(supporter=supporter, support_user=supported_user, supporter_message8__isnull=False).exists()):
                                                        if(Support.objects.filter(supporter=supporter, support_user=supported_user, supporter_message9__isnull=False).exists()):
                                                            if(Support.objects.filter(supporter=supporter, support_user=supported_user, supporter_message10__isnull=False).exists()):
                                                                if(Support.objects.filter(supporter=supporter, support_user=supported_user, supporter_message11__isnull=False).exists()):
                                                                    if(Support.objects.filter(supporter=supporter, support_user=supported_user, supporter_message12__isnull=False).exists()):
                                                                        if(Support.objects.filter(supporter=supporter, support_user=supported_user, supporter_message13__isnull=False).exists()):
                                                                            if(Support.objects.filter(supporter=supporter, support_user=supported_user, supporter_message14__isnull=False).exists()):
                                                                                if(Support.objects.filter(supporter=supporter, support_user=supported_user, supporter_message15__isnull=False).exists()):
                                                                                    if(Support.objects.filter(supporter=supporter, support_user=supported_user, supporter_message16__isnull=False).exists()):
                                                                                        if(Support.objects.filter(supporter=supporter, support_user=supported_user, supporter_message17__isnull=False).exists()):
                                                                                            if(Support.objects.filter(supporter=supporter, support_user=supported_user, supporter_message18__isnull=False).exists()):
                                                                                                if(Support.objects.filter(supporter=supporter, support_user=supported_user, supporter_message19__isnull=False).exists()):
                                                                                                    Support.objects.filter(supporter=supporter, support_user=supported_user).update(
                                                                                                        supporter_message0 = support_message,
                                                                                                        supporter_message1 = None,
                                                                                                        supporter_message2 = None,
                                                                                                        supporter_message3 = None,
                                                                                                        supporter_message4 = None,
                                                                                                        supporter_message5 = None,
                                                                                                        supporter_message6 = None,
                                                                                                        supporter_message7 = None,
                                                                                                        supporter_message8 = None,
                                                                                                        supporter_message9 = None,
                                                                                                        supporter_message10 = None,
                                                                                                        supporter_message11 = None,
                                                                                                        supporter_message12 = None,
                                                                                                        supporter_message13 = None,
                                                                                                        supporter_message14 = None,
                                                                                                        supporter_message15 = None,
                                                                                                        supporter_message16 = None,
                                                                                                        supporter_message17 = None,
                                                                                                        supporter_message18 = None,
                                                                                                        supporter_message19 = None,
                                                                                                    )
                                                                                                    return JsonResponse({'status':support_message, 'success': True})
                                                                                                else:
                                                                                                    Support.objects.filter(supporter=supporter, support_user=supported_user).update(supporter_message19=support_message)
                                                                                                    return JsonResponse({'status':support_message, 'success': True})
                                                                                            else:
                                                                                                Support.objects.filter(supporter=supporter, support_user=supported_user).update(supporter_message18=support_message)
                                                                                                return JsonResponse({'status':support_message, 'success': True})
                                                                                        else:
                                                                                            Support.objects.filter(supporter=supporter, support_user=supported_user).update(supporter_message17=support_message)
                                                                                            return JsonResponse({'status':support_message, 'success': True})
                                                                                    else:
                                                                                        Support.objects.filter(supporter=supporter, support_user=supported_user).update(supporter_message16=support_message)
                                                                                        return JsonResponse({'status':support_message, 'success': True})
                                                                                else:
                                                                                    Support.objects.filter(supporter=supporter, support_user=supported_user).update(supporter_message15=support_message)
                                                                                    return JsonResponse({'status':support_message, 'success': True})
                                                                            else:
                                                                                Support.objects.filter(supporter=supporter, support_user=supported_user).update(supporter_message14=support_message)
                                                                                return JsonResponse({'status':support_message, 'success': True})
                                                                        else:
                                                                            Support.objects.filter(supporter=supporter, support_user=supported_user).update(supporter_message13=support_message)
                                                                            return JsonResponse({'status':support_message, 'success': True})
                                                                    else:
                                                                        Support.objects.filter(supporter=supporter, support_user=supported_user).update(supporter_message12=support_message)
                                                                        return JsonResponse({'status':support_message, 'success': True})
                                                                else:
                                                                    Support.objects.filter(supporter=supporter, support_user=supported_user).update(supporter_message11=support_message)
                                                                    return JsonResponse({'status':support_message, 'success': True})
                                                            else:
                                                                Support.objects.filter(supporter=supporter, support_user=supported_user).update(supporter_message10=support_message)
                                                                return JsonResponse({'status':support_message, 'success': True})
                                                        else:
                                                            Support.objects.filter(supporter=supporter, support_user=supported_user).update(supporter_message9=support_message)
                                                            return JsonResponse({'status':support_message, 'success': True})
                                                    else:
                                                        Support.objects.filter(supporter=supporter, support_user=supported_user).update(supporter_message8=support_message)
                                                        return JsonResponse({'status':support_message, 'success': True})
                                                else:
                                                    Support.objects.filter(supporter=supporter, support_user=supported_user).update(supporter_message7=support_message)
                                                    return JsonResponse({'status':support_message, 'success': True})
                                            else:
                                                Support.objects.filter(supporter=supporter, support_user=supported_user).update(supporter_message6=support_message)
                                                return JsonResponse({'status':support_message, 'success': True})
                                        else:
                                            Support.objects.filter(supporter=supporter, support_user=supported_user).update(supporter_message5=support_message)
                                            return JsonResponse({'status':support_message, 'success': True})
                                    else:
                                        Support.objects.filter(supporter=supporter, support_user=supported_user).update(supporter_message4=support_message)
                                        return JsonResponse({'status':support_message, 'success': True})
                                else:
                                    Support.objects.filter(supporter=supporter, support_user=supported_user).update(supporter_message3=support_message)
                                    return JsonResponse({'status':support_message, 'success': True})
                            else:
                                Support.objects.filter(supporter=supporter, support_user=supported_user).update(supporter_message2=support_message)
                                return JsonResponse({'status':support_message, 'success': True})
                        else:
                            Support.objects.filter(supporter=supporter, support_user=supported_user).update(supporter_message1=support_message)
                            return JsonResponse({'status':support_message, 'success': True})
                    elif(Support.objects.filter(support_user=supported_user, user_message0__isnull=False).exists()):
                        Support.objects.filter(support_user=supported_user, ).update(
                            supporter = supporter,
                            supporter_message0 = support_message,
                        )
                        return JsonResponse({'status':support_message, 'success': True})
                    else:
                        return JsonResponse({'status':"پشتیبانی کاربر توسط اپراتور پشتیبان دیگری رزرو شده", 'success': False})
                except:
                    return JsonResponse({'status':"مشکل غیر منتظره ای رخ داده - پشتیبان گرامی لطفا با توسعه دهنده تماس حاصل فرمایید", 'success': False})
            else:
                # if user not sopporter:
                try:
                    pass
                except:
                    return JsonResponse({'status':"مشکل غیر منتظره ای رخ داده - پشتیبان گرامی لطفا با توسعه دهنده تماس حاصل فرمایید", 'success': False})
        else:
            return JsonResponse({'status':"برای ارسال پیام پشتیبانی ابتدا وارد سایت شوید یا ثبت نام کنید", 'success': False})
    else:
        return JsonResponse({'status':"درخواست معتبر نیست", 'success': False})