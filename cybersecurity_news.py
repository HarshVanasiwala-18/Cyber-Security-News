from calendar import c
import feedparser
import webbrowser
import requests
import json

def cyber_news():
    print('--Security News Website List--')
    print('Index.       Name.')
    print(' 0.      TheHackerNews')
    print(' 1.       ThreatPost')
    print(' 2.      NakedSecurity')

    website_list = ('https://feeds.feedburner.com/TheHackersNews', 'https://threatpost.com/feed', 'https://nakedsecurity.sophos.com/feed')

    website_input = int(input('Enter website by number (0-2): '))

    NewsFeed = feedparser.parse(website_list[website_input])
    article_list = []
    article_link = []
    for i in range(5):
        article = NewsFeed.entries[i]
        titles = article.title
        link = article.link
        article_link.append(link)
        article_list.append(titles)

    article_num = 1
    for article in article_list:
        print('[{}] {}'.format(str(article_num), article))
        article_num += 1

    article_link_click = False
    while not article_link_click:
        user_click = int(input('Choose the link you want to open (1-5): '))
        webbrowser.open(article_link[user_click-1])
        article_link_click = True

def cve():

    content = requests.get('https://cve.circl.lu/api/last')
    json = content.json()

    for item in json:
        print("{} {}".format('Vuln Num:', item['id']))
        print("{} {}\n".format('Description:', item['summary']))

print('1. Cyber News')
print('2. Vuln CVE')
var = int(input('Enter number (1 or 2): '))
if var == 1:
    cyber_news()
elif var == 2:
    cve()
