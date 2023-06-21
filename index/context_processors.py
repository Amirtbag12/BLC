from .models import Comments, Comments_like

def like_items(request, post):
    if request.user.is_authenticated:
        like = Comments_like.objects.filter(post=post)
    else:
        like = 0
    return {'like_items': like}

def comment_items(request):
    if request.user.is_authenticated:
        comment = Comments.objects.filter(post=post)
    else:
        comment = 0
    return {'comment_items': comment}