from django.http import HttpResponse


def home(request):
    return HttpResponse('<html><body><h1>Olá Django</h1></body></html>')
