from django.shortcuts import render
from django.views.generic import ListView,DetailView
from .models import Sale
from reports.forms import ReportForms
from .forms import SalesSearchForm
import pandas as pd
from .utils import get_salesman_id,get_customer_id,get_chart
# Create your views here.
#function view are readable than class based views
def home_view(request):
    sale_df=None
    postitions_df = None
    mergedf=None
    df=None
    chart=None
    postition_data=[]
    no_data=None
    search_form=SalesSearchForm(request.POST or None)
    report_form=ReportForms()
    if request.method == 'POST':
        date_from = request.POST.get('date_from')
        date_to = request.POST.get('date_to')
        chart_type = request.POST['chart_type']
        results_by = request.POST['results_by']
        # print(date_from,chart_type,date_to)
        sale_querySet=Sale.objects.filter(created__date__lte=date_to, created__date__gte=date_from)
        if len(sale_querySet) > 0:        
            sale_df=pd.DataFrame(sale_querySet.values())
            sale_df['customer_id']=sale_df['customer_id'].apply(get_customer_id)
            sale_df['salesman_id']=sale_df['salesman_id'].apply(get_salesman_id)
            sale_df['created']=sale_df['created'].apply(lambda x:x.strftime('%d-%m-%Y'))
            sale_df['updated']=sale_df['updated'].apply(lambda x:x.strftime('%d-%m-%Y'))
            sale_df.rename({'salesman_id':'Salesman','customer_id':'Customer','id':'sales_id'},axis=1,inplace=True)
            for sale in sale_querySet:
                for pos in sale.get_postions():
                    obj={
                        'position_id':pos.id,
                        'product':pos.product.name,
                        'quantity':pos.quantity,
                        'price':pos.price,
                        'sales_id':pos.get_sales_id(),
                    }
                    postition_data.append(obj)
            postition_data =pd.DataFrame(postition_data)
            mergedf=pd.merge(postition_data,sale_df,on='sales_id')
            df=mergedf.groupby('transaction_id',as_index=False)['price'].agg('sum')
            chart=get_chart(chart_type,sale_df,results_by)
            
            sale_df=sale_df.to_html()
            postition_data=postition_data.to_html()
            mergedf=mergedf.to_html()           
            df=df.to_html()
            # print(postition_data)
        else:
            no_data='No data is available in this Date range'
            # print('no data')
    context={
        'search_form':search_form,
        'report_form':report_form,
        'sale_df':sale_df,
        'postition_data':postition_data,
        'mergedf':mergedf,
        'df':df,
        'chart':chart,
        'no_data':no_data
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