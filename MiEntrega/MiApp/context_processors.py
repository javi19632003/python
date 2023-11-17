from django.contrib.auth.context_processors import auth
from .models                                import User1
from django.conf                            import settings

def custom_avatar(request):
    context = auth(request)
    user = context['user']
    if user.is_authenticated:
        try:
            image = User1.objects.get(user= request.user.id)
            mi_avatar = image.dame_ruta()
        except:
            mi_avatar = ""
            
        if len(mi_avatar) > 0:
            context['mi_avatar'] = mi_avatar
        else:
            context['mi_avatar'] = f"{settings.MEDIA_URL}avatares/generico.png"
    return context        
                
                
