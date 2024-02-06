from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    context = {
        'name': 'Patrick',
        'age': 23,
        'nationality': 'British'
    }
    return render(request, 'index.html', context)

def counter(request):
    words = request.POST['words1']
    n_words = len(words.split())
    return render(request, 'counter.html', 
                  {'n_words': n_words})