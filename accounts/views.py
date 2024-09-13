from django.shortcuts import render
from django.http import HttpResponse 
from django.contrib.auth.models import AbstractUser
from .models import User
from products.models import Order
from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, login, authenticate
from django.views.generic import CreateView
from .forms import UserForm
# from .models import User



@login_required
def show_profile(request):
    orders = Order.objects.filter(user=request.user)
    return render(request, 'accounts/user_profile.html', {'orders': orders})


class CreateUserView(CreateView):
    model = User
    form_class = UserForm
    template_name = 'registration/signup.html'
    success_url = '/accounts/login'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect(reverse('login'))

def logout_user(request):
    logout(request)
    return redirect('http://127.0.0.1:8000/project/')


# from django.shortcuts import render, redirect, get_object_or_404
# from django.contrib.auth.decorators import login_required
# from .forms import UserUpdateForm

# @login_required
# def update_user(request):
#     user = request.user  
#     if request.method == 'POST':
#         form = UserUpdateForm(request.POST, request.FILES, instance=user)
#         if form.is_valid():
#             form.save()
#             return redirect('profile')  
#     else:
#         form = UserUpdateForm(instance=user)
#     return render(request, 'accounts/update_user.html', {'form': form})



