from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Feature


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email already used')
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username Already Used')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username,
                                                email=email,
                                                password=password)
                user.save()
                return redirect('login')
        else:
            messages.info(request, 'Password Not The Same')
            return redirect('register')
        
    else:
        return render(request, 'register.html')
    

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Credentials Invalid')
            return redirect('login')
    else:
        return render(request, 'login.html')
    
def logout(request):
    auth.logout(request)
    return redirect('/')


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