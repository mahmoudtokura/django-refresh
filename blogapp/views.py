from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator
from django.utils.text import slugify
from django.db.models import Q

from .models import Blog
from .forms import CreateBlogForm


def index(request):
    f_blogs = Blog.objects.filter(featured=True)
    context = {"f_blogs": f_blogs}
    return render(request, "blogapp/index.html", context)


def details(request, slug):
    blog = Blog.objects.get(slug=slug)
    context = {"blog": blog}
    return render(request, "blogapp/details.html", context)


@login_required(login_url="core:login")
def user_blogs(request):
    blogs = Blog.objects.filter(author=request.user)
    paginator = Paginator(blogs, 3)
    page = request.GET.get("page")
    blogs = paginator.get_page(page)
    context = {"blogs": blogs, "paginator": paginator}
    return render(request, "blogapp/user_blogs.html", context)


@login_required(login_url="core:login")
def create_blog(request):
    form = CreateBlogForm()
    if request.method == "POST":
        form = CreateBlogForm(request.POST, request.FILES)
        if form.is_valid():
            new_blog = form.save(commit=False)
            new_blog.author = request.user
            new_blog.slug = slugify(new_blog.title)
            new_blog.save()
            messages.success(request, "Blog Created Successfully")

            return redirect("blogapp:details", slug=form.instance.slug)
    context = {"form": form}
    return render(request, "blogapp/create_blog.html", context)


@login_required(login_url="core:login")
def update_blog(request, slug):
    blog = Blog.objects.get(slug=slug)
    if request.user != blog.author:
        return redirect("blogapp:details", slug=slug)
    form = CreateBlogForm(instance=blog)
    if request.method == "POST":
        form = CreateBlogForm(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            form.save()
            messages.success(request, "Blog Updated Successfully")
            return redirect("blogapp:details", slug=form.instance.slug)
    context = {"form": form}
    return render(request, "blogapp/create_blog.html", context)


@login_required(login_url="core:login")
def delete_blog(request, slug):
    blog = Blog.objects.get(slug=slug)
    if request.user != blog.author:
        return redirect("blogapp:details", slug=slug)
    blog.delete()
    messages.success(request, "Blog Deleted Successfully")
    return redirect("blogapp:index")


def search_blog(request):
    if request.method == "GET":
        search = request.GET.get("search")
        if search:
            blogs = Blog.objects.filter(
                Q(title__icontains=search) | Q(content__icontains=search)
            )
            if blogs.exists():
                context = {"blogs": blogs, "keyword": search}
                return render(request, "blogapp/search.html", context)
            else:
                messages.warning(request, "No Blogs Found")
                return redirect("blogapp:index")
        else:
            return redirect("blogapp:index")
    else:
        return redirect("blogapp:index")
