from django.shortcuts import render
from django.views.generic import ListView,DetailView
from .models import Sale
from .forms import SalesSearchForm
# Create your views here.
#function view are readable than class based views
def home_view(request):
    form=SalesSearchForm(request.POST or None)
    st='hello this is anisha'
    context={
        'st':st,
        'form':form
    }
    return render(request,'sales/home.html',context)

class SalesListView(ListView):
    model = Sale
    template_name = 'sales/main.html'
    context_object_name ='SalesList'

class SalesDetailView(DetailView):
    model = Sale
    template_name = 'sales/detail.html'
    context_object_name ='SalesList'