from django.urls import path
from . import views

urlpatterns = [
    path('', views.homePage, name="homePage"),
    path('signin/', views.signin, name="signin"),
    path('logout/', views.logout, name='logout'),

   ## path('WebcamInvigilation/', views.WebcamInvigilation, name='WebcamInvigilation'),
    path('SmartInvigilationProject/', views.SmartInvigilationProject, name='SmartInvigilationProject'),
    path('record_video/', views.record_video, name='record_video'),
    path('recording_video_page/', views.recording_video_page, name='recording_video_page'),

    path('starting_page/', views.starting_page, name='starting_page'),
    path('wifi_page/', views.wifi_page, name='wifi_page'),

]