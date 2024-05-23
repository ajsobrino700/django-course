from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string
from django.shortcuts import render

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
    "december": None
}

def index(request):
    #response_data = render_to_string("challenges/challenge.html")
    #return HttpResponse(bytes(response_data,'utf8'))
    return render(request,"challenges/index.html",{ 
            "months": list(monthly_challenges.keys())
        }
    )


def january(request):
    return HttpResponse(b"This works!")

def febrary(request):
    return HttpResponse(b"Walk for at least 20 minutes evert day!")

def march(request):
    return HttpResponse(b"Learn django for at least 20 minutes every day!")

def monthly_challenge(request,month):
    try:    
        challenge_text = monthly_challenges[month]
        return render(request,"challenges/challenge.html",{
            "month": month,
            "text":challenge_text
        })
    except:
        response_data = render_to_string("404.html")
        raise Http404(bytes(response_data,'utf8'))

def monthly_challenge_by_number(request, month: int):
    try:
        forward_month = list(monthly_challenges.keys())
        redirect_path = reverse("month-challenge",args = [forward_month[month-1]])
        return HttpResponseRedirect(redirect_path)
    except:
        raise Http404(bytes(render_to_string("404.html"),'utf8'))
