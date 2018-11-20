#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 15 20:26:39 2018

@author: stavenvanderbilt
"""
#叶奕妹 1801010539

import random

#自定义抽牌函数 和计算一手牌大小
def changeCardAndCount(cards, player, player_flag_s, j):
    if player_flag_s == 'y' and player[2] == True:
        player[3].append(cards[j])
        print("玩家：" + player[0] + "获得" + cards[j])
        totalValue = 0  #一手牌总点数
        for privateCard in player[3]:
            totalValue  += dict[privateCard[0:len(privateCard)-2]]
        player[4] = totalValue
        print("玩家：" + player[0] + "当前总点数为：" + str(totalValue))
        if totalValue >= 10.5: #如果该玩家点数达到10.5或者超过，则不能再要牌   
            player[2] = False
            print("玩家：" + player[0] + "点数达到10.5或者超过接下来发牌将默认不要牌！")
            
    else:
        player[2] = False 
        
#自定义函数检测是否还有玩家要牌
def checkPlayer(playerList):
    for player in playerList:
        if player[2] == True:
            return True
    return False

#把全部玩家放到一个列表
playerList = []




player2 = []
player2_name = input("请输入第一个闲家的姓名:")
player2.append(player2_name)
player2_money = 100
player2.append(player2_money)
player2_flag = True
player2.append(player2_flag)
player2_cards = []
player2.append(player2_cards)
player2_pointsum = 0
player2.append(player2_pointsum)
player2_bit = 0
player2.append(player2_bit)
#将玩家加入
playerList.append(player2)


player3 = []
player3_name = input("请输入第二个闲家的姓名:")
player3.append(player3_name)
player3_money = 100
player3.append(player3_money)
player3_flag = True
player3.append(player3_flag)
player3_cards = []
player3.append(player3_cards)
player3_pointsum = 0
player3.append(player3_pointsum)
player3_bit = 0
player3.append(player3_bit)
#将玩家加入
playerList.append(player3)


player4 = []
player4_name = input("请输入第三个闲家的姓名:")
player4.append(player4_name)
player4_money = 100
player4.append(player4_money)
player4_flag = True
player4.append(player4_flag)
player4_cards = []
player4.append(player4_cards)
player4_pointsum = 0
player4.append(player4_pointsum)
player4_bit = 0
player4.append(player4_bit)
#将玩家加入
playerList.append(player4)


player1 = []
player1_name = input("请输入庄家的姓名:")
player1.append(player1_name)
player1_money = 100
player1.append(player1_money)
player1_flag = True
player1.append(player1_flag)
player1_cards = []
player1.append(player1_cards)
player1_pointsum = 0
player1.append(player1_pointsum)
player1_bet = 0
player1.append(player1_bet)
#将玩家加入
playerList.append(player1)

#是否进行下一局游戏
nextGame = True

while nextGame == True:
   
    #新一轮游戏玩家状态信息重置（筹码不重置）
    for player in playerList: 
        player[2] = True
        player[3] = []
        player[4] = 0
        player[5] = 0
        
    print("当前所有玩家信息：")
    for player in playerList:
        print(player)
    
    #print(player1, player2, player3, player4)
    
    
    player2_bit = input(player2[0] + ":请下注")
    while int(player2_bit) > 20 or int(player2_bit) < 1 or int(player2_bit) > player2[1]:
        print("请重新下注:")
        player2_bit = input(player2[0] + ":请下注")
    print(player2_bit)
    player2[5] = int(player2_bit)
    
    player3_bit = input(player3[0] + ":请下注")
    while int(player3_bit) > 20 or int(player3_bit) < 1 or int(player3_bit) > player3[1]:
        print("请重新下注:")
        player3_bit = input(player3[0] + ":请下注")
    print(player3_bit)
    player3[5]=int(player3_bit)
    
    player4_bit = input(player4[0] + ":请下注")
    while int(player4_bit) > 20 or int(player4_bit) < 1 or int(player4_bit) > player4[1]:
        print("请重新下注:")
        player4_bit = input(player4[0] + ":请下注")
    print(player4_bit)
    player4[5]=int(player4_bit)
    
    print(player1, player2, player3, player4)
    
    
    count = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "j", "k", "Q"]
    color = ["红桃", "黑桃", "梅花", "方块"]
    cards = []
    for i in count:
        for j in color:
            cards.append(i+j)
    
    random.shuffle(cards)
    print('=========  第二次洗牌  ==========')
    print(cards)
    
    dict={'A':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10,'j':0.5,'k':0.5,'Q':0.5}
    print(dict)
    
    
    j = 0
    card1 = cards[j]
    print(card1)
    player1_cards = card1
    player1[3].append(player1_cards)
    player1[4] = dict[card1[0:len(cards[j])-2]]
    
    
    j = j+1
    card2 = cards[j]
    print(card2)
    player2_cards = card2
    player2[3].append(player2_cards)
    player2[4] = dict[card2[0:len(cards[j])-2]]
    
    
    j = j+1
    card3 = cards[j]
    print(card3)
    player3_cards = card3
    player3[3].append(player3_cards)
    player3[4] = dict[card3[0:len(cards[j])-2]]
    
    
    j = j+1
    card4 = cards[j]
    print(card4)
    player4_cards = card4
    player4[3].append(player4_cards)
    player4[4] = dict[card4[0:len(cards[j])-2]]
    
    
    print(player1, player2, player3, player4)
    
    
    
            
    #player1_flag_s = input(player1[0] + ": 还需要牌吗？y/n")
    #changeCardAndCount(cards, player1, player1_flag_s,j+1)
    
    #player2_flag_s = input(player1[0] + ": 还需要牌吗？y/n")
    #changeCardAndCount(cards, player2, player2_flag_s,j+1)
    
    #player3_flag_s = input(player1[0] + ": 还需要牌吗？y/n")
    #changeCardAndCount(cards, player3, player3_flag_s,j+1)
    
    #player4_flag_s = input(player1[0] + ": 还需要牌吗？y/n")
    #changeCardAndCount(cards, player4, player4_flag_s,j+1)
    
    
    #循环发牌
    lunshu = 1
    while checkPlayer(playerList):
        #洗牌
        random.shuffle(cards)
        lunshu += 1
        print("当前第"+ str(lunshu) + "轮发牌....")
        j=0
        for player in playerList:   #循环玩家要牌
            if player[2] == True:           
                player_flag_s = input(player[0] + ": 还需要牌吗？y/n")
                j += 1
                changeCardAndCount(cards, player, player_flag_s,j)
    
        print("当前所有玩家信息：")
        for player in playerList:
            print(player)
    
    
    #所有人不再要牌，进行比较牌大小
    
    #情况一：庄家爆牌，存在闲家不爆牌，那么庄家需要给所有玩家进行赔付，默认最后一个玩家是庄家
    for player in playerList:
        if player[0] != playerList[len(playerList)-1][0] and ((playerList[len(playerList)-1][4] > 10.5 and player[4] <= 10.5) or (playerList[len(playerList)-1][4] <= 10.5 and player[4] <= 10.5 and playerList[len(playerList)-1][4] <  player[4])): #拿没有爆点的玩家进行赔偿
            playerList[len(playerList)-1][1]  = playerList[len(playerList)-1][1] - player[5]
            player[1] = player[1] + player[5]
        if player[0] != playerList[len(playerList)-1][0] and playerList[len(playerList)-1][4] <= 10.5 and (player[4] > 10.5 or (player[4] <= 10.5 and playerList[len(playerList)-1][4] >=  player[4])):          
            playerList[len(playerList)-1][1]  = playerList[len(playerList)-1][1] + player[5]
            player[1] = player[1] - player[5]
    print("当前所有玩家信息：")
    for player in playerList:
        print(player)
    
    print("当局游戏结束！")
    #如果有玩家没筹码了就不能继续游戏
    for player in playerList:
        if player[1] <= 0:
            nextGame = False
        
    if_next_game = "" 
    if nextGame:       
        if_next_game = input("是否进入新一局游戏？y/n")
    if if_next_game != 'y':
        nextGame = False