
import json
from db import excute_sql
from sql.data_sql import thounds_data

def queryData():
    data = excute_sql(thounds_data, ())
    with open('record.json', 'w') as f:
        json.dump(data, f)


def loadData():
    data = None
    with open('record.json', 'r') as f:
        data = json.load(f)

    return data