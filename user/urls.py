from django.urls import path
from .views import RegisterView, LoginView, WishlistView, ResetPasswordView, AccountView

app_name = 'user'

urlpatterns = [
    path('', AccountView, name='register'),
    path('login/', LoginView, name='login'),
    path('register/', RegisterView, name='logout'),
    path('wishlist/', WishlistView, name='wishlist'),
    path('reset-password/', ResetPasswordView, name='reset_password'),
]