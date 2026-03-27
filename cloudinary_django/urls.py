from django.urls import path
from .views import upload_3d_model

urlpatterns = [
    path('imagen/', upload_3d_model, name='upload_3d_model'),
]
