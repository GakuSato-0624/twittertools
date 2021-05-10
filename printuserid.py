# 使用するライブラリをインポート
import tweepy

# 取得したAPIキーを入力
CONSUMER_KEY = "4DFeL8Ilu5bJ9jrnl5izH9I66"
CONSUMER_SECRET = "wsS9zxhjz1V32bKEDfVFuv77r1FqlvQwls7fFBU2ZUl5LvDcAc"
ACCESS_TOKEN = "832566770162556929-gFsjjU3LOmQiJPz4HF0KSNau5wOvy7E"
ACCESS_TOKEN_SECRET = "fMFqxFRg9yBWfXqC5AU2Zu0oAwNIMnQgWcPH1i81ZJ0lo"

# フォローリスト取得処理
cursor = -1
while cursor != 0:
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth, wait_on_rate_limit=True)
    # "XXX"には取得元のアカウント名を入力
    itr = tweepy.Cursor(api.friends_ids, id='@kooooook1215', cursor=cursor).pages()
    try:
        for friends_ids in itr.next():
            try:
                user = api.get_user(friends_ids)
                user_info = [user.screen_name]
                print(user_info)
            # tweepyでエラーが発生時の例外処理
            except tweepy.error.TweepError as e:
                print(e.reason)
    # 接続エラー発生時の例外処理
    except ConnectionError as e:
        print(e.reason)
    cursor = itr.next_cursor
