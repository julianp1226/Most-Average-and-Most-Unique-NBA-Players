# Most-Average-and-Most-Unique-NBA-Players
This Python script finds the top 10 most average NBA players in a season, and the top 10 most unique.
I scraped the player stats for every season from 1991-Present from Basketball Reference using Beautiful Soup.
The notebook for this script is in the repo, just make sure you have Chrome Webdriver for it to work. 
The script first finds the average of all major stat categories for the season that the user inputs. Then, it compares
that average to all of the players' stats that played over 50 games that season. Adding the differences up
creates a total difference score, which is used to rank the players from most average to most unique or vice versa.
