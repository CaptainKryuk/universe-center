from django.shortcuts import render
from universe.settings import MEDIA_ROOT, BASE_DIR
import imghdr
import os

# Create your views here.

def index(request):
    media_url = os.path.join(BASE_DIR, 'media')
    images = [img for img in os.listdir(media_url) if imghdr.what(media_url + '/' + img)]
    return render(request, 'index.html', context={'images': images, 'first_image': images[0] })