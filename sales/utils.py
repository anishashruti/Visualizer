import uuid,base64
from customers.models import Customer
from profiles.models import Profiles
import matplotlib.pyplot as plt
from io import BytesIO

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

def get_chart(chart_type,data,**kwargs):
    plt.switch_backend('AGG')
    if chart_type =='#1':
        print('bar chart')
        plt.bar(data('transaction_id'),data['price'])
    elif  chart_type == '#2':
        print('pie chart')
    elif  chart_type == '#3':
        print('line chart')
    else:
        print('no charts')
    chart=get_graph()
    return chart
