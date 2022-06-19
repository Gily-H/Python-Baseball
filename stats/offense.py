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

# assign a new column to the DataFrame
# column names are the keywords - columnName=ColumnData
hits = hits.assign(hit_type=hit_type)

# group the hits data by the inning and type of hit
# groupby() - returns a GroupBy object with a new column representing the count for each hit
# reset_index() - convert the GroupBy object back into a DataFrame and label the new column as count
hits = hits.groupby(["inning", "hit_type"]).size().reset_index(name="count")

# convert the hit type to Categorical to save memory - provide a list of the 4 hit type categories
hits["hit_type"] = pd.Categorical(hits["hit_type"], ["single", "double", "triple", "hr"])

# sort the data by inning and hit type
hits = hits.sort_values(["inning", "hit_type"])

# reshape hits dataframe for plotting
hits = hits.pivot(index="inning", columns="hit_type", values="count")

# display the hits data as a stacked bar graph
hits.plot.bar(stacked=True)
plt.xlabel("Innings")
plt.ylabel("Total Hits")
plt.show()

print(hits)
