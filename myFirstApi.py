# Assign ClientId and API Key from reddit account
CLIENT_ID = 'lcZiBbfE360yiR5Im_bjcg'
API_KEY = 'SecretApiKey'

# Import requests library
import requests

# assign basic authorization to clientId and API Key
auth = requests.auth.HTTPBasicAuth(CLIENT_ID, API_KEY)

# tell script to read user's password from file
with open('pw.txt', 'r') as f:
    pw = f.read()
# assign access type, username, password to variable
data = {
    'grant_type': 'password',
    'username': 'Mordstreichlol',
    'password': pw
}

# assign metadata to headers via reddit api user-agent
headers = {'User-Agent': 'myFirstApi/1.0'}

# request our OAuth Token via api V1
res = requests.post('https://www.reddit.com/api/v1/access_token',
                    auth=auth, data=data, headers=headers)
                    # keys     login-data     headers
# assign access token to variable
TOKEN = res.json()['access_token']
# assign header authorization token
headers['Authorization'] = f'bearer {TOKEN}'

# request data from first endpoint via metadata and write to json to test, commented out
# print(requests.get('https://oauth.reddit.com/api/v1/me', headers=headers).json())

# pull posts from r/python
res = requests.get('https://oauth.reddit.com/r/all/new',
                    headers=headers)

# import panda for dataframe
import pandas as pd

# define dataframe
df = pd.DataFrame()

# use a loop to find posts in subreddit
for post in res.json()['data']['children'][:5]:
    # assign columns to dataframe rows via dictionary
    df = df.append({
        'subreddit': post['data']['subreddit'],
        'title': post['data']['title'],
        'selftext': post['data']['selftext'],
        'upvote_ratio': post['data']['upvote_ratio'],
        'ups': post['data']['ups'],
        'downs': post['data']['downs'],
        'score': post['data']['score']
    }, ignore_index=True)

# print dataframe
print(df)

# I understand the assignment was to pull a random title from the front page
# however, while i can pull a post from the front page I'm unsure of what to do
# to parse the data in the same way because when I use random, I get a type error. 