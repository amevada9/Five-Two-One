from django.shortcuts import render

# Create your views here.
def five_two_one(request):
    return render(request, 'index.html')