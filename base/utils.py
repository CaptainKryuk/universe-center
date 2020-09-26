from base.models import SportSection, Coach
from universe.settings import POSTMARK_API_KEY, POSTMARK_SENDER
from postmarker.core import PostmarkClient

def get_sections():
    # get all sections
    return SportSection.objects.all()

def send_email(text):
    postmark = PostmarkClient(server_token=POSTMARK_API_KEY)

    postmark.emails.send(
        From=POSTMARK_SENDER,
        To='info@universe-center.ru',
        Subject='Новый вопрос',
        HtmlBody=text
    )