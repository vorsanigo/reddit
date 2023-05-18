import requests
import os
import pandas as pd
import praw
from pmaw import PushshiftAPI
import datetime as dt
import json

#TODO subreddit.hot() - subreddit.new() - subreddit.top(time_filter="day") -> or month, year, all, hour
# subreddit -> https://praw.readthedocs.io/en/stable/code_overview/models/subreddit.html#praw.models.Subreddit.top
# praw documentation -> https://praw.readthedocs.io/en/stable/index.html
# praw github -> https://github.com/mattpodolak/pmaw
# praw example -> https://medium.com/mcd-unison/using-pushshift-api-for-data-analysis-on-reddit-b08d339c48b8


# note that CLIENT_ID refers to 'personal use script' and SECRET_TOKEN to 'token'
'''auth = requests.auth.HTTPBasicAuth('tEa4Ddj6AGrkDgCW2VEukw', '2KTHCrQWnbgz28NScHFFSBSg4oIgPw')

# here we pass our login method (password), username, and password
data = {'grant_type': 'password',
        'username': 'veror_',
        'password': 'reddit00'}

# setup our header info, which gives reddit a brief description of our app
headers = {'User-Agent': 'MyBot/0.0.1'}

# send our request for an OAuth token
res = requests.post('https://www.reddit.com/api/v1/access_token',
                    auth=auth, data=data, headers=headers)

# convert response to JSON and pull access_token value
TOKEN = res.json()['access_token']

# add authorization to our headers dictionary
headers = {**headers, **{'Authorization': f"bearer {TOKEN}"}}

# while the token is valid (~2 hours) we just add headers=headers to our requests
requests.get('https://oauth.reddit.com/api/v1/me', headers=headers)


res = requests.get("https://oauth.reddit.com/r/python/hot",
                   headers=headers)

df = pd.DataFrame()  # initialize dataframe

# loop through each post retrieved from GET request
for post in res.json()['data']['children']:
    # append relevant data to dataframe
    df = pd.concat([df, pd.DataFrame({
        'subreddit': [post['data']['subreddit']],
        'title': [post['data']['title']],
        'selftext': [post['data']['selftext']],
        'upvote_ratio': [post['data']['upvote_ratio']],
        'ups': [post['data']['ups']],
        'downs': [post['data']['downs']],
        'score': [post['data']['score']]
    })], ignore_index=True)

with open("prova.json", "w") as file:
    json.dump(res.json()["data"], file)

with open("prova.json", "r") as openfile:
    json_o = json.load(openfile)
print(json_o)
'''
'''print(df)
print(res.json()['data']['children'][1]['data'].keys())  # let's see what we get


for post in res.json()['data']['children']:
    print(post['data']['title'])'''





'''reddit = praw.Reddit(
    client_id='tEa4Ddj6AGrkDgCW2VEukw',
    client_secret='2KTHCrQWnbgz28NScHFFSBSg4oIgPw',
    password='reddit00',
    user_agent='veror'
)


# search submission
subreddit='ADHD'
start_time = int(dt.datetime(2023, 3, 1).timestamp())
end_time = int(dt.datetime(2023, 3, 2).timestamp())
limit = 1000
api = PushshiftAPI()
posts = list(api.search_submissions(subreddit=subreddit, after=start_time, before=end_time, limit=limit))
print(type(posts))
print(posts)
print(pd.DataFrame(posts).to_csv('ADHD_march_1_2.csv'))'''





'''api_praw = PushshiftAPI(praw=reddit)
comments = api_praw.search_comments(q="quantum", subreddit="science", limit=100, until=1629990795)
comments_df = pd.DataFrame(comments)
comments_df.to_csv('proca_comm.csv')'''

'''subreddit = reddit.subreddit('ADHD')
num = 0

reddit_df = pd.DataFrame()

for submission in subreddit.top(time_filter="year", limit=10): #(limit=10):
    if hasattr(submission, 'title'):
        title = submission.title
    else:
        title = None
    if hasattr(submission, 'link'):
        link = submission.url
    else:
        link = None
    if hasattr(submission, 'author_fullname'):
        author = submission.author_fullname
    else:
        author = None
    if hasattr(submission, 'score'):
        score = submission.score
    else:
        score = None
    if hasattr(submission, 'created_utc'):
        created_utc = submission.created_utc
    else:
        created_utc = None
    if hasattr(submission, 'selftext'):
        text = submission.selftext
    else:
        text = None
    reddit_df = pd.concat([reddit_df, pd.DataFrame({'title': [title], 'link': [link], 'author': [author], 'score': [score],
                                                    'created_utc': [created_utc], 'text': [text]})])
    #print((title, link, author, score, created, submission.selftext))
    print(num)
    print('\n\n')
    num+=1
reddit_df.to_csv('reddit_ADHD_1.csv', index=False)'''

# ('worldnews', '2qh13', 'A place for major news from around the world, excluding US-internal news.', 1201231119.0)
#print(comments_df)


'''api = PushshiftAPI(praw='reddit')

before = int(dt.datetime(2023,5,8,0,0).timestamp())
after = int(dt.datetime(2023,5,3,0,0).timestamp())

subreddit = "science"
limit = 100

comments = api.search_submissions(subreddit=subreddit, limit=limit, before=before, after=after)
post_list = [post for post in comments]
'''
'''comments_df = pd.DataFrame(comments)'''

'''print(comments_df)

comments_df.to_csv('prova.csv', index=False)'''

#print(post_list)






# merge datasets

dir = 'ADHD_datasets/'
files = os.listdir(dir)

dataset = pd.DataFrame()

for file in files:
    df = pd.read_csv(dir+file)
    dataset = pd.concat([dataset, df])

dataset.to_csv('ADHD_dataset.csv')
