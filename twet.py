
import socket
import tweepy
#Hashtags
hashtags=['#politics','#cats','#pfizer','#deports','#dogs','#colombia','#school','#g>

apikey="u2R8aiTfw6E0TPmVAPJl3KNrK"
apisecret="FKXeyOZt22vC8Z7NuyPI8bdfzz0FVpS25QMKADIvpt5kDNBLE7"
access_token="970453817513992193-PhFNcOVbtj3mBvSojJRrBml4NtPqa9n"
access_token_secret="sQtAG7KuSZ0COLYJbIxg3lEJVr4f6AIYIu3H7HMXMcHmK"

#Socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(('localhost',9898))
s.listen()
conn,addr=s.accept()
print(f'conectado con {addr}')

#Funcion escucha
class TwitterListener(tweepy.StreamListener):
    def on_status(self, status):
        diccionario=status.entities['hashtags']
        print(30*'*')
        for hashtag in diccionario:
          if '#'+str(hashtag['text']) in hashtags:
            conn.sendall(bytes(hashtag['text']+'\n',encoding='utf-8'))
            print(hashtag['text'])

auth=tweepy.OAuthHandler(apikey,apisecret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
streamListener = TwitterListener()
stream = tweepy.Stream(auth = api.auth, listener=streamListener)
stream.filter(track=hashtags)
