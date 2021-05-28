from django.shortcuts import render
from django.views.generic import ListView
from .models import Sale
# Create your views here.
#function view are readable than class based views
def home_view(request):
    st='hello this is anisha'
    return render(request,'sales/home.html',{'st':st})

class SalesListView(ListView):
    model = Sale
    template_name = 'sales/main.html'