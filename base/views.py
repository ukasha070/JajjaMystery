from django.db.models import Q
from django.contrib import messages
from django.contrib.auth import logout
from django.core.paginator import Paginator
from django.shortcuts import render, redirect

from service.models import Service, ServiceList
from jajjaMystery.send_emails import send_email_to_jajja

from .forms import MessageForm
from .models import Testimonial


def index_view(request):
    services = Service.objects.all()[:3]
    testimonials = Testimonial.objects.all()[:3]
    services_list = ServiceList.objects.all()
    form = MessageForm()

    context = {
        "form": form,
        "services": services,
        "testimonials": testimonials,
        "services_list": services_list,
    }
    return render(request, "base/index.html", context)

def about_view(request):
    return render(request, "base/about_jajja.html")

def testimonials_view(request):
    pageNum = request.GET.get("page")

    if pageNum:
        pageNum = pageNum
    else:
        pageNum = 1

    testimonials = Testimonial.objects.filter(published=True).order_by("id")
    p = Paginator(testimonials, 1)

    page_obj = p.get_page(pageNum)

    context = {"page_obj": page_obj, "page_num": pageNum}
    return render(request, "base/testimonials.html", context)


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