import sys
import subprocess
import os
import importlib

def install(package):
    if(package=="tweepy"):
        subprocess.call([sys.executable, "-m", "pip", "install","-U", "git+https://github.com/tweepy/tweepy.git@2efe385fc69385b57733f747ee62e6be12a1338b"])
    else:
        subprocess.call([sys.executable, "-m", "pip", "install", package])

def install_and_import(package,Auto_Install = False):
    import importlib
    #print(package)
    try:
        globals()[package] = importlib.import_module(package)
    except ImportError:
        if Auto_Install:
            print("\n >> Auto Installing " + package)
            #os.system('python -m pip install '+package)
            install(package)
            print("\n >> " + package +" Installed.\n")
    finally:
        if Auto_Install:
            globals()[package] = importlib.import_module(package)

print("Checking for Python Version...")

try:
    if(True):
        assert sys.version_info >= (3, 7)
    print("\nYay! You're Good to Go!")
except AssertionError:
    print("\nOops! Seems Like You Don't Have Python >= 3.7.x")
    print("Consider Upgrading it. Then Try Again")
    input("\n>>> Press Enter to Quit for Now")
    quit()


print("\nChecking For pip...")



print("\nChecking Dependencies...")
print("All Error Logs are Optimized for Python 3.7")
def Check_consent():
    Auto_Install = False
    response = ""
    while True:
        response = input("\nWould you like to fix missing packages while checking ( if any )? [Y / N] => ")
        if(response.lower() == 'y'):
            Auto_Install = True
            break
        elif(response.lower()=="n"):
            Auto_Install = False
            break
        else:
            print("Sorry that was an Incorrect input.")
    if(Auto_Install):
        return True
    else:
        return False


Auto_Install=Check_consent()
    
    



error=False

install_and_import("colorama",Auto_Install)
install_and_import("termcolor",Auto_Install)
from termcolor import colored
import time
install_and_import("ctypes",Auto_Install)
install_and_import("pyfiglet",Auto_Install)
install_and_import("tweepy",Auto_Install)


try:
    import pyfiglet
except ImportError:
    print ('\nWARNING!!!!!!!!! Error, pyfiglet is required')
    print ("\n\tQuick Fix:\n")
    print ("--Try Running 'python -m pip install pyfiglet' in CMD / Terminal\n")
    error=True

try:
    import tweepy
except ImportError:
    print ('\nWARNING!!!!!!!!! Error, Tweepy is required')
    print ("\n\tQuick Fix:\n")
    print ("--For Python 3.6 => Try Running 'python -m pip install tweepy' in CMD / Terminal")
    print ("--For Python 3.7 => Try Running \n\t'python -m pip install -U git+https://github.com/tweepy/tweepy.git@2efe385fc69385b57733f747ee62e6be12a1338b' in CMD / Terminal")
    error=True
'''
try:
    from termcolor import colored
except ImportError:
    print ('Error, termcolor is required')
    error=True

try:
    import ctypes
except ImportError:
    print ('Error, pathlib is required')
    error=True
'''

from time import sleep as SleepTime
install_and_import("pathlib",Auto_Install)
#try:
#    import pathlib
#except ImportError:
#    print ('Error, pathlib is required')
#    error=True


if(error):
    print("\n\nThere is/are one or more Dependencies, which are not installed.")
    print("Please run 'pip install package_name' to install them.")
    print("Then Come Back and Try Again")
    input("Press Enter to terminate for now")
    quit()  


def createDir(nameofdir, hidden = False):
    pathlib.Path(os.getcwd()+"\\"+nameofdir).mkdir(exist_ok=True)
    if(hidden):
        ctypes.windll.kernel32.SetFileAttributesW(os.getcwd()+"\\"+nameofdir, 2)



#--------------------------------------------------------#
colorama.init()

