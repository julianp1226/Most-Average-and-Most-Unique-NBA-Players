import pandas as pd

while True:
    # getting user input on year they want to look at
    year = int(input("Input a year from 1991-2022!\n"))
    if not 1991 <= year <= 2022:
        print("Sorry, not a valid year!")
    else:
        # reading csv file of NBA player's stats for the season based on user input
        df = pd.read_csv("NBA Stats 1991-2022/{}_nba_players.csv".format(year))

        # found the mean of all the stats in the dataset and appends it to the bottom
        df.loc['Average'] = df.mean(numeric_only=True)

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

        # calculating the differences in each players stat and the average of that stat across the league
        df['DiffAge'] = abs(df["Age"] - df["Age"]['Average'])
        df['DiffG'] = abs(df["G"] - df["G"]['Average'])
        df['DiffGS'] = abs(df["GS"] - df["GS"]['Average'])
        df['DiffMP'] = abs(df["MP"] - df["MP"]['Average'])
        df['DiffFG'] = abs(df["FG"] - df["FG"]['Average'])
        df['DiffFGA'] = abs(df["FGA"] - df["FGA"]['Average'])
        df['DiffFG%'] = abs(df["FG%"] - df["FG%"]['Average'])
        df['Diff3P'] = abs(df["3P"] - df["3P"]['Average'])
        df['Diff3PA'] = abs(df["3PA"] - df["3PA"]['Average'])
        df['Diff3P%'] = abs(df["3P%"] - df["3P%"]['Average'])
        df['Diff2P'] = abs(df["2P"] - df["2P"]['Average'])
        df['Diff2PA'] = abs(df["2PA"] - df["2PA"]['Average'])
        df['Diff2P%'] = abs(df["2P%"] - df["2P%"]['Average'])
        df['DiffeFG%'] = abs(df["eFG%"] - df["eFG%"]['Average'])
        df['DiffFT'] = abs(df["FT"] - df["FT"]['Average'])
        df['DiffFTA'] = abs(df["FTA"] - df["FTA"]['Average'])
        df['DiffFT%'] = abs(df["FT%"] - df["FT%"]['Average'])
        df['DiffORB'] = abs(df["ORB"] - df["ORB"]['Average'])
        df['DiffDRB'] = abs(df["DRB"] - df["DRB"]['Average'])
        df['DiffTRB'] = abs(df["TRB"] - df["TRB"]['Average'])
        df['DiffAST'] = abs(df["AST"] - df["AST"]['Average'])
        df['DiffSTL'] = abs(df["STL"] - df["STL"]['Average'])
        df['DiffBLK'] = abs(df["BLK"] - df["BLK"]['Average'])
        df['DiffTOV'] = abs(df["TOV"] - df["TOV"]['Average'])
        df['DiffPF'] = abs(df["PF"] - df["PF"]['Average'])
        df['DiffPTS'] = abs(df["PTS"] - df["PTS"]['Average'])

        # calculating the total difference score of each player
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
