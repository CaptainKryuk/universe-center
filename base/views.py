from django.shortcuts import render, redirect
from universe.settings import MEDIA_ROOT, BASE_DIR, STATIC_ROOT
import imghdr
import os
from base.models import SportSection, Coach
from django.shortcuts import get_object_or_404
from .forms import SportSectionForm, ContactForm
from .utils import get_sections, send_email
from django.contrib import messages

# Create your views here.

def index(request):

    # get slideshow
    media_url = os.path.join(BASE_DIR, 'media')
    images = [img for img in os.listdir(media_url) if os.path.isfile(media_url + '/' + img) and imghdr.what(media_url + '/' + img)]

    # get coaches
    coaches = Coach.objects.all()
    

    return render(request, 'index.html', context={'images': images, 
                                                  'first_image': images[0],
                                                  'last_image': images[len(images) - 1],
                                                  'str_images': ';'.join(images),
                                                  'contact_form': ContactForm(),
                                                  # sections
                                                  'sections': get_sections(),
                                                  # coaches
                                                  'coaches': coaches })

def gallery(request):
    gallery_url = os.path.join(BASE_DIR, 'universe', 'static', 'gallery')
    images = [img for img in os.listdir(gallery_url)]
    return render(request, 'gallery.html', context={'images': images, 
                                                    'contact_form': ContactForm(),
                                                    'sections': get_sections(),
                                                    'title': 'Галерея'})

def sport_section(request, slug):

    if request.method == 'POST':
        form = SportSectionForm(request.POST)
        if form.is_valid():
            for field in form:
                html_text = '<br/>'.join(["{} - {}".format(field.label, field.data)])
            send_email(html_text)
            messages.add_message(request, messages.SUCCESS, 'Ваша вопрос успешно отправлен')
            return redirect(request.path)
        messages.add_message(request, messages.ERROR, 'Ошибка при заполнении формы, убедитесь в правильности её заполнения')

    # get form for page
    form = SportSectionForm()

    # get section
    section = get_object_or_404(SportSection, slug=slug)

    # get list of sections
    sections = SportSection.objects.all()

    sections_menu = []
    for s in sections:
        s_class = 'default'
        if s.id == section.id:
            s_class = 'selected'

        sections_menu.append({'name': s.title, 'class': s_class, 'slug': s.slug})

    return render(request, 'sport_section.html', context={'sport': section, 
                                                          'sections': get_sections(), 
                                                          's_menu': sections_menu, 
                                                          'form': form, 
                                                          'contact_form': ContactForm(),
                                                          'title': section.title})


def contact_form(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            
            black_list = ['current_page_url']
            for field in form:
                html_text = '<br/>'.join(["{} - {}".format(field.label, field.data)])
                send_email(html_text)
            messages.add_message(request, messages.SUCCESS, 'Ваш запрос успешно отправлен')
            return redirect(request.POST['current_page_url'])                
        messages.add_message(request, messages.ERROR, 'Ошибка при заполнении формы, убедитесь в правильности её заполнения')
        return redirect(request.POST['current_page_url'])        
    return redirect('/404')


def requisites_view(request):
    return render(request, 'requisites.html', context={'contact_form': ContactForm(),
                                                       'sections': get_sections(),
                                                       'title': "Реквизиты"})


def pricelist_view(request):
    return render(request, 'pricelist.html', context={'contact_form': ContactForm(),
                                                       'sections': get_sections(),
                                                       'title': "Секции"})

def about_view(request):
    # get coaches
    coaches = Coach.objects.all()

    return render(request, 'about.html', context={'contact_form': ContactForm(),
                                                  'sections': get_sections(),
                                                  'coaches': coaches,
                                                  'title': "О нас"})