def prRed(skk): print("\033[91m{}\033[00m" .format(skk),end="") 
def prGreen(skk): print("\033[92m{}\033[00m" .format(skk),end="") 
def prYellow(skk): print("\033[93m{}\033[00m" .format(skk), end="") 
def prCyan(skk): print("\033[96m{}\033[00m" .format(skk),end="") 
def prWhite(skk): print("\033[97m{}\033[00m" .format(skk),end="") 
def prBlack(skk): print("\033[98m{}\033[00m" .format(skk),end="")



def AnimatedPrint(Text,duration=.01,color="white",con=False):
    for char in Text:
        if(color=="red"):
            prRed(char)
        elif(color=="green"):
            prGreen(char)
        elif(color=="yellow"):
            prYellow(char)
        elif(color=="cyan"):
            prCyan(char)
        elif(color=="white"):
            prWhite(char)
        else:
            prBlack(char)
        SleepTime(duration)
    if not con:
        print()



# Print iterations progress
def printProgressBar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█'):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print('\r%s |%s| %s%% %s' % (prefix, bar, percent, suffix), end = '\r')
    # Print New Line on Complete
    if iteration == total: 
        print()



def sprint(string,style=""):
    try:
        result = pyfiglet.figlet_format(string, font=style)
    except:
        result = pyfiglet.figlet_format(string)
    #print(prYellow("\n"+result),end="")
    return result



def intro():
    items = list(range(0, 57))
    l = len(items)
    # Initial call to print 0% progress
    printProgressBar(0, l, prefix = 'Loading App...', suffix = 'Please Wait...', length = 40)
    for i, item in enumerate(items):
        # Do stuff...
        SleepTime(0.02)
        # Update Progress Bar
        printProgressBar(i + 1, l, prefix = 'Loading App...', suffix = 'Please Wait...', length = 50)
    AnimatedPrint("\t\t\t\tLoading Done...!\n",color="green",duration=.02)
    SleepTime(.5)
    AnimatedPrint("-"*45)
    AnimatedPrint(sprint(" W E L C O M E ","bubble"),color="yellow")
    AnimatedPrint(sprint("Twitter Auto Reply Bot", "digital"),color="yellow")
    AnimatedPrint("          Made by Tuhin Karmakar",duration=.05,color="yellow")
    print()
    AnimatedPrint("GitHub: http://github.com/tuhinkarmakar3882",color="cyan")
    print()
    AnimatedPrint("-"*45)

    ViewInfo=input("Would you like to view the 'HOW TO USE IT' information? (Y/N): ")
    if(len(ViewInfo)!=0 and ViewInfo[0].lower()=='y'):
        AnimatedPrint("\n>>> Info :\n\tThis app is made to make it easier for you to set an Auto Reply Response on Twitter."
                     + "\n\tIt requires some basic setup to get you started."
                     + "\n\tJust follow up the below stuffs carefully and"
                     + " you'll be up and running within a few moments!")
    AnimatedPrint("\nAll Right! Let's Dig in.\n")


def isExistingUser(): #check for Existing User or Not
    try:
        os.chdir(os.getcwd()+"//data_Twi")
        userStat= open(".userstat","r")
        userStat.close()
        os.chdir("..")
        return True
    except:
        return False

def BasicInfo():
    AnimatedPrint("\t---Basic Details---")
    Name_User=""
    while(Name_User==""):
        AnimatedPrint(">>> What should we call you? => ",con=True)
        Name_User=str(input())
        if(Name_User==""):
            AnimatedPrint("Oh Snap! That's Empty, Let's Try Again.\n")
    AnimatedPrint("Hello, "+Name_User,duration=.05)
    return(Name_User)


def CheckForDevAc():
    agree=["y","yes"]
    disagree=["n","no"]

    Have_Dev_AC=""
    has_ac=False
    while(True):
        AnimatedPrint(">>> Do you Have a Twitter Developer Account? (Y/N) => ",con=True)
        Have_Dev_AC=str(input())
        if(Have_Dev_AC.lower() in agree):
            AnimatedPrint("Great...!!! Let's Fast Forward to our Main Goal.")
            has_ac=True
            break
        elif(Have_Dev_AC.lower() in disagree):
            AnimatedPrint("Ah, Not a Problem. Let's Get you Fixed.")
            has_ac=False
            break
        else:
            AnimatedPrint("Looks like, that was an INCORRECT input.\n"
               + "Not to worry Let's Try Again.\n")
    return(has_ac)

