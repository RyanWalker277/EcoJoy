from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .views import *
from .forms import *
from .models import *
from django.core.paginator import Paginator


@login_required(login_url="/login/")
def create_blog(request):
    try:
        context = {"form": BlogForm}
        if request.method == "POST":
            form = BlogForm(request.POST)
            title = request.POST.get("title")
            designation = request.POST.get("designation")
            facebook = request.POST.get("facebook")
            twitter = request.POST.get("twitter")
            instagram = request.POST.get("instagram")
            google = request.POST.get("google")
            cover_image = request.FILES["coverImage"]

            if form.is_valid():
                content = form.cleaned_data["content"]
                Blogs.objects.create(
                    title=title,
                    content=content,
                    author=request.user,
                    thumbnail=cover_image,
                    author_fb=facebook,
                    author_google=google,
                    author_twitter=twitter,
                    author_instagram=instagram,
                )
                return redirect("/blog/")
        return render(request, "createBlog.html", context)
    except Exception as e:
        print(e)
        return HttpResponse("Something went wrong!")


def show_comments(request, id):
    try:
        blog_id = Blogs.objects.get(id=id)
        comments = Comments.objects.filter(blog=blog_id).order_by("-created")
        page = request.GET.get("page", 1)
        p = Paginator(comments, 5)
        try:
            comments = p.page(page)
        except:
            comments = p.page(1)
        context = {"blog": blog_id, "comments": comments, "page_obj": comments}
        return render(request, "showComments.html", context)
    except Exception as e:
        print(e)


def blog(request):
    context = {}
    blogs = Blogs.objects.all().order_by("-created")
    recent_blogs = Blogs.objects.all().order_by("-created")
    page = request.GET.get("page", 1)
    p = Paginator(blogs, 6)
    try:
        blogs = p.page(page)
    except:
        blogs = p.page(1)
    return render(
        request,
        "blog.html",
        context={"blogs": blogs, "page_obj": blogs, "recent_blogs": recent_blogs},
    )


def blogpage(request, id):
    try:
        blog = Blogs.objects.get(id=id)
        comments_obj = Comments.objects.filter(blog=blog)
        context = {"blog": blog, "comments": comments_obj}
        if request.method == "POST" and not request.user.is_authenticated:
            name = request.POST.get("name")
            email = request.POST.get("email")
            comment = request.POST.get("comment")
            Comments.objects.create(
                blog=blog, anonymous_user=name, person_email=email, comment=comment
            )
            return render(request, "blogpage.html", context)
        elif request.method == "POST" and request.user.is_authenticated:
            comment = request.POST.get("comment")
            Comments.objects.create(blog=blog, user=request.user, comment=comment)
            return render(request, "blogpage.html", context)
        return render(request, "blogpage.html", context)
    except Exception as e:
        print(e)
    return render(request, "blogpage.html", context)
