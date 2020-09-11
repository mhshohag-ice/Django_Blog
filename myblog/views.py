from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Category
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

	def get_context_data(self, *args, **kwargs):
		cat_menu = Category.objects.all()
		context = super(IndexView, self).get_context_data(*args, **kwargs)
		context["cat_menu"] = cat_menu
		return context

def CategoryListView(request):
	cat_menu_list = Category.objects.all()
	return render(request, 'myblog/category_list.html',{'cat_menu_list': cat_menu_list})


def CategoryView(request, cats):
	category_posts = Post.objects.filter(category=cats.replace('-',' '))
	return render(request, 'myblog/categories.html', {'cats': cats.title().replace('-',' '), 'category_posts':category_posts})

class ArticleDetailView(DetailView):
	model = Post
	template_name = 'myblog/article_details.html'

	def get_context_data(self, *args, **kwargs):
		cat_menu = Category.objects.all()
		context = super(ArticleDetailView, self).get_context_data(*args, **kwargs)
		context["cat_menu"] = cat_menu
		return context

class AddPostView(CreateView):
	model = Post
	form_class = PostForm
	template_name = 'myblog/add_post.html'
	#fields = '__all__'
	#fields = ('title', 'body')

	def get_context_data(self, *args, **kwargs):
		cat_menu = Category.objects.all()
		context = super(AddPostView, self).get_context_data(*args, **kwargs)
		context["cat_menu"] = cat_menu
		return context

class AddCategoryView(CreateView):
	model = Category
	#form_class = PostForm
	template_name = 'myblog/add_category.html'
	fields = '__all__'
	#fields = ('title', 'body')

class UpdatePostView(UpdateView):
	model = Post
	form_class = EditForm
	template_name = 'myblog/update_post.html'
	#fields = ['title', 'title_tag', 'body']

	def get_context_data(self, *args, **kwargs):
		cat_menu = Category.objects.all()
		context = super(UpdatePostView, self).get_context_data(*args, **kwargs)
		context["cat_menu"] = cat_menu
		return context

class DeletePostView(DeleteView):
	model = Post
	template_name = 'myblog/delete_post.html'
	success_url = reverse_lazy('index')

	def get_context_data(self, *args, **kwargs):
		cat_menu = Category.objects.all()
		context = super(DeletePostView, self).get_context_data(*args, **kwargs)
		context["cat_menu"] = cat_menu
		return context
