from django.shortcuts import render
from django.shortcuts import get_object_or_404
# Create your views here.
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from .models import Post

@login_required
def index(request):
    latest_post_list = Post.objects.order_by('-pub_date')
    context = {'latest_post_list': latest_post_list}
    return render(request, 'cubica/index.html',context)


@login_required
def detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)  
    return render(request, 'cubica/detail.html', {'post': post})

def entry(request):
    return render(request,'cubica/entry.html', {})
