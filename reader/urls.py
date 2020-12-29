from django.urls import path

#views
from .views import (
    ListReaderAPI,
    RegisterReaderAPI,
    LoginReaderAPI,
    ListReaderAPI,
)

urlpatterns = [
    path('readers', ListReaderAPI.as_view(), name='readers'),
    path('reader-register', RegisterReaderAPI.as_view(), name='reader-register'),
    path('reader-login', LoginReaderAPI.as_view(), name='reader-login'),
    path('reader-profile', ListReaderAPI.as_view(), name='reader-profile'),
]
