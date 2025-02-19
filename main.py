import requests
from datetime import datetime, date

headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:135.0) Gecko/20100101 Firefox/135.0"
}

url = "https://collegetsaritsyno.mskobr.ru/v1/api/folder_and_file/list/30190"


def get_link(url, course, week):
    s = requests.Session()
    response = s.get(url=url, headers=headers)

    resp = response.json()
    try:
        
        req = resp["data"]["folders"][2]['files'][course + 4*week]
        
        altName = req.get('altName')
        title = req.get('title')
        link = "https://collegetsaritsyno.mskobr.ru"+req.get('src')

        if altName[:10] == 'raspisanie':
            date_diff = get_date_diff(title[-10:])
            return link
        else:
            return None

    except Exception as ex:
        print(ex)
        return None


def get_date_diff(getted_date):
    try:
        date_format = '%d.%m.%Y'

        today = date.today()
        last_day = datetime.strptime(getted_date, date_format).date()

        delta = last_day - today
        return delta.days
    except Exception as ex:
        print(ex)
        return None