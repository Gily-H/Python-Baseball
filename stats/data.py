import os
import glob  # file path recognition module
import pandas as pd

# collect all files with the corresponding naming format
game_files = glob.glob(os.path.join(os.getcwd(), "games", "*.EVE"))

# sort the files in place
game_files.sort()

# list of pandas dataframes
game_frames = [];

# loop through each game file
for game_file in game_files:
    # read a csv file into a pandas dataframe
    # names=[list of column headers]
    game_frame = pd.read_csv(game_file, names=["type", "multi2", "multi3", "multi4", "multi5", "multi6", "event"])
    game_frames.append(game_frame) # append the dataframe to a list of dataframes


# create a single large dataframe (games) from the list of dataframes (game_frames)
games = pd.concat(game_frames)

### cleanup data

# select all rows where there is a "??" in the multi5 column
# replace the "??" input with an empty string ""
games.loc[games["multi5"] == "??", "multi5"] = ""

# extract the string values in column multi2 that match the regular expression
identifiers = games["multi2"].str.extract(r'(.LS(\d{4})\d{5})')

# fill empty data (Na/NaN) with the previous valid value
identifiers = identifiers.fillna(method="ffill")

# rename identifier columns
identifiers.columns = ["game_id", "year"]

# append the updated identifiers dataframe to the games dataframe
# axis=1 - concat along the columns
games = pd.concat([games, identifiers], axis=1, sort=False)

# fill empty spaces (Na/NaN) with a literal whitespace
games = games.fillna(" ")

# save memory by making the "type" column Categorical
# passing in : as the condition - selects all rows
games.loc[:, "type"] = pd.Categorical(games.loc[:, "type"])

# print the first 5 rows in the dataframe
print(games.head(5))