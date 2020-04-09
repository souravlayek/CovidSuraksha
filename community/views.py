from django.shortcuts import render,redirect,get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView
from .forms import PostForm,CommentForm
from .models import Post,Comments
from django.shortcuts import _get_queryset
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.template.loader import render_to_string,get_template
from django.http import JsonResponse,HttpResponse


def get_object_or_notfound(klass, *args, **kwargs):
    queryset = _get_queryset(klass)

    try:
        return queryset.filter(*args, **kwargs)
    except:
        return False


@login_required
def PostCreate(request):
    if request.method == 'POST':
        forms = PostForm
        form = forms(request.POST, request.FILES)
        if form.is_valid():
            instances = form.save(commit=False)
            instances.author = request.user
            instances.save()
            return redirect('community:communityhome')
    else:
        form = PostForm
        return render(request, 'community/feed.html', {'form':form})

@login_required
def AddPost(request):
    if request.method == 'POST':
        forms = PostForm
        form = forms(request.POST, request.FILES)
        if form.is_valid():
            instances = form.save(commit=False)
            instances.author = request.user
            instances.save()
            return redirect('community:communityhome')
    else:
        form = PostForm
        return render(request, 'community/newpost.html', {'form':form})

@login_required
def PostView(request):
    post = _get_queryset(Post)
    form = PostForm
    # maylike = post
    return render(request,'community/feed.html',{'posts': post, 'form': form, 'nots': post[:10]})

    
@login_required
def like_post(request,id):
    post = get_object_or_404(Post,id=id)
    post.likes_count +=1
    post.save()
    context = {
        'post': post,
    }
    if request.is_ajax():
        html = render_to_string('partials/_likes.html',context,request=request)
        return JsonResponse({'data':html})

@login_required
def dislike_post(request,id):
    post = get_object_or_404(Post,id=id)
    post.dislikes_count +=1
    post.save()
    context = {
        'post': post,
    }
    if request.is_ajax():
        html = render_to_string('partials/_likes.html',context,request=request)
        return JsonResponse({'data':html})
@login_required
def CommentPost(request,id):
    post = get_object_or_404(Post, id=id)
    if request.method == 'POST':
        forms = CommentForm
        form = forms(request.POST, request.FILES)
        if form.is_valid():
            instances = form.save(commit=False)
            instances.post = post
            instances.writter = request.user.first_name + ' ' + request.user.last_name
            instances.save()
            post_instances = post
            post_instances.comment_count += 1
            post_instances.save()
            return redirect('community:comment', id=id)
    else:
        form = CommentForm
        comments = get_object_or_notfound(Comments, post = post)
        return render(request, 'community/comment.html', {'form':form,'comments':comments,'post':post})
@login_required
def search(request):
    if request.GET:
        search_term = request.GET['search_term']
        search_results = _get_queryset(Post).filter(
            Q(community_type__iexact=search_term) |
            Q(title__icontains=search_term) |
            Q(content__icontains=search_term) |
            Q(tags__icontains=search_term)
        )
        form = PostForm
        context = {
            'search_term': search_term,
            'posts': search_results,
            'form':form
        }
        print(search_results)
        return render(request, 'community/feed.html', context)
    else:
        return redirect('home')
@login_required
def filterpost(request,filter_by):
    if filter_by != "all":
        filter_results = _get_queryset(Post).filter(community_type=filter_by)
    else:
        filter_results = _get_queryset(Post)
    form = PostForm
    return render(request,'community/feed.html',{'posts':filter_results,'form':form})
@login_required
def sortpost(request,sort_by):
    if sort_by != "all":
        sort_results = _get_queryset(Post).order_by(sort_by)
    else:
        sort_results = _get_queryset(Post)
    form = PostForm
    return render(request,'community/feed.html',{'posts':sort_results,'form':form})
