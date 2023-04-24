from django.shortcuts import render

def index(request):
    return render(request, 'main-site/index.html')

def about(request):
    return render(request, 'main-site/about.html')

def gallery(request):
    return render(request, 'main-site/gallery.html')

def contact(request):
    return render(request, 'main-site/contact.html')

def trade(request):
    return render(request, 'main-site/trade_clients.html')

def restoration(request):
    return render(request, 'main-site/restoration.html')

def retailer(request):
    return render(request, 'main-site/retailer.html')