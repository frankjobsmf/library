from django.urls import path

#views
from .views import (
    ListReaderAPI,
    RegisterReaderAPI,
)

urlpatterns = [
    path('readers', ListReaderAPI.as_view(), name='readers'),
    path('reader-register', RegisterReaderAPI.as_view(), name='reader-register'),
]
