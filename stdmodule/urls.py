from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('menu/', views.menu, name='menu'),
    path('login/',views.login, name='login'),
    path('about/',views.about, name='about'),
    path('documentation/',views.contact, name='documentation'),



    path('menu2/', views.menu2, name='adminnav'),
    path('ahome/',views.ahome, name='teacherhome'),
    path('studentregister/',views.studentregister, name='addstudent'),
    path('studentview/',views.studentview, name='viewstudent'),
    path('markupdate/',views.markupdate, name='markupdate'),
    path('feedbackview/', views.feedbackview, name='viewfeedback'),
    path('sendemail/',views.sendemail, name='sendemail'),


    path('menu3/',views.menu3, name='studentnav'),
    path('shome/',views.shome, name='studenthome'),
    path('studentviewdetails/', views.studentviewdetails, name='markview'),
    path('feedbackupload/',views.feedbackupload, name='sendfeedback'),

    path('upload/', views.upload, name='upload'),
    path('display/', views.display, name='display'),
]

if settings.DEBUG:
    urlpatterns += static( settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)