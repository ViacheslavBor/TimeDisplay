from django.shortcuts import render, HttpResponse, redirect
from time import strftime

def index(request):
	context = {
	"date": strftime("%b %d %Y"),
	"time": strftime("%H:%M")
	}
	return render(request,'blog/time.html', context)

