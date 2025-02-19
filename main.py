import requests
import json

headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:135.0) Gecko/20100101 Firefox/135.0"
}

def get_page(url):
    s = requests.Session()
    response = s.get(url=url, headers=headers)

    with open("index.html", "w") as file:
        file.write(response.text)

def get_json(url):
    s = requests.Session()
    response = s.get(url=url, headers=headers)

    with open("result.json", "w") as file:
        json.dump(response.json(), file, indent=4, ensure_ascii=False)

def get_link(url):
    s = requests.Session()
    response = s.get(url=url, headers=headers)

    resp = response.json()
    link = resp["data"]["folders"][2]['files'][0]
    print(link.get('src'))


def main():
    get_link("https://collegetsaritsyno.mskobr.ru/v1/api/folder_and_file/list/30190")

if __name__ == "__main__":
    main()