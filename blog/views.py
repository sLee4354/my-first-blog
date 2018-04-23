from django.shortcuts import render
def post_list(request):
    return render(request, 'blog/post_list.html', {})
def dashboard(request):
    return render(request, 'blog/dashboard.html', {})
# Create your views here.
