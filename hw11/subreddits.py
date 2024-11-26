"""
Select 6 subreddits  
select r/sports, r/montreal, r/volleyball, r/soccer, r/football, r/tennis. 
Note that, generally speaking, the more related the subreddits are, the more helpful TF-IDF will be.
Once you've selected them, download the latest 200 posts from each. Put them in files: <subreddit_name>.json
"""

import requests
import json
import time

subreddits = ['sports', 'montreal', 'volleyball', 'soccer', 'football', 'tennis']
headers = {'User-Agent': 'Mozilla/5.0 (compatible; RedditPostFetcher/1.0)'}

def fetch_posts(subreddit_name):
    url = f"https://www.reddit.com/r/{subreddit_name}/new.json?limit=100"
    all_posts = []

    after = None
    while len(all_posts) < 200:
        params = {'after': after} if after else {}
        response = requests.get(url, headers=headers, params=params)
        if response.status_code != 200:
            print(f"Failed to fetch posts for {subreddit_name}. Status code: {response.status_code}")
            break

        data = response.json()
        posts = data.get('data', {}).get('children', [])
        if not posts:
            break

        for post in posts:
            all_posts.append({
                'title': post['data']['title'],
                'score': post['data']['score'],
                'id': post['data']['id'],
                'url': post['data']['url'],
                'created_utc': post['data']['created_utc'],
                'num_comments': post['data']['num_comments'],
                'selftext': post['data']['selftext'],
                'author': post['data']['author']
            })

        after = data['data'].get('after')
        if not after:
            break

        time.sleep(1)

    return all_posts[:200]

def main():
    for subreddit in subreddits:
        posts = fetch_posts(subreddit)
        with open(f"{subreddit}.json", "w", encoding="utf-8") as file:
            json.dump(posts, file, ensure_ascii=False, indent=4)

    print("Posts have been saved successfully!")

if __name__ == "__main__":
    main()