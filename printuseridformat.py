# 使用するライブラリをインポート
import tweepy

# 取得したAPIキーを入力
CONSUMER_KEY = "XXX"
CONSUMER_SECRET = "XXX"
ACCESS_TOKEN = "XXX"
ACCESS_TOKEN_SECRET = "XXX"


# フォローリスト取得処理
cursor = -1
while cursor != 0:
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth, wait_on_rate_limit=True)
    # "XXX"には取得元のアカウント名を入力
    itr = tweepy.Cursor(api.friends_ids, id='@XXX', cursor=cursor).pages()
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
