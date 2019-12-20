"""
pages/views.py
"""
from django.http import HttpResponse, JsonResponse
# from django.contrib.auth.models import User
from django.shortcuts import render # STEP 1 - Import
from django.shortcuts import redirect


# --- HOMEPAGE --- #

def welcome_page(request):
    return render(request, "pages/homepage/welcome.html", {})

def contactus_page(request):
    return render(request, "pages/homepage/contactus.html", {})


# --- GATEWAY --- #
def register_page(request):
    return render(request, "pages/gateway/register.html", {})

def register_success_page(request):
    return render(request, "pages/gateway/register_success.html", {})

def login_page(request):
    return render(request, "pages/gateway/login.html", {})

def logout_page(request):
    return render(request, "pages/gateway/logout.html", {})
