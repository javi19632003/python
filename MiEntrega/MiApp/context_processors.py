from django.contrib.auth.context_processors import auth
from .models                                import User1
from django.conf                            import settings

def custom_avatar(request):
    context = auth(request)
    user = context['user']
    print("en contexto")
    if user.is_authenticated:
        image = User1.objects.filter(user= request.user.id)[0]
        mi_avatar = image.dame_ruta()
        if len(mi_avatar) > 0:
            context['mi_avatar'] = mi_avatar
        else:
            context['mi_avatar'] = f"{settings.MEDIA_URL}avatares/generico.png"
    return context        
                