# Project Documentation

# Task 1
* Data retrieved from http://climate.weather.gc.ca on Jun 5th, 2017, regarding the annual temperatures of 2015 for 3 cities in Canada: Montreal, Victoria and Ottawa (downloaded in .csv files).
* In order to obtain the correct data to create the plots showing the annual cycle of min/max daily temperatures for each city, the required information was compiled in one .csv file containing the days, min/max daily temperatures and the cumulative GDD (growing degree days) for each city. Each .scv file was used to create 2 plots: 1) the annual min/max daily temperatures and 2) the cumulative GDD.
* To calculate the GDD using the 'tbase' and 'tupper' as arguments, we created a script file called gdd.py to run the data from the .csv files into readable and useful information for the two plots. 
  * $ gdd temperatures.csv tbase tupper
  * store output
* The script Temperature_plots.py was used to create the plots for max and min temperatures for each city (figures are found in Plots folder named 'ThreeCitiesAnnualTemp'). We also compared the temperatures for all cities represented in one graph of min and max temperature (figures are found in Plots folder named 'CompareMaxMinTemp'). Moreover, the accumulate GDD is shown in one plot for the 3 cities.
* Create plots showing accumulated GDD vs time for selected cities like:  
![alt text](http://www.greatnorthwestwine.com/wp-content/uploads/2016/09/walla-walla-valley-gdd-9-1-16.jpg)
* LaTeX report
* Web based presenation
  * The remark-js library is nice for doing HTML based presenations
  * Host your presenation on a gh-pages branch of GitHub.
* Implement your entire workflow as a Makefile
* Create a test suite.
* Your project should include adequate documentation both with your source code and an overall project Readme.md file to explain how to use/build your project
test
