"""portafolios URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from portafolios.views import primera_p
from portafolioapp.views import contacto, index,enviar
from clima.views import indexclima
from noteblock.views import notes,save_note,delete_event,save_note_guarda
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # app portafolios
    path('admin/', admin.site.urls),
    path('index/', index),
    path('contacto/', contacto),
    path('contacto/enviar/', enviar),
    # app notes
    path('notes/', notes),
    path('save_note/',save_note),
    path('save_note/guarda/',save_note_guarda),
    path('delete_event/<int:noteblock_id>',delete_event, name='delete_event'),
    # app notes clima
    path('indexclima/',indexclima),
 
    
 
    


] +static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)




