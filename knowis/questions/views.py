from django.shortcuts import render
from .models import  Question

# Create your views here.

Question.get_published()
