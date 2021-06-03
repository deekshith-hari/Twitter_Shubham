from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from .models import Post

# def index(render):
#     return HttpResponse('HELLO')

from .forms import PostForm 
# from .forms import UpdateForm 
from cloudinary.forms import cl_init_js_callbacks

# Create your views here.

def index(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
        else:
            return HttpResponseRedirect(form.errors.as_json())

    posts = Post.objects.order_by('created_at').reverse().all()[:20]
    # Tweet.objects.order_by('created_at').reverse().all()[:20]

    return render(request, 'posts.html', 
                  {'posts': posts}) 
def delete(request, post_id):
    post = Post.objects.get(id = post_id)
    post.delete()
    return HttpResponseRedirect('/')
    
def edit(request, post_id):
     post = Post.objects.get(id = post_id)
     print(post)
     if request.method == 'POST':
         form = PostForm(request.POST, request.FILES, instance=post)
         if form.is_valid():
             form.save()
             return HttpResponseRedirect('/')
         else:
             return HttpResponseRedirect(form.errors.as_json())
     else:
    # Show editting screen
        form = PostForm
        return render(request, 'edit.html',
        {'post': post, 'form': form})


def postLikeAdd(request,post_id):
  
    post = Post.objects.get(id = post_id)
  
    new_like_count = post.like_count + 1
    post.like_count = new_like_count
  
    print(post.like_count)
    post.save()

    return HttpResponseRedirect('/')  