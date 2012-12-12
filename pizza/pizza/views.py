from django import http

def home(request):
    html = "<h1>Hello World!</h1>"
    return http.HttpResponse(html)

