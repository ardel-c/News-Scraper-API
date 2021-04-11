import requests
from bs4 import BeautifulSoup
from .models import News

def create_news(keyword):

    request_payload = {'query': keyword}
    resp = requests.get('https://www.detik.com/search/searchall', params = request_payload)
    soup = BeautifulSoup(resp.text, features="html.parser")

    # get the title
    title=[]
    for s in soup.find_all('h2', attrs={'class':'title'}):
        title.append(s.text)

    # get the date
    date=[]
    for s in soup.find_all('span', attrs={'class':'date'}):
        date.append(s.text)

    # date reformatting, example: 10 Apr 2021 16:27 WIB
    dates = [x[-21:] for x in date]

    # get the category
    category=[]
    for s in soup.find_all('span', attrs={'class':'category'}):
        category.append(s.text)

    # get the description
    description=[]
    for s in soup.find_all('span', attrs={'class':'box_text'}):
        for desc in s.find_all('p'):   
            description.append(desc.text)

    # get the news link
    url=[]
    for s in soup.find_all('div', attrs={'class':'list media_rows list-berita'}):
        for a in s.find_all('a'):   
            url.append(a.get('href'))

    News.objects.all().delete()
    for idx in range(len(title)):
        # create objects in database
        News.objects.create(
            title=title[idx],
            date=dates[idx],
            category=category[idx],
            description=description[idx],
            url=url[idx],
        )