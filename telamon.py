from datetime import datetime
import socket
import os
import argparse


parser = argparse.ArgumentParser()


now = datetime.now()

current_time = now.strftime("%H:%M:%S")


COLORS = {\
"black":"\u001b[30;1m",
"red": "\u001b[31;1m",
"green":"\u001b[32m",
"yellow":"\u001b[33;1m",
"blue":"\u001b[34;1m",
"magenta":"\u001b[35m",
"cyan": "\u001b[36m",
"white":"\u001b[37m",
"yellow-background":"\u001b[43m",
"black-background":"\u001b[40m",
"cyan-background":"\u001b[46;1m",
}


def colorText(text):
    for color in COLORS:
        text = text.replace("[[" + color + "]]", COLORS[color])
    return text





oner = "[[blue]]Önerilen[[white]]"
onerilen = colorText(oner)

vrenkli = "[[red]]-[[green]]Beta[[white]]"
vrenklibas = colorText(vrenkli)

print(f"""

@@@@@@@  @@@@@@@@  @@@        @@@@@@   @@@@@@@@@@    @@@@@@   @@@  @@@  
@@@@@@@  @@@@@@@@  @@@       @@@@@@@@  @@@@@@@@@@@  @@@@@@@@  @@@@ @@@  
  @@!    @@!       @@!       @@!  @@@  @@! @@! @@!  @@!  @@@  @@!@!@@@  
  !@!    !@!       !@!       !@!  @!@  !@! !@! !@!  !@!  @!@  !@!!@!@!  
  @!!    @!!!:!    @!!       @!@!@!@!  @!! !!@ @!@  @!@  !@!  @!@ !!@!  
  !!!    !!!!!:    !!!       !!!@!!!!  !@!   ! !@!  !@!  !!!  !@!  !!!  
  !!:    !!:       !!:       !!:  !!!  !!:     !!:  !!:  !!!  !!:  !!!  
  :!:    :!:        :!:      :!:  !:!  :!:     :!:  :!:  !:!  :!:  !:!  
   ::     :: ::::   :: ::::  ::   :::  :::     ::   ::::: ::   ::   ::  
   :     : :: ::   : :: : :   :   : :   :      :     : :  :   ::    :   

                                                                    {vrenklibas}
                                                    
""")
                                                                        



parser.add_argument("-s", "--scan", help='Memindai status situs / IP dari port tertentu', action="store_true" )
parser.add_argument("-t", "--test", help='lihat apakah situs tersebut terbuka atau tertutup', action="store_true" )
parser.add_argument("-a", "--all", help='memindai semua port dari situs', action="store_true" )
parser.add_argument("-sA", "--scanall", help='Memindai status port antara port yang telah di tentukan', action="store_true" )
parser.add_argument("target", help='ip atau situs web', type=str)
args = parser.parse_args()




s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

Target = args.target


if args.all:

    print(f"""
            


@@@@@@@  @@@@@@@@  @@@        @@@@@@   @@@@@@@@@@    @@@@@@   @@@  @@@  
@@@@@@@  @@@@@@@@  @@@       @@@@@@@@  @@@@@@@@@@@  @@@@@@@@  @@@@ @@@  
  @@!    @@!       @@!       @@!  @@@  @@! @@! @@!  @@!  @@@  @@!@!@@@  
  !@!    !@!       !@!       !@!  @!@  !@! !@! !@!  !@!  @!@  !@!!@!@!  
  @!!    @!!!:!    @!!       @!@!@!@!  @!! !!@ @!@  @!@  !@!  @!@ !!@!  
  !!!    !!!!!:    !!!       !!!@!!!!  !@!   ! !@!  !@!  !!!  !@!  !!!  
  !!:    !!:       !!:       !!:  !!!  !!:     !!:  !!:  !!!  !!:  !!!  
  :!:    :!:        :!:      :!:  !:!  :!:     :!:  :!:  !:!  :!:  !:!  
   ::     :: ::::   :: ::::  ::   :::  :::     ::   ::::: ::   ::   ::  
   :     : :: ::   : :: : :   :   : :   :      :     : :  :   ::    :   

                                                                    {vrenklibas}

            
|----------------------------------------------------------------|
|                                                                |
|  Target IP/domain :  {Target}                                            
|                                                                |
|  dimualai pada : {current_time}                                 
|                                                                |  
|----------------------------------------------------------------|   
            """)
    for Port in range(1,6112):
        try:
            s.connect((Target , Port))
            print("[+] Port Terbuka>> "+str(Port))
            
        except:
            print("[-] Port tertutup>> "+str(Port))

