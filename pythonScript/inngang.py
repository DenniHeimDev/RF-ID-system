from datetime import datetime
from time import sleep  # Legg til denne importen

idDict = {
    "02C915B180D900": "Dennis Heimsaeter",
    "047570AA985A80": "Rikard Solar",
    "5C8FA70C": "Sadner Rebni"
}

def timestamp():
    now = datetime.now()
    time = datetime.timestamp(now)
    return time
    

while True:
    forNavn = ""

    keyError = False
    
    print("Scan kortet:")

    x = input()

    try:
        forNavn = idDict[x]
    except KeyError as e:
        print("Feil Kort!")
        keyError = True
        
    if(keyError == True):
        print("Prøv Igjen...")
        keyError = False
    else:
        print("Velkommen: %s. Du kom %s" % (forNavn, datetime.now()))
        saveFile = open("inngangsinfo.txt", "a")
        saveFile.write("%s,%s\n" % (forNavn, timestamp())) 
        sleep(1)  # Endret fra pause(1) til sleep(1)
        saveFile.close()
        
    
    #print("Velkommen: ", idDict[x], ".", "Du kom klokka ", datetime.now())
