import pandas as pd
import matplotlib.pyplot as plt

from frames import games, info, events

# select all rows that have type 'play' but do not have 'NP' as an event
plays = games.query("type == 'play' & event != 'NP'")

# rename the column headers
plays.columns = ["type", "inning", "team", "player", "count", "pitches", "event", "game_id", "year"]

# remove duplicate at-bat data to calculate plate appearances only
# shift() - shift index by a desired number
# retain the given list of columns
pa = plays.loc[plays["player"].shift() != plays["player"], ["year", "game_id", "inning", "team", "player"]]

# group the data on plate appearances by year, game_id, and team
# label the newly formed column PA for plate appearance count
# convert the resulting GroupBy object back into a DataFrame object
pa = pa.groupby(["year", "game_id", "team"]).size().reset_index(name="PA")

# set the index of events to four columns (year, game_id, team, event_type)
events = events.set_index(["year", "game_id", "team", "event_type"])

# unstack the events data back into a table view and fill empty values with 0
events = events.unstack().fillna(0).reset_index()

print(events)  # before column level drop
# drop a layer of column names
events.columns = events.columns.droplevel()

# rename the column headers
events.columns = ["year", "game_id", "team", "BB", "E", "H", "HBP", "HR", "ROE", "SO"]
events = events.rename_axis(None, axis="columns")

# merge the plate appearances with the events - both DataFrames have similar columns
events_plus_pa = pd.merge(events, pa, how="outer", left_on=["year", "game_id", "team"],
                          right_on=["year", "game_id", "team"])

# merge in DataFrame "info" containing data on which team was the home team and which was the away team
defense = pd.merge(events_plus_pa, info)

# calculate the DER - Defensive Efficiency Ratio into a new column for every row
defense.loc[:, "DER"] = 1 - ((defense["H"] + defense["ROE"]) / (
            defense["PA"] - defense["BB"] - defense["SO"] - defense["HBP"] - defense["HR"]))

# convert the values in the year column from string to number
defense.loc[:, "year"] = pd.to_numeric(defense["year"])

# retrieve the der data within the past 40 years
der = defense.loc[defense["year"] >= 1978, ["year", "defense", "DER"]]

# adjust data for plotting
der = der.pivot(index="year", columns="defense", values="DER")

# display the DER data using a line plot
# x_compat - suppress the default tick behavior
der.plot(x_compat=True, xticks=range(1978, 2018, 4), rot=45)
plt.xlabel("Year")
plt.ylabel("Defensive Efficiency Ratio")
plt.show()

print(der)
