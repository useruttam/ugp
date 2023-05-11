import numpy as np
import csv

# Open the CSV file and read the data into a numpy array
with open('Book1.csv', 'r') as f:
    reader = csv.reader(f)
    data = np.array(list(reader)).astype(float)

# Calculate the standard deviation of each column
std_devs = np.std(data, axis=0)

# Append the standard deviations to the CSV file
with open('Book1.csv', 'a', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Standard deviations:'] + list(std_devs))