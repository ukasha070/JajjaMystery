from django.shortcuts import get_object_or_404, render
from django.core.paginator import Paginator
from django.db.models import Q

from jajjaMystery.utils import check_for_xss


from .models import Service



def services_list_view(request):
    searchQuery = request.GET.get("search")
    pageNum = request.GET.get("page")
    searchQs = None

    if(searchQuery and check_for_xss(searchQuery)):
        searchQs = ' '.join(searchQuery.split())
        services = Service.objects.filter(Q(published=True) & (Q(title__icontains=searchQs) | Q(description__icontains=searchQs))).distinct().order_by("-id")

        p = Paginator(services, 2)
        page_obj = p.get_page(pageNum)
            
    else:
        services = Service.objects.filter(published=True).order_by("id")
        p = Paginator(services, 2)

        page_obj = p.get_page(pageNum)

    context = {"page_obj": page_obj, "searchQs": searchQs, "page_num": pageNum}
    return render(request, "services/list.html", context)


def services_detail_view(request, title):
    service = get_object_or_404(Service, title=title)

    context = {"service": service}
    return render(request, "services/detail.html", context=context)



