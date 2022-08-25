import pandas as pd
import numpy as np

# reading csv file of NBA player's stats for the 2021-22 season
df = pd.read_csv("nba_players_2022.csv")

# found the mean of all the stats in the dataset
#mean_df = df.mean()


# outputs list of top 10 scorers in the league for 2021-22
def top_scorer():
    highest_scoring = df[df["G"] > 50].sort_values(
        "PTS", ascending=False).head(10)
    print(highest_scoring)

# outputs the most average scorer PPG-wise in the league


def mr_AverageScorer():
    average_scoring = df[df["G"] > 50].sort_values(
        "DiffPTS", ascending=True).head(1)
    print(average_scoring["Player"])


df['DiffAge'] = abs(df["Age"] - df["Age"][605])
df['DiffG'] = abs(df["G"] - df["G"][605])
df['DiffGS'] = abs(df["GS"] - df["GS"][605])
df['DiffMP'] = abs(df["MP"] - df["MP"][605])
df['DiffFG'] = abs(df["FG"] - df["FG"][605])
df['DiffFGA'] = abs(df["FGA"] - df["FGA"][605])
df['DiffFG%'] = abs(df["FG%"] - df["FG%"][605])
df['Diff3P'] = abs(df["3P"] - df["3P"][605])
df['Diff3PA'] = abs(df["3PA"] - df["3PA"][605])
df['Diff3P%'] = abs(df["3P%"] - df["3P%"][605])
df['Diff2P'] = abs(df["2P"] - df["2P"][605])
df['Diff2PA'] = abs(df["2PA"] - df["2PA"][605])
df['Diff2P%'] = abs(df["2P%"] - df["2P%"][605])
df['DiffeFG%'] = abs(df["eFG%"] - df["eFG%"][605])
df['DiffFT'] = abs(df["FT"] - df["FT"][605])
df['DiffFTA'] = abs(df["FTA"] - df["FTA"][605])
df['DiffFT%'] = abs(df["FT%"] - df["FT%"][605])
df['DiffORB'] = abs(df["ORB"] - df["ORB"][605])
df['DiffDRB'] = abs(df["DRB"] - df["DRB"][605])
df['DiffTRB'] = abs(df["TRB"] - df["TRB"][605])
df['DiffAST'] = abs(df["AST"] - df["AST"][605])
df['DiffSTL'] = abs(df["STL"] - df["STL"][605])
df['DiffBLK'] = abs(df["BLK"] - df["BLK"][605])
df['DiffTOV'] = abs(df["TOV"] - df["TOV"][605])
df['DiffPF'] = abs(df["PF"] - df["PF"][605])
df['DiffPTS'] = abs(df["PTS"] - df["PTS"][605])

df["TotalDiff"] = df["DiffAge"] + df["DiffG"] + df["DiffGS"] + df["DiffMP"] + df["DiffFG"] + df["DiffFG%"] + df["Diff3P"] + df["Diff3PA"] + df["Diff3P%"] + df["Diff2P"] + df["Diff2PA"] + df["Diff2P%"] + \
    df["DiffeFG%"] + df["DiffFT"] + df["DiffFTA"] + df["DiffFT%"] + df["DiffORB"] + df["DiffDRB"] + \
    df["DiffTRB"] + df["DiffAST"] + df["DiffSTL"] + \
    df["DiffBLK"] + df["DiffTOV"] + df["DiffPF"] + df["DiffPTS"]

# Top 10 most average players in the NBA


def mr_Average():
    average = df[df["G"] > 50].sort_values(
        "TotalDiff", ascending=True)
    average2 = average.loc[:, average.columns != "Unnamed: 0"]
    print(average2.head(10))


# Top 10 most unique players in the NBA
def mr_Unique():
    average = df[df["G"] > 50].sort_values(
        "TotalDiff", ascending=False)
    average2 = average.loc[:, average.columns != "Unnamed: 0"]
    print(average2.head(10))


# create function map to allow function call on user input
func_map = {'a': mr_Average, 'u': mr_Unique}

# user input loop
while True:
    func_input = input(
        "Type a for the top 10 most average players in the NBA, or type u for the top 10 most unique!\n")

    if func_input.strip() == 'exit':
        print('goodbye! ')
        exit()

    if func_input.strip() in func_map.keys():
        func_map[func_input]()
    else:
        print("Sorry no function for that!")
