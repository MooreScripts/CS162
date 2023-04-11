import matplotlib.pyplot as plot
# Setting up list data that forms the pie chart
numlist = [2, 2, 3, 4, 3]
namelist = ['Tauren', 'Orc', 'Undead', 'Troll', 'Blood Elf']
colorlist = ['brown', 'green', 'grey', 'yellow', 'red']
explodelist = [0.2, 0.0, 0.0, 0.0, 0.1]
# Create pie chart with plot.pie()
plot.pie(numlist, labels=namelist, autopct='%d%%', colors=colorlist, explode=explodelist, startangle=90)
# Set axis to equal which forms a circular graph
plot.axis('equal')
# Set a title for the graph that's not attached to anything
plot.title('Horde race distribution in wow classic')
# Display the plot
plot.show()
# Save the plot as a .png
plot.savefig('piechart.png')