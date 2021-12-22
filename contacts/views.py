from django.shortcuts import render
from django.shortcuts import redirect

from .models import *
from .forms import *
from .filters import *

# Create your views here.
def index(request):
    contacts = Contact.objects.all()
    filter = ContactFilter(request.GET, queryset = contacts)
    contacts = filter.qs
    context = {'contacts': contacts, 'filter': filter}
    return render(request, 'contacts/index.html', context)

def view_profile(request, pk):
    contact = Contact.objects.get(pk = pk)
    context = {'contact': contact}
    return render(request, 'contacts/profile.html', context)

def create(request):
    if request.method == "POST":
        form = ContactForm(data = request.POST)
        if form.is_valid:
            form.save()
            return redirect('/')
    form = ContactForm()
    return render(request, 'contacts/create.html', {'form': form})

def edit_profile(request, pk):
    contact = Contact.objects.get(pk = pk)

    if request.method =='POST':
        form = ContactForm(data=request.POST, instance = contact)
        if form.is_valid:
            form.save()
            return redirect('contacts:index')
    
    form = ContactForm(instance = contact)
    
    context = {'contact': contact, 'form': form}
    return render(request, 'contacts/edit.html', context)

def delete(request, pk):
    contact = Contact.objects.get(pk = pk)
    if request.method == 'POST':
        contact.delete()
        return redirect('/')
    return render(request, 'contacts/delete.html', {'contact': contact})