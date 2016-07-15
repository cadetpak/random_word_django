from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string

def index(request):
	if request.session.get("counter", True):
		request.session["number"] = request.session["number"] + 1
	else:
		request.session["counter"] = True
		request.session["number"] = 0

	random_string = get_random_string(length=6)
	context = {
		'string': random_string,
		'counter': request.session["number"],
	}
	return render(request, 'generator/index.html', context)

def generate(request):
	return redirect('/')

def destroy(request):
	request.session["counter"] = False
	del request.session["number"]
	return redirect('/')
