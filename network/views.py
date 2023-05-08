
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django import forms
from datetime import datetime
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
import json
from .models import *
from django.core.paginator import Paginator



class NewPost(forms.Form):
    New_Post = forms.CharField(widget=forms.Textarea(attrs={'name':'b', 
                                                        'style': 'height: 6rem; width: 100%; display:block; border-radius:1rem; padding: 10px; font-size: 16px;'}))

          
def index(request):
    posts_list = Post.objects.all().order_by('-time')
    paginator = Paginator(posts_list, 10)  # Show 10 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    liked_posts = []
    if request.user.is_authenticated:
        # liked or not
        liked_posts = request.user.liked_posts.all().values_list('id', flat=True)

    next = False
    if posts_list.count() > 10:
        next = True

    return render(request, "network/index.html", {
        "posts": page_obj,
        "form": NewPost,
        "user": request.user,
        "liked_posts": liked_posts,
        "next": next
    })



def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "network/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "network/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "network/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "network/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "network/register.html")

@login_required
def newPost(request):
    if request.method == 'POST':
        
        usernames = request.user

        forming = NewPost(request.POST)

        today = datetime.today()
        d = str(today.strftime("%B %d, %Y %I:%M %p")) 
        
        if forming.is_valid():
            new_content = forming.cleaned_data['New_Post']
            Post.objects.create(user = usernames, content = new_content, timestamp = d, time = today)

            return HttpResponseRedirect(reverse('index'))
    else:        
        return HttpResponseRedirect(reverse('index'))

def profile(request, profile):

    user = get_object_or_404(User, username=profile)

    posts_list = Post.objects.filter(user=user).order_by('-time')
    paginator = Paginator(posts_list, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    next = False
    if posts_list.count() > 10:
        next = True

    liked_posts = []
    if request.user.is_authenticated:
        for post in posts_list:
            if post.likes.filter(id=request.user.id).exists():
                liked_posts.append(post.id)

        following = request.user.following.filter(id=user.id).exists()
        my_own_profile = request.user.username == user.username

        return render(request, 'network/profile.html', {
            "profile": user,
            "user_posts": page_obj,
            "following": following,
            "liked_posts": liked_posts,
            "next": next,
            "my_own_profile": my_own_profile
        })
    return render(request, 'network/profile.html', {
        "profile": user,
        "user_posts": page_obj,
        "next": next
    })


def follow(request, profile):
    if request.method == "POST":
        followed_user = User.objects.get(username=profile)
        following_user = request.user

        if following_user != followed_user:
            following_user.following.add(followed_user)
            return HttpResponseRedirect(reverse('profile', kwargs={"profile": profile}))
        else:
            return JsonResponse({"error": "You cannot follow yourself."}, status=400)


def unfollow(request, profile):
    if request.method == "POST":
        unfollowed_user = User.objects.get(username=profile)
        unfollowing_user = request.user

        unfollowing_user.following.remove(unfollowed_user)
        return HttpResponseRedirect(reverse('profile', kwargs={"profile": profile}))   
     
def following(request):
    if request.user.is_authenticated:
        user = request.user
        all_following = user.following.all()

        posts = []
        for i in all_following:
            foo = Post.objects.filter(user=i)
            for bar in foo:
                posts.append(bar)

        posts.sort(key=lambda x: x.time, reverse=True)

        paginator = Paginator(posts, 10)  # Show 10 contacts per page.
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        next = False
        if len(posts) > 10:
            next = True

        liked_posts = []
        if request.user.is_authenticated:
            liked_posts = [post.id for post in user.liked_posts.all()]

        return render(request, 'network/following.html', {
            "following_posts": page_obj,
            "liked_posts": liked_posts,
            "next": next
        })

    return render(request, 'network/following.html', {
        "following_posts": [],
        "message": "There are no posts in this section!"
    })

    
@csrf_exempt
def like(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        post_id = data['post_id']
        post = get_object_or_404(Post, id=post_id)
        liked = request.user in post.likes.all()

        if liked:
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return JsonResponse({'liked': not liked, 'likes_count': post.likes.count()}, status=200)

            


@csrf_exempt
def edit(request):
    if request.method == "POST" and request.user.is_authenticated:
        data = json.loads(request.body)
        user_id = data.get("user_id")
        id = data.get("id")
        new_content = data.get("body")

        if int(user_id) == int(request.user.id):
            post = Post.objects.get(pk=id)
            post.content = new_content
            post.save()

        return JsonResponse({"id": id, "content": new_content}, safe=False)

    return False
