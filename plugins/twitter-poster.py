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

    api = twitter.Api(consumer_key=config['consumer_key'],
            consumer_secret=config['consumer_secret'],
            access_token_key=config['access_token_key'],
            access_token_secret=config['access_token_secret'])
    extras_length = len(post['link']) + 4
    cut_index = 140-extras_length
    status = api.PostUpdate('{}... {}'.format( post['summary'][:cut_index], post['link']))
    print(status)
