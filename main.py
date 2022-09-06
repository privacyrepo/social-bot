from Twitter_base import Twitter as Tw


# Twitter basic functionality; Reference - Twitter_base.py


# Twitter post text;
def tw_post_text(caption):
    Tw.tweet_text(caption)
    pass


# Twitter post media + text;
def tw_post_media_text(image, caption):
    Tw.tweet_media_text(image, caption)
    pass


# Twitter reply to post with text using the post id;
def tw_reply(tw_id, caption):
    Tw.tweet_reply(tw_id, caption)
    pass


# Returns tweets created before the given date, in the given language containing the keyword.
def tw_search(keyword_input, language_input, until_date):
    Tw.tweet_search(keyword_input, language_input, until_date)

# keyword = 'python'
# lang = 'en'
# until = '2022-09-01'
# tw_search(keyword, lang, until)
