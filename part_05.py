
# datadotworld module has been imported as dw
import datadotworld as dw

## Complete the SQL query to select state, the count of farmers markets (fmid), and average obesity rate from agriculture.`national-farmers-markets`.export, LEFT JOINED against health.`obesity-by-state-2014`.adult_obese on state and location
sql_query = "SELECT state, count(fmid) as count, Avg(obesity.Value) as obesityAvg FROM Export LEFT JOIN health.`obesity-by-state-2014`.`adult_obese` as obesity ON state = obesity.location GROUP BY state ORDER BY count desc"

## Use the `query` method of the datadotworld module to run the `sql_query` against the `https://data.world/agriculture/national-farmers-markets` dataset. Assign the results to a `queryResults` variable.
queryResults = dw.query('https://data.world/agriculture/national-farmers-markets', sql_query)

## Use the dataframes property of the resulting query to create a dataframe variable named `stateStats`
stateStats = queryResults.dataframe

## Plot the stateStats results using state as the x-axis (matplotlib is already imported)
stateStats.plot(x='state')

plt.show()
