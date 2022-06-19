import pandas as pd
import matplotlib.pyplot as plt

from frames import games, info, events

# select all rows that have type 'play' but do not have 'NP' as an event
plays = games.query("type == 'play' & event != 'NP'")

# rename the column headers
plays.columns = ["type", "inning", "team", "player", "count", "pitches", "event", "game_id", "year"]
print(plays)

# remove duplicate at-bat data to calculate plate appearances only
# shift() - shift index by a desired number
# retain the given list of columns
pa = plays.loc[plays["player"].shift() != plays["player"], ["year", "game_id", "inning", "team", "player"]]

# group the data on plate appearances by year, game_id, and team
# label the newly formed column PA for plate appearance count
# convert the resulting GroupBy object back into a DataFrame object
pa = pa.groupby(["year", "game_id", "team"]).size().reset_index(name="PA")

# set the index of events to four columns (year, game_id, team, event_type)
print(events)
events = events.set_index(["year", "game_id", "team", "event_type"])
print(events)

events = events.unstack().fillna(0).reset_index()

print(pa)
print(events)
