from django.shortcuts import render

# Create your views here.
def index(request):
    context_dict = {'text': 'Hello, World!', 'number': 2122}
    return render(request, 'templatesapp/index.html', context_dict);

def other(request):
    return render(request, 'templatesapp/other.html');

def relative(request):
    return render(request, 'templatesapp/rel_url_templates.html');
