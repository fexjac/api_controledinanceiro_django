from datetime import datetime
def trata_data(data):
    data_obj = datetime.strptime(data, '%Y-%m-%d')

    return data_obj.strftime('%Y-%m-%d')