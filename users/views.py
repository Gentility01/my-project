from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm,UserUpdateForm,ProfileUpdateForm
from blog.models import Post, Profile







# Create your views here.
def register(request):
    if request.method == 'POST':
         form = UserRegisterForm(request.POST)
         if form.is_valid():
             form.save()
             username =form.cleaned_data.get('username')
             messages.success(request, f'Your account was created successfully you can login now')
             return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html',{'form':form})

@login_required
def profile(request):
    profile = Profile.objects.get(user = request.user)
    context = {
        'profile': profile,
    }
    return render(request, 'users/profile.html',context)

@login_required
def u_profile(request):
    if request.method == 'POST':
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance = request.user.profile)

        if   p_form.is_valid():
            p_form.save()
           

        messages.success(request, f'Your account has been updated!')
        return redirect('profile')    

    else:
        p_form = ProfileUpdateForm(instance = request.user.profile)    

    context = {
        
        'p_form' : p_form
    }
    
    return render(request, 'users/u_profile.html',context)

def cover_photo(request):
    return render(request, 'users/cover_photo.html')



@login_required
def edit_profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance = request.user)
        

        if u_form.is_valid():
           
            u_form.save()

        messages.success(request, f'Your account has been updated!')
        return redirect('profile')    

    else:
        u_form = UserUpdateForm(instance = request.user)
           

    context = {
        'u_form' : u_form,
    }
    return render (request,'users/edit_profile.html',context)





