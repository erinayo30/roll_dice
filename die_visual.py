import plotly.express as px
from die import Die


# create a D6
die= Die()
# Make some rolls, and store results in a list
results= []
for roll_num in range(1000):
    result = die.roll()
    results.append(result)

# Analyze the results.
frequencies= []
pos_results = range(1, die.num_sides+1)
for value in pos_results:
    frequency = results.count(value)
    frequencies.append(f"{value} appears {frequency}")

# print(frequencies)
#
# print(results)
# Visualize the results
fig = px.bar(x=pos_results, y= frequencies,)
fig.show()