from django.urls import path, include

from Petstagram.photos import views

urlpatterns = (
    path('add/', views.PhotoAddPage.as_view(), name='photo-add'),
    path('<int:pk>/', include([
        path('', views.PhotoDetailsPage.as_view(), name='photo-details'),
        path('edit/', views.PhotoEditPage.as_view(), name='photo-edit'),
        path('delete/', views.photo_delete, name='photo-delete'),
    ])),
)
