# Data Instruction
The instruction of the datasets is as below.

## Data Source
The data was scraped from the following urls.
* Match history data: https://www.famulei.com/data/team
* Player data: https://www.wanplus.com/lol/playerstats

## Data Files:
1. Player Data.csv: processed players' KPI data which is scrapted from https://www.wanplus.com/lol/playerstats.
2. Game History.csv: processed game history data which is scrapted from https://www.famulei.com/data/team.
3. Team Data.csv: processed data reflecting team information (including KPIs of players in the team).
4. Mapping Dataset.csv: mapped data so that convert from "team vs team" relationship in each game history to "5 players vs 5 players" relationship.
5. Confusion Matrix Analysis.csv: the confusion matrix data of 3 models (before tuning and after tuning).

## Special Fields Instruction
1. Mapping Dataset.csv:

"Result" field

Value  | Meaning
------------- | -------------
0  | Team 1 lose
1  | Team 1 win
