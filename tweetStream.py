import tweepy

consumerKey = '2G9h07H0K0ituLF6QAzxQUrzP'
consumerSecret = 'ETn10ZMeNcAZI83tFSBe9Q0TsOTeRjxQEtCEe37NNB9YuDmoNv'
accessToken = '990189313693487104-r4Bjs1ZSfLOCCwZcCjWLZO4tdakq1BJ'
accessTokenSecret = 'Y0UFFbixy262EZGG3RPyyBSNLBGGId7f8KvJjr0JAUrYH'

class TwitterStreamListener(tweepy.StreamListener):
    """ A listener handles tweets are the received from the stream.
    This is a basic listener that just prints received tweets to stdout.
    """

    def on_status(self, status):
        getTweet(status)

    def on_error(self, status_code):
        if status_code == 403:
            print("The request is understood, but it has been refused or access is not allowed. Limit is maybe reached")
            return False
def getTweet(tweet):
    if len(tweet.text) >= 50:
        print(tweet.text)



# Authentication
auth = tweepy.OAuthHandler(consumerKey, consumerSecret) #logs in to twitter
auth.secure = True
auth.set_access_token(accessToken, accessTokenSecret)
api = tweepy.API(auth)

streamListener = TwitterStreamListener()

stream = tweepy.Stream(auth=api.auth, listener=streamListener)

try:

    stream.filter(languages=['de'], track=['ich', 'es', 'gibt'])
except:
    print("search interrupted")
