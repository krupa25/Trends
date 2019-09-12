from django.shortcuts import render

# Create your views here.
import requests
import json

def home(request):
	url="https://newsapi.org/v2/top-headlines?sources=google-news&sortBy=popularity&apiKey=1c128e3aadde471f842601390b1f598c"
	api_request=requests.get(url)
	api=json.loads(api_request.content)
	if api["status"]=="error":
		return render(request,'error.html',{})
	return render(request,'home.html',{'api':api})

def world(request):
	url="https://newsapi.org/v2/everything?sources=al-jazeera-english,bbc-news,cnn&language=en&apiKey=1c128e3aadde471f842601390b1f598c"
	api_request=requests.get(url)
	api=json.loads(api_request.content)
	if api["status"]=="error":
		return render(request,'error.html',{})
	return render(request,'home.html',{'api':api})

def sports(request):
	url="https://newsapi.org/v2/top-headlines?country=us&category=sports&sortBy=popularity&apiKey=1c128e3aadde471f842601390b1f598c"
	api_request=requests.get(url)
	api=json.loads(api_request.content)
	if api["status"]=="error":
		return render(request,'error.html',{})
	return render(request,'home.html',{'api':api})

def entertainment(request):
	url="https://newsapi.org/v2/top-headlines?country=us&category=entertainment&sortBy=popularity&apiKey=1c128e3aadde471f842601390b1f598c"
	api_request=requests.get(url)
	api=json.loads(api_request.content)
	if api["status"]=="error":
		return render(request,'error.html',{})
	return render(request,'home.html',{'api':api})

def finance(request):
	url="https://newsapi.org/v2/top-headlines?sources=cnbc,the-wall-street-journal&sortBy=popularity&apiKey=1c128e3aadde471f842601390b1f598c"
	api_request=requests.get(url)
	api=json.loads(api_request.content)
	if api["status"]=="error":
		return render(request,'error.html',{})
	return render(request,'home.html',{'api':api})

def business(request):
	url="https://newsapi.org/v2/top-headlines?country=us&category=business&sortBy=popularity&apiKey=1c128e3aadde471f842601390b1f598c"
	api_request=requests.get(url)
	api=json.loads(api_request.content)
	if api["status"]=="error":
		return render(request,'error.html',{})
	return render(request,'home.html',{'api':api})

def tech(request):
	url="https://newsapi.org/v2/top-headlines?country=us&category=technology&sortBy=popularity&apiKey=1c128e3aadde471f842601390b1f598c"
	api_request=requests.get(url)
	api=json.loads(api_request.content)
	if api["status"]=="error":
		return render(request,'error.html',{})
	return render(request,'home.html',{'api':api})

def trending(request):
	url="https://newsapi.org/v2/everything?domains=dailymail.co.uk&apiKey=1c128e3aadde471f842601390b1f598c"
	api_request=requests.get(url)
	api = json.loads(api_request.content)
	if api["status"]=="error":
		return render(request,'error.html',{})
	return render(request,'home.html',{'api':api})
