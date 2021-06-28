# Luke Fetchko
# CSCI U236 -- Dr. Wooster
# Program 06 -- Pandas
# Hours invested: 7-8
# Status of program: Runs as expected and computes wanted data according to assignment instructions
# Problems encountered: When creating DataFrames while excluding the price of 0, at first I tried to just use DataFrame.price != 0, but I realized for some columns it was not working correctly,
# and I needed to wrap it with pd.to_numeric in order to actually compare the integer values of the price for the conditional.
# Another issue came up when trying to use sum() without wrapping the series in pd.to_numeric, I was getting an invalid operand for the + operator error.
# I took a long time to figure out how to approach the last question we needed to answer, but it finally became clear that I could solve the last problem using a nested for loop
# with the unique values for manufacturers and fuel types.

import pandas as pd
import numpy as np

# create fields list for needed columns
fields = ['price','manufacturer','cylinders','fuel','odometer','type']
# read csv file into DataFrame with only necessary columns
df = pd.read_csv('/Users/lukefetchko/Desktop/vehicles.csv',usecols = fields,dtype=object)
# create DataFrame with all 6 cylinder vehicles
df_six_cyl = df[df.cylinders == "6 cylinders"]
# create Series for odometer readings with NaN values for odometer dropped
odometer_series = df_six_cyl['odometer'].dropna()
# calculate average by summing the odometer Series and dividing by size of the odometer Series, round to two decimal places
avg_odometer = round(pd.to_numeric(odometer_series).sum() / odometer_series.size, 2)
# print average odometer reading for six cylinder vehicles
print("Average odometer reading for six cylinder vehicles: " + str(avg_odometer))
print()


# create DataFrame with all SUV vehicles
df_SUVs = df[df.type == "SUV"]
# create DataFrame with all SUV vehicles which do not have a price of 0
df_prices = df_SUVs[pd.to_numeric(df_SUVs.price) != 0]
# create Series for SUV prices
prices_series = df_prices['price']
# calculate average by summing the prices Series and dividing by size of prices Series, round to two decimal places
avg_SUV_price = round(pd.to_numeric(prices_series).sum() / prices_series.size, 2)
# print average SUV price
print("Average SUV price: " + str(avg_SUV_price))
print()

# create DataFrame with all pickup and truck vehicles
df_pickups_trucks = df[(df.type == "pickup") | (df.type == "truck")]
# create DataFrame with all pickup and truck vehicles which do not have a price of 0
df_pickupstrucks_prices = df_pickups_trucks[pd.to_numeric(df_pickups_trucks.price) != 0]
# create Series for pickup and truck prices
pickupstrucks_prices_series = df_pickupstrucks_prices['price']
# calculate average by summing the pickup and truck prices Series and dividing by size of pickup and truck prices series, round to two decimal places
avg_pickupstrucks_price = round(pd.to_numeric(pickupstrucks_prices_series).sum() / pickupstrucks_prices_series.size, 2)
# print average pickup/truck price
print("Average pickup/truck price: " + str(avg_pickupstrucks_price))
print()

# create DataFrame with all vehicles that do NOT have null values for manufacturer and fuel type
df_manufacturers_fuel_notnull = df[(df.manufacturer.notnull()) & (df.fuel.notnull())]
# create DataFrame that contains only the manufacturer and fuel columns from df_manufacturers_fuel_notnull
df_manufacturers_to_fuel = df_manufacturers_fuel_notnull[['manufacturer','fuel']]
# outer loop iterates through unique values of sorted manufacturer column
for i in df_manufacturers_to_fuel.sort_values(by=['manufacturer'])['manufacturer'].unique():
    # inner loop iterates through unique values of sorted fuel type column
    for j in df_manufacturers_to_fuel.sort_values(by=['fuel'])['fuel'].unique():
        # check if length of specific DataFrame containg matching manufacturer and fuel type values from loops is greater than 0 (means at least one vehicle for that manufacturer and fuel type)
        if len(df_manufacturers_to_fuel[(df_manufacturers_to_fuel.manufacturer == str(i)) & (df_manufacturers_to_fuel.fuel == str(j))]) > 0:
            # if so, print the manufacturer name, the name of the fuel type, and the number of vehicles for the specific manufacturer and fuel type
            print("Manufacturer: " + str(i) + " | Fuel Type: " + str(j) + " | Number of Vehicles: " + str(len(df_manufacturers_to_fuel[(df_manufacturers_to_fuel.manufacturer == str(i)) & (df_manufacturers_to_fuel.fuel == str(j))])))
            print()
