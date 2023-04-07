from datetime import datetime, date
from dateutil.relativedelta import relativedelta
def trata_data(data):
    data_obj = datetime.strptime(data, '%Y-%m-%d')

    while verifica_fds(data_obj) is True:
        data_ver = decrementa_dia(data_obj)
        data_obj = datetime.strptime(data_ver, '%Y-%m-%d')

    return data_obj.strftime('%Y-%m-%d')

def incrementa_mes(data):
    data_obj = datetime.strptime(data, '%Y-%m-%d')
    nova_data_obj = data_obj + relativedelta(months=+1)

    return nova_data_obj.strftime('%Y-%m-%d')

def verifica_fds(data):
    if isinstance(data, datetime):
        data_str = data.strftime('%Y-%m-%d')
    else:
        data_str = data

    data_obj = datetime.strptime(data_str, '%Y-%m-%d')
    dv = data_obj.weekday()

    return True if dv in (5, 6) else False

def decrementa_dia(data):
    if isinstance(data, datetime):
        data_str = data.strftime('%Y-%m-%d')
    else:
        data_str = data

    data_obj = datetime.strptime(data_str, '%Y-%m-%d')
    nova_data_obj = data_obj + relativedelta(days=-1)

    return nova_data_obj.strftime('%Y-%m-%d')


