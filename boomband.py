import requests
from bs4 import BeautifulSoup


headers = {'Authorization': 'Basic YWRtaW46MDMzOWU2'}

page = requests.get('http://192.168.0.1/wlstatbl.htm', headers=headers)
soup = BeautifulSoup(page.content, 'html.parser')

rows = soup.find_all('tr')[3:8]

for tr in rows:
    columns = tr.find_all('td')[:4]

    columns_text = []
    list_ = []
    for td in columns:
        list_.append(td.text.strip())

    received = str(int(list_[2]) / 10**3)
    sent = str(int(list_[3]) / 10**3)

    columns_text.append(list_[0])
    columns_text.append(received)
    columns_text.append(sent)

    print("\t".join(columns_text))
