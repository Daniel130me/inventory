from django.shortcuts import render, redirect
from .forms import CreateUserForm, ProfileUserForm
from django.contrib.auth.forms import AuthenticationForm
from django.http import JsonResponse
from django.contrib.auth import login, authenticate, logout
from .models import Profile
# Create your views here.
def register(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        # print(request.POST.get('username'))
        if form.is_valid():
            print("val")
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                print(request.user)
                print(request.user.email)
            return JsonResponse({'url_to':'../','message': 'success'})
        else:
            return JsonResponse({'message': 'Registration failed'})
    # form = CreateUserForm()
    
    return render(request, 'user/register.html')

# def profile_update(request):
#     if request.method == 'POST':
#         form = CreateUserForm(request.POST)
#         # profileform = ProfileUserForm(request.POST)
#         print('lid')
#         print(request.POST['username'])
#         if form.is_valid():
#             print('valid')
    
    
#     return JsonResponse({'message':'here'})


def signin(request):
    form = AuthenticationForm()

    if request.user.is_authenticated:
        return redirect('dashboard-index')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username = username, password=password)
        if user is not None:
            login(request, user)
            # return redirect('dashboard-index')
            return JsonResponse({'url_to': '../', 'message':'success'})
        else:
            return JsonResponse({'message':'username or password incorrect!'})
    return render(request, 'user/login.html', {'form':form})



def signout(request):
    logout(request)
    return redirect('user-login')
    
def profile_details(request):
    return render(request, 'user/profile_details.html')

def profile(request):
    if request.method == 'POST':
        request.user.username = request.POST['username']
        request.user.email = request.POST['email']
        request.user.save()

        request.user.profile.phone = request.POST['phone']
        request.user.profile.address = request.POST['address']
        request.user.profile.save()
        return JsonResponse({'message':'success'})
        
    return render(request, 'user/profile.html')


