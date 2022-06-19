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

# plot the attendance data as a bar graph
# figsize=(width, height) - inches
attendance.plot(x="year", y="attendance", figsize=(15,7), kind="bar")

# add labels to the axis
plt.xlabel("Year")
plt.ylabel("Attendance")

# add a horizontal dashed green line to represent the mean of the attendance data
# plt.axhline(y-position of line, label, linestyle, color)
plt.axhline(y=attendance["attendance"].mean(), label="Mean", linestyle="--", color="green")

# display the bar graph of attendance data
plt.show()



