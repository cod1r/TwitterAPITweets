import requests
from pandas import DataFrame
import json
import urllib.parse
import settings
# s = input("What keywords do you want? ")
# print("DATE FORMAT MUST BE YYYY-MM-DD")
# date = 'since:' + input("Since when?: ")
# date1 = 'until:' + input("Until when?: ")
# sEn = urllib.parse.quote(s)
# dateEn = urllib.parse.quote(date)
# date1En = urllib.parse.quote(date1)
# count = input("How many tweets? Max is 100: ")
# url = "https://api.twitter.com/1.1/search/tweets.json?q="+sEn+"&"+date1En+"&"+dateEn+"&"+"count="+count
headers = {
    "Authorization": "Bearer "+settings.BEARERToken
}
url = "https://api.twitter.com/1.1/search/tweets.json?q=corona&src=typed_query&count=100"
r = requests.get(url, headers=headers)
with open("data.json",'w', encoding='utf8') as f:
    f.write(r.text)
d = r.json()
print(len(d['statuses']), len(d))
for x in d['statuses']:
    print(x['created_at'])
    print(x['text'])
df = DataFrame.from_dict(d['statuses']).transpose()
df.to_csv("data.csv")
