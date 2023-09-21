from django.shortcuts import render


def description(request):
    template = 'about/description.html'
    context = {'view_name':'about:description'}
    return render(request, template, context)
