import tweepy
from client_secrets import twitter_apikey, twitter_apikey_secret
from client_secrets import twitter_access_token, twitter_access_token_secret

# Twitter Base-Logic;
# This is the class that holds and proceed all the processes such as post, reply & etc.


class Twitter:

    def __init__(self, *args, **kwargs):
        pass

    # Twitter post text;
    def tweet_text(caption):
        auth = tweepy.OAuthHandler(twitter_apikey, twitter_apikey_secret)
        auth.set_access_token(twitter_access_token, twitter_access_token_secret)
        api = tweepy.API(auth)
        api.update_status(str(caption))
        print(f'Successfully posted! - text: "{caption}"')
        print(f'Action taken by Twitter_apikey: "{twitter_apikey}"')
        print(f'Action taken by Twitter_apikey_secret: "{twitter_apikey_secret}"')
        pass

    # Twitter post media + text;
    def tweet_media_text(image, caption):
        auth = tweepy.OAuthHandler(twitter_apikey, twitter_apikey_secret)
        auth.set_access_token(twitter_access_token, twitter_access_token_secret)
        api = tweepy.API(auth)
        status = str(caption)
        filename = "image1.jpeg"
        api.update_status_with_media(status, filename)
        print(f'Successfully posted! - text: "{caption}", Media (cannot be displayed yet)')
        print(f'Action taken by Twitter_apikey: "{twitter_apikey}"')
        print(f'Action taken by Twitter_apikey_secret: "{twitter_apikey_secret}"')
        pass

    # Twitter reply to post with text using the post id;
    def tweet_reply(tw_id, caption):
        auth = tweepy.OAuthHandler(twitter_apikey, twitter_apikey_secret)
        auth.set_access_token(twitter_access_token, twitter_access_token_secret)
        api = tweepy.API(auth)
        api.update_status(status=caption,
                          in_reply_to_status_id=tw_id, auto_populate_reply_metadata=True)
        print(f'Successfully replied! - text: "{caption}" @ post_id: "{tw_id}"')
        print(f'Action taken by Twitter_apikey: "{twitter_apikey}"')
        print(f'Action taken by Twitter_apikey_secret: "{twitter_apikey_secret}"')
        pass

    # Returns tweets created before the given date, in the given language containing the keyword.
    def tweet_search(keyword, language, until_date):
        auth = tweepy.OAuthHandler(twitter_apikey, twitter_apikey_secret)
        auth.set_access_token(twitter_access_token, twitter_access_token_secret)
        api = tweepy.API(auth, wait_on_rate_limit=True)
        tweets = api.search_tweets(keyword, lang=language, until=until_date, tweet_mode="extended")
        for tweet in tweets:
            print(tweet)

