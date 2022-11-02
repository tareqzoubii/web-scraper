from idna import alabel
import requests
from bs4 import BeautifulSoup

URL = 'https://en.wikipedia.org/wiki/History_of_Mexico'

def get_citations_needed_count(url):
    '''web scraper should report the number of citations needed.'''

    URL = url
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

def get_citations_needed_report(url):
    '''web scraper function should identify those cases AND include the relevant passage'''

    URL2 =  url
    page2 = requests.get(URL2)
    soup = BeautifulSoup(page2.content, 'html.parser')
    all = soup.find_all('span', text='citation needed')
    all_paragraphs = []
    for post in all:
        all_paragraphs.append(post.find_parents('p')[0].text.strip())
        clean_paragraphs = '\n'.join(all_paragraphs)
    return clean_paragraphs

#print(get_citations_needed_report(URL))
#print(get_citations_needed_count(URL))
count = get_citations_needed_count(URL)
paragraphs = get_citations_needed_report(URL)
print(count)
print(paragraphs)