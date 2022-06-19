import pandas as pd
import matplotlib.pyplot as plt
from data import games

# select the rows with "play" in the type column
plays = games[games["type"] == "play"]

# rename the column headers
plays.columns = ["type", "inning", "team", "player", "count", "pitches", "event", "game_id", "year"]

# retrieve all the hits data that matches the given regex and get the inning and event columns
hits = plays.loc[plays["event"].str.contains('^(?:S(?!B)|D|T|HR)'), ["inning", "event"]]

# convert the values in the inning column from string to number
hits.loc[:, "inning"] = pd.to_numeric(hits.loc[:, "inning"])

# create a dictionary for the type of hits
replacements = {
    r'^S(.*)': 'single',
    r'^D(.*)': 'double',
    r'^T(.*)': 'triple',
    r'^HR(.*)': 'hr'
}

# replace the values in the event column with the predefined replacements
# returns a DataFrame object
hit_type = hits['event'].replace(replacements, regex=True)

print(hit_type)