if args.test:
    print(f"""
            

@@@@@@@  @@@@@@@@  @@@        @@@@@@   @@@@@@@@@@    @@@@@@   @@@  @@@  
@@@@@@@  @@@@@@@@  @@@       @@@@@@@@  @@@@@@@@@@@  @@@@@@@@  @@@@ @@@  
  @@!    @@!       @@!       @@!  @@@  @@! @@! @@!  @@!  @@@  @@!@!@@@  
  !@!    !@!       !@!       !@!  @!@  !@! !@! !@!  !@!  @!@  !@!!@!@!  
  @!!    @!!!:!    @!!       @!@!@!@!  @!! !!@ @!@  @!@  !@!  @!@ !!@!  
  !!!    !!!!!:    !!!       !!!@!!!!  !@!   ! !@!  !@!  !!!  !@!  !!!  
  !!:    !!:       !!:       !!:  !!!  !!:     !!:  !!:  !!!  !!:  !!!  
  :!:    :!:        :!:      :!:  !:!  :!:     :!:  :!:  !:!  :!:  !:!  
   ::     :: ::::   :: ::::  ::   :::  :::     ::   ::::: ::   ::   ::  
   :     : :: ::   : :: : :   :   : :   :      :     : :  :   ::    :   

                                                                    {vrenklibas}

            
|----------------------------------------------------------------|
|                                                                |
|  Target IP/domain :  {Target}                                            
|                                                                |
|  dimualai pada : {current_time}                                 
|                                                                |  
|----------------------------------------------------------------|   
            """)

    os.system(f"ping {Target}")


if args.scan:
    x = int(input("Port >"))
    Port = x
    print(f"""
            


@@@@@@@  @@@@@@@@  @@@        @@@@@@   @@@@@@@@@@    @@@@@@   @@@  @@@  
@@@@@@@  @@@@@@@@  @@@       @@@@@@@@  @@@@@@@@@@@  @@@@@@@@  @@@@ @@@  
  @@!    @@!       @@!       @@!  @@@  @@! @@! @@!  @@!  @@@  @@!@!@@@  
  !@!    !@!       !@!       !@!  @!@  !@! !@! !@!  !@!  @!@  !@!!@!@!  
  @!!    @!!!:!    @!!       @!@!@!@!  @!! !!@ @!@  @!@  !@!  @!@ !!@!  
  !!!    !!!!!:    !!!       !!!@!!!!  !@!   ! !@!  !@!  !!!  !@!  !!!  
  !!:    !!:       !!:       !!:  !!!  !!:     !!:  !!:  !!!  !!:  !!!  
  :!:    :!:        :!:      :!:  !:!  :!:     :!:  :!:  !:!  :!:  !:!  
   ::     :: ::::   :: ::::  ::   :::  :::     ::   ::::: ::   ::   ::  
   :     : :: ::   : :: : :   :   : :   :      :     : :  :   ::    :   

                                                                    {vrenklibas}
            
|----------------------------------------------------------------|
|                                                                |
|  Target IP/domain :  {Target}                                            
|                                                                |
|  dimualai pada : {current_time}                                 
|                                                                |  
|----------------------------------------------------------------|   
            """)

            

    try:
        s.connect((Target , Port))
        print("[+] Port Terbuka>> "+str(Port))
    except:
        print("[-] Port Tertutup>> "+str(Port))

if args.scanall:

    min = int(input("port terkecil >"))
    max = int(input("port max >"))

    print(f"""
            


@@@@@@@  @@@@@@@@  @@@        @@@@@@   @@@@@@@@@@    @@@@@@   @@@  @@@  
@@@@@@@  @@@@@@@@  @@@       @@@@@@@@  @@@@@@@@@@@  @@@@@@@@  @@@@ @@@  
  @@!    @@!       @@!       @@!  @@@  @@! @@! @@!  @@!  @@@  @@!@!@@@  
  !@!    !@!       !@!       !@!  @!@  !@! !@! !@!  !@!  @!@  !@!!@!@!  
  @!!    @!!!:!    @!!       @!@!@!@!  @!! !!@ @!@  @!@  !@!  @!@ !!@!  
  !!!    !!!!!:    !!!       !!!@!!!!  !@!   ! !@!  !@!  !!!  !@!  !!!  
  !!:    !!:       !!:       !!:  !!!  !!:     !!:  !!:  !!!  !!:  !!!  
  :!:    :!:        :!:      :!:  !:!  :!:     :!:  :!:  !:!  :!:  !:!  
   ::     :: ::::   :: ::::  ::   :::  :::     ::   ::::: ::   ::   ::  
   :     : :: ::   : :: : :   :   : :   :      :     : :  :   ::    :   

                                                                    {vrenklibas}

            
|----------------------------------------------------------------|
|                                                                |
|  Target IP/domain :  {Target}                                            
|                                                                |
|  dimualai pada : {current_time}                                  
|                                                                |  
|----------------------------------------------------------------|   
            """)
            
    for Port in range(min, max + 1):
        try:
            s.connect((Target , Port))
            print("[+] Port terbuka>> "+str(Port))
            
        except:
            print("[-] Port Tertutup>> "+str(Port))
