from django.shortcuts import render
from .forms import ContactForm
from nw_users_app.models import UserProfile

def index(request):
    return render(request, 'main-site/index.html')

def about(request):
    return render(request, 'main-site/about.html')

def gallery(request):
    return render(request, 'main-site/gallery.html')

def contact(request):
    if request.method == "GET":
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            
            body = {
                'name' : form.cleaned_data['name'],
                'email' : form.cleaned_data['email'],
                'message' : form.cleaned_data['message'],
            }
            message = "\n".join(body.values())
            # try:
            #     send_mail(subject, message, "buzzbombscott@gmail.com", ["scott.henry.moore@gmail.com"])
            # except BadHeaderError:
            #     return HttpResponse("Invalid header found.")
            # return redirect("success")
    return render(request, "main-site/contact.html", {"form": form})

def trade(request):
    return render(request, 'main-site/trade_clients.html')

def restoration(request):
    return render(request, 'main-site/restoration.html')

def retailer(request):
    shops = UserProfile.objects.all()
    context = {
        'shops': shops
    }
    return render(request, 'main-site/retailer.html', context)