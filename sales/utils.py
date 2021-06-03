import uuid,base64
from customers.models import Customer
from profiles.models import Profiles
import matplotlib.pyplot as plt
from io import BytesIO
import seaborn as sns

def generate_code():
    code=str(uuid.uuid4()).replace('-',' ')[:12]
    return code

def get_salesman_id(val):
    salesman=Profiles.objects.get(id=val)
    return salesman.user.username

def get_customer_id(val):
    customer=Customer.objects.get(id=val)
    return customer

def get_graph():
    buffer = BytesIO()
    plt.savefig(buffer,format='png')
    buffer.seek(0)
    image_png= buffer.getvalue()
    graph=base64.b64encode(image_png)
    graph=graph.decode('utf-8')
    buffer.close()
    return graph

def get_key(res_by):
    if res_by == '#1':
        key= 'transaction_id'
    elif res_by == '#2':
        key='created'
    return key

def get_chart(chart_type,data,results_by,**kwargs):
    plt.switch_backend('AGG')
    fig=plt.figure(figsize=(10,4))
    key=get_key(results_by)
    d=data.groupby(key,as_index=False)['total'].agg('sum')
    if chart_type =='#1':
        print('bar chart')
        # plt.bar(data['transaction_id'],data['price'])
        sns.barplot(x=key,y='total',data=d)
    elif  chart_type == '#2':
        print('pie chart')
        plt.pie(data=d,x='total',labels=d[key].values)
    elif  chart_type == '#3':
        print('line chart')
        plt.plot(d[key],d['total'],color='black',marker='o')
    else:
        print('no charts')
    plt.tight_layout()
    chart=get_graph()
    return chart
