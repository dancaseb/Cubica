from django.shortcuts import render, redirect
from django.http import HttpResponse
from cubica.models import Person, Post
from .models import Message
from .forms import ShareForm
from django.shortcuts import get_object_or_404


def index(request):
    return render(request, 'message/index.html', {})


def sent(request):
    current_user = request.user
    person = get_object_or_404(Person, user=current_user)
    messages = Message.objects.filter(sender=person).order_by('sent_date')
    return render(request, 'message/sent.html', {'messages': messages})


def received(request):
    current_user = request.user
    person = get_object_or_404(Person, user=current_user)
    messages = Message.objects.filter(receiver=person).order_by('sent_date')

    return render(request, 'message/received.html', {'messages': messages})

# post_id je id postu, ktery se bude sdilet


def newmessage(request, sub_id, post_id):

    post = get_object_or_404(Post, pk=post_id)

    current_user = request.user
    sender = get_object_or_404(Person, user=current_user)
    if request.method == 'POST':

        share_form = ShareForm(request.POST)

        if share_form.is_valid():

            text = share_form.cleaned_data['text']
            receiver = share_form.cleaned_data['receiver']
            if receiver.id == sender.id:
                return render(request, 'message/error.html', {'sub_id': sub_id})
            message = Message(sender=sender, receiver=receiver,
                              shared_post=post, text=text)
            message.save()

            return redirect('cubica:group_detail', sub_id=post.subcube.id)


# Create your views here.
