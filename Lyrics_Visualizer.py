
###Things should be changed across different songs###
sound = "sound.wav"
beats_per_bar = 4
bpm = 130.5
audio_offset = 0 #(second)
bar_line = '!'
wait = '$' #(second)
#####################################################

from itertools import islice
import time
import simpleaudio as sa

def main():
    input("Press Enter to start")
    
def sleep(duration, get_now = time.perf_counter):
    now = get_now()
    end = now + duration
    while now < end:
        now = get_now()
    
def song():
    
    lyrics = \
    """
!\033[1;31;48mSwitch on the power line
!Remember to put on PROTECTION
!Lay down your pieces
!And let's begin \033[1;32;48mOBJECT CREATION\033[1;37;0m
!Fill in my data
!Parameters INITIALISATION
!\033[1;31;48mSetup, a new world
!And let's begin \033[1;36;48mTHE SIMULATION
!$8                      _  _     ____________.--.
                  \|\\|_|//_.-"" .'    \\   /|  |
                  |.-\"\"\"-.|   /       \\_/ |  |
                  \\  ||  /| __\\_____________ |
                  _\\_||_/_| .-\"\"            \"\"-.  __
                .' '.    \\//                    \".\\/
                ||   '. >()_  \033[1;33;48mworld.execute(me)\033[1;36;48m  |()<
                ||__.-' |/\\ \\                    |/\\
                   |   / "|  \\__________________/.""
                  /   //  | / \\ "-.__________/  /\\
               ___|__/_|__|/___\\___".______//__/__\\
              /|\\     [____________] \__/         |\\
             //\\ \\     |  |=====| |   /\\\\         |\\\\
            // |\\ \\    |  |=====| |   | \\\\        | \\\\        ____...____....----
          .//__| \\ \\   |  |=====| |   | |\\\\       |--\\\\---\"\"\"\"     .            ..
_____....-//___|  \\_\\  |  |=====| |   |_|_\\\\      |___\\\\    .                 ...'
 .      .//-.__|_______|__|_____|_|_____[__\\\\_____|__.-\\\\      .     .    ...::
        //        //        /          \\ `-_\\\\/         \\\\          .....:::
  -... //     .  / /       /____________\\    \\\\       .  \\ \\     .            .
      //   .. .-/_/-.                 .       \\\\        .-\\_\\-.                 .
     / /      '-----'           .             \\ \\      '._____.'         .
  .-/_/-.         .                          .-\\_\\-.                          ...
 '._____.'                            .     '._____.'                       .....
        .                                                             ...... ..
    .            .                  .                        .
   ...                    .                      .                       .      .
        ....     .                       .                    ....
          ......           . ..                       ......'
             .......             '...              ....
                                   ''''''      .              .
!\033[1;31;48mIf I'm a set of points
!Then I will give you my \033[1;33;48mdimension
!\033[1;31;48mIf I'm a circle
!Then I will give you my \033[1;33;48mcircumference
!\033[1;31;48mIf I'm a sine wave
!Then you can sit on all my \033[1;33;48mtangents
!\033[1;31;48mIf I approach infinity
!then you can be MY \033[1;36;48mLIMITATIONS
!
!\033[1;32;48mSwitch my current
To !AC to DC
And then !blind my vision
\033[1;31;48mSo !dizzy, so dizzy
\033[1;32;48mOh, !we can travel
To !A.D to B.C
And !we can unite
\033[1;31;48mSo !deeply, so deeply
!
!\033[1;35;48mIf I can
If I can, !give you all THE \033[1;33;48mSIMULATIONS
!\033[1;35;48mThen I can
Then I can, !be your only \033[1;33;48mSATISFACTION
!\033[1;32;48mIf I can make you happy
!Then I'll run the \033[1;33;48mEXECUTION
!\033[1;31;48mThough we are trapped
In this !strange, strange \033[1;33;48mSIMULATION
!
!\033[1;32;48mIf I'm an eggplant
!Then I will give you my \033[1;33;48mNUTRIENTS
!\033[1;32;48mIf I'm a tomato
!Then I'll give you \033[1;33;48mANTIOXIDANTS
!\033[1;32;48mIf I'm a tabby cat
!Then I will purr for your \033[1;33;48mENJOYMENT
!\033[1;32;48mIf I'm the only god
!Then your the proof of my \033[1;33;48mEXISTENCE
!
!\033[1;31;48mSwitch my gender
!\033[1;33;48mTo F to M
!\033[1;31;48mAnd then do whatever
!\033[1;33;48mFrom AM to PM
!\033[1;31;48mI will switch my role
!\033[1;33;48mTo S to M
!\033[1;31;48mSo we can enter
!\033[1;33;48mThe trance, the trance
!
!\033[1;35;48mIf I can
If I can, !feel your \033[1;33;48mVIBRATIONS
!\033[1;34;48mThen I can
Then I can, !finally be \033[1;33;48mCOMPLETION
!\033[1;31;48mThough you have left
You have !left
You have left
You have !left
You have left
You have !left me in \033[1;33;48mISOLATION
!
!\033[1;35;48mIf I can
If I can, !Erase all the pointless \033[1;33;48mFRAGMENTS
!\033[1;34;48mThen maybe, then maybe
!You won't leave me so \033[1;33;48mDISHEARTENED
!\033[1;31;48mChallenging your !god
You have !made some \033[1;33;48m!ILLEGAL ARGUMENTS
!$8                                                       .                                                                                              
  .+*##-:.                                                                                                                                   ::+##**  
:-#****%%*..                                                             ............                                                      .+#%*#*#*. 
 .**#**@@@@@@-.                                                  ::...:=##+.......:.:.                                                 .:@@@@@@*#*#*. 
   :+**#%@@@@@@@@+-.                                             :-==*#####******===.:+                                           ..+@@@@@@@@@****=.  
  .****:#*#*@@*@@@@@@*..*                         :  ..@@@@+.  #*::==*=*@@@@@@%**===.:#@+.-@@@@=..::                          ..:@@@@@@%*@@#**.****:  
  .*#**%***#@@@#**%%@@@@@@@-:-=-..              =+-@@@@@%%%@@@@+-:.==****#####*=*===.:-@@@@%%%@@@@@=-*                .-:--@@@@@@@@%#**@@@@***@**#*:  
   :*#****#%@@@@@@******#@@@@@@@@@+++++--------++%@@@#++---=+*@@+:.--##****####***-=.:#@%++---=+*@@@@++:=--=:-:+++++%@@@@@@@@%******#@@@@@#%*******   
    .:**###**@@@@@@@@@@*********@@@@@@@@@@@@@@@@@@@**=+:=-=-*:*@+:.+##*#####*###**#-.:##++-=---=:**%@@@@@@@@@@@@@@@@@@%********%@@@@@@@@@***##**-:    
     :*+--*****@@@@@@@@@@@******##*****************+-.:--====.=#+:-##+:-::-=---**###.:#*.-====--..+******************##*****@@@@@@@@@@@*****+-=#=*    
    .#***@@@@##@@@@@%**@@@@@%#********************....:----=*.=**#*###-:.-:.--.:=##*.:**.*=-=--:....=***#***************#*@@@@@***@@@@@*#@@@@**#*:    
     -****#####*@@@@%*****@@@@*@@@@@@***************....=+:...##=#**###::--=-::=**##*.=#=..:=+....-#*************%@@@@@*%@@@@*****@@@@**####****:.    
      *+++*****+*@%%@@***@@@@@@@@@@%**************#.:-::::.-#*+=####*#**#@@@@@:#*##**#**+#*.:::---.+***************@@@@@@@@@@%**@@%@#++******+=*.     
      .=**@@@@******@@@@@#*@@@*@@@%*****###******#+:::::::..=++**##+**#-.-%%%:.##*#:*+##=#-:::::::::********###*****@@@*%@@**@@@@@*******@@@***#      
        -#**##**###@%@##**@@@@@******************:::::::::...*+-#**-+=#-*@@@%*=#*=#=##+=**...::::::::.-*****************@@@@***%%@@%*#***##***=       
          :-==++*@##*******@@@@%****@@@*******:-.::::::::...=======-**#-@@@%@@@+*##-====-=:...:::::::-==-.-****@@@%****@@@@*******#*@**+===*:         
             -**********@@@#**#****@@@****=:..==.::::=:::.:---=:=-=*+-#+-*@@@=-**:**===:=--:.:::::::::======-.-*@@@********@@@***********=            
               -++++++*@@%**+#=#@***+==....:..++..-::=:..:=--##=------=##-=---**-----==++--=#.::::::-:=++======-.-***@@******@@#*++++++-              
                  ********#*:#+@****:.....:+++*+=:-:==:=::--------=-====---=*#=======--=----=.--+:::+:=**+++======-.**@@@********#**=                 
                    ..+**+-@@=****...:.:++****#*#:*++###+-----=========%+::=.---=========---+:#-*:*+*:=#****+++======.:#*%@+-***:-+                   
                        .*#*+==::==...+****#%@@##**+=++#*=--========-*==.*-##-:-=-===========.#######+=@@@#****+=======:.+***. .                      
                          .-:..====:=****##@@@@@#%+....=#+========#+-==-:+.::=.-==**:========:####*####@@@@@##****=======:...                         
                           ....====**#%%%@@@@@@@##*#+*:..:*====-.:=-==---.:-::===-=+==-=====::*########@@@@@@%%%#**++======:..                        
                         #.==.:=****#@@@@@@@@@####.:+-=....:...=.*-==-=--=====#==-==**---==:.::#*##-:#**#@@@@@@@@@#**++======..                       
                        .:==.-#+***@@@@@@@@@#*****@@#%@@##:.%@@=====---==--*=+----+====---..::+-:=*:*+***#%@@@@@@@@#***+======-..                     
                      ..====-+**#%@@@@@@@@%#*****%#@@#@@@%*-*@@=======-*=--===++=======---:.::::-*:::=+++**#@@@@@@@@@##**+======:.                    
                     .-====+***#@@@@@@@@@#****@@@@@#%@@@@@%#*=====--------=====-----======-.::::.::.-====+***%@@@@@@@@%***+=======.:                  
                    .=====+**###@@@@@@##**#@@@@@@@@@@*@%#@@@======------------------=======  ::::..========+**##%@@@@@@%#**++======.:                 
                   .====++**#%@@@@@@%##*+@@@@@@@@@+.+*@@@@@=======-=----=---------==-======     .:...========+**##@@@@@@@%***+======..                
                 ..=====++*%@@@@@@@***+#@@@@@@@@-.=%@@@@@%========-=---===--==-===---========      .=..========****#@@@@@@@#*+=======:.-              
                .:=====+*##%@@@@@###*+%#*%%#%%:.=+#+===+==========-==---=======------==========      ==::========+***@@@@@@##**+======:.:             
               .:====****#@@@@@@%#**++*+=*#+=.-:+=+....==========--==-----======------===-======      ==%.:======+**#%%@@@@@%#**+======:..            
               .====+***#%@@@@%##**+%*++#=+.:+-++#*=**+*#-=======---==----==-=====----====--          ==* ..======+***##@@@@@%#**++=====:..           
              .=====+***%@@@@@###**=+#++#+.+++-++#*=**+*#-======---==----===-======---======-          =-   .-=====++***%@@@@@##*++======..           
             .-===+***#@@@@@@@##***@@@@@*-%@@@*#@@@@@@@@#=======-===----====--======---=======         =-    .:=====+*##%@@@@@@@#**++=====.:          
            :.=====++*##@@@@@@@%**#@@@@*=@@@@@##%@@@@@@@@+=========-----====---======---=====-         -      .:=====++**#@@@@@@##*++=====-.-         
           -.-=====++**#@@@@@@#**=#%%%+=########*@%@@@@%%*:---====-----=====----======----::.         ==       .:====+***#@@@@@@##*++======..         
           .:=====++**#%@@@@@@#** ===:.         -=**#@#%%+-::-===-----======-----======---::-       :=:        ..:====++*##@@@@@@#***+=====-..        
          ..======+***#@@@@@%##*: ===.            -==##+--**-.=======*.=====----========-. .=-=-  =.             .-====+*##%@@@@@#***+======..        
          ..======+***%@@@@@%##+  ==.             .*--=--*# -. ..:.-=*::.===----+===...        ==-:              -.====+*##%@@@@@#***+======-.:       
         ..=======****%@@@@@%##   =-.          .+++=..:         -:.-=*:::@@*====+===.:.        .-+==++=-:         .-=****#@@@@@%##*+=======-          

!\033[1;37;0mExecution, Execution, !Execution, Execution
!Execution, Execution, !Execution, Execution
!Execution, Execution, !Execution, Execution
!Ein, Dos, Trois
Ne, !Fem, Liu
EXECUTION
!
!\033[1;35;48mIf I can
If I can, !give you all the \033[1;33;48mEXECUTION
!\033[1;34;48mThen I can
Then I can, !be your only \033[1;33;48mEXECUTION
!\033[1;35;48mIf I can, have you back
\033[1;34;48mThen !I will run the \033[1;33;48mEXECUTION
!\033[1;31;48mThough we are trapped
!We are trapped ah
!
!\033[1;34;48mI've studied
I've studied, !how to properly LO-O-OVE
!\033[1;31;48mQuestion me
Question me, !I can answer all LO-O-OVE
!I know the algebraic
!expression of LO-O-OVE
!Though you are free
I am !trapped
Trapped in LO-O-OVE\033[1;37;0m
!$8 
!\033[1;31;48mEXECUTION
!
    """
