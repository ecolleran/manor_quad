from django.shortcuts import render

# Create your views here.

def open_dashboard(request):
    return render(request, 'homepage.html', {'new_user': False, 'new_name': ''})