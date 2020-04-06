#!/bin/python3

def showInstructions():
  #印出主選單和指令
  print('''
角色扮演遊戲
========
指令:
  前進 [方向]
  拾取 [物品]
''')

def showStatus():
  #印出玩家的當前狀態
  print('---------------------------')
  print('你正位於 ' + currentRoom)
  #印出當前包中的物品
  print('背包 : ' + str(inventory))
  #如果發現有物品，把它印出來
  if "item" in rooms[currentRoom]:
    print('你看到了 ' + rooms[currentRoom]['item'])
  print("---------------------------")

#一個庫存清單,一開始設定是空的
#
inventory = []

#一個房間連接關係的字典
rooms = {

            '大廳' : { 
                  '南' : '廚房'
                },

            '廚房' : {
                  '北' : '大廳'
                }

        }

#一開始將玩家放置在大廳的位置上
currentRoom = '大廳'

showInstructions()

#重複執行到永遠
while True:

  showStatus()

  #取得玩家的下一個動作
  #.split() 將字串分離成一個陣列
  #範例: 輸入 '前往 東' 會得到這個陣列:
  #['前往','東']
  move = ''
  while move == '':  
    move = input('>')
    
  move = move.lower().split()

  #如果他們先輸入 '前往'
  if move[0] == '前往':
    #檢查他們要前進的方向能不能走
    if move[1] in rooms[currentRoom]:
      #將目前鎖在房間設定成新的房間
      currentRoom = rooms[currentRoom][move[1]]
    #如果那裏沒有路(房間)可以前往
    else:
        print('你不能往這個方向走!')

  #如果他們先輸入 '拾取' 
  if move[0] == '拾取' :
    #如果這間房間有東西，而且這個物品是玩家想要達到的
    if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
      #把物品放進背包裡面
      inventory += [move[1]]
      #顯示成功獲取的訊息
      print(move[1] + ' got!')
      #將物品從房間中刪除
      del rooms[currentRoom]['item']
    #如果這間房間沒有玩家能撿的物品，則
    else:
      #告訴他們 你不能拿到這個物品!
      print('拿不到' + move[1] + '!')

