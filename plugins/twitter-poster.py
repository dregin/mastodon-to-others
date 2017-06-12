import twitter
import yaml


def post(post):
    print("Posting to Twitter")
    # Attempt to load config
    config_location = "config/twitter.yml"
    config = {}
    try:
        with open(config_location, 'r') as stream:
            try:
                config = yaml.load(stream)['config']
            except yaml.YAMLError as e:
                print(e)
    except IOError:
        print("Please create config: {}".format(config_location))
        print("Use helper script @ https://github.com/bear/python-twitter/blob/master/get_access_token.py")

    share_token = config['share_token'].strip('#')
    tag_present = False
    for tag in post['tags']:
        if tag.term == share_token:
            tag_present = True

    if tag_present:
        api = twitter.Api(consumer_key=config['consumer_key'],
                consumer_secret=config['consumer_secret'],
                access_token_key=config['access_token_key'],
                access_token_secret=config['access_token_secret'])
        try:
            api.PostUpdate(post['link'])
            print('Posted to twitter')
        except twitter.TwitterError as e:
            print(e.message[0]['message'])
    else:
        print("Post doesn't contain the share token - {}".format(share_token))
