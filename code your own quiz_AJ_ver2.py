levl= ['easy','medium','hard']
paragraph= [ "Chicago is a city of ___1____ state. Positioned along Lake ____2____. It's famous with the __3__ dish piza. In 1920s the famous gangster was ___4____.","____1____ is the capital of Saudi Arabia, The official language of the country is _____2____. It's a religous country which ___3____ rules the constitution. The current ruler is King ___4___ AL Saud","Udacity is a for-profit educational organization founded by ____1____ and others. The name Udacity comes from the company's desire to be ''___2____' the student'. It was launched in ___3___. HQ in ___4___", ]
answers= [['illinos',"michigan","deep","alcapone"],["riyadh","arabic","islam","sulman"],[" sebastian","audacious","2012","usa"]]
dict_answers=[[{ "___1____":'illinos'},{"____2____":"michigan"},{"__3__":"deep"},{"___4____":"alcapone"}],[{"____1____":"riyadh"},{"_____2____":"arabic"},{"___3____":"islam"},{"___4___":"sulman" }],[{"____1____":" sebastian"},{"___2____":"audacious"},{" ___3___":"2012"},{"___4___":"usa"}]]
import sys
def get_levl():# this for selecting levl by raw_input. Output= index of levl for reuse in all funcs.
    lvlinput= raw_input("[[select levl EASY, MEDIUM or HARD...]]").lower()
    if lvlinput in levl:
        lvlindex= levl.index(lvlinput) #this is how to search in list by onle string
        print paragraph[lvlindex]
        return lvlindex
    else: #all bellow are extra
        print "[[wrong entry]]"
        confirmation= raw_input("do you wanna conntinoue plying?(Y/N)").lower()
        if confirmation=="y":
            return get_levl
        else:
            quit("thank you for ur time")

def match(lvlindexM):# Please note there are some extra features I hope not to count them out of the 18 lines 
# input: paragraph, dict of blanks, annswerinput. Process: boolean, search and looping. output: print feedback and boolean
    counter_down=2
    end_counter=0
    counterIndex=1
    blankIndex=0
    para_lvl= paragraph[lvlindexM]
    while blankIndex<len(answers[lvlindexM]):
        ansinput= raw_input("[[please add your answer one blank at a time]]").lower()
        if ansinput == answers[lvlindexM][blankIndex]:#for order
            answerindex=answers[lvlindexM].index(ansinput) #start at 0 
            dictlocal= dict_answers[lvlindexM][answerindex]
            blankIndex+=1
            answerindex+=1
            for blank, ans in dictlocal.iteritems():
                print "correct>>>>  " + str(para_lvl.replace(blank, ans))
            result= True #this is extra
        else: 
            print "[[incorrect.. you got " + str(counter_down-counterIndex) + "   tries]]"
            result= False
            counter_down-=1
            if counter_down==end_counter:#this is extra
                quit("bye bye!") #this is extra
            
    return result #this is extra

def main (match):#goal is to control the game. input: functions [get lvl, match]. output: direct the calls of functions
    lvlindexM=get_levl()
    matchM= match(lvlindexM)
    if matchM:#= True: #all extra
        print " you won!"
        reentery= raw_input("[[do you want to play again(Y/N)?]]").lower()
        if reentery=="y":
            main(match)
        else:
            quit("bye bye!")

main(match)
