from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import logout

from .forms import MessageForm
from service.models import Service, ServiceList
from jajjaMystery.send_emails import send_email_to_jajja


def index_view(request):
    services = Service.objects.all()[:3]
    services_list = ServiceList.objects.all()
    form = MessageForm()

    context = {
        "services": services,
        "services_list": services_list,
        "form": form
    }
    return render(request, "base/index.html", context)

def about_view(request):
    return render(request, "base/about_jajja.html")

def contact_view(request):
    form =  MessageForm()
    context = {
        "form": form
    }
    return render(request, "base/contact.html", context)

def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect("/")
    else:
        messages.error(request, "You must be logged in.")
        return redirect("/")

def send_contact_message_view(request):
    form = MessageForm()

    if request.POST:
        form = MessageForm(request.POST)
        
        if form.is_valid():
            send_email_to_jajja("mails/contact.html", context=form.cleaned_data)
            messages.success(request, "Message was sent to Jajja soon responding.")
            return redirect("/")
        else:
            services = Service.objects.all()[:3]
            context = {
                "services": services,
                "form": form
            }
            return render(request, "base/index.html", context)
    else:
        return redirect("/")
   
def error_404_view(request, exception):
    """
    Custom 404 error view.
    """
    return render(request, '404.html', status=404)