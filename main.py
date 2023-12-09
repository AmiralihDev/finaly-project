import pyautogui
import random

pyautogui.alert(text="welcome to this game",title="welcome",button="OK")
# create klid
money = 0
hadseGame = False
joraaaatGame = False
klid = True
while klid == True:
# which game questions
    whichGame = pyautogui.confirm(text="which ? ",title="game",buttons=["rock-sisser-paper","joraat,hagigat","hadse adad","cheat panel", "shop","exit",'about developers'])
    
    if whichGame == 'exit':
        yesORno = pyautogui.confirm(text="aya motmaeen hastid ke mikhahid bazi ra tark konid ?",buttons=["yes","no"])
        if yesORno == "yes" :
            pyautogui.alert(text="good bay ")
            klid = False
# about developers

    elif whichGame == "about developers":
        pyautogui.alert(text="this game developers is amirali and amirhossien ") 
    if whichGame == "rock-sisser-paper" :
        
        pyautogui.alert(text='wellcome to ✊ ✋ ✌', title='wellcome', button='OK')
        where = pyautogui.confirm(text='which where do you want to go?', title='choose', buttons=['play game'])
# play game 
        if where == ("play game") :
            pyautogui.alert(text="ok, your game is slected!",title="select",button="Thanks")

            gamegu = pyautogui.confirm(text='which one do you want to play?', title='choose', buttons=['player vs player', 'player vs bot', 'bot vs bot','exit'])

# rock scisser paper : player vs bot
       
        if gamegu == 'player vs bot' :
            pyautogui.alert(text='wellcome to  player vs bot', title='wellcome', button='OK')   
            gCount = int(pyautogui.prompt(text="chand dor bazi mikonid ? "))
        
            for i in range(gCount):
               
                botList = ["rock","scissor","paper"]
                player1 = pyautogui.confirm(text='which one do you want to play? player1', title='choose', buttons=['rock', 'paper', 'scissor'])
                bot = random.choice(botList)
                pyautogui.alert(text=bot)

                if player1 == bot  :
                    pyautogui.alert(text='mosavi', title='game', button='OK')
                    
                    money += 10
                    pyautogui.alert(text=f'your mony is {money}', title='game', button='OK')
                elif player1 == "paper" and bot == "rock" :
                    pyautogui.alert(text='player1 is winner', title='game', button='OK')
                    money += 20
                    pyautogui.alert(text=f'your mony is {money}', title='game', button='OK')
                elif player1 == "paper" and bot == "scissor" :
                    pyautogui.alert(text='bot is winner', title='game', button='OK') 

                elif player1 == "rock" and bot == "paper" :
                    pyautogui.alert(text='bot is winner', title='game', button='OK') 

                elif player1 == "rock" and bot == "scissor" :
                    pyautogui.alert(text='player1 is winner', title='game', button='OK')
                    money += 20
                    pyautogui.alert(text=f'your mony is {money}', title='game', button='OK')

                elif player1 == "scissor" and bot == "paper" :
                    pyautogui.alert(text='player1 is winner', title='game', button='OK')
                    
                    money += 20
                    pyautogui.alert(text=f'your mony is {money}', title='game', button='OK')
                elif player1 == "scissor" and bot == "rock" :
                    pyautogui.alert(text='bot is winner', title='game', button='OK')
# rock scisser paper : player vs player       
        elif gamegu == "player vs player" : 
            pyautogui.confirm(text='wellcome to  player vs player', title='wellcome', buttons=['OK'])   

            meCount = int(pyautogui.prompt(text="chand dor bazi mikonid ? "))
            for i in range(meCount):
                

                player1 = pyautogui.confirm(text='which one do you want to play? player1', title='choose', buttons=['rock', 'paper', 'scissor'])
                player2 = pyautogui.confirm(text='which one do you want to play? player2', title='choose', buttons=['rock', 'paper', 'scissor'])

                if player1 == player2  :
                    pyautogui.alert(text='mosavi', title='game', button='OK')

                elif player1 == "paper" and player2 == "rock" :
                    pyautogui.alert(text='player1 is winner', title='game', button='OK')
                
                elif player1 == "paper" and player2 == "scissor" :
                    pyautogui.alert(text='player2 is winner', title='game', button='OK') 

                elif player1 == "rock" and player2 == "paper" :
                    pyautogui.alert(text='player2 is winner', title='game', button='OK') 

                elif player1 == "rock" and player2 == "scissor" :
                    pyautogui.alert(text='player1 is winner', title='game', button='OK')

                elif player1 == "scissor" and player2 == "paper" :
                    pyautogui.alert(text='player1 is winner', title='game', button='OK')

                elif player1 == "scissor" and player2 == "rock" :
                    pyautogui.alert(text='player2 is winner', title='game', button='OK')
        
        
