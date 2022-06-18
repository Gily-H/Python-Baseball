import os
import glob  # file path recognition module
import pandas as pd

# collect all files with the corresponding naming format
game_files = glob.glob(os.path.join(os.getcwd(), "games", "*.EVE"))

# sort the files in place
game_files.sort()

game_frames = [];

# loop through each game file
for game_file in game_files:
    game_frame = pd.read_csv(game_file, names=["type", "multi2", "multi3", "multi4", "multi5", "multi6", "event"])
    game_frames.append(game_frame)

games = pd.concat(game_frames)


