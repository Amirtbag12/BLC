from django.views.decorators.csrf import csrf_exempt
from django.http import HttpRequest, JsonResponse
from django.shortcuts import render, redirect
from .serializers import CartSerializer #support_serialize
from .models import Support


@csrf_exempt
def post_message(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            message = request.POST.get('support_message')
            support_room = request.POST.get('support_room')
            user = request.user.phoneNumber
            support = Support.objects.create(room=support_room, support_user=user, message=message)
            return JsonResponse({'message': support.message, 'timestamp': support.timestamp.isoformat()})
        else:
            return JsonResponse({'status':"برای ارسال پیام پشتیبانی ابتدا وارد سایت شوید یا ثبت نام کنید", 'success': False})
    else:
        return JsonResponse({'status':"درخواست معتبر نیست", 'success': False})

@csrf_exempt
def get_message(request):
    timestamp = request.GET.get('timestamp')
    support_room = request.GET.get('support_room')
    supports = Support.objects.filter(room=support_room, timestamp__gt=timestamp)
    response = [{'message': support.message, 'timestamp': support.timestamp.isoformat()} for support in supports]
    return JsonResponse({'messages': response})