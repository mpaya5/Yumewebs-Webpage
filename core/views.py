from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings

from .forms import ContactForm


# Create your views here.
# 404: página no encontrada
def error_404(request, exception):
    return render(request, "core/404.html")


def home(request):
    contact_form = ContactForm

    if request.method == "POST":

        subject = request.POST["subject"]
        message = request.POST["message"] + " " + request.POST["email"]
        email_from = settings.EMAIL_HOST_USER

        recipient_list = ["yumewebs@gmail.com"]

        send_mail(subject, message, email_from, recipient_list)

    return render(request, "core/index.html", {'form':contact_form})

def about(request):
    return render(request, "core/about.html")

def contact(request):
    contact_form = ContactForm

    if request.method == "POST":

        subject = request.POST["subject"]
        message = request.POST["message"] + " " + request.POST["email"]
        email_from = settings.EMAIL_HOST_USER

        recipient_list = ["yumewebs@gmail.com"]

        send_mail(subject, message, email_from, recipient_list)
        
    return render(request, "core/contact.html", {'form': contact_form})