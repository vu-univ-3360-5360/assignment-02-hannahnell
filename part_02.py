# Import the datadotworld module as dw
import datadotworld as dw

# Import the city council votes dataset
dataset = dw.load_dataset("https://data.world/stephen-hoover/chicago-city-council-votes")

# Use describe() to review all the metadata that is downloaded with the dataset. 
# Print it to the screen using pp.pprint().
pp.pprint(dataset.describe())

# Use describe() again to get a description of a specific resource: alderman_votes. Print it to the screen.
pp.pprint(dataset.describe("alderman_votes"))

alderman_votes = dataset.describe("alderman_votes")

# The datadotworld module and dataset have already been loaded for you:
import datadotworld as dw
dataset = dw.load_dataset('https://data.world/stephen-hoover/chicago-city-council-votes')

# Use the dataframes property to assign the alderman_votes table to the variable votes_dataframe.
votes_dataframe = dataset.dataframes['alderman_votes']

# Use the pandas shape property to get rows/columns size for the `votes_dataframe` dataframe.
pp.pprint(votes_dataframe.shape)

# Use the pandas head function to print the first 3 rows of the `votes_dataframe` dataframe.
pp.pprint(votes_dataframe.head(3))
