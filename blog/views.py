from django.shortcuts import render
import feedparser
# Create your views here.

def home(request):
    
    return render(request, 'home.html', {})

def reader(request):
    lis = ''
    if request.method == 'POST':
       url_input = request.POST.get('url_input','')
     
       d = feedparser.parse(url_input)
       lis = []
       for i in range(5):
           res = d['entries'][i]['title'] 
           lis.append(res)


       
    return render(request, 'reader.html', {'value': lis })
