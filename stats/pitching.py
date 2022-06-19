import pandas as pd
import matplotlib.pyplot as plt
from data import games

# shortcut for finding rows with "play" in the type column
# dataframe with only plays data
plays = games[games["type"] == "play"]

# shortcut to select all plays with strikeouts in the event column
strike_outs = plays[plays["event"].str.contains("K")]
print(strike_outs.head(10))

# groups the strikeouts data by year and game_id
# will create a new unlabeled column representing the number of strikeouts
# returns a DataFrameGroupBy object
strike_outs = strike_outs.groupby(["year", "game_id"]).size()

# convert the GroupBy object back into a DataFrame object
# assign the newly formed column with given column name
strike_outs = strike_outs.reset_index(name="strike_outs")




print(strike_outs)
