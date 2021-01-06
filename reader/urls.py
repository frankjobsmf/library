from django.urls import path

#knox
from knox.views import LogoutView

#views
from .views import (
    ListReaderAPI,
    RegisterReaderAPI,
    LoginReaderAPI,
    ListReaderAPI,
    UpdateReaderProfileAPI,
)

urlpatterns = [
    path('readers', ListReaderAPI.as_view(), name='readers'),
    path('reader-register', RegisterReaderAPI.as_view(), name='reader-register'),
    path('reader-login', LoginReaderAPI.as_view(), name='reader-login'),
    path('reader-logout', LogoutView.as_view(), name='reader-logout'),
    path('reader-profile', ListReaderAPI.as_view(), name='reader-profile'),
    path('reader-profile-update', UpdateReaderProfileAPI.as_view(), name='reader-profile-update'),
]
