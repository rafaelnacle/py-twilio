import requests
from bs4 import BeautifulSoup

base_url = 'https://www.linkcorreios.com.br/'


def tracking_info(code):
    tracking_data = []
    url = f"{base_url}?id={code}"
    r_correios = requests.get(url)

    html_correios = r_correios.text

    soup = BeautifulSoup(html_correios, "html.parser")

    card = soup.find('div', class_="card-header")
    uls = card.find_all('ul', class_="linha_status")

    for ul in uls:
        lis = ul.find_all('li')
        status = lis[0].text
        date = lis[1].text
        origin = lis[2].text
        destination = lis[3].text

        data = {
            'status': status,
            'date': date,
            'origin': origin,
            'destination': destination,
        }
        tracking_data.append(data)

    print(tracking_data)
    return f"{data['status']}\n{data['date']}\n{data['origin']}\n{data['destination']}"
