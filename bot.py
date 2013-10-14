import requests
import tweepy

class Bot:
    def __init__(self):
        get_auth_tokens()
    def timeout(self):
        import time
        # sleep for 30 minutes
        time.sleep(1800)
    def check_diff(self):
    def get_auth_tokens(self):
        f = open('authenticators.txt', 'rb')
        self.consumer_key = f.readline().strip()
        self.consumer_secret = f.readline().strip()
        self.access_token = f.readline().strip()
        self.access_secret = f.readline().strip()
        f.close()
        auth = tweepy.OAuthHandler(self.consumer_key, self.consumer_secret)
        auth.set_access_token(self.access_token, self.access_secret)
        self.auth = auth
        api = tweepy.API(self.auth)
        self.api = api
    def tweet_new(self, link, msg_name):
        tweet = 'Updated: ' + msg_name + ' ' + link
        self.api.update_status(tweet)
    def download_page(self):
        page = 'https://www.lds.org/pages/mormon-messages/topics?lang=eng'
        r = requests.get(page, stream=True)
        while r.status_code != 200:
            r = requests.get(page, stream=True)
        f = open('updated.html', 'wb')
        f.write(r.content)
        f.close()

if __name__ == "__main__":
    b = Bot()
