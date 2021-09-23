from django.shortcuts import render, HttpResponse
from django.views.generic import TemplateView
from .forms import ContactUsForm

class IndexView(TemplateView):
  template_name = 'order/index.html'

  def get_context_data(self, **kwargs):
    age = 20
    names = ['ihsan', 'ali', 'nouman']

    context = {'age':age, 'names':names}
    return context


# def index(request):
#     age = 20
#     names = ['ihsan', 'ali', 'nouman']

#     context = {'age':age, 'names':names}
#     return render(request, 'order/index.html', context=context)

def login(request):
    return render(request, 'order/login.html')

def cart(request):
    return render(request, 'order/cart.html')

def contact(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']

        context = {'email':email, 'password':password}
        return render(request, 'order/contactus.html', context)

    return render(request, 'order/contactus.html')

def contact_2(request):
    if request.method == "POST":
        form = ContactUsForm(request.POST)

        if form.is_valid():
            return HttpResponse("Thank you")
        return render(request, 'order/contact2.html', {'form':form})

    return render(request, 'order/contact2.html', {'form':ContactUsForm})