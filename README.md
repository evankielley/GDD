# Growing Degree Days in Canada - Data Project

* This project aimed to gain experience with computational workflow for a scientific problem in which data was retrived from the Historial Climate Data from the Government of Canada to calculate the growing degree days (GDD) in three cities: Montreal, Ottawa and Victoria. The GDD is a heat index (heat accumulation) that describes the best timing of biological process such as when a crop will reach maturity, when a flower will bloom, or even when animals will migrate. It is calculated through the formula GDD = [(Tmax + Tmin)/2] - Tbase, in which Tmax and Tmin are the daily maximum and minimum temperatures, and Tbase is the base temperature. Calculations where made according to the second method, described in [1].

## Presentation
https://evankielley.github.io/GDD/Presentation/presentation.html#1

## Build
* The entire workflow of this project is done by calling 'Make all', which will run the Makefile and all the scripts to generate the output required. 

## Task 1
* The data retrieved from http://climate.weather.gc.ca on Jun 5th, 2017, contains the annual temperatures of 2015 for 3 cities in Canada: Montreal, Victoria and Ottawa (downloaded as 2015_city_temp.csv files).
* The .csv files contain extra information that are not used in this task. Therefore, we created a script file called gdd.py to run the data from the .csv files into more readable and useful information to create the plots, thus containing only the days, min/max daily temperatures and the cumulative GDD (growing degree days) already calculated for each city. These files were then named 2015_city_gdd.csv. The data obtained was used to create plots showing the annual cycle of min/max daily temperatures for each city and the accumulation GDD. The files obtained when using the gdd.py script were also used to calculate the GDD by calling the 'tbase' and 'tupper' as arguments that were set up to be 10 and 30, respectively.  
  * $ gdd temperatures.csv tbase tupper
  * store output
* The script create_plots.py was used to create the plots for max and min temperatures for each city and the accumulated GDD. In the former, we compared the temperatures for all cities represented in 3 plots of min and max temperatures for each city (figures are found in Plots folder named 'CompareMaxMinTemp'). Moreover, the accumulate GDD is shown in one plot for the 3 cities (also found in Plots folder, figure named CumulativeGDD).

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

## References
* (1) Growing degree-days: one equation, two interpretations http://digitalcommons.unl.edu/cgi/viewcontent.cgi?article=1086&context=usdaarsfacpub 


