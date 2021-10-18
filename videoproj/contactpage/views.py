from django.shortcuts import render, redirect
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from videoapp.models import Project


class PostList(generic.ListView):
  queryset = Project.objects.filter(status=1).order_by('-created_on')
  template_name = 'videoapp/index.html'

def contactView(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['email']
            message = form.cleaned_data['message']
            from_email = 'rogervideo@elysiancoder.com'
            to_email = ['bewater475@gmail.com']
            try:
                send_mail(subject, message, from_email, to_email)
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('success/')
    return render(request, "contactpage/contact.html", {'form': form})

def successView(request):
    #return HttpResponse('Success! Thank you for your message.')
    return render(request, "contactpage/success.html")
