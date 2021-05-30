from django.shortcuts import render
from django.views.generic import ListView,DetailView
from .models import Sale
from .forms import SalesSearchForm
import pandas as pd
# Create your views here.
#function view are readable than class based views
def home_view(request):
    sale_df=None
    postitions_df = None
    form=SalesSearchForm(request.POST or None)
    if request.method == 'POST':
        date_from = request.POST.get('date_from')
        date_to = request.POST.get('date_to')
        chart_type = request.POST['chart_type']
        # print(date_from,chart_type,date_to)
        sale_querySet=Sale.objects.filter(created__date__lte=date_to, created__date__gte=date_from)
        if len(sale_querySet) > 0:        
            sale_df=pd.DataFrame(sale_querySet.values())
            postition_data=[]
            for sale in sale_querySet:
                for pos in sale.get_postions():
                    obj={
                        'position_id':pos.id,
                        'product':pos.product.name,
                        'quantity':pos.quantity,
                        'price':pos.price,
                    }
                    postition_data.append(obj)
            postition_data =pd.DataFrame(postition_data)
            sale_df=sale_df.to_html()
            postition_data=postition_data.to_html()
            # print(postition_data)
        else:
            print('no data')
    context={
        'form':form,
        'sale_df':sale_df,
        'postition_data':postition_data
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