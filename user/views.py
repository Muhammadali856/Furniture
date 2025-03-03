from django.shortcuts import render



def AccountView(request):
    return render(request, 'auth/account.html')

def RegisterView(request):
    return render(request, template_name='auth/register.html')

def LoginView(request):
    return render(request, 'auth/login.html')

def WishlistView(request):
    return render(request, 'auth/user_wishlist.html')

def ResetPasswordView(request):
    return render(request, 'auth/reset_password.html')
