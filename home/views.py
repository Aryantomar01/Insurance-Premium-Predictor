from django.shortcuts import render, HttpResponse

import joblib
model = joblib.load('static/RandomForestModel')

# Create your views here.


def index(request):
    # return HttpResponse("This is homepage") # This is a HttpResponse object
    return render(request, 'index.html')  # This is a render object


def about(request):
    # return HttpResponse("This is about page") # This is a HttpResponse object
    return render(request, 'about.html')  # This is a render object


def prediction(request):
    # return HttpResponse("This is prediction page") # This is a HttpResponse object

    if request.method == "POST":
        age = int(request.POST.get('age'))
        sex = int(request.POST.get('sex'))
        bmi = int(request.POST.get('bmi'))
        children = int(request.POST.get('children'))
        smoker = int(request.POST.get('smoker'))
        region = int(request.POST.get('region'))

        print(age, sex, bmi, children, smoker, region)

        pred = round(model.predict([[age, sex, bmi, children, smoker, region]])[0])

        print(pred)

        output={
            "output": pred
        }

        return render(request, 'prediction.html', output)  
    else:
        return render(request, 'prediction.html')  # This is a render object


def contact(request):
    # return HttpResponse("This is contact page") # This is a HttpResponse object
    return render(request, 'contact.html')  # This is a render object


def login(request):

    return render(request, 'login.html')  # This is a render object

def signup(request):

    return render(request, 'signup.html')  # This is a render object
