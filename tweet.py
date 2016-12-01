import tweepy

ckey = "KQRcC5Gb6IV1dxmQrzOtl7exM"
csec = "Gy8oFSP1tBvsxO9Cee9xcM27N7TGNaw1IGepgSjt0xRxqEquLC"
at = "601808805-37UZFta5MgGglZMKhnrlwn214TUQwZKwCyeeuC05"
ats = "q99TfO6xVSUL4yU9UKojVDHyIoNjnyr4esX3IxGddB2Qx"

auth = tweepy.OAuthHandler(ckey, csec)
auth.set_access_token(at, ats)
api = tweepy.API(auth)


name = raw_input("Enter Tweeter Username (without @): ")

# print(name)

num = raw_input("How many tweets you want to extract: ")
try:
	user = api.user_timeline(name,count=num)

	# print(user)	
	i = 1
	for tweets in user:

		print("("+str(i)+") " + tweets.text)
		print("")
		# print("")
		i = i + 1

except:
	print("User not Found")


# api = tweepy.API(auth)

# public_tweets = api.home_timeline()
# for tweet in public_tweets:
#     print tweet.text