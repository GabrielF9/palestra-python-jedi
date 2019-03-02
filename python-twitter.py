keys = {
  'consumer_key': None,
  'consumer_secret': None,
  'access_token': None,
  'access_token_secret': None
}

# Importação de Libs
from twython import Twython

consumer_key = keys['consumer_key']
consumer_secret = keys['consumer_secret']
access_token = keys['access_token']
access_token_secret = keys['access_token_secret']

tw = Twython(consumer_key, consumer_secret, access_token, access_token_secret)

""" query = 'python'
result = tw.search(q=query, count=1, lang='pt')

print(result['statuses'][0]['text']) """

person = tw.get_user_timeline(screen_name="@souogabriel_py")
print(person[1]['text'])
