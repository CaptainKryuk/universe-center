from django.forms import Form, CharField
from base.models import SportSection

class SportSectionForm(Form):
    """
    Form for questiong for email
    Имя, телефон / емайл, сообщение
    """
    name = CharField(label="Имя")
    contact = CharField(label="Телефон или e-mail")
    message = CharField(label="Ваш вопрос")

class ContactForm(Form):
    """
    Form for questiong for email
    Имя, телефон / емайл, сообщение
    """
    name = CharField(label="Имя")
    contact = CharField(label="Телефон по которому с вами можно связаться")