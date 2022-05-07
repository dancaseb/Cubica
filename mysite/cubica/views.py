from django.shortcuts import render,redirect
from django.shortcuts import get_object_or_404
# Create your views here.
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import CommentForm, PostForm
from .models import Post, SubCube, Person,Comment

@login_required
def index(request):
    #latest_post_list = Post.objects.order_by('-pub_date')
    #context = {'latest_post_list': latest_post_list}
    context = {}
    post_list = Post.objects.order_by('?')
    if len(post_list) >=4:
        first_posts = post_list[:2]
        second_posts = post_list[2:4]
        context = {'first_posts':first_posts, 'second_posts':second_posts}

    return render(request, 'cubica/index.html',context)

# @login_required
# def pos(request):
#     latest_post_list = Post.objects.order_by('-pub_date')
#     context = {'latest_post_list': latest_post_list}
#     return render(request, 'cubica/entry.html', {})

#shows latest posts
def latest(request):
    post_list = Post.objects.order_by('-pub_date')
    latest_post_list = post_list[0:5]
    context = {'latest_post_list': latest_post_list}
    return render(request, 'cubica/latest.html',context)

@login_required
def detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    comment_form = CommentForm()

    return render(request, 'cubica/detail.html', {'post': post, 'comment_form':comment_form})

def entry(request):
    return render(request,'cubica/entry.html', {})

def logout(request):
    return render(request, 'cubica/logout.html', {})

@login_required
def groups(request):
    groups = SubCube.objects.order_by('?')

    context = {'groups':groups}
    return render(request, 'cubica/groups.html',context)

@login_required
def group_detail(request,sub_id):
    group = get_object_or_404(SubCube, pk=sub_id) 
    post_form = PostForm()
    return render(request, 'cubica/group_detail.html', {'group': group, 'post_form':post_form}) 

@login_required
def profile(request):
    current_user = request.user
    person = get_object_or_404(Person, user=current_user) 
    return render(request,'cubica/profile.html', {'person':person})

def postcomment(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if request.method == 'POST':
        
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            text = comment_form.cleaned_data['comment_text']
            #ziskam aktualne prihlaseneho usera
            current_user = request.user
            profile = get_object_or_404(Person, user=current_user) 
            comment = Comment(post=post, comment_text=text, person=profile)
            comment.save()

            return redirect('cubica:detail', post_id=post.id)

def addpost(request, sub_id):

    subcube = get_object_or_404(SubCube, pk=sub_id)
    current_user = request.user
    profile = get_object_or_404(Person, user=current_user) 
    if request.method == 'POST':
        post_form = PostForm(request.POST, request.FILES)
        if post_form.is_valid():
            text = post_form.cleaned_data['post_text']
            name = post_form.cleaned_data['post_name']
            image = post_form.cleaned_data['pic']
            
            post = Post(post_name= name, subcube=subcube, person=profile, post_text = text, pic = image)
            post.save()
            return redirect('cubica:group_detail', sub_id = sub_id)
    

    