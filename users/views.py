from django.shortcuts import render

# Create your views here.
def users(requets):
    return render(requets, 'users/register.html')