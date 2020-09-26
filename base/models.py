from django.db.models import Model, \
                             CharField, \
                             ImageField, \
                             FileField, \
                             TextField, \
                             ForeignKey, \
                             SlugField, \
                             CASCADE, \
                             IntegerField
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

    img = FileField(upload_to="sections", verbose_name="Картинка секции")

    slug = SlugField("Slug поле", max_length=50, default=title)

    long_description = TextField("Описание секции", blank=True)

    invoice = IntegerField(verbose_name="Сумма месячной оплаты", default=3000)

    section_tag = CharField("Таг отображения", max_length=50)

    class Meta:
        verbose_name = "Секция"
        verbose_name_plural = "Спортивные секции"

    def __str__(self):
        return self.title

    def get_coaches(self):
        return self.coach_set.all()


class Coach(Model):

    name = CharField("ФИО тренера", max_length=255)

    rank = CharField("Позиция тренера", max_length=255)

    description = TextField("Описание")

    section = ForeignKey(SportSection, verbose_name="Спортивная секция", on_delete=CASCADE)

    photo = ImageField(upload_to="coach_photos", verbose_name="Фотография тренера")

    class Meta:
        verbose_name = "Тренер"
        verbose_name_plural = "Тренера"

    def __str__(self):
        return self.name + ' -- ' + self.section.title

# class SectionTableModel(Model):
#     """
#     Sport section in table list
#     """
#     name = CharField("Наименование секции", max_length=255)
