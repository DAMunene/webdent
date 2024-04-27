from django.shortcuts import render


# Create your views here
def home(request):
    if request.method == "POST":
        name = request.POST.get('message-name')
        email = request.POST.get('message-email')
        message = request.POST.get('message')
        return render(request, 'Eweb/home.html', {'name':name})
    else:
        return render(request, 'Eweb/home.html', {})

def about(request):
    return render(request, 'Eweb/about.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('message-name')
        email = request.POST.get('message-email')
        message = request.POST.get('message')       
        return render(request, 'Eweb/contact.html' ,{'name':name})

    else:   
        return render(request, 'Eweb/contact.html' ,{})
 

def services(request):
    return render(request, 'Eweb/services.html')