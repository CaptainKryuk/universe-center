from django.db.models import Model, CharField, ImageField, FileField, TextField
from django.shortcuts import render


class SlideshowImage(Model):
    name = CharField("Название фотографии", max_length=255, blank=True)

    img = ImageField("Изображение")

    class Meta:
        verbose_name = "Изображение"
        verbose_name_plural = "Изображения для слайд шоу"

    def __str__(self):
        return self.name or self.img.name


class SportSection(Model):

    title = CharField("Название секции", max_length=255)

    description = CharField("Описание секции", max_length=255)

    # icon = ImageField(upload_to="sections", verbose_name="Иконка")

    img = FileField(upload_to="sections", verbose_name="Картинка секции")

    class Meta:
        verbose_name = "Секция"
        verbose_name_plural = "Секции из раздела 'Мы помогаем вашим детям...'"

    def __str__(self):
        return self.title


class Coach(Model):

    SPORT_SECTION = (
        ('taekwondo', 'Тхэквондо'),
        ('grappling', 'Грепплинг'),
        ('combat', 'Рукопашный бой'),
        ('gymnastic', 'Художественная гимнастика'),
        ('brain', 'Секция МОЗГ'),
        ('karate', "Карате")
    )

    name = CharField("ФИО тренера", max_length=255)

    rank = CharField("Позиция тренера", max_length=255)

    description = TextField("Описание")

    section = CharField("Спортивная секция", choices=SPORT_SECTION, max_length=50)

    photo = ImageField(upload_to="coach_photos", verbose_name="Фотография тренера")

    class Meta:
        verbose_name = "Тренер"
        verbose_name_plural = "Тренера"

    def __str__(self):
        return self.name + ' -- ' + self.section