##################Lyrics ends here#######################

    c = 0
    l = 0
    t = 60 * beats_per_bar / bpm #(seconds) times (beats per bar) divide by (BPM)
    for j in lyrics: #counts line nums for array initialization
        if j == bar_line or j == wait:
            c += 1
    length = [0] * (c + 1)
    length[c] = 1000
    c = 0
    i = iter(lyrics)
    for j in i: #counts chr nums for every line
        if j == bar_line:
            length[l] = c
            c = 0
            l += 1
        elif j == wait:
            j = next(i)
            length[l] = int(j)
            l += 1
        elif j == '\033':
            while j != 'm':
                j = next(i)
        elif j == '\n':
            continue
        else:
            c += 1
    try:
        wave_obj = sa.WaveObject.from_wave_file(sound) #sound file
    except:
        print("\033[1;31;48mError: sound.wav not found, or simpleaudio is not installed.\033[1;37;0m")
        exit()
    play_obj = wave_obj.play()
    sleep(audio_offset) #for audio latency offset
    l = 0
    i = iter(lyrics)
    for j in i: #read and show the lyrics on time
        if j == '\033':
            while j != 'm':
                print(j, end='')
                j = next(i)
            print(j, end='')
        elif j == bar_line:
            l += 1
            c = 0
        elif j =='\n':
            print("\n    ", end='')
        elif j == wait:
            j = next(i)
            length[l + 1] /= length[l]
            l += 1
            continue
        else:
            sleep(t / length[l])
            print(j, end='')
            c += 1
            
if __name__ == "__main__":
    main()
    song()