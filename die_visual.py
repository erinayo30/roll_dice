import plotly.express as px
from die import Die
import plotly.io as pio


pio.renderers.default = "browser"


# create a D6
die_1= Die()
die_2 =Die()
# Make some rolls, and store results in a list
results= []
for roll_num in range(1000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

# Analyze the results.
frequencies= []
max_results = die_1.num_sides + die_2.num_sides
pos_results = range(2,max_results+1)
for value in pos_results:
    frequency = results.count(value)
    frequencies.append(frequency)

# print(frequencies)
#
# print(results)
# Visualize the results
title= "Results of Rolling Two D6 1,000 Times"
labels= {'x': "Results", "y": "Frequency of results"}
fig = px.bar(x=pos_results, y= frequencies, title=title, labels=labels)
fig.show(renderer="browser")
fig.write_html("dice_results.html", auto_open=True)