from django.http import response
def index(request):
    return response.HttpResponse("<h1>This is Music HomePage.</h1>")

def details(request,album_id):
    return response.HttpResponse("<h2>Details for album id : " + str(album_id) + "</h2>")
