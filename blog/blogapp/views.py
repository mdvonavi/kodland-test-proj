from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from blogapp.models import Post
from django.shortcuts import redirect
from django.utils import timezone
from django.views.generic.edit import CreateView
from django.views.generic import ListView
from django.urls import reverse_lazy # новый
 
from .forms import PostForm # новый



def home(request):
    postList = Post.objects.filter()
    paginator = Paginator(postList, 10)
    page = request.GET.get('page')
    posts = paginator.get_page(page)

    context = {
        "posts": posts,
        "title": "Главная страница блога",
        "desc": "Описание для главной страницы",
        "key": "ключевые, слова",
    }
    return render(request, "partial/home.html", context)

def single(request, id=None):
    post = get_object_or_404(Post, id=id)

    context = {
        "post": post,
    }
    return render(request, "partial/single.html", context)



class CreatePostView(CreateView): # новый
    model = Post
    form_class = PostForm
    template_name = 'post.html'
    success_url = reverse_lazy('home')

"""class HomePageView(ListView):
    model = Post
    template_name = 'partial/home.html'    """



