import requests
import yaml

def post(post):
    # Attempt to load config
    config_location = "config/ifttt.yml"
    config = {}
    try:
        with open(config_location, 'r') as stream:
            try:
                config = yaml.load(stream)['config']
            except yaml.YAMLError as e:
                print(e)
    except IOError:
        print("Please create config: {}".format(config_location))

    if not config['enabled'] == 'True':
        print('IFTTT disabled')
        return

    print("Posting to IFTTT")
    share_token = config['share_token'].strip('#')
    tag_present = False
    for tag in post['tags']:
        if tag.term == share_token:
            tag_present = True

    if tag_present:
        report = {}
        report["value1"] = post['link']
        message = post['summary'].strip(config['share_token']).strip()
        try:
            if config['invite']:
                message = "{}\n\nJoin my Mastodon Instance through this invite: {}".format(message, config['invite'])
        except KeyError:
            pass
        report["value2"] = message
        requests.post(config['maker_url'], data=report)    