def guideUser():
    print()
    AnimatedPrint("To get started, we need to do the following.", color="cyan")
    AnimatedPrint("\nStep 1 of 5: Open https://developer.twitter.com/",color="yellow")
    AnimatedPrint("Hit Enter When Done...",color="red")
    input()
    
    AnimatedPrint("\nStep 2 of 5: Log in with Twitter and Click on Apply.",color="yellow")
    AnimatedPrint("Hit Enter When Done...",color="red")
    input()
    
    AnimatedPrint("\nStep 3 of 5: Fill Up the Details Over there and Click on Next/Submit.",color="yellow")
    AnimatedPrint("Hit Enter When Done...",color="red")
    input()
    
    AnimatedPrint("\nStep 4 of 5 : Now that you have an Twitter Developer Account"
           + " click on Apps-> Create an App."
           + "Now Fill up the details.\nDon't Worry about the Website link just add anything in it. "
           + "It hardly Matters."
           ,color="yellow")
    AnimatedPrint("Hit Enter When Done...",color="red")
    input()

    AnimatedPrint("\nStep 5 of 5: Go to the Keys & Tokens of the App and hit Generate and Save the Keys.",color="yellow")
    AnimatedPrint("\n\tNote! These keys are sensitive! Don't Expose it to Anyone else."
       +"\n\tThis app uses them just to connect to your Twitter account\n\tand retrieve the Tweets in order"
       +" to send replies as per your specifications.",duration=.1,color="cyan")
    AnimatedPrint("Hit Enter When Done...",color="red")
    input()
    

def retrieve_last_seen_id(file_name):
    
    f_read = open(file_name, 'r')
    last_seen_id = int(f_read.read().strip())
    f_read.close()
    return last_seen_id

def store_last_seen_id(last_seen_id, file_name):
    f_write = open(file_name, 'w')
    f_write.write(str(last_seen_id))
    f_write.close()
    return

def reply_to_tweets(FILE_NAME, hashTag, YourMsg, Name_User):
    AnimatedPrint(sprint("---Synchronizing---","bubble"),color="yellow")
    
    AnimatedPrint("Checking for New Tweets...",color="cyan")
    AnimatedPrint('Replying to new tweets (if any)...',color="cyan")
    # DEV NOTE: use 1060651988453654528 for testing.
    last_seen_id = retrieve_last_seen_id(FILE_NAME)
    # NOTE: We need to use tweet_mode='extended' below to show
    # all full tweets (with full_text). Without it, long tweets
    # would be cut off.
    mentions = api.mentions_timeline(last_seen_id,tweet_mode='extended')
    #try:
    #    mentions = api.mentions_timeline(last_seen_id,tweet_mode='extended')
    #except:
    #    AnimatedPrint(sprint("<<<<<WRONG CREDENTIALS IN KEYS>>>>>",style="digital"),color="red")
    #    AnimatedPrint(sprint("Press Enter to exit and Try Again",style="digital"),color="yellow")
    #    input()        
    #    quit()
    
    for mention in reversed(mentions):
        AnimatedPrint(str(mention.id) + ' - ' + mention.full_text,duration=.001)# flush=True)
        last_seen_id = mention.id
        store_last_seen_id(last_seen_id, FILE_NAME)
        if hashTag.lower() in mention.full_text.lower():
            AnimatedPrint('Found! '+hashTag, color="yellow")
            AnimatedPrint('Responding back...!',color="green")
            api.update_status('@' + mention.user.screen_name +" "
                    + hashTag + " " + YourMsg + "\n - " + Name_User
                              + "<sent via Twitter-Auto-Reply-Bot>", mention.id)


