from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from .forms import PostForm
from .forms import EditForm
from django.urls import reverse_lazy

# Create your views here.
#def index(request):
	#return render(request, 'myblog/index.html', {})

class IndexView(ListView):
	model = Post
	template_name = 'myblog/index.html'
	#ordering = ['-id']
	ordering = ['-post_date']

class ArticleDetailView(DetailView):
	model = Post
	template_name = 'myblog/article_details.html'

class AddPostView(CreateView):
	model = Post
	form_class = PostForm
	template_name = 'myblog/add_post.html'
	#fields = '__all__'
	#fields = ('title', 'body')

class UpdatePostView(UpdateView):
	model = Post
	form_class = EditForm
	template_name = 'myblog/update_post.html'
	#fields = ['title', 'title_tag', 'body']

class DeletePostView(DeleteView):
	model = Post
	template_name = 'myblog/delete_post.html'
	success_url = reverse_lazy('index')
