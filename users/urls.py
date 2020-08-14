from django.urls import path
from .views import SignUpView, PassWordEditView, ProfileEditView


urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('password_change/', PassWordEditView.as_view(), name='password_change'),
    path('edit_profile/', ProfileEditView.as_view(), name='edit_profile'),
]