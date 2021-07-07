from django.shortcuts import render, get_object_or_404, redirect 
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView,  CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from .models import Like, Post
from users.models import Profile
# from .forms import PictureUpdateForm

# Create your views here.
# @login_required
# def home(request):
#     context = {
#         'posts': Post.objects.all(),
#         # 'pictures':Post_pictures.objects.all()    
            
#     }
#     return render(request, 'blog/home.html', context)

def like_unlike_post(request):
    user = request.user
    if request.method == 'POST':
        post_id = request.POST.get('post_id')
        post_obj = Post.objects.get(id=post_id)
        profile = Profile.obects.get(user=user)

        if profile in post_obj.liked.all():
            post_obj.liked.remove(profile)
        else:
            post_obj.liked.add(profile)

        like, created = Like.objects.get_or_create(user=profile, post_id=post_id)

        if not created:
            if like.value=='Like':
                like.value='Unlike'
            else:
                like.value ='Like'
        else:
           like.value = 'Like' 
           

           post_obj.save()
           like.save()
    # return redirect('blog:main-post-view')

class PostListView(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering =  ['-dateposted']
    paginate_by = 5






class UserPostListView(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'blog/user_posts.html'
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-dateposted')



class PostDetailView(LoginRequiredMixin, DetailView):
    model = Post

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['content','picture']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['content', 'picture']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False   



# class PostCreateViews(LoginRequiredMixin, UserPassesTestMixin, ListView):
#     model = Post_pictures
#     context_object_name = 'post_picture'
#     template_name = 'blog/galery.html'
#     fields = ['picture', 'comment']

    



class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def gallery(request):
    if request.method == 'POST':
        p_form = PictureUpdateForm(request.POST, instance = request.user)
        

        if p_form.is_valid():
           
            p_form.save()

        return redirect('profile')    

    else:
        p_form = PictureUpdateForm(instance = request.user)
           

    context = {
        'p_form' : p_form,
    }

    return render(request, 'blog/gallery.html',context)

def addPhoto(request):
    return render(request, 'blog/add.html')

def viewPhotos(request, pk):
    return render(request, 'blog/photos.html')


   