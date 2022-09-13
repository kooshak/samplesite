from django.http import HttpResponse

from .models import db

def index(request):
    s = 'list of announcment\r\n\r\n\r\n'
    for bb in db.objects.order_by('-published'):
        s+= bb.title + bb.content + '\r\n\r\n'
    return HttpResponse(s, content_type = 'text/plain; charset=utf-8')

