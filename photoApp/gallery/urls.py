from django.urls import path, re_path

from .views import GalleryView, ImageList, Image

urlpatterns=[
    path('',GalleryView.as_view(),name='gallery'),
    path('photo/list/', ImageList.as_view()),
    path('photo/<int:pk>/',Image.as_view())

]