from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Profile
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate


def profile(request, id):
    profiles = Profile.objects.get(user__id=id)
    if 'subscribe' in request.POST:
        id = request.POST.get('user_id')
        post_obj = Post.objects.get(id=id)
        try:
            subscribe = Subscribe.objects.get(user=request.user, post=post_obj)
            subscribe.delete()
        except:
            subscribe.objects.create(user=request.user, post=post_obj)
    return render(request, 'profile.html', {"profile": profiles})


# def signup(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         nickname = request.POST.get('nickname')
#         image = request.FILES.get('image')
#         password1 = request.POST.get('password1')
#         password2 = request.POST.get('password2')
#         print(image)
#         if password1 == password2:
#             try:
#                 user = User.objects.create(username=username)
#                 user.set_password(password1)
#                 user.save()
#                 profile = Profile.objects.create(user=user, nickname=nickname, image=image)
#                 user = authenticate(username=username, password=password1)
#                 login(request, user)
#                 return redirect('index')
#             except:
#                 messages.error(request, 'Not correct some value')
#         else:
#             messages.error(request, 'Not correct password')
#     return render(request, 'login/singup.html')
#
#
# def login_user(request):
#     if request.method == 'POST':
#         try:
#             username = request.POST.get('username')
#             password = request.POST.get('password')
#             user = User.objects.get(username=username)
#             user = authenticate(username=username, password=password)
#             login(request, user)
#             return redirect('index')
#         except:
#             messages.error(request, 'Not correct login or password')
#     return render(request, 'users/login.html')


