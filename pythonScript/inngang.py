from datetime import datetime

idDict = {
    "1234": "Dennis Heimsaeter",
    "4321": "Rikard Solar",
    "2314": "Sadner Rebni"
}

def timestamp():
    now = datetime.now()
    time = datetime.timestamp(now)
    return time
    

while True:
    forNavn = ""
    etterNavn = ""

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
        print("Velkommen: %s %s. Du kom klokka %s" % (forNavn, etterNavn, datetime.now()))
        saveFile = open("inngangsinfo.txt", "a")
        saveFile.write("%s,%s\n" % (forNavn, timestamp())) 
        saveFile.close()   
        
    
    #print("Velkommen: ", navn, ".", "Du kom klokka ", datetime.now())

