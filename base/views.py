from django.shortcuts import render
from universe.settings import MEDIA_ROOT, BASE_DIR, STATIC_ROOT
import imghdr
import os
from base.models import SportSection, Coach

# Create your views here.

def index(request):

    # get slideshow
    media_url = os.path.join(BASE_DIR, 'media')
    images = [img for img in os.listdir(media_url) if os.path.isfile(media_url + '/' + img) and imghdr.what(media_url + '/' + img)]

    # get sections
    sections = SportSection.objects.all()

    # get coaches
    coaches = Coach.objects.all()
    

    return render(request, 'index.html', context={'images': images, 
                                                  'first_image': images[0],
                                                  'last_image': images[len(images) - 1],
                                                  'str_images': ';'.join(images),
                                                  # sections
                                                  'sections': sections,
                                                  # coaches
                                                  'coaches': coaches })

def gallery(request):
    gallery_url = os.path.join(BASE_DIR, 'universe', 'static', 'gallery')
    images = [img for img in os.listdir(gallery_url)]
    return render(request, 'gallery.html', context={'images': images})