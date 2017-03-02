
 # __    __   __                                           ______             __
# /  |  /  | /  |                                         /      \           /  |
# $$ |  $$ |_$$ |_     ______    ______   _______        /$$$$$$  |  ______  $$/  _______    _______
# $$  \/$$// $$   |   /      \  /      \ /       \       $$ |  $$/  /      \ /  |/       \  /       |
 # $$  $$< $$$$$$/   /$$$$$$  |/$$$$$$  |$$$$$$$  |      $$ |      /$$$$$$  |$$ |$$$$$$$  |/$$$$$$$/
#  $$$$  \  $$ | __ $$    $$ |$$ |  $$/ $$ |  $$ |      $$ |   __ $$ |  $$ |$$ |$$ |  $$ |$$      \
# $$ /$$  | $$ |/  |$$$$$$$$/ $$ |      $$ |  $$ |      $$ \__/  |$$ \__$$ |$$ |$$ |  $$ | $$$$$$  |
#$$ |  $$ | $$  $$/ $$       |$$ |      $$ |  $$ |      $$    $$/ $$    $$/ $$ |$$ |  $$ |/     $$/
#$$/   $$/   $$$$/   $$$$$$$/ $$/       $$/   $$/        $$$$$$/   $$$$$$/  $$/ $$/   $$/ $$$$$$$/

#made with http://patorjk.com/software/taag/

# Xtern Intern Techincal interview
# Josh Martin
# contact@cjoshmartin.com
# 2016

import json
import uuid
import random
import time

## Location of file
filename ="data.json"

def newGuess():
    # makes new numbers each time alled
    return random.randint(0,10)

# init guess 
correctGuess = newGuess()

def newUser():
    # new init of a user
    userid = str(uuid.uuid1())
    data={userid:{'coins':0,'guess':0}}
    with open(filename,'w') as f:
        json.dump(data,f)
    return userid
def OpenJson():
    # opens the json file satisfied at the top of the document
    with open(filename,'r+') as f:
        data =json.load(f)
    return data
    
def AddACoin(userid):
    # adds a coin to current user
    data = OpenJson()
    tmp=data[userid]['coins']
    tmp+=1
    data[userid]['coins']=tmp
    JsonFile=open(filename,"w+")
    JsonFile.write(json.dumps(data))
    JsonFile.close()

def GuessCount(userid):
    # keeps track of guess
    data = OpenJson()
    tmp=data[userid]['guess']
    tmp+=1
    data[userid]['guess']=tmp
    JsonFile=open(filename,"w+")
    JsonFile.write(json.dumps(data))
    JsonFile.close()
    print 'that is {} trys in total.'.format(tmp)

def GetCoins(userid):
    # gets current amount of coins
    getamount =OpenJson()[userid]['coins']
    return getamount

def HandleGuess(userid,guess):
    # returns a Boolean value based off if the guess is right or not
    print 'the current user, "{}" has guessed: {}'.format(userid,guess)
    if guess == correctGuess:
        print 'the user,"{}" has guessed correctly and now has {} XternCoins.'.format(userid,(GetCoins(userid)+1))
        return True
    print 'the user has nt guessed right, please try again.'
    return False
    
def StartGuessing():
    user =newUser()
    while True:
        print(""" 
        
        
        
        
        
 __    __   __                                           ______             __                     
/  |  /  | /  |                                         /      \           /  |                    
$$ |  $$ |_$$ |_     ______    ______   _______        /$$$$$$  |  ______  $$/  _______    _______ 
$$  \/$$// $$   |   /      \  /      \ /       \       $$ |  $$/  /      \ /  |/       \  /       |
 $$  $$< $$$$$$/   /$$$$$$  |/$$$$$$  |$$$$$$$  |      $$ |      /$$$$$$  |$$ |$$$$$$$  |/$$$$$$$/ 
  $$$$  \  $$ | __ $$    $$ |$$ |  $$/ $$ |  $$ |      $$ |   __ $$ |  $$ |$$ |$$ |  $$ |$$      \ 
 $$ /$$  | $$ |/  |$$$$$$$$/ $$ |      $$ |  $$ |      $$ \__/  |$$ \__$$ |$$ |$$ |  $$ | $$$$$$  |
$$ |  $$ | $$  $$/ $$       |$$ |      $$ |  $$ |      $$    $$/ $$    $$/ $$ |$$ |  $$ |/     $$/ 
$$/   $$/   $$$$/   $$$$$$$/ $$/       $$/   $$/        $$$$$$/   $$$$$$/  $$/ $$/   $$/ $$$$$$$/
        
        
        
        
        
        
        
        
        
        
        """) #cheap "gui" to clear the screen a bit and look pretty 
        print 'the current user, "{}" has {} XternCoins'.format(user,OpenJson()[user]['coins'])
        guess =HandleGuess(user,random.randint(0,10))
        if guess :
            AddACoin(user)
            correctGuess=newGuess() # makes a new number to guess
        GuessCount(user)
        time.sleep(3) # makes program readable to humans not just computers

