from django.contrib import admin
from django.urls import path
from home.views import *
from food.views import *
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', home, name="home"),
    path('recipies/',recipies,name="recipies"),
    
    path('delete-recipe/<id>/', delete_recipe, name="delete_recipe"),
    path('update-recipe/<id>/', update_recipe, name="update_recipe"),

    path('contact/', contact, name="contact"),
    path('about/', about, name="about"),
    path('login/', login_page, name="login_page"),
    path('register/', register, name="register"),

    path('logout/', logout_page, name="logout_page"),

    path('success-page/', success_page, name = "success_page"),
    
    path('admin/', admin.site.urls),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

urlpatterns  += staticfiles_urlpatterns()