def validateKeys(FILE_NAME,CONSUMER_KEY,CONSUMER_SECRET,ACCESS_KEY,ACCESS_SECRET):
    try:
        AnimatedPrint("Setting Keys")
        auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
        AnimatedPrint("Setting Parameters")
        auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
        AnimatedPrint("Connecting...")
        api = tweepy.API(auth)
        AnimatedPrint("Verifying...")
        ment= api.mentions_timeline(1060651988453654528,tweet_mode='extended')
        return True
    except:
        AnimatedPrint(sprint("<<<<<WRONG CREDENTIALS IN KEYS>>>>>",style="digital"),color="red")
        AnimatedPrint(sprint("\tTry Again",style="digital"),color="yellow")
        return False



if __name__ == '__main__':
    intro()
    userstat=isExistingUser()
    UseIt=False
    if userstat:
        while(True):
            AnimatedPrint(">>> Existing Configuation Found... Would you like to \n\t1:Use it or 2:Change it?", color="cyan")
            AnimatedPrint("Response : ", color="cyan", con=True)
            option=str(input())
            if(option=='1'):
                UseIt=True
                break
            elif(option=='2'):
                UseIt=False
                break
            else:
                AnimatedPrint("Wrong Option. Please Select the Valid One\n", color="red")
            
                
    
    if (not userstat) or (not UseIt):
        Name_User=BasicInfo()
        has_ac=CheckForDevAc()
        if not has_ac:
            guideUser()
        SleepTime(.3)
        #Take the keys as Input
        AnimatedPrint("-"*45)
        AnimatedPrint("\nAlright, now, that You've an account, Please Specify the Required Settings",color="cyan")
        AnimatedPrint("\n Step 1 of 4: ",color="yellow")
        AnimatedPrint("\t Enter Your Consumer Key => ",con="True")       
        CONSUMER_KEY = str(input())

        AnimatedPrint("\n Step 2 of 4: ",color="yellow")
        AnimatedPrint("\t Enter Your Consumer Secret Key => ",con="True")
        CONSUMER_SECRET = str(input())
        
        AnimatedPrint("\n Step 3 of 4: ",color="yellow")
        AnimatedPrint("\t Enter Your Access Key => ",con="True")
        ACCESS_KEY = str(input())

        AnimatedPrint("\n Step 4 of 4: ",color="yellow")
        AnimatedPrint("\t Enter Your Access Secret Key => ",con="True")
        ACCESS_SECRET = str(input())

        createDir("data_Twi", hidden=True)
        os.chdir(os.getcwd()+"\\data_Twi")
        
        file=open('.CONSUMER_KEY','w')
        file.write(CONSUMER_KEY)
        file.close()
        
        file=open('.CONSUMER_SECRET','w')
        file.write(CONSUMER_SECRET)
        file.close()

        file=open('.ACCESS_KEY','w')
        file.write(ACCESS_KEY)
        file.close()

        file=open('.ACCESS_SECRET','w')
        file.write(ACCESS_SECRET)
        file.close()
        
        lastseenfile=open('.LastSeenValue',"w")
        lastseenfile.write("1060651988453654528")
        lastseenfile.close()

        file=open('.USER_NAME','w')
        file.write(Name_User)
        file.close()

        file = open('.userstat','w')
        file.write("User has been Successfully Created") #ADDD EXSISTENCE
        file.close()
        
        os.chdir("..")
        
    else:
        
        CONSUMER_KEY = ""
        CONSUMER_SECRET = ""
        ACCESS_KEY = ""
        ACCESS_SECRET = ""
        Name_User = ""

        #change The Dir
        os.chdir(os.getcwd()+"\\data_Twi")
                
        #Load Data from Existing File
        file=open('.USER_NAME','r')
        for name in file:
            Name_User = name
        file.close()

        AnimatedPrint("Welcome Back, "+Name_User, duration=.2, color="yellow")
        
        file=open('.CONSUMER_KEY','r')
        for key in file:
            CONSUMER_KEY = key
        file.close()
        
        file=open('.CONSUMER_SECRET','r')
        for key in file:
            CONSUMER_SECRET = key
        file.close()

        file=open('.ACCESS_KEY','r')
        for key in file:
            ACCESS_KEY = key
        file.close()

        file=open('.ACCESS_SECRET','r')
        for key in file:
            ACCESS_SECRET = key
        file.close()

        os.chdir("..")

    #Perform the Connections

    AnimatedPrint('\n>>> Activating The Twitter Bot <<<',color='red')
    

    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
    api = tweepy.API(auth)    
    FILE_NAME = '.LastSeenValue'
    attempt=3
    while(  not validateKeys(FILE_NAME,CONSUMER_KEY,CONSUMER_SECRET,ACCESS_KEY,ACCESS_SECRET) ):
        if(attempt==0):
            AnimatedPrint(sprint("Too Many Wrong Attempts",style="digital"),color="red")
            AnimatedPrint(sprint("Terminating in 5secs",style="bubble"),color="red")
            SleepTime(5)
            quit()
         
        AnimatedPrint("\n Step 1 of 4: ",color="yellow")
        AnimatedPrint("\t Enter Your Consumer Key => ",con="True")       
        CONSUMER_KEY = str(input())

        AnimatedPrint("\n Step 2 of 4: ",color="yellow")
        AnimatedPrint("\t Enter Your Consumer Secret Key => ",con="True")
        CONSUMER_SECRET = str(input())
        
        AnimatedPrint("\n Step 3 of 4: ",color="yellow")
        AnimatedPrint("\t Enter Your Access Key => ",con="True")
        ACCESS_KEY = str(input())

        AnimatedPrint("\n Step 4 of 4: ",color="yellow")
        AnimatedPrint("\t Enter Your Access Secret Key => ",con="True")
        ACCESS_SECRET = str(input())

        os.chdir(os.getcwd()+"\\data_Twi")
        
        file=open('.CONSUMER_KEY','w')
        file.write(CONSUMER_KEY)
        file.close()
        
        file=open('.CONSUMER_SECRET','w')
        file.write(CONSUMER_SECRET)
        file.close()

        file=open('.ACCESS_KEY','w')
        file.write(ACCESS_KEY)
        file.close()

        file=open('.ACCESS_SECRET','w')
        file.write(ACCESS_SECRET)
        file.close()

        
        os.chdir("..")
        attempt-=1

        
    
    AnimatedPrint('\t      Activated!\n',color='green')    

    SleepTime(.3)
        
    AnimatedPrint("-"*45)
    AnimatedPrint("Final Step...", color="cyan")
    os.chdir(os.getcwd()+"\\data_Twi")
    while(True):        
        AnimatedPrint("\nStep 1 of 2:\n\tWhich HashTag would you like to Target? [e.g. #HelloWorld] => ",color="yellow", con=True)
        hashTag = str(input())
        if('#' in hashTag):
            AnimatedPrint("Alright! HashTag Acquired", color="green")
            break
        else:
            AnimatedPrint("Ouch! Did you forget to include a #?", color="red")

    while(True):
        AnimatedPrint("\nStep 2 of 2:\n\tEnter Your Auto Reply => ",color="yellow", con=True)
        YourMsg=str(input())
        if(len(YourMsg)!=0):
            AnimatedPrint("Great! Auto Response Message Saved", color="green")
            break
        else:
            AnimatedPrint("Ouch! Did you forget to include a Message?", color="red")

    AnimatedPrint("Yay! Ready to Deploy Now!")
    items = list(range(0, 100))
    l = len(items)
    # Initial call to print 0% progress
    printProgressBar(0, l, prefix = 'Loading App...', suffix = 'Please Wait...', length = 50)
    for i, item in enumerate(items):
        # Do stuff...
        SleepTime(0.02)
        # Update Progress Bar
        printProgressBar(i + 1, l, prefix = 'Deploying App...', suffix = 'Please Wait...', length = 50)
    AnimatedPrint("\n\t\tYou're Live Now! We'll Refresh in Every 15 Seconds",color="green")
    AnimatedPrint("\n\t\t\t To Teminate, just close this Window",color="red")
    
    
    while True:
        reply_to_tweets(FILE_NAME, hashTag, YourMsg, Name_User)
        time.sleep(15)