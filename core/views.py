from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic import CreateView

from core.forms import ContactForm

def home(request):
    return render(request, "index.html")


def about(request):
    return render(request, "about.html")


class ContactView(CreateView):
    template_name = 'contact.html'
    form_class = ContactForm
    success_url = reverse_lazy("core:contact")

    def form_valid(self, form):
        messages.add_message(self.request, messages.SUCCESS, _("Your messages sent successfully!"))
        return super().form_valid(form)
    
    def form_invalid(self, form: BaseModelForm) -> HttpResponse:
        messages.add_message(self.request, messages.ERROR, _("Your message was not sent!"))
        return super().form_invalid(form)


def p404_page(request):
    return render(request, "404.html")


def contact(request):
    form = ContactForm()
    print("GET")

    if request.method == "POST":
        form = ContactForm(data = request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, _("Your messages sent successfully!"))
            return redirect(reverse_lazy("core:contact"))
        else:
            messages.add_message(request, messages.ERROR, _("Your message was not sent!"))


    context = {
        "form": form
    }
    return render(request, "contact.html", context=context)