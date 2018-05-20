import sys
import requests
from win10toast import ToastNotifier
from bs4 import BeautifulSoup
t=ToastNotifier()
def main():
    url= "https://synd.cricbuzz.com/j2me/1.0/livematches.xml"
    r=requests.get(url)
    soup = BeautifulSoup(r.text,"html.parser")
    print(soup)
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
    s1=e['1st team']+"_"+e['over1']+"_"+e['score1']+"_"+e['wicket1']
    s2=e['2nd team']+"_"+e['over2']+"_"+e['score2']+"_"+e['wicket2']
    s1=str(s1)
    s2=str(s2)
    t.show_toast(s1,duration=5)
    t.show_toast(s2,duration=5)
    return e
if __name__=="__main__":
    main()
