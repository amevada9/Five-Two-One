from django.shortcuts import render

# Create your views here.
def location_chooser(request):
    return render(request, 'location_index.html')