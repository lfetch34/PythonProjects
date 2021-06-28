# Luke Fetchko
# CSCI U236 -- Dr. Wooster
# This program goes out to basketballnoise.com and parses the correct tables containg player heights using pandas,
# and then appends these heights to a list, then the raw heights data is processed by converting to inches,
# and appended to a list height_in_inches. Then the program will write to a file named nba2020.txt all of the heights in inches of every NBA player, one height per line.
# Helped with scraping technique from https://stackoverflow.com/questions/6325216/parse-html-table-to-python-list

# Demonstration of running benford.py with nba2020.txt
# We can see that there are no player heights in inches that start with 1,2,3,4,5, or 9
# This does not conform to Benford's Law as the chance of each digit appearing is not equal.
# All of the first digits of the heights in inches are between 6 and 8.
# This data set is not ideal to analyze with Benford's Law and Benford's Law is not applicable for this data.

#Digit	Count	Percent
#1	0	0.0
#2	0	0.0
#3	0	0.0
#4	0	0.0
#5	0	0.0
#6	2	0.38
#7	321	61.03
#8	203	38.59
#9	0	0.0
#Total	526	100.0


# Import pandas
import pandas as pd
# Provide URL of website to scrape
url = r'https://basketballnoise.com/nba-players-height-2019-2020/'
# Returns list of all tables on page
tables = pd.read_html(url)
# Create heights list
heights = []
# Iterate through tables of all 30 NBA teams and heights column and append to heights list
for i in range(1,31):
    for j in range(1,len(tables[i][1])):
        heights.append(tables[i][1][j])
# Create list for heights in inches
heights_in_inches = []
# iterate though heights list and convert to inches, append to heights in inches list
for i in range(len(heights)):
    heights_in_inches.append((12 * int(heights[i][0])) + int(heights[i][2:]))
# open file for writing with context manager, iterate through heights in inches list and write to file if not blank, one on each line
with open('nba2020.txt','w') as file:
    for item in heights_in_inches:
        if item != '':
            file.write('%s\n' % item)
