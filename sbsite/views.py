from django.http import HttpResponse,JsonResponse

def http_test(request):
    return HttpResponse('<h1>This is a first test</h1>')

def json_test(requests):
    return JsonResponse({'name' : 'ali'})

