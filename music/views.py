from django.http import response
def index(request):
    return response.HttpResponse("<h1>This is Music HomePage.</h1>")