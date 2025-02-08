from django.shortcuts import render

# Create a dummy data
posts = [
    {
        "author": "CoreyMS",
        "title": "Blog Post 1",
        "content": "First post content",
        "date_posted": "August 11, 2021",
    },
    {
        "author": "Jane Doe",
        "title": "Blog Post 2",
        "content": "Second post content",
        "date_posted": "August 12, 2021",
    },
]


def home(request):
    context = {"posts": posts}
    return render(request, "blog/home.html", context=context)


def about(request):
    return render(request, "blog/about.html", {"title": "About"})
