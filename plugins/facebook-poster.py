import facebook
import yaml


def get_api(cfg):
    print(cfg['access_token'])
    graph = facebook.GraphAPI(cfg['access_token'])
    return graph


def post(post):
    # Attempt to load config
    config_location = "config/facebook.yml"
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
        print('Facebook disabled')
        return

    print("Posting to Facebook")
    share_token = config['share_token'].strip('#')
    tag_present = False
    for tag in post['tags']:
        if tag.term == share_token:
            tag_present = True

    if tag_present:
        api = get_api(config)
        try:
            status = api.put_wall_post(post['link'])
            print(status)
        except facebook.GraphAPIError as e:
            print(e)
    else:
        print("Post doesn't contain the share token - {}".format(share_token))
