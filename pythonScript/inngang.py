from datetime import datetime



idDict = {
    "1234": "Dennis Heimsaeter",
    "4321": "Rikard Solar",
    "2314": "Sadner Rebni"
}

now = datetime.now()
print(now)
timestamp = datetime.timestamp(now)
print("timestamp =", timestamp)

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
    else:
        print("Velkommen: %s. Du kom klokka %s" % (forNavn, datetime.now()))    
        
    
    #print("Velkommen: ", navn, ".", "Du kom klokka ", datetime.now())

