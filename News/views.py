from django.shortcuts import render
import requests
from datetime import date
from datetime import datetime, timedelta


def index(request):
    if request.method=="POST":
        post = "post"
        Term = request.POST.get('term')
        if request.POST.get('date'):
            From = request.POST.get('date')

        url = ('https://newsapi.org/v2/everything?'
       'q=Apple&'
       'from=2019-08-19&'
       'sortBy=popularity&'
       'apiKey=67ac10d12a0b4275b2b2afb37695f9c2')
        url = url.replace("Apple",Term)
        if request.POST.get('date'):
            url = url.replace("2019-08-19",From)
        else:
            today = datetime.now() - timedelta(days=1)
            today = today.strftime("%Y-%m-%d")
            url = url.replace("2019-08-19",today)

        response = requests.get(url).json()
        return render(request, 'News/home.html',{'response':response,'post':post})
    else:
        return render(request, 'News/home.html')

    
