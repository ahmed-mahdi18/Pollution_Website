"""this imports the pandas package as a shortcut called pd from the python library"""
import pandas as pd

""" this imports the matplotlib package from python to allow me to graph data"""
import matplotlib.pyplot as plt

""" a variable called workbook is created which stores the excel file i will be graphing"""
workbook1 = "surface-plastic-mass-by-ocean.csv"

""" the pd.read command is used to read in the data from the excel file"""
data = pd.read_csv(workbook1)
""" the data is printed to make sure the program is functioning correctly"""
print(data)

""" this picks the values i need for my graph, the ocean column and  All sizes (total mass) (tonnes) column"""
values = data[["Ocean" , "All sizes (total mass) (tonnes)"]]
print(values)

"""" this graphs the information from the values variable, the x-axis is the ocean names and the
mass of the plastic is assigned the y-axis"""
graph = values.plot.bar(x="Ocean" , y="All sizes (total mass) (tonnes)",rot=0)
"""and finally the plt.show command is used to display the graph"""
plt.show()
