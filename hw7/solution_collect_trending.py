import requests
import argparse
import os
import json
from datetime import datetime
import bs4

def get_page_with_caching(url, cache_loc, time_diff=60*30):
    out_html = None
    if os.path.isfile(cache_loc):
        print("Cache found for %s." % url)
        with open(cache_loc, 'r') as f:
            outdict = json.load(f)
        
        last_cached = datetime.strptime(outdict['last_cached'], "%y-%m-%d %H:%M:%S")

        if (datetime.now() - last_cached).total_seconds() <= time_diff:
            out_html = outdict['html']

    if out_html is None:
        print("Cache not found for %s." % url)
        useragent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36'
        r = requests.get(url, headers={'User-Agent': useragent})
        out_html = r.text

        outdict = {'last_cached': datetime.strftime(datetime.now(), "%y-%m-%d %H:%M:%S"),
                   'html': out_html}
        with open(cache_loc, 'w') as f:
            json.dump(outdict, f)
    
    return out_html

def get_cache_hash(title, hashfile):
    with open(hashfile, 'r') as f:
        hashlist = json.load(f)

    if title in hashlist:
        return hashlist[title]
    
    new_index = max(hashlist.values())+1 if len(hashlist.items()) > 0 else 0
    hashlist[title] = new_index

    with open(hashfile, 'w') as f:
        json.dump(hashlist, f)
    
    return new_index

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-o", "--outputfile", required=True, type=str, help='Output file')

    args = parser.parse_args()

    BASE_URL = 'https://montrealgazette.com'

    homepage_text = get_page_with_caching(BASE_URL + '/category/news/',
                                          'cache_files/homepage.json')

    soup = bs4.BeautifulSoup(homepage_text, 'html.parser')
    trending_div = soup.find('div', class_='col-xs-12 top-trending')
    trending_stories = trending_div.find_all('a', class_='article-card__link')
    ts_links = [BASE_URL + ele['href'] for ele in trending_stories]

    story_details = []
    for story in trending_stories:
        hashindex = get_cache_hash(story['aria-label'], 'cache_files/hash_list.json')

        story_text = get_page_with_caching(BASE_URL + story['href'],
                                          'cache_files/%d.json' % hashindex)

        soup = bs4.BeautifulSoup(story_text, 'html.parser')
        title = soup.find("h1", class_="article-title").text
        publication_date = soup.find("span", class_="published-date__since").text
        author_object = soup.find("span", class_="published-by__author")
        if author_object is None:
            author = "Montreal Gazette"
        else:
            author = author_object.find("a").text
        blurb = soup.find("p", class_="article-subtitle").text

        story_details.append({'title': title, 'publication_date': publication_date,
                              'author': author, 'blurb': blurb})
    
    with open(args.outputfile, 'w') as f:
        json.dump(story_details, f)

if __name__=="__main__":
    main()