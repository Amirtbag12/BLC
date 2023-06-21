from .models import Comments, Comments_like

''''def like_items(request):
    if request.user.is_authenticated:
        like = Comments_like.objects.all()
    else:
        like = 0
    return {'like_items': like}

def comment_items(request):
    if request.user.is_authenticated:
        comment = Comments.objects.filter(post=post)
    else:
        comment = 0
    return {'comment_items': comment}
    
                'index.context_processors.comment_items',
                'index.context_processors.like_items',
    '''