import tweepy

#ich hab mal die access keys raus, die musst du dann wieder einfügen
class TwitterStreamListener(tweepy.StreamListener):

    #initialize the listener with a variable to keep track of the received tweets and the accepted tweets
    #as well as a variable for how many tweets we want to get and a list that will temporarily store the
    #tweets before saving them to a json file
    def __init__(self):
        super().__init__()
        self.unfilteredCount = 0
        self.filteredCount = 0
        self.limit = 10
        self.tweets = []

    def on_data(self, data):
        #increase the received tweets count and load the received tweet to json format
        self.unfilteredCount += 1
        data_json = json.loads(data)

        #if the tweet text has 50 or more characters, add it to the list
        if len(data_json["text"]) >= 50:
            self.tweets.append(data_json)
            self.filteredCount += 1

        #as long as we have less than the amount of tweets we want, we continue
        if self.filteredCount < self.limit:
            return True
        #once we've received the desired amount of tweets, write the list containing the tweets to a json file
        else:
            file = open("swe.json", "a+")
            file.write(json.dumps(self.tweets))

            #write the yieldrate into a separate file
            yieldfile = open("yieldrate.txt", "a+")
            yieldfile.write(str(self.filteredCount) + " out of " + str(self.unfilteredCount)
                            + " received tweets\nyieldrate: " + str(self.filteredCount * 100 / self.unfilteredCount)
                            + "%")
            #and end the stream
            stream.disconnect()


    def on_error(self, status_code):
        if status_code == 403:
            print("The request is understood, but it has been refused or access is not allowed. Limit is maybe reached")
            return False


auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
auth.secure = True
auth.set_access_token(accessToken, accessTokenSecret)
api = tweepy.API(auth)

streamListener = TwitterStreamListener()

stream = tweepy.Stream(auth=api.auth, listener=streamListener)



stream.filter(languages= ['sv'], track=['och', 'på', 'som'], async = 'true')

