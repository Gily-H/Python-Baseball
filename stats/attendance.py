import pandas as pd
import matplotlib.pyplot as plt
from data import games

# find all rows with type "info" and multi2 "attendance"
# save only the year and multi3 columns from the selected rows
attendance = games.loc[(games["type"] == "info") & (games["multi2"] == "attendance"), ["year", "multi3"]]

# change the column header names
attendance.columns = ["year", "attendance"]

# convert the attendance column values from string to number
attendance.loc[:, "attendance"] = pd.to_numeric(attendance.loc[:, "attendance"])

# plot and display the attendance data as a bar graph
# figsize=(width, height) - inches
attendance.plot(x="year", y="attendance", figsize=(15,7), kind="bar")
plt.show()



