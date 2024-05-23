from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse


# Create your views here.
monthly_challenges = {
    "january": "Eat no meat for the entire month!",
    "febrary": "Walk for at least 20 minutes every day!",
    "march": "Learn Django fot at least 20 minutes evert day!",
    "april": "Eat no meat for the entire month!",
    "may": "Walk for at least 20 minutes every day!",
    "june": "Learn Django fot at least 20 minutes evert day!",
    "july": "Eat no meat for the entire month!",
    "august": "Walk for at least 20 minutes every day!",
    "septemtber": "Learn Django fot at least 20 minutes evert day!",
    "october": "Eat no meat for the entire month!",
    "november": "Walk for at least 20 minutes every day!",
    "december": "Learn Django fot at least 20 minutes evert day!",
}

def index(request):
    months = list(monthly_challenges.keys())
    html_text  = [f'<li><a href="/challenge/{month.capitalize()}">{month.capitalize()}</a></li>' for month in months]
    response_data = "<ul>"+''.join(html_text)+"</ul>"
    return HttpResponse(bytes(response_data,'utf8'))


def january(request):
    return HttpResponse(b"This works!")

def febrary(request):
    return HttpResponse(b"Walk for at least 20 minutes evert day!")

def march(request):
    return HttpResponse(b"Learn django for at least 20 minutes every day!")

def monthly_challenge(request,month):
    try:    
        challenge_text = monthly_challenges[month]
        return HttpResponse(bytes(challenge_text,'utf8'))
    except:
        return HttpResponseNotFound(b"This month is not supported!")

def monthly_challenge_by_number(request, month: int):
    try:
        forward_month = list(monthly_challenges.keys())
        redirect_path = reverse("month-challenge",args = [forward_month[month-1]])
        return HttpResponseRedirect(redirect_path)
    except:
        return HttpResponseNotFound(b"This month is not supported!")
