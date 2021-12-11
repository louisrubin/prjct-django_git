from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

# Create your views here.

from .models import Post

class Inicio(ListView):
    template_name = "posts/posts.html"
    model = Post
    context_object_name = "posts"
        
    # return de query + filter
    def get_queryset(self):
        # self.request
        return Post.objects.all().order_by("id")