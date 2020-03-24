#!/bin/python3

from random import choice

#從檔案中匯入隊員名單
players = []
file = open('players.txt', 'r')
players = file.read().splitlines()
print('隊員：', players)

#從檔案中導入團隊名單
teamNames = []
file = open('teamNames.txt', 'r')
teamNames = file.read().splitlines()
print('隊名：', teamNames)

#建立空的團隊人員名單
teamA = []
teamB = []

#重複迴圈直到所有隊員全部被選走
while len(players) > 0:
  
  #為A隊隨機選擇一名隊員
  playerA = choice(players)
  teamA.append(playerA)
  #將已選的隊員從隊員名單中去除
  players.remove(playerA)
  
  #如果沒有隊員剩下了，則跳出迴圈
  if players == []: 
    break
  
  #為B隊隨機選擇一名隊員
  playerB = choice(players)
  teamB.append(playerB)
  #將已選的隊員從隊員名單中去除
  players.remove(playerB)

#為兩隊隨機選擇隊名
teamNameA = choice(teamNames)
teamNames.remove(teamNameA)
teamNameB = choice(teamNames)
teamNames.remove(teamNameB)

#顯示隊名
print("\nHere are your teams:\n")
print(teamNameA, teamA)
print(teamNameB, teamB)
