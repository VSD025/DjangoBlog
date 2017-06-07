from django.shortcuts import render, render_to_response
from django.utils import timezone
from .models import Post,Comment
from django.shortcuts import render, get_object_or_404
from .forms import PostForm
from django.shortcuts import redirect
from .forms import PostForm, CommentForm
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.views.generic.base import View
from django.contrib.auth import logout
from django.contrib.auth import login
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm



def search_form(request):
	return render(request,'blog/search_form.html')


def search(request):
    if 'inquiry' in request.GET and request.GET['inquiry']:
        inquiry = request.GET['inquiry']
        posts = Post.objects.filter(title__icontains=inquiry)
        return render_to_response('blog/post_list.html',{'posts': posts, 'query': inquiry})
    else:
        return HttpResponse('Please submit a search term!')



class RegisterFormView(FormView):
    form_class = UserCreationForm
    success_url = '/login/'
    template_name = 'blog/register.html'

    def form_valid(self, form):
        form.save()
        return super(RegisterFormView, self).form_valid(form)



class LoginFormView(FormView):
    form_class = AuthenticationForm
    template_name = 'blog/login.html'
    success_url = 'http://127.0.0.1:8000/'

    def form_valid(self, form):
        self.user = form.get_user()
        login(self.request, self.user)
        return super(LoginFormView, self).form_valid(form)



class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect('/')



def post_list(request):
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request,'blog/post_list.html',{'posts':posts})



def post_detail(request, pk):
	if request.user.is_authenticated:
		post = get_object_or_404(Post, pk=pk)
		comments = post.comments.filter(active=True)
		if request.method == "POST":
			comment_form = CommentForm(data=request.POST)
			if comment_form.is_valid():
				new_comment = comment_form.save(commit=False)
				new_comment.post = post
				new_comment.save()
			return redirect('post_detail',pk=post.pk)
		else:
			comment_form = CommentForm()
			return render(request,'blog/post_detail.html',{'post': post,'comments': comments,'comment_form': comment_form})




def post_new(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = PostForm(request.POST)
            if form.is_valid():
                post = form.save(commit=False)
                post.author = request.user
                post.published_date = timezone.now()
                post.save()
                return redirect('post_detail', pk=post.pk)
        else:
            form = PostForm()
        return render(request, 'blog/post_edit.html', {'form': form})





def post_edit(request, pk):
	if request.user.is_authenticated:
		post = get_object_or_404(Post, pk=pk)
		if request.user == post.author:
			if request.method == "POST":
				form = PostForm(request.POST, instance=post)
				if form.is_valid():
					post = form.save(commit=False)
					post.author = request.user
					post.published_date = timezone.now()
					post.save()
				return redirect('post_detail', pk=post.pk)
			else:
				form = PostForm(instance=post)
			return render(request, 'blog/post_edit.html', {'form': form})
		else:
			return render(request, 'blog/not_owner.html')



