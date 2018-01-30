# datadotworld module has been imported as dw
import datadotworld as dw

# We've loaded two datasets to use
int_dataset = dw.load_dataset('https://data.world/jonloyens/intermediate-data-world')
fipsCodes_dataset = dw.load_dataset('https://data.world/uscensusbureau/fips-state-codes')

# Create two dataframes: police_shootings from the 'fatal_police_shootings_data' table of int_dataset and state_abbrvs, from the 'statesfipscodes' table of fipsCodes_dataset
police_shootings = int_dataset.dataframes['fatal_police_shootings_data']
state_abbrvs = fipsCodes_dataset.dataframes['statesfipscodes']

## Merge the two datasets together on the state and stusab fields. Assign to a merged_dataframe variable.
merged_dataframe = police_shootings.merge(state_abbrvs, how = 'left', left_on = 'state', right_on='stusab')

## Add a 'citystate' column to the merged_dataframe dataframe, populating it with the concatinated values from the 'city' and 'state_name' columns, separated by ', '. 
merged_dataframe["citystate"] = merged_dataframe["city"] + ", " + merged_dataframe["state_name"]

## Print head of merged_dataframe
pp.pprint(merged_dataframe.head(5))
