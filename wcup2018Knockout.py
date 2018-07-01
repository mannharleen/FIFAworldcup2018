__author__ = 'Harleen Singh Mann<mannharleen(at)gmail.com>'
__license__ = 'LGPL'
__version__ = '0.1.0'

import json, sys, requests, os, texttable

os.environ['http_proxy'] = ''
URL = "http://api.football-data.org/v1/competitions/467/fixtures"
headers = {
    "X-Auth-Token": "14c82fcc05f14df483676b5edd94c555"
}

class knockOutMatch:
    """Class that defines a match and return the scoreboard for that match in the required format
    """
    def __init__(self, team1='', team2='', team1Score=0, team2Score=0, date=''):
        self.team1 = team1
        self.team2 = team2
        self.team1Score = team1Score
        self.team2Score = team2Score
        self.date = date[:10]
        self.table = texttable.Texttable()

    def __str__(self):
        text = [[str(self.team1), str(self.team1Score)], [str(self.team2), str(self.team2Score)]]
        self.table.set_cols_width([11,4])
        self.table.add_row([self.date,''])
        self.table.add_rows(text, header=False)
        return(self.table.draw() + "\n")

def run(argv):
    fixtures = requests.get(URL, headers=headers).json()['fixtures']
    fixturesR16_json = list(filter(lambda x: x['matchday'] == 4, fixtures))
    fixturesR8_json_QF = list(filter(lambda x: x['matchday'] == 5, fixtures))
    fixturesR4_json_SF = list(filter(lambda x: x['matchday'] == 6, fixtures))
    fixturesR2_json_F = list(filter(lambda x: x['matchday'] == 7, fixtures))
    fixturesR2_json_TP = list(filter(lambda x: x['matchday'] == 8, fixtures))

    fixturesR16_knockOutMatch = list(map(
        lambda x: knockOutMatch(x['homeTeamName'], x['awayTeamName'], x['result']['goalsHomeTeam'],
                                x['result']['goalsAwayTeam'], x['date']).__str__(), fixturesR16_json))
    fixturesR8_knockOutMatch_QF = list(map(
        lambda x: knockOutMatch(x['homeTeamName'], x['awayTeamName'], x['result']['goalsHomeTeam'],
                                x['result']['goalsAwayTeam'], x['date']).__str__(), fixturesR8_json_QF))
    fixturesR4_knockOutMatch_SF = list(map(
        lambda x: knockOutMatch(x['homeTeamName'], x['awayTeamName'], x['result']['goalsHomeTeam'],
                                x['result']['goalsAwayTeam'], x['date']).__str__(), fixturesR4_json_SF))
    fixturesR2_knockOutMatch_F = list(map(
        lambda x: knockOutMatch(x['homeTeamName'], x['awayTeamName'], x['result']['goalsHomeTeam'],
                                x['result']['goalsAwayTeam'], x['date']).__str__(), fixturesR2_json_F))
    fixturesR2_knockOutMatch_TP = list(map(
        lambda x: knockOutMatch(x['homeTeamName'], x['awayTeamName'], x['result']['goalsHomeTeam'],
                                x['result']['goalsAwayTeam'], x['date']).__str__(), fixturesR2_json_TP))

    rightDownArrow = "\n\n_ _ _ _ _ _          .\n|\n|\n|\n|\n\u2193"
    rightUpArrow = "\u2191\n|\n|\n|\n|\n_ _ _ _ _ _          .\n\n"
    downDownArrow = "\n|\n|\n|\n|\n|\n|\n|\n\u2193"
    upUpArrow = "\u2191\n|\n|\n|\n|\n|\n|\n|"
    #
    r16 = [fixturesR16_knockOutMatch[0], '', fixturesR16_knockOutMatch[1], '', fixturesR16_knockOutMatch[2], '',
           fixturesR16_knockOutMatch[3], '', fixturesR16_knockOutMatch[4], '', fixturesR16_knockOutMatch[5], '',
           fixturesR16_knockOutMatch[6], '', fixturesR16_knockOutMatch[7]
           ]
    qf = [rightDownArrow, fixturesR8_knockOutMatch_QF[0], rightUpArrow,'',rightDownArrow, fixturesR8_knockOutMatch_QF[1], rightUpArrow,'',rightDownArrow,
              fixturesR8_knockOutMatch_QF[2], rightUpArrow,'',rightDownArrow, fixturesR8_knockOutMatch_QF[3], rightUpArrow
          ]
    sf = ['',rightDownArrow, downDownArrow, fixturesR4_knockOutMatch_SF[0],
          upUpArrow, rightUpArrow, '','','',rightDownArrow, downDownArrow, fixturesR4_knockOutMatch_SF[1],
          upUpArrow, rightUpArrow, ''
          ]
    f = ['', '', '',rightDownArrow, downDownArrow, downDownArrow, downDownArrow,
         fixturesR2_knockOutMatch_F[0],
         upUpArrow, upUpArrow, upUpArrow, rightUpArrow, '', '', ''
         ]

    l_all_matches_transpose = [r16, qf, sf, f]
    l_all_matches = list(zip(*l_all_matches_transpose))

    print('+---------------------------------------------------------------------------------------------------+')
    print('---------------------------------FIFA WORLDCUP 2018 KNOCK-OUT STAGE----------------------------------')
    table = texttable.Texttable()
    table.set_cols_align(["c", "c", "c", "c"])
    table.set_cols_width([22, 22, 22, 22])
    table.set_deco(table.BORDER)
    table.add_rows(l_all_matches, header=False)
    print(table.draw())
    print('---------------------------------created by harleen mann on 30-6-18----------------------------------')

if __name__ == '__main__':
    run(sys.argv[1:])
