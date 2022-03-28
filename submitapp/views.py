from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from .models import Contact
from .forms import ContactForm
from django.views.generic import ListView, DetailView


def create(request):
    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request, 'submitapp/success.html', locals())
    form = ContactForm()

    return render(request,'submitapp/create.html',{'form': form})

   