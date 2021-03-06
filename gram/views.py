from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse,Http404
from .models import Image,Profile,Comments
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from .forms import NewPostForm,SignUpForm,EditProfileForm,CommentForm
from django.contrib import messages
from django.contrib.auth import logout



# Create your views here.

@login_required(login_url = '/accounts/login/')
def timeline(request):
    '''
    Function to render the homepage
    '''
    timeline_pics = Image.all_images()
    return render(request,'timeline.html',{"timeline_pics":timeline_pics})
    

def like(request,id):
    '''
    Function to like a post
    '''
    image = get_object_or_404(Image,id=request.POST.get('ig_pic_id'))
    user = request.User
    image.likes.add(user)
    return (redirect,'timeline')

@login_required(login_url = '/accounts/login/')
def new_post(request):
    '''
    Function that uploads a new post
    '''
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
    '''
    Function that sends email on sign up
    '''
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
    '''
    Function that renders the active user's profile
    '''
    my_posts = Image.user_pics(request.user)
    return render(request,'profile.html',{'my_posts':my_posts})

@login_required(login_url = '/accounts/login/')
def edit_profile(request):
    '''
    Function that updates profile information
    '''
    if request.method=='POST':
        form = EditProfileForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('profile')

    else:
        form = EditProfileForm(instance=request.user)
    return render(request,'update_profile.html',{'form':form})

@login_required(login_url = '/accounts/login/')
def comment(request,id):
    '''
    Function for commenting on a post,Args:id The id of the post
    '''
    id =id
    if request.method=='POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            image = Image.objects.get(id = id)
            comment.ig_pic_id = image
            comment.save()
            return redirect('timeline')

        else:
            pic_id = id
            messages.info(request,'Make sure you fill all fields correctly')
            return redirect('comment',id=pic_id)
    else:
        id = id
        form =CommentForm()
        return render(request,"comment.html",{'form':form,"id":id})
        


@login_required(login_url = '/accounts/login/')
def single_pic(request,id):
    '''
    Function for getting just a single post
    Args:id The id of the post
    '''
    post = Image.objects.get(id = id)
    comments = Comments.objects.filter(ig_pic_id = id)
    return render(request,'single_pic.html',{'post':post,"comments":comments})

@login_required(login_url = '/accounts/login/')
def search_results(request):
    '''
    Function for searching a post with its name
    '''
    if 'image' in request.GET and request.GET['image']:
        search_term = request.GET.get('image')
        searched_pics = Image.search_image(search_term)
        message = f'{search_term}'

        return render(request,'search.html',{'message':message,'image':searched_pics})

    else:
        message = "You have not entered anything to search"
        return render(request,'search.html',{"message":message})

@login_required(login_url="/accounts/login/")
def logout_request(request):
  '''
  Function for logging out user
  '''

  logout(request)
  return redirect('timeline')
