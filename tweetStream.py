import tweepy

#ich hab mal die access keys raus, die musst du dann wieder einfügen
class TwitterStreamListener(tweepy.StreamListener):
    """ A listener handles tweets are the received from the stream.
    This is a basic listener that just prints received tweets to stdout.
    """

    def __init__(self):
        super().__init__()
        self.UnfilteredCount = 0
        self.FilteredCount = 0
        self.limit = 10
        self.receivedTweets = "0"

    def on_data(self, data):
        data_json = json.loads(data)
        TweetToJson(data_json)
        self.FilteredCount += 1
        if self.FilteredCount < self.limit:
            return True
        else:
            stream.disconnect()



    def on_status(self, status):
        getTweet(status)
        self.count += 1
        if self.count < self.limit:
            return True
        else:
            stream.disconnect()
        #TweetIDtoTxt(status)



    def on_error(self, status_code):
        if status_code == 403:
            print("The request is understood, but it has been refused or access is not allowed. Limit is maybe reached")
            return False


tweetCount = 0;

def getTweet(tweet):
    if len(tweet.text) >= 50:
        print("NEW TWEET")
        print(tweet.text)
        print(tweet.lang)

def TweetIDtoTxt(tweet):
    file = open("swe.txt", "a+")
    file.write(tweet.id_str + "\n")

def TweetToJson(tweet):
    if len(tweet.text) >= 50:
        file = open("swe.json", "a+")
        file.write(str (tweet))

# Authentication
auth = tweepy.OAuthHandler(consumerKey, consumerSecret) #logs in to twitter
auth.secure = True
auth.set_access_token(accessToken, accessTokenSecret)
api = tweepy.API(auth)

streamListener = TwitterStreamListener()

stream = tweepy.Stream(auth=api.auth, listener=streamListener)

try:


    stream.filter(languages= ['sv'], track=['och', 'på', 'som'], async = 'true')

except:
    print("search interrupted")
