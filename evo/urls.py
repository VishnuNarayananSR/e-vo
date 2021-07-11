from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.homepage, name='home'),
    path('candidates/', include('candidates.urls')),
    path('voters/', include('voters.urls')),
    # path('cam/', views.cam_page),
    path("cam/", views.cam_stream),
    path('signal/', views.cam_stream, name="video_stream")
]
urlpatterns += staticfiles_urlpatterns()