from django.shortcuts import render
def post_list(request):
    return render(request, 'blog/post_list.html', {})
def indexPage(request):
    return render(request, 'blog/index.html', {})
# Create your views here.
