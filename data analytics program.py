
import requests
import json
import pandas as pd

# put your TBA auth key in this variable

authKey = " "

# use this variable for the filepath of your data spreadsheet
# to read just one sheet out of the workbook, put a comma after the filepath and then the name of the sheet
# filepath and sheet name should both be strings

scoutingSheet = pd.read_excel(' ', " ")

codeLoop = True

yearRequest = input("Enter your event year: ")
eventRequest = input("Enter your event code (w/o year): ")

eventCode = yearRequest + eventRequest

# provided you have one row per match, the following row works. if not, feel free to comment it out/not use it

print("At " + eventCode + ", there were " + str(len(scoutingSheet)) + " matches.")

while codeLoop == True:

    
    matchRequest = input("Which qualification match would you like to view?: ")

    eventMatchCode = str(yearRequest + eventRequest + "_qm" + matchRequest)

    matchRequest = int(matchRequest)

    # for my sample spreadsheet, match numbers are in column 0, red alliance scores are in column 1, blue alliance scores are in column 2. adjust to match your spreadsheet design as needed
    # your [0,0] will be the first row/column that isn't a header
    # iat asks for [row, column] in the square brackets

    scoutingRedScore = scoutingSheet.iat[matchRequest-1,1]
    scoutingBlueScore = scoutingSheet.iat[matchRequest-1,2]

    print("Scouting results for match " + str(scoutingSheet.iat[matchRequest-1,0]))
    print("Red alliance scouting score (from data, w/o fouls): " + str(scoutingRedScore))
    print("Blue alliance scouting score (from data, w/o fouls): " + str(scoutingBlueScore))

    # if your scouting app already counts fouls/tech fouls, you can use match/[event code]/simple to just get the final score. if you need to manually add in fouls/tech fouls, use match/[event code]

    tbaRequest = json.loads(requests.get('https://www.thebluealliance.com/api/v3/match/' + eventMatchCode, headers={'X-TBA-Auth-Key':authKey}).text)

    
    scoutingRedScoreFouls = scoutingSheet.iat[matchRequest-1,1]+tbaRequest["score_breakdown"]["red"]["foulPoints"]
    scoutingBlueScoreFouls = scoutingSheet.iat[matchRequest-1,2]+tbaRequest["score_breakdown"]["blue"]["foulPoints"]


    print("Red scouting score WITH fouls: " + str(scoutingRedScoreFouls))
    print("Blue scouting score WITH fouls: " + str(scoutingBlueScoreFouls))
    
    
    tbaRedScore = tbaRequest["alliances"]["red"]["score"]
    tbaBlueScore = tbaRequest["alliances"]["blue"]["score"]

    
    print("TBA Red Alliance Score: " + str(tbaRedScore))
    print("TBA Blue Alliance Score: " + str(tbaBlueScore))

  
    if abs((tbaRedScore-scoutingRedScoreFouls)) <= tbaRedScore / 20:
        print("Red alliance score is within 5% of the official score. Nice work, scouters!")
    elif abs((tbaRedScore-scoutingRedScoreFouls)) >= tbaRedScore / 20:
        print("Red alliance score is more than 5% different than the official score. Looks like something is up with your data.")


    if abs((tbaBlueScore-scoutingBlueScoreFouls)) <= tbaBlueScore / 20:
        print("Blue alliance score is within 5% of the official score. Nice work, scouters!")
    elif abs((tbaBlueScore-scoutingBlueScoreFouls)) >= tbaBlueScore / 20:
        print("Blue alliance score is more than 5% different than the official score. Looks like something is up with your data.")

    
    userChoice = input("Would you like to look at another match? (y/n): ")

    if userChoice == "n":
        break
    else:
        pass
