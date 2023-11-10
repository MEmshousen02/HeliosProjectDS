import pandas as pd
import matplotlib.pyplot as plt
#allows me to make the nice chart in output
from IPython.display import display

# getting the data from the csv file
DataFourtoFive = pd.read_csv("/Users/joshuahernandez/Documents/GitHub/HeliosProjectDS/Solar_flare_RHESSI_2004_05.csv")
display(DataFourtoFive)

batchMaxSize = 4
overlap = 2

# Creates an array to store the batches of DataFrames
dataframes = []
#Gets max value of Data4to5
max_month = DataFourtoFive['month'].max()

# Go through the data and create batches
for start_month in range(1, max_month - batchMaxSize + 2, batchMaxSize - overlap):
    end_month = start_month + batchMaxSize - 1
    #code below will create a batch within the parameters of endmonth and startmonth
    batch = DataFourtoFive[(DataFourtoFive['month'] >= start_month) & (DataFourtoFive['month'] <= end_month)]
    dataframes.append(batch)

# Displaying all dataframes to make sure they all work
display(dataframes[0])
# display(dataframes[1])
# display(dataframes[2])
# display(dataframes[3])
# display(dataframes[4])
# print(len(dataframes))

#plot data in xy coordinates 
scatter = dataframes[0].plot.scatter(x="x.pos.asec", y="y.pos.asec")
plt.show(scatter)

#create for loop to make graphs for all batches
for df in dataframes:
    scatter = df.plot.scatter(x="x.pos.asec", y="y.pos.asec")
    plt.show(scatter)