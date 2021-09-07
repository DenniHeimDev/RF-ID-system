from datetime import datetime



idDict = {
    "1234": "Dennis",
    "4321": "Rikard",
    "2314": "Sadner"
}

now = datetime.now()
print(now)
timestamp = datetime.timestamp(now)
print("timestamp =", timestamp)

while True:
    print("Scan kortet:")
    navn = ""

    x = input()

    navn = idDict[x]

    print("Velkommen: %s. Du kom klokka %s" % (navn, datetime.now()))
    #print("Velkommen: ", navn, ".", "Du kom klokka ", datetime.now())

