from django.shortcuts import render
from django.http import HttpResponse
from .models import Feature

# Create your views here.
def index(request):
    context = {
        'name': 'Patrick',
        'age': 23,
        'nationality': 'British'
    }
    feature1 = Feature()
    feature1.id = 0
    feature1.name = 'Fast'
    feature1.is_true = True
    feature1.details = 'Our service is very quick'

    features = Feature.objects.all()

    #features = [feature1, feature2, feature3, feature4]

    return render(request, 'index.html', 
                  {'features': features})

def counter(request):
    words = request.POST['words1']
    n_words = len(words.split())
    return render(request, 'counter.html', 
                  {'n_words': n_words})