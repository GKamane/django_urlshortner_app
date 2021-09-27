from django.shortcuts import render, redirect
import uuid
from .models import Urls
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'index.html')

def create(request):
    if request.method == 'POST':
        link = request.POST['link']
        uid = str(uuid.uuid4())[:5]
        new_url = Urls(link=link,uuid=uid)
        new_url.save()
        return HttpResponse(uid)

def go(request, pk):
    url_details = Urls.objects.get(uuid=pk)
    return redirect('https://'+url_details.link)