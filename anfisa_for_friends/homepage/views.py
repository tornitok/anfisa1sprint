from django.shortcuts import render


def index(request):
    template = 'homepage/index.html'
    context = {'view_name':'homepage:index'}
    return render(request, template, context)
