from django.http import HttpResponse
from django.shortcuts import render
from django.urls.base import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import ContactForm
from django.conf import settings
from django.core.mail import send_mail
from blog.models import Post

def HomeView(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            email_subject = f'New contact {form.cleaned_data["email"]}: {form.cleaned_data["subject"]}'
            email_message = form.cleaned_data['message']
            send_mail(email_subject, email_message, settings.CONTACT_EMAIL, settings.ADMIN_EMAILS)
            return render(request, 'blog/about.html')
    form = ContactForm()
    context = {'form': form}
    return render(request, 'blog/home.html', context)

class BlogView(ListView):
    model = Post
    template_name = 'blog/blog.html'
    ordering = ['-id']
    def get_context_data(self,*args, **kwargs):
        context = super(BlogView, self).get_context_data(*args,**kwargs)
        return context
    #ordering = ['post_date']

class IndividualPostView(DetailView):
    model = Post
    template_name = 'blog/post.html'
    slug_url_kwarg = 'myslug'
    slug_field = 'slug'

    def get_context_data(self,*args, **kwargs):
        context = super(IndividualPostView, self).get_context_data(*args,**kwargs)
        return context

class AboutView(TemplateView):
    template_name = "blog/about.html"

def ContactView(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            email_subject = f'New contact {form.cleaned_data["email"]}: {form.cleaned_data["subject"]}'
            email_message = form.cleaned_data['message']
            send_mail(email_subject, email_message, settings.CONTACT_EMAIL, settings.ADMIN_EMAILS)
            return render(request, 'blog/about.html')
    form = ContactForm()
    context = {'form': form}
    return render(request, 'blog/contact.html', context)

def ContactFormView(request):
    form = ContactForm()
    context = {'form': form}
    return render(request, 'contact/contact.html', context)