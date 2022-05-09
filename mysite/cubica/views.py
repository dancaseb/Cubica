from django.shortcuts import render,redirect
from django.shortcuts import get_object_or_404
# Create your views here.
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import CommentForm, PostForm, AddToGroup, ChangePicture
from .models import Post, SubCube, Person,Comment,Achievement
from message.forms import ShareForm
#from django.contrib.auth import login
#from django.contrib import messages


@login_required
def index(request):
    #latest_post_list = Post.objects.order_by('-pub_date')
    #context = {'latest_post_list': latest_post_list}
  
    post_list = Post.objects.order_by('?')
    comment_list = Comment.objects.order_by('?')
    subcube_list = SubCube.objects.order_by('?')
    context = {}
    if not post_list:
        context['post']= None
    else:
        post = post_list[0]
        context['post'] = post
    if not comment_list:
        context['comment']= None
    else:
        comment = comment_list[0]
        context['comment'] = comment
    if not subcube_list:
        context['subcube']= None
    else:
        subcube = subcube_list[0]
        context['subcube'] = subcube



    return render(request, 'cubica/index.html',context)

# @login_required
# def pos(request):
#     latest_post_list = Post.objects.order_by('-pub_date')
#     context = {'latest_post_list': latest_post_list}
#     return render(request, 'cubica/entry.html', {})

#shows latest posts
@login_required
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

@login_required
def share(request,sub_id, post_id):
    share_form = ShareForm()
    return render(request,'message/share.html', {'share_form':share_form,'sub_id':sub_id, 'post_id':post_id})

#def logout(request):
    #return render(request, 'registration/logout.html', {})

@login_required
def groups(request):
    groups = SubCube.objects.order_by('subname')

    context = {'groups':groups}
    return render(request, 'cubica/groups.html',context)

@login_required
def group_detail(request,sub_id):
    group = get_object_or_404(SubCube, pk=sub_id) 
    post_form = PostForm()
    addtogroup_form = AddToGroup()
    #people = group.people.all()
    posts = Post.objects.filter(subcube=group)
    # for p in people:
    #     post_tmp = Post.objects.filter(subcube=sub_id)
    #     for i in post_tmp:
    #         posts.append(i)
    posts.order_by('pub_date')
    current_user = request.user
    person = get_object_or_404(Person, user=current_user) 
    return render(request, 'cubica/group_detail.html', {'group': group, 'post_form':post_form,'addtogroup_form':addtogroup_form, 'posts':posts, 'person':person}) 

@login_required
def myprofile(request):
    current_user = request.user
    person = get_object_or_404(Person, user=current_user) 
    change_picture = ChangePicture()
    achievements = person.achievements.all()
    return render(request,'cubica/myprofile.html', {'person':person,'change_picture':change_picture,'achievements':achievements})

@login_required
def profile(request,person_id):
    person = get_object_or_404(Person, pk=person_id)
    change_picture = ChangePicture()
    achievements = person.achievements.all()
    return render(request,'cubica/profile.html', {'person':person, 'change_picture':change_picture,'achievements':achievements})

@login_required
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
            a = Achievement.objects.filter(name='has_comment')
            if not profile.achievements.contains(a.first()):
                profile.achievements.add(a.first())
            comment.save()

            return redirect('cubica:detail', post_id=post.id)

@login_required
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
            #add achievement if not contained
            a = Achievement.objects.filter(name='has_post')
            if not profile.achievements.contains(a.first()):
                profile.achievements.add(a.first())
            post = Post(post_name= name, subcube=subcube, person=profile, post_text = text, pic = image)
            
            post.save()
            return redirect('cubica:group_detail', sub_id = sub_id)

@login_required
def addtogroup(request, sub_id):
    subcube = get_object_or_404(SubCube, pk=sub_id)
    current_user = request.user
    profile = get_object_or_404(Person, user=current_user) 
    if request.method == 'POST':
        addtogroup_form = AddToGroup(request.POST)
        if addtogroup_form.is_valid():
            person_ids = []
            people_in_sub = subcube.people.all()
            for p in people_in_sub:
                person_ids.append(p.id)
            person_ids.append(profile.id)
            profiles = Person.objects.filter(id__in=person_ids)
            subcube.people.set(profiles)
            a = Achievement.objects.filter(name='has_subcube')
            if not profile.achievements.contains(a.first()):
                profile.achievements.add(a.first())
            return redirect('cubica:group_detail', sub_id = sub_id)
@login_required
def changepicture(request, person_id):
    person = get_object_or_404(Person, pk=person_id)
    if request.method == 'POST':
        changepicture_form = ChangePicture(request.POST, request.FILES)
        if changepicture_form.is_valid():
            picture = request.FILES['profile_pic']
            
            person.profile_pic= picture
            person.save()
            
            
            #return redirect('cubica:profile', person_id = person_id)
            return redirect('cubica:myprofile')

    
