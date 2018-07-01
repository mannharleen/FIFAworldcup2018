# Get Football World Cup 2018 details
# Version: 0.1
# Created by: Harleen Mann
# Last modified date: 25-6-18

# v0.1: get tournament name
#       get table standings

import requests
import sys
import json
import texttable
import os

os.environ['http_proxy'] = ''

URL = "http://api.football-data.org/v1/"
headers = {
    "X-Auth-Token": "14c82fcc05f14df483676b5edd94c555",
    "X-Response-Control": "minified"
}


def get_competition():
    return requests.get(URL + "competitions/467", headers=headers)

def get_table():
    return requests.get(URL + "competitions/467/leagueTable", headers=headers)

def run(argv):
    if (argv == "1"):
        result = get_competition().json()
        print(result['caption'])

    if (argv == "groupStage"):
        result = get_table().json()

        for groupName in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']:
            table = texttable.Texttable()
            ref = result['standings'][groupName]
            l = [["Group", "Rank", "Country", "Played", "Points", "GF", "GA", "GD"]]
            for team in range(0, len(ref)):
                teamRow = list(ref[team].values())
                l.append(teamRow[:3] + teamRow[4:5] + teamRow[6:])
            table.add_rows(l)
            print(table.draw() + "\n")

if __name__ == '__main__':
    if len(sys.argv) <= 1:
        print("usage: python try-requests.py x \n"
              "\t \t where x can be \n \t \t 1 for tournament name \n \t \t 2 for league table")
    else:
        main(sys.argv[1])