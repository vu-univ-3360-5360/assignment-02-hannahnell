# datadotworld module has been imported as dw
import datadotworld as dw

## Complete the SQL query to select all rows from the `unhcr_all` table where `Year` equals 2010. Assign the query string to a `sql_query` variable.
sql_query = "SELECT * FROM `unhcr_all` WHERE Year = 2010"

## Use the `query` method of the datadotworld module to run the `sql_query` against the `https://data.world/nrippner/refugee-host-nations` dataset. Assign the results to a `query2010` variable.
query2010 = dw.query('https://data.world/nrippner/refugee-host-nations', sql_query)

## Use the dataframe property of the resulting query to create a dataframe variable named `unhcr2010`
unhcr2010 = query2010.dataframe

## Print the first 5 rows using the head method.
pp.pprint(unhcr2010.head(5))
