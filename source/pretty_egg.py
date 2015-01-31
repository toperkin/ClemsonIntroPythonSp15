import pandas as pd
import matplotlib.pyplot as plt

data = pd.Series.from_csv('price-of-a-dozen-eggs-19001993-i.csv', header=0)

ma = pd.rolling_mean(data, 10, center=True)
mstd = pd.rolling_std(data, 10, center=True)

# You typically want your plot to be ~1.33x wider than tall.
# Common sizes: (10, 7.5) and (12, 9)
plt.figure(figsize=(12, 9))

# Remove the plot frame lines. They are unnecessary chartjunk.
ax = plt.subplot(111)
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

# Ensure that the axis ticks only show up on the bottom and left of the plot.
# Ticks on the right and top of the plot are generally unnecessary chartjunk.
ax.get_xaxis().tick_bottom()
ax.get_yaxis().tick_left()


# Along the same vein, make sure your axis labels are large
# enough to be easily read as well. Make them slightly larger
# than your axis tick labels so they stand out.
plt.ylabel("Price of eggs", fontsize=16)


# Use matplotlib's fill_between() call to create error bars.
# Use the dark blue "#3F5D7D" as a nice fill color.
plt.fill_between(mstd.index, ma-2*mstd, ma+2*mstd, color='#3F5D7D')

# Plot the original data as a white line in between the error bars.
# White stands out best against the dark blue.
plt.plot(data.index, data, color="white", lw=2)


# Make the title big enough so it spans the entire plot, but don't make it
# so big that it requires two lines to show.
plt.title("Price of a dozen eggs by year", fontsize=22)


# Always include your data source(s) and copyright notice! And for your
# data sources, tell your viewers exactly where the data came from,
# preferably with a direct link to the data. Just telling your viewers
# that you used data from the "U.S. Census Bureau" is completely useless:
# the U.S. Census Bureau provides all kinds of data, so how are your
# viewers supposed to know which data set you used?
plt.xlabel("\nData source: https://datamarket.com/data/set/22tq/price-of-a-dozen-eggs-1900-1993-in-constant | "
        "Author: Tony Perkins", fontsize=10)

# Finally, save the figure as a PNG.
# You can also save it as a PDF, JPEG, etc.
# Just change the file extension in this call.
# bbox_inches="tight" removes all the extra whitespace on the edges of your plot.
plt.savefig('pretty-eggs', bbox_inches="tight")
