from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .forms import ContactForm
from .settings.base import EMAIL_HOST_USER

class inicio(TemplateView):
    template_name='inicio.html'

def contactView(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            contact_name = request.POST['contact_name']
            email_from= EMAIL_HOST_USER
            content = request.POST['content'] + " " + request.POST['contact_email']
            recipient_list=["nahuelbarreiro@gmail.com"]
            try:
                send_mail(contact_name, content, email_from, recipient_list)
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('success')
    return render(request, "contacto.html", {'form': form})

def successView(request):
    return render(request, "success.html")
