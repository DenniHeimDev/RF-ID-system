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

    x = input()
    print("Velkommen: ", idDict[x], ".", "Du kom klokka ", datetime.now())