# rock scisser paper : bot vs bot      
        elif gamegu == "bot vs bot":
            pyautogui.alert(text="ok, your game is slected!",title="select",button="Thanks")

            gamCount = int(pyautogui.prompt(text="chand dor bazi mikonid ? "))
    
            for i in range(gamCount):
                botList = ["rock","scissor",]
                bot1 = random.choice(botList)
                bot2 = random.choice(botList)
                pyautogui.alert(text=f"bot1 slected : {bot1}")
                pyautogui.alert(text=f"bot2 slected : {bot2}")
                if bot1 == bot2  :
                    pyautogui.alert(text='mosavi', title='game', button='OK')

                elif bot1 == "paper" and bot2 == "rock" :
                    pyautogui.alert(text='bot1 is winner', title='game', button='OK')
                
                elif bot1 == "paper" and bot2 == "scissor" :
                    pyautogui.alert(text='bot2 is winner', title='game', button='OK') 

                elif bot1 == "rock" and bot2 == "paper" :
                    pyautogui.alert(text='bot2 is winner', title='game', button='OK') 

                elif bot1 == "rock" and bot2 == "scissor" :
                    pyautogui.alert(text='bot1 is winner', title='game', button='OK')

                elif bot1 == "scissor" and bot2 == "paper" :
                    pyautogui.alert(text='bot1 is winner', title='game', button='OK')

                elif bot1 == "scissor" and bot2 == "rock" :
                    pyautogui.alert(text='bot2 is winner', title='game', button='OK')
# joraat hagigat game : main               
    elif whichGame == "joraat,hagigat" :
        if joraaaatGame == True :
            player = []
# joraat questions list
            joraat = ["yeki az 'kanal' hato biar bala","akharin chatet ro neshon bede"]
# hagigat questions list
            hagigat = ["kamtarin nomreii ke gerefti baraye che darsi bode ??","moshakhasat systemet chie"]
            pyautogui.alert(text="ok, your game is slected!",title="select",button="Thanks")
            joraat_count = int(pyautogui.prompt(text="chand dor bazi mikonid ? ",title="door"))
            player_count = int(pyautogui.prompt(text="chand nafar hastid ? ",title="nafar"))
            for item in range(1,player_count+1):
                name = pyautogui.prompt(text=f"player : {item}",title=item)
# add users name to nameList
                player.append(name)
            for i in range(1,joraat_count+1):
# select player
                rnd = random.choice(player)
                pyautogui.alert(text="start",button="OK")
                pyautogui.alert(text=f"{rnd} is selected")
                entekhab = pyautogui.confirm(text="joraat or hagigat ? ",buttons=["hagigat","jorat"])
                if entekhab == "hagigat":
                    # select hagigat question
                    hagigatrnd = random.choice(hagigat)
                    pyautogui.alert(text=f"{rnd} aziz {hagigatrnd}")
                else :
                    # select joraat question
                    joratrnd = random.choice(hagigat)
                    pyautogui.alert(text=f"{rnd} aziz {joratrnd}")
        elif joraaaatGame == False :
            pyautogui.alert(text="you dont have this game please buy it in shop thanks !")


# shop page
    elif whichGame == "shop" :
# if joraat and hadse is false
        if joraaaatGame == False and hadseGame == False:
            buy = pyautogui.confirm(text="which game you want buy and forosh ?",buttons=["kharid joraat and hagigat","kharid hadse adad","exit"])
            if buy == "kharid joraat and hagigat" :
                motmaeen =pyautogui.confirm(text="aya motmaeen hastid ke mikhahid kharidari konid ?",buttons=["yes","no"])
                if motmaeen == "yes":
# + and _ money                

                 
                    if money >= 200 :
                        joraaaatGame = True
                        money -= 200
                        pyautogui.alert(text=f"now you can play joraat hagigat game and your mony now is {money}")
                    
                    else :
                        pyautogui.alert(text=f"shoma pol kafi baraye in kharid ra nadarid  pol shoma :  {money}")
            elif buy == "kharid hadse adad" :
                motmaeen = pyautogui.confirm(text="aya motmaeen hastid ke mikhahid kharidari konid ?",buttons=["yes","no"])
# + and _ money                

                if motmaeen == "yes":
                 
                    if money >= 100 :
                        hadseGame = True
                        money -= 100
                        pyautogui.alert(text=f"now you can play hadse adad game and your mony now is {money}")
                    
                    else :
                        pyautogui.alert(text=f"shoma pol kafi baraye in kharid ra nadarid  pol shoma :  {money}")
# if joraat True hadse is True
        elif joraaaatGame == True and hadseGame == True:
            buy = pyautogui.confirm(text="which game you want buy and forosh ?",buttons=["forosh joraat and hagigat","forosh hadse adad","exit"])
