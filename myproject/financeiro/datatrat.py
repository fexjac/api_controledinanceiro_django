from datetime import datetime, date
from dateutil.relativedelta import relativedelta
def trata_data(data):
    data_obj = datetime.strptime(data, '%Y-%m-%d')

    while verifica_fds() is True:
        data_obj = decrementa_dia(data_obj)

    return data_obj.strftime('%Y-%m-%d')

def incrementa_mes(data):
    data_obj = datetime.strptime(data, '%Y-%m-%d')
    nova_data_obj = data_obj + relativedelta(months=+1)

    return nova_data_obj.strftime('%Y-%m-%d')

def verifica_fds(data):
    data_obj = datetime.strptime(data, '%Y-%m-%d')
    dv = data.weekday()

    return True if dv in (5, 6) else False

def decrementa_dia(data):
    data_obj = datetime.strptime(data, '%Y-%m-%d')
    nova_data_obj = data_obj + relativedelta(days=-1)

    return nova_data_obj.strftime('%Y-%m-%d')


