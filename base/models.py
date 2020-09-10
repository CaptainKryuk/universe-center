from django.db.models import Model, CharField, ImageField
from django.shortcuts import render


class SlideshowImage(Model):
    name = CharField("Название фотографии", max_length=255, blank=True)

    img = ImageField("Изображение")

    class Meta:
        verbose_name = "Изображение"
        verbose_name_plural = "Изображения для слайд шоу"

    def __str__(self):
        return self.name or self.img.name