# + and _ money                

            if buy == "forosh joraat and hagigat" :
                motmaeenForosh = pyautogui.confirm(text="aya motmaeen be forosh in bazi hastid ? shoma az forosh in bazi 120 money be dast miavarid",buttons=["yes","no"])
                if motmaeenForosh == "yes" :
                    joraaaatGame = False
                    money += 120
                    pyautogui.alert(text=f"be shoma 120 money ezaf shod alaan money shoma : {money}")
            elif buy == "forosh hadse adad":
                motmaeenForosh = pyautogui.confirm(text="aya motmaeen be forosh in bazi hastid ? shoma az forosh in bazi 60 money be dast miavarid",buttons=["yes","no"])
                if motmaeenForosh == "yes" :
                    hadseGame = False
                    money += 60
                    pyautogui.alert(text=f"be shoma 60 money ezaf shod alaan money shoma : {money}")
# if just joraat True
        elif joraaaatGame == True and hadseGame == False :
            buy = pyautogui.confirm(text="which game you want buy and forosh ?",buttons=["forosh joraat and hagigat","kharid hadse adad","exit"])
            if buy == "forosh joraat and hagigat" :
                motmaeenForosh = pyautogui.confirm(text="aya motmaeen be forosh in bazi hastid ? shoma az forosh in bazi 120 money be dast miavarid",buttons=["yes","no"])
                if motmaeenForosh == "yes" :
                    joraaaatGame = False
                    money += 120
                    pyautogui.alert(text=f"be shoma 120 money ezaf shod alaan money shoma : {money}")
            elif buy == "kharid hadse adad" :
                motmaeen = pyautogui.confirm(text="aya motmaeen hastid ke mikhahid kharidari konid ?",buttons=["yes","no"])
# + and _ money                

                if motmaeen == "yes":
                 
                    if money >= 100 :
                        hadseGame = True
                        money -= 100
                        pyautogui.alert(text=f"now you can play joraat hagigat game and your mony now is {money}")
                    
                    else :
                        pyautogui.alert(text=f"shoma pol kafi baraye in kharid ra nadarid  pol shoma :  {money}")
# if just hadse True
        elif hadseGame == True and joraaaatGame == False :
            buy = pyautogui.confirm(text="which game you want buy and forosh ?",buttons=["kharid joraat and hagigat","forosh hadse adad","exit"])
            if buy == "kharid joraat and hagigat" :
                motmaeen =pyautogui.confirm(text="aya motmaeen hastid ke mikhahid kharidari konid ?",buttons=["yes","no"])
                if motmaeen == "yes":
# + and _ money                
                    if money >= 200 :
                        joraaaatGame = True
                        money -= 200
                        pyautogui.alert(text=f"now you can play joraat hagigat game and your mony now is {money}")
                    
                    else :
                        pyautogui.alert(text=f"shoma pol kafi baraye in kharid ra nadarid  pol shoma :  {money}")

            if buy == "forosh hadse adad" :
                motmaeenForosh = pyautogui.confirm(text="aya motmaeen be forosh in bazi hastid ? shoma az forosh in bazi 60 money be dast miavarid",buttons=["yes","no"])
                if motmaeenForosh == "yes" :
                    hadseGame = False
                    money += 60
                    pyautogui.alert(text=f"be shoma 60 money ezaf shod alaan money shoma : {money}")
# cheat panel
    elif whichGame == "cheat panel" : 
# cheat code list
        cheatList = [21115,55520,75945]
        cheat = random.choice(cheatList)
# cheat menu
        whichCheat = pyautogui.confirm(text="which ?",buttons=["enter cheat code","buy cheat code","exit"])
# entet cheat code
        if whichCheat == "enter cheat code" :
            enterCheat = int(pyautogui.prompt(text="enter your code : "))
# which code for which money
            if enterCheat == cheatList[0] :
                
                money += 300
               
                
            elif enterCheat == cheatList[1] :
                money += 400
                
                
            elif enterCheat == cheatList[2] :
                money += 350
#show money               
            pyautogui.alert(text=f'your money now is {money}')
#show cheat code
        elif whichCheat == "buy cheat code" :
            pyautogui.alert(text=f'this is your code : {cheat}')
# hadse adad game 
    elif whichGame == "hadse adad":
        if hadseGame == True :
            pyautogui.alert(text="welcome to game")
            gamCou = int(pyautogui.prompt(text="chand dor bazi mikonid ?"))
            number = random.randint(1,10)
            for i in range(gamCou):
                number = random.randint(1,10)
                numberUser = pyautogui.prompt(text="adad hadse zade khod ra vared konid !")
# show cpu adad (random)
                pyautogui.alert(text=f"adad entekhabi computer is {number}")
                if number == numberUser :
                    money += 10
                    pyautogui.alert(text=f"adad entekhabi shoma dorost ast aknon shoma 10 money daryaft kardid  ! your money now is : {money}")
                else :
                    pyautogui.alert(text=f"adad shoms dorost nist zira adad shoma : {numberUser} and adad computer is {number} ast !")
        elif hadseGame == False :
            pyautogui.alert(text="you dont have this game please buy this game in shop Thanks !")  
              


