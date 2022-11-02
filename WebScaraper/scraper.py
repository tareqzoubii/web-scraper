import requests
from bs4 import BeautifulSoup

URL = 'https://en.wikipedia.org/wiki/History_of_Mexico'
page = requests.get(URL)
# print(page.content)
# now i need to change the content to HTML
soup = BeautifulSoup(page.content, 'html.parser')
#print(soup)
all_texts = soup.find_all('span', text='citation needed')
#print(all_texts)
count = len(all_texts)
print(count) # 12! good!

# now i need to put every thing inside a def!

def get_citations_needed_count():
    '''web scraper should report the number of citations needed.'''

    URL = 'https://en.wikipedia.org/wiki/History_of_Mexico'
    page = requests.get(URL)
    # print(page.content)
    # now i need to change the content to HTML
    soup = BeautifulSoup(page.content, 'html.parser')
    #print(soup)
    all_texts = soup.find_all('span', text='citation needed')
    #print(all_texts)
    count = len(all_texts)
    # print(count) # 12! good!
    return count

# def get_citations_needed_report():
#     '''web scraper should identify those cases AND include the relevant passage'''

#     URL2 =  'https://en.wikipedia.org/wiki/History_of_Mexico'
#     page2 = requests.get(URL2)
#     soup = BeautifulSoup(page2.content, 'html.parser')
#     all = soup.find_all('span', text='citation needed')
#     all_paragraphs = []
#     for post in all:
#         paragraphs = post.find_all('p', text='citation needed')
#         print(paragraphs)
#     return paragraphs