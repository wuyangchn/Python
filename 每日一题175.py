#题目源自鱼C论坛（http://bbs.fishc.com/forum.php），python交流版块，第175题
#大学快结束突然想学学编程 大概是傻了QAQ

#得到由一个随机四位数的每个数字组成的列表
import random
number = str(random.randint(1000,10000))
numlist = [int(number[item:item+1] ) for item in range(0, 4, 1)]

#变为集合方便判断有无重复数字
numset = set(numlist)

while len(numset) != 4:
    number = str(random.randint(1000,10000))
    numlist = [int(number[item:item+1] ) for item in range(0, 4, 1)]
    numset = set(numlist)
print(number)
    
print('========无限尝试，输入Q退出=========')

count0 = 1
guessdict = {}

while True:
    guess = str(input('请输入无重复数字的四位数：'))
    if guess == 'Q':
        print('退出游戏，答案是：'+str(number))
        break

    if guess == number:
        print('恭喜你，猜对啦！')
        print('当前成绩： %s次' % (count0))
        with open('record.txt','a''+') as record:
            record.write(str(count0)+'\n')
            record.seek(0,0)
            scoreslist = list(record)
            scoreslist_2 = []
            for eachscore in scoreslist:
                score = eachscore.splitlines()
                scoreslist_2.append(int(score[0]))
                
            scoreslist_2.sort()
            print('最佳成绩： %s次' % (scoreslist_2[0]))
            
        guessdict.clear()
        break

    elif guess.isdigit() and len(guess) == 4:
        guesslist = [int(guess[item:item+1] ) for item in range(0, 4, 1)]
        guessset = set(guesslist)

        if len(guessset) == 4 and guesslist[0] != 0:
            guesslist = [int(guess[item:item+1] ) for item in range(0, 4, 1)]
            guessset = set(guesslist)
        
            count1 = 0
            count2 = 0
    
            for eachitem in guesslist:
                tag = guesslist.index(eachitem) 
                if guesslist[tag] == numlist[tag]:
                    count1 +=1
                else:
                    if eachitem in numlist:
                        count2 +=1

            guessdict[str(count0) + '. ' +  guess] = '%dA%dB' % (count1,count2)
            print('HISTORY:')
            for each in guessdict:
                print('%s --> %s' % (each,guessdict[each]))

            count0 += 1
            continue
    else:
        continue

    
