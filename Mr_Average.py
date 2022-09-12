import pandas as pd
import numpy as np

while True:
    # getting user input on year they want to look at
    year = int(input("Input a year from 1991-2022!\n"))
    if not 1991 <= year <= 2022:
        print("Sorry, not a valid year!")
    else:
        # reading csv file of NBA player's stats for the season based on user input
        df = pd.read_csv(
            "NBA Stats 1991-Present/{}_nba_players.csv".format(year))

        # found the mean of all the stats in the dataset and appends it to the bottom
        df.loc['Average'] = df.mean(numeric_only=True)

        # adding the columns for the difference between the players' averages and the average of that stat across the league
        for column_name in df.select_dtypes([np.number]).columns:
            df["Diff" +
                column_name] = abs(df[column_name] - df[column_name]['Average'])

        # dropping difference in year, since it's the same for all players
        df.drop("DiffYear", inplace=True, axis=1)

        # adding up all the difference columns to get a total difference score
        df["TotalDiff"] = df["DiffAge"] + df["DiffG"] + df["DiffGS"] + df["DiffMP"] + df["DiffFG"] + df["DiffFG%"] + df["Diff3P"] + df["Diff3PA"] + df["Diff3P%"] + df["Diff2P"] + df["Diff2PA"] + df["Diff2P%"] + \
            df["DiffeFG%"] + df["DiffFT"] + df["DiffFTA"] + df["DiffFT%"] + df["DiffORB"] + df["DiffDRB"] + \
            df["DiffTRB"] + df["DiffAST"] + df["DiffSTL"] + \
            df["DiffBLK"] + df["DiffTOV"] + df["DiffPF"] + df["DiffPTS"]

        # Top 10 most average players in the NBA
        def mr_Average():
            average = df[df["MP"] >= 15].sort_values(
                "TotalDiff", ascending=True)
            average2 = average.drop(
                'Average').loc[:, average.columns != "Unnamed: 0"]
            print(average2.head(10))

        # Top 10 most unique players in the NBA
        def mr_Unique():
            average = df[df["MP"] >= 15].sort_values(
                "TotalDiff", ascending=False)
            average2 = average.drop(
                'Average').loc[:, average.columns != "Unnamed: 0"]
            print(average2.head(10))

         # outputs list of top 10 scorers in the league
        def top_scorer():
            highest_scoring = df[df["MP"] > 15].sort_values(
                "PTS", ascending=False).head(10)
            print(highest_scoring)

        # outputs the most average scorer PPG-wise in the league
        def mr_AverageScorer():
            average_scoring = df[df["MP"] > 15].sort_values(
                "DiffPTS", ascending=True).head(1)
            print(average_scoring["Player"])

        # create function map to allow function call on user input
        func_map = {'a': mr_Average, 'u': mr_Unique}

        # user input loop
        done = True
        while done == True:
            func_input = input(
                "Type a for the top 10 most average players in the NBA, or type u for the top 10 most unique!\n")

            if func_input.strip() == 'exit':
                print('goodbye!')
                exit()

            if func_input.strip() in func_map.keys():
                func_map[func_input]()
                done = False
            else:
                print("Sorry, not valid input!")
