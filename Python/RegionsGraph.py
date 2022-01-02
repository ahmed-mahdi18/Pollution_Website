"""this imports the pandas package as a shortcut called pd from the python library"""
import pandas as pd

""" this imports the matplotlib package from python to allow me to graph data"""
import matplotlib.pyplot as plt

""" a variable called workbook is created which stores the excel file i will be graphing"""
workbook1 = "mismanaged-plastic-waste-by-region.csv"

""" the pd.read command is used to read in the data from the excel file"""
data = pd.read_csv(workbook1)
""" the data is printed to make sure the program is functioning correctly"""
print(data)

""" this picks the values i need for my graph, the region column and
Mismanaged plastic waste by region (% global total) (% of global total) column"""
values = data[["Region" , "Mismanaged plastic waste by region (% global total) (% of global total)"]]
print(values)

"""" this graphs the information from the values variable, the x-axis is assigned to the region names and the
percentage of wasted plastic by region is assigned the y-axis"""
graph = values.plot.bar(x="Region" , y="Mismanaged plastic waste by region (% global total) (% of global total)",rot=0)

"""and finally the plt.show command is used to display the graph"""
plt.show()
