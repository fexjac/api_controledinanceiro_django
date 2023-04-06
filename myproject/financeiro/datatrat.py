from datetime import datetime
from dateutil.relativedelta import relativedelta
def trata_data(data):
    data_obj = datetime.strptime(data, '%Y-%m-%d')

    return data_obj.strftime('%Y-%m-%d')

def incrementa_mes(data):
    data_obj = datetime.strptime(data, '%Y-%m-%d')
    nova_data_obj = data_obj + relativedelta(months=+1)

    return nova_data_obj.strftime('%Y-%m-%d')