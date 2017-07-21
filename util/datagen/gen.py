
stations = open("stations.txt").read().splitlines()
cmdPatterns = open("commandPatterns.txt").read().splitlines()
datePatterns = open("shortdatePatterns.txt").read().splitlines()
timePatterns = open("timePatterns.txt").read().splitlines()

file = open("requests.txt", "w")

step = 0
for station in stations:
    for command in cmdPatterns:
        for strtime in timePatterns:
            for strdate in datePatterns:
                # date + time + station + command
                strdatetime = strdate + ' ' + strtime
                strdatetime = strdatetime.strip()
                strRequest = strdatetime + ' ' + station + '행 열차 ' + command
                file.write(strRequest+'\n')
                strRequest = strdatetime + ' ' + station + '가는 열차 ' + command
                file.write(strRequest+'\n')
                strRequest = strdatetime + ' ' + station + '행 기차 ' + command
                file.write(strRequest+'\n')
                strRequest = strdatetime + ' ' + station + '가는 기차 ' + command
                file.write(strRequest+'\n')

                # date + station + time + command

                # station + date + time + command

    print(station)
    step += 1
    if step==10:
        break

file.close()

#10개역만 했을 때 약 100메가바이트~~
