import requests
from fake_useragent import UserAgent
from bs4 import BeautifulSoup

# Глобальные переменные
a = 1

page_link = input("Введите URL: ").strip()
outfile = open('database.txt', 'w', encoding='utf-8')

response = requests.get(page_link, headers={'User-Agent': UserAgent().chrome})
soup = BeautifulSoup(response.text, 'html.parser')
link = soup.find('a', attrs={'data-auto-id': 'loadMoreProducts'})
while link:
    NextPage = link.get('href')
    if NextPage:
        a += 1
        response = requests.get(NextPage, headers={'User-Agent': UserAgent().chrome})
        soup = BeautifulSoup(response.text, 'html.parser')
        link = soup.find('a', attrs={'data-auto-id': 'loadMoreProducts'})
print(a)
for i in range(a):
    response = requests.get(page_link, headers={'User-Agent': UserAgent().chrome})
    soup = BeautifulSoup(response.text, 'html.parser')
    for link in soup.find_all('a', attrs={'class': '_3TqU78D'}):
        link1 = link.get('aria-label')
        if link1:
            outfile.write(link1)
            outfile.write('\n')
            print(link1)
    try:
        page_link = soup.find('a', attrs={'data-auto-id':'loadMoreProducts'})
        page_link = page_link.get('href')
    except:
        b = 10
outfile.close()
