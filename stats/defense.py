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
plate_appearances = plays.loc[
    plays["player"].shift() != plays["player"], ["year", "game_id", "inning", "team", "player"]]

plate_appearances = plate_appearances.groupby(["year", "game_id", "team"]).size().reset_index(name="PA")

print(plate_appearances)
