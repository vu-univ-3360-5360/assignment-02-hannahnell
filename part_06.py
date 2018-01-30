# datadotworld module has been imported as dw
import datadotworld as dw

# We've written a SPARQL query for you and assigned it to the `sparql_query` variable: 
sparql_query = "PREFIX GOT: <https://tutorial.linked.data.world/d/sparqltutorial/> SELECT ?FName ?LName WHERE {?person GOT:col-got-house \"Stark\" . ?person GOT:col-got-fname ?FName . ?person GOT:col-got-lname ?LName .}"

# Use the pre-defined SPARQL query to query dataset http://data.world/tutorial/sparqltutorial and return the results to a queryResults variable
queryResults = dw.query('http://data.world/tutorial/sparqltutorial', sparql_query, query_type='sparql')

# Use the dataframe property of the resulting query to create a dataframe variable named `houseStark`
houseStark = queryResults.dataframe

# Use pp.pprint() to print the dataframe to the screen.
pp.pprint(houseStark)

# Import the datadotworld module as dw and the sys module
import datadotworld as dw
import sys

# Import a dataset
refugee_dataset = dw.load_dataset('nrippner/refugee-host-nations')

# Get the size of the dataset:
sys.getsizeof(refugee_dataset)

# List all of the data files:
dataframes = refugee_dataset.dataframes
for df in dataframes:
    pp.pprint(df)
    
# print all of the files in a dataset:
resources = refugee_dataset.describe()['resources']
pp.pprint('name:')
for r in resources:
    pp.pprint(r['name'])
pp.pprint('\ntype of file:')
for r in resources:
    pp.pprint(r['format'])
