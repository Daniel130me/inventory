from django.contrib.auth import login
from django.http import JsonResponse
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_staff = True
            user.is_superuser = True
            user.save()
            login(request, user)
            return JsonResponse({'success': True})
        else:
            errors = form.errors.as_json()
            return JsonResponse({'success': False, 'errors': errors})
    else:
        form = CustomUserCreationForm()
    return render(request, 'user/register.html', {'form': form})

# def login(request):
#     form = AuthenticationForm()
#     return render(request, 'user/login.html', {'form':form})
    # login()
    # print('kkkk')
    # if request.method == 'POST':
    #     form = CreateUserForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return JsonResponse({'redirect_url': '/login/'})
    #     else:
    #         errors = form.errors.as_json()
    #         return JsonResponse({'errors': errors}, status=400)
    
    # form = CreateUserForm()
    # context = {
    #     'form':form,
    # }
    # return render(request, 'user/register.html')
    # return render(request, 'user/register.html',context)


    # if request.method == 'POST':
	#     form = CreateUserForm(request.POST)
	#     if form.is_valid():
	# 		form.save()
	# 		return JsonResponse({'redirect_url': '/login/'})
	# 	else:
	# 		errors = form.errors.as_json()
	# 		return JsonResponse({'errors': errors}, status=400)
	# else:
	# 	form = CreateUserForm()

	# return render(request, 'register.html', {'form': form})





    

def profile(request):
    return render(request, 'user/profile.html')