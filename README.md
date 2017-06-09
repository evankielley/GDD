# Project Documentation
Presentation: https://evankielley.github.io/GDD/Presentation/presentation.html#1
## Build
* Add info about makefile

## Task 1
* The data was retrieved from http://climate.weather.gc.ca on Jun 5th, 2017, containing the annual temperatures of 2015 for 3 cities in Canada: Montreal, Victoria and Ottawa (downloaded as 2015_city_temp.csv files).
* These .csv files contain extra information that are not used in this task. Therefore, we created a script file called gdd.py to run the data from the .csv files into more readable and useful information for the plots, thus containing only the days, min/max daily temperatures and the cumulative GDD (growing degree days) calculated for each city. These files were then named 2015_city_gdd.csv. The data obtained was used to create plots showing the annual cycle of min/max daily temperatures for each city and the GDD for example. The files obtained when using the gdd.py script were also used to calculate the GDD by calling the 'tbase' and 'tupper' as arguments. 
  * $ gdd temperatures.csv tbase tupper
  * store output
* The script **Temperature_plots.py** was used to create the plots for max and min temperatures for each city (figures are found in Plots folder named 'ThreeCitiesAnnualTemp'). We also compared the temperatures for all cities represented in one graph of min and other graph for the max temperatures (figures are found in Plots folder named 'CompareMaxMinTemp'). Moreover, the accumulate GDD is shown in one plot for the 3 cities (also found in Plots folder, figure named CumulativeGDD).

* Create plots showing accumulated GDD vs time for selected cities like: 
![alt text](https://github.com/evankielley/GDD/blob/master/Plots/CumulativeGDD.png)
* LaTeX report
* Web based presenation
  * include the HTML link
  * Host your presenation on a gh-pages branch of GitHub.
* Implement your entire workflow as a Makefile - this will be in the begining 
* Create a test suite.

## Task 2

## Final Task


