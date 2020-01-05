from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse,Http404
from .models import Image,Profile
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from .forms import NewPostForm,SignUpForm,EditProfileForm



# Create your views here.

@login_required(login_url = '/accounts/login/')
def timeline(request):
    timeline_pics = Image.all_images()
    return render(request,'timeline.html',{"timeline_pics":timeline_pics})
    

def like(request):
    image = get_object_or_404(Image,id=request.POST.get('ig_pic_id'))
    user = request.User
    image.likes.add(user)
    return (redirect,'timeline')

@login_required(login_url = '/accounts/login/')
def new_post(request):
    if request.method=='POST':
        form = NewPostForm(request.POST,request.FILES)
        if form.is_valid():
            post=form.save(commit=False)
            post.user = request.user
            post.save()

            return redirect('timeline')

    else:
        form = NewPostForm()
        
    return render(request,'new_post.html',{'form':form})

def signUp(request):
    if request.method=='POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            name=form.cleaned_data['username']
            email = form.cleaned_data['email']
            send=welcome_email(name,email)
            HttpResponseRedirect('timeline')

    else:
        form = SignUpForm()

    return render(request,'registration/registration_form.html',{'form':form})

@login_required(login_url = '/accounts/login/')
def profile(request):
    my_posts = Image.user_pics(request.user)
    return render(request,'profile.html',{'my_posts':my_posts})

@login_required(login_url = '/accounts/login/')
def edit_profile(request):
    if request.method=='POST':
        form = EditProfileForm(request.POST,request.FILES,instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect('profile')

        else:
            form = EditProfileForm(instance=request.user)
        return render(request,'profile.html',{'form':form})