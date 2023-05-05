import requests
from datetime import datetime


def get_data(endpoint):
    req = requests.get(endpoint)
    return req.json()

def get_month_year(date):
    try:    
        date_obj = datetime.strptime(date, '%Y-%m-%d')
        return date_obj.strftime('%B %Y')
    except:
        return None

def get_year(date):
    try:
        date_index = date.split("-")
        return date_index[0]
    except:
        return None
    
def filter_data(endpoint):
    req = get_data(endpoint)
    res = list()
    for items in req['data']:
        res.append({
            'manga_id': items['id'],
            'titles': items['attributes']['canonicalTitle'],
            'start_date': get_year(items['attributes']['startDate']),
            'poster_image': items['attributes']['posterImage']['original']
        })

    return res

def get_details(manga):
    req = get_data(manga)
    res = []

    items = req['data']

    res.append({
        'manga_id': items['id'],
        'titles': items['attributes']['canonicalTitle'],
        'start_date': get_month_year(items['attributes']['startDate']),
        'poster_image': items['attributes']['posterImage']['original'],
        'manga_type': items['attributes']['mangaType'],
        'descritpion': items['attributes']['synopsis']
    })

    return res
