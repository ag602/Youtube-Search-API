from django.shortcuts import render
from .models import *
from django.core.paginator import Paginator
# Create your views here.
# import arrow
def home(request):
    # for i in Vidata.objects.values.order_by('-id')[0]:
    #     print(i)
    # print(Vidata.objects.values().order_by('-id')[0])
    c = Vidata.objects.order_by('-publishedAt').all()
    paginator = Paginator(c, 10) # Show 25 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'index.html', {'page_obj': page_obj})

def watch(request, video_id=None):
    c = Vidata.objects.filter(videoid=video_id)
    data = c.all()
    return render(request, 'watch.html', {"data":data})
