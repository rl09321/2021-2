
print('게으름 뱅이 짱구를 심부름 보내야해요!')

print('야채가게: 상추1000원, 당근 1000원, 호박2000원, 오이2000원, 피망2500원, 마늘3000원,')
print('과일가게: 사과1500원, 바나나1500원, 귤2500원, 키위2500원')
print('생선가게:조기8000원, 고등어9000원, 참돔 12000원, 갈치110000원')
print('정육점: 돼지고기12000원, 소고기10000원, 양고기13000원, 오리고기10000원')
print('슈퍼마켓:초코비3500원, 라면6000원, 어묵5000원, 계란7000원, 우유4000원')
print('1. 짱구가 사올 재료를 6개 선택해주세요!')



Food = ['상추', '당근', '호박', '오이', '피망', '마늘', '사과', '바나나', '귤', '키위', '조기', '고등어', '참돔','갈치', '돼지고기', '소고기', '양고기', '오리고기', '초코비', '라면', '어묵', '계란', '우유']
vegetable = ('상추', '당근', '호박', '오이', '피망', '마늘')
fruits =('사과', '바나나', '귤', '키위')
fish = ('조기', '고등어', '참돔','갈치')
meat =('돼지고기', '소고기', '양고기', '오리고기')
market =('초코비', '라면', '어묵', '계란', '우유')

bringFood = []
def choose_one(): #재료 6가지 입력 중복 X
    global bringFood
    bringFood=[]
    choice = []
    count = 0
    while True:
        choice = input()
        if choice in Food:
            if bringFood.count(choice) == 0:
                bringFood += [choice]
                count += 1
                if count == 6:
                    return bringFood
                    break
            else:
                print('짱구: 재료는 중복되면 안되요!')
        else:
             print('짱구 : 없는 재료를 고르면 어떻게 가요?!')
def onlymeat():
        lovemeat = 0
        global bringFood
        for il in range(len(bringFood)):
            if bringFood[il] in  meat:
                lovemeat +=1
            elif bringFood[il] in fish:
                lovemeat +=1
        if lovemeat == 0:
            print('짱구:생선이나 고기는 꼭 포함되야해요!\n','처음부터 다시 골라줘요')
            choose_one()
            onlymeat()
        else:
            return True

def mart (): 
    global bringFood
    global get
    b=0
    c=0
    d=0
    e=0
    g=0  
    for u in range (len(bringFood)): #가게의 수 계산 5개중 3개까지만
        if bringFood[u] in vegetable:
            b +=1
        elif bringFood[u] in fruits:
            c+=1
        elif bringFood[u] in meat:
            d+=1
        elif bringFood[u] in fish:
            e+=1
        elif bringFood[u] in market:
            g+=1
        get = [b,c,d,e,g]
        if b > 0:
            get[0] = '야채가게'
        if c>0:
            get[1] = '과일가게'
        if d>0:
            get[2] = '정육점'
        if e>0:
            get[3] = '생선가게'
        if g>0:
            get[4] = '슈퍼마켓'
        con = 0
        con += int(get.count(0))
        for i in range(con):
            get.remove(0)
    if len(get) <4: #가야하는가게의 수
        return True
    else:
        print('짱구가 가야하는 가게들: ',get)
        print('짱구:가게는 3곳까지만  갈래요!\n','처음부터 다시 골라줘요!')
        choose_one()
        onlymeat()       
        mart()
    



         
print(end='')
mart11 = ['야채가게', '과일가게', '정육점', '생선가게', '슈퍼마켓']
vegetable2 = [('상추',1000), ('당근',1000), ('호박',2000), ('오이',2000), ('피망',2500), ('마늘',3000)]
fruits2 =[('사과',1500), ('바나나',1500), ('귤',2500), ('키위',2500)]
fish2 = [('조기',8000), ('고등어',9000), ('참돔',12000),('갈치',11000)]
meat2 =[('돼지고기',12000), ('소고기',10000), ('양고기',13000), ('오리고기',10000)]
market2 =[('초코비',3500), ('라면',6000), ('어묵',5000), ('계란',7000), ('우유',4000)]
def showMoney (pp):
    global bringFood
    for ii in range(6): #총 가격 계산
        if vegetable[ii] in bringFood:
            pp += vegetable2[ii][1]
    for ik in range(4):
        if fish[ik] in bringFood:
            pp += fish2[ik][1]
        if fruits[ik] in bringFood:
           pp += fruits2[ik][1]
        if meat[ik] in bringFood:
            pp += meat2[ik][1]
    for o in range(5):
        if market[o] in bringFood:
           pp += market2[o][1]
        

    if '피망' in bringFood:
        bringFood.remove('피망')
        pp = pp - 2500


    for yy in range (1,5):
        if market[yy] in bringFood:
            if '초코비' in bringFood:
                break
            else:
                bringFood += ['초코비']
                pp += 3500
                break
    return pp
choose_one()
onlymeat()
mart()
Foodprice =0
Foodprice = showMoney(Foodprice) 

while True:
    if Foodprice > 30000:
        print('짱구가 사야하는  재료들:\n', bringFood,)
        print('총 금액:%d'%Foodprice)
        print('짱구: 3만원 넘게 사면 어떻게해요? 다시 골라줘요!')
        choose_one()
        onlymeat()
        mart()
        Foodprice =0
        Foodprice = showMoney(Foodprice)
        continue
    
    elif Foodprice <= 30000:
        print('짱구:알겠어요 심부름 다녀오겠습니다!')
        print('짱구가 갔다온 가게들: ',get)
        print('짱구가 사온 재료들:', bringFood,)
        print('총 금액:%d'%Foodprice)
        print('착한 짱구를 심부름 시키기 성공했어요!')
        break
