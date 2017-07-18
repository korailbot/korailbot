
stations = open("stations.txt").read().splitlines()
cmdPatterns = open("commandPatterns.txt").read().splitlines()

file = open("requests.txt", "w")

for station in stations:
    for command in cmdPatterns:
        strRequest = station + '행 열차 ' + command
        file.write(strRequest+'\n')
        strRequest = station + '가는 열차 ' + command
        file.write(strRequest+'\n')
        strRequest = station + '행 기차 ' + command
        file.write(strRequest+'\n')
        strRequest = station + '가는 기차 ' + command
        file.write(strRequest+'\n')
    print(station)

file.close()
