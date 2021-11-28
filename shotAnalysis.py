def shotLocation(shot):
    #determines shot location
    #options: "2PT", "NC3", "C3"
    #2 pointer, non corner 3, corner 3
    x = float(shot[1])
    y = float(shot[2])
    if abs(x) >= 22 and y<=7.8:
        return "C3"
    if (x**2)+(y**2)>564.0625:
        return "NC3"
    return "2P"

def main():
    #reading in data
    data = open('shots_data.csv', 'r').readlines()
    for i in range(len(data)):
        data[i] = data[i].split(',')
        data[i][3] = data[i][3].strip('\n')

    #removing headers
    data.pop(0)

    #Naming: Team, shot type, make/miss
    #e.g. ANC3_make is a Team A non corner 3 that went in
    AC3_make = 0
    AC3_miss = 0
    ANC3_make = 0
    ANC3_miss = 0
    A2P_make = 0
    A2P_miss = 0
    BC3_make = 0
    BC3_miss = 0
    BNC3_make = 0
    BNC3_miss = 0
    B2P_make = 0
    B2P_miss = 0

    #Iterating through data to find total makes and
    #misses in each zone for each team
    for i in range(len(data)):
        shotPlace = shotLocation(data[i])
        if data[i][0] == "Team A":
            if shotPlace == "C3":
                if data[i][3] == "1":
                    AC3_make += 1
                else:
                    AC3_miss += 1
            if shotPlace == "NC3":
                if data[i][3] == "1":
                    ANC3_make += 1
                else:
                    ANC3_miss += 1
            if shotPlace == "2P":
                if data[i][3] == "1":
                    A2P_make += 1
                else:
                    A2P_miss += 1
        else:
            if shotPlace == "C3":
                if data[i][3] == "1":
                    BC3_make += 1
                else:
                    BC3_miss += 1
            if shotPlace == "NC3":
                if data[i][3] == "1":
                    BNC3_make += 1
                else:
                    BNC3_miss += 1
            if shotPlace == "2P":
                if data[i][3] == "1":
                    B2P_make += 1
                else:
                    B2P_miss += 1
    
    #Finding Shot distribution for each team
    #Naming: Team, Shot, "Percent"
    #e.g. B2PPercent is the percent of shots taken by team B that are 2 pointers
    ATotal = AC3_make + AC3_miss + ANC3_make + ANC3_miss + A2P_make + A2P_miss
    BTotal = BC3_make + BC3_miss + BNC3_make + BNC3_miss + B2P_make + B2P_miss
    AC3Percent = round(((AC3_make + AC3_miss)/ATotal), 3)
    ANC3Percent = round(((ANC3_make + ANC3_miss)/ATotal),3)
    A2PPercent = round(((A2P_make + A2P_miss)/ATotal),3)
    BC3Percent = round(((BC3_make + BC3_miss)/BTotal), 3)
    BNC3Percent = round(((BNC3_make + BNC3_miss)/BTotal), 3)
    B2PPercent = round(((B2P_make + B2P_miss)/BTotal), 3)

    #Finding efg for each team
    #Naming: "eFG", Team, Shot
    #e.g. eFGB2P is the efg of team B for 2 pointers
    eFGAC3 = round((((AC3_make)*1.5)/(AC3_make+AC3_miss)), 3)
    eFGANC3 = round((((ANC3_make)*1.5)/(ANC3_make+ANC3_miss)), 3)
    eFGA2P = round((((A2P_make)*1)/(A2P_make+A2P_miss)), 3)
    eFGBC3 = round((((BC3_make)*1.5)/(BC3_make+BC3_miss)), 3)
    eFGBNC3 = round((((BNC3_make)*1.5)/(BNC3_make+BNC3_miss)), 3)
    eFGB2P = round((((B2P_make)*1)/(B2P_make+B2P_miss)), 3)

    #printing all found values
    print()
    print("Totals")
    print()
    print("Shot Distribution")
    print("Team A")
    print("Corner 3:", AC3Percent)
    print("Non-Corner 3:", ANC3Percent)
    print("2 Point:", A2PPercent)
    print()
    print("Team B")
    print("Corner 3:", BC3Percent)
    print("Non-Corner 3:", BNC3Percent)
    print("2 Point:", B2PPercent)
    print()
    print("Effective Field Goal Percents")
    print("Team A")
    print("Corner 3:", eFGAC3)
    print("Non-Corner 3:", eFGANC3)
    print("2 Point:", eFGA2P)
    print()
    print("Team B")
    print("Corner 3:", eFGBC3)
    print("Non-Corner 3:", eFGBNC3)
    print("2 Point:", eFGB2P)

main()