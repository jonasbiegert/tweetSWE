import tweepy

#ich hab mal die access keys raus, die musst du dann wieder einfügen

class TwitterStreamListener(tweepy.StreamListener):
    """ A listener handles tweets are the received from the stream.
    This is a basic listener that just prints received tweets to stdout.
    """

    def on_status(self, status):
        #getTweet(status)
        TweetIDtoTxt(status)




    def on_error(self, status_code):
        if status_code == 403:
            print("The request is understood, but it has been refused or access is not allowed. Limit is maybe reached")
            return False

def getTweet(tweet):
    if len(tweet.text) >= 50:
        print("NEW TWEET")
        print(tweet.text)
        print(tweet.lang)

def TweetIDtoTxt(tweet):
    file = open("swe.txt", "a+")
    file.write(tweet.id_str)

# Authentication
auth = tweepy.OAuthHandler(consumerKey, consumerSecret) #logs in to twitter
auth.secure = True
auth.set_access_token(accessToken, accessTokenSecret)
api = tweepy.API(auth)

streamListener = TwitterStreamListener()

stream = tweepy.Stream(auth=api.auth, listener=streamListener)

try:


    stream.filter(languages= ['sv'], track=['och', 'på', 'som'])

except:
    print("search interrupted")
