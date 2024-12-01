from django.http import JsonResponse
from django.shortcuts import render, redirect
from .models import MyWork, Contact
from .forms import ContactForm

# Create your views here.


def index(request):
    myworks = MyWork.objects.all()
    contact = Contact.objects.all()
    is_success = request.session.pop('is_success', False)
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        Contact.objects.create(name=name, email=email, message=message)
        is_success = True
        return redirect('index')
    return render(request, 'index.html', {'myworks': myworks, 'is_success': is_success})
