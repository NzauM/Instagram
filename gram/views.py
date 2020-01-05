from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse,Http404
from .models import Image,Profile
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from .forms import NewPostForm



# Create your views here.

@login_required(login_url = '/accounts/login/')
def timeline(request):
    timeline_pics = Image.all_images()
    return render(request,'timeline.html',{"timeline_pics":timeline_pics})
    

def like(request):
    image = get_object_or_404(Image,id=request.POST.get(str('ig_pic.id')))
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