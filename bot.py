import requests
import tweepy
from bs4 import BeautifulSoup
import time
import datetime

class Bot:
    def __init__(self):
        self.valid_links = ['www.lds.org/media-library/video','www.lds.org/pages/mormon-messages','www.lds.org/youth/video']
        self.get_auth_tokens()
    def run(self):
        while True:
            self.download_page()
            self.extract_links()
            self.timeout()
    def timeout(self):
        # sleep for 60 minutes
        time.sleep(3600)
    def extract_links(self):
        soup = BeautifulSoup(open('page.html'))
        tags = soup.find_all('a')
        links = []
        for link in tags:
            links.append(link.get('href'))
        valid = []
        for link in links:
            for possible in self.valid_links:
                if possible in link:
                    valid.append(link)
                    break
        no_dups = list(set(valid))
        self.compare_new_and_old(no_dups)
    def compare_new_and_old(self,valid):
        lines = []
        with open('existing.txt','rb') as f:
            lines = f.readlines()
        stripped = []
        if len(lines) > 0:
            stripped = [line.strip() for line in lines]
        new_links = []
        for link in valid:
            if link not in stripped:
                new_links.append(link)
        if len(new_links) > 0:
            for link in new_links:
                self.tweet_new(link)
            with open('existing.txt','a') as f:
                for link in new_links:
                    f.write(link+'\n')
    def get_auth_tokens(self):
        with open('authenticators.txt', 'rb') as f:
            self.consumer_key = f.readline().strip()
            self.consumer_secret = f.readline().strip()
            self.access_token = f.readline().strip()
            self.access_secret = f.readline().strip()
        auth = tweepy.OAuthHandler(self.consumer_key, self.consumer_secret)
        auth.set_access_token(self.access_token, self.access_secret)
        self.auth = auth
        api = tweepy.API(self.auth)
        self.api = api
    def tweet_new(self, link):
        tweet = 'New Mormon Message at ' + link + ' ' + datetime.datetime.now().strftime("%I:%M:%S%p on %B %d, %Y")
        self.api.update_status(tweet)
    def download_page(self):
        page = 'https://www.lds.org/pages/mormon-messages/topics?lang=eng'
        r = requests.get(page, stream=True)
        while r.status_code != 200:
            r = requests.get(page, stream=True)
        with open('page.html', 'wb') as f:
            for chunk in r.iter_content(10000):
                f.write(chunk)

if __name__ == "__main__":
    b = Bot()
    b.run()
