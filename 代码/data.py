import json,urllib.requests

url="http://platform.sina.com.cn/sports_all/client_api?_sport_t_=football&_sport_s_=opta&_sport_a_=playerorder&item=13&app_key=3571367214&type=213&limit=50&callback=callPlayerList&callback=aa"
page=urllib.request.urlopen(url).read()
tmp=page.decode('UTF-8')
tmp = tmp[3:]
tmp = tmp[:-2]
jsonData = json.loads(tmp)
team = jsonData["result"]["data"]
print('名次        球员        进球        球队')
for person in team:
    print('{0}        {1}        {2}        {3}'.format(person["num"], person["player_name"], person["item1"], person["team_name"]))
