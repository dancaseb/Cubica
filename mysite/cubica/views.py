from django.shortcuts import render
from django.shortcuts import get_object_or_404
# Create your views here.
from django.http import HttpResponse

from .models import Post


def index(request):
    latest_post_list = Post.objects.order_by('-pub_date')
    context = {'latest_post_list': latest_post_list}
    return render(request, 'cubica/index.html',context)



def detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'cubica/detail.html', {'post': post})