import requests
from bs4 import BeautifulSoup

def main():
    url= "https://synd.cricbuzz.com/j2me/1.0/livematches.xml"
    r=requests.get(url)
    soup = BeautifulSoup(r.text,"html.parser")
    #print(soup)
    matches=soup.find_all('match')
    info=[]
    for i in matches:
        info.append(matchinfo(i))
    print(info)
    score=[]
    team=soup.find_all('mscr')
    for i in team:
        score.append(teaminfo(i))
    print(score)

def matchinfo(match):
    d={}
    d['id']=match['id']
    d['srs']=match['srs'] #IPL etc..
    d['match']=match['mchdesc'] #team name
    d['date']=match['mnum'] #date
    #d['ground']=match['grnd'] #ground
    d['match_status']=match.state['mchstate']
    return d
def teaminfo(team):
    e={}
    e['1st team']=team.bttm['sname']
    e['over1']=team.inngs['ovrs']
    e['score1']=team.inngs['r']
    e['wicket1']=team.inngs['wkts']
    e['2nd team']=team.blgtm['sname']
    e['over2']=team.blgtm.inngs['ovrs']
    e['score2']=team.blgtm.inngs['r']
    e['wicket2']=team.blgtm.inngs['wkts']
    return e
if __name__=="__main__":
    main()