import requests_cache
from bs4 import BeautifulSoup
import requests
import json

requests_cache.install_cache('montreal_gazetter_cache', expire_after=300)

def get_trending_links():
    url = "https://montrealgazette.com/"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    # find all 5 trending articles and get their links
    trending_links = []
    base_url = 'https://montrealgazette.com'

    trending_articles = soup.find('div', attrs={'class': 'article-card__details'}) 
    links = trending_articles.find_all('a', class_='article-card__link')
    base_url = 'https://montrealgazette.com'
    for link_tag in links:
        link = link_tag.get('href')
        if link:
            full_link = base_url + link
            trending_links.append(full_link)

    #do the same for the other 4 articles
    tt = soup.find('div', class_='col-xs-12 col-sm-4 col-lg-5 hero-feed__mini-col')
    trenders = tt.find_all('article', class_='article-card article-card--no-category-top article-card--small-padlock')
    for trend in trenders:
        link = trend.find('a', class_='article-card__link').get('href')
        full_link = base_url + link
        trending_links.append(full_link)
        
    return trending_links

def get_article_content(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    article = {}
    article['title'] = soup.find('h1', class_='article-title').text
    article['publication_date'] = soup.find('span', class_='published-date__since').text
    article['author'] = soup.find('span', class_='published-by__author').text
    article['blurb'] = soup.find('div', class_='article-header__detail__texts').text
    return article

def get_trending_articles():
    trending_links = get_trending_links()
    trending_articles = []
    for link in trending_links:
        article = get_article_content(link)
        trending_articles.append(article)
    return trending_articles

def main():
    trending_articles = get_trending_articles()
    print(json.dumps(trending_articles, indent=4))
    # put into -o argument given named file

    import argparse
    parser = argparse.ArgumentParser(description='Scrape Montreal Gazette for trending stories')
    parser.add_argument('-o', '--output', type=str, help='Output JSON file', required=True)
    args = parser.parse_args()
    with open(args.output, 'w') as f:
        json.dump(trending_articles, f, indent=4)


if __name__ == '__main__':
    main()
