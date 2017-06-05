# Project Documentation

# Task 1
* Data retrieved from http://climate.weather.gc.ca on Jun 5th, 2017, regarding the annual temperatures of 2015 for 3 cities in Canada: Montreal, Victoria and Ottawa (downloaded in .csv files).
* In order to obtain the correct data to create the plots showing the annual cycle of min/max daily temperatures for each city, the required information was compiled in one .csv file containing the days, min/max daily temperatures and the cumulative GDD (growing degree days) for each city. Each .scv file was used to create 2 plots: 1) the annual min/max daily temperatures and 2) the cumulative GDD.
* To take the arguments to calculate the GDD by using the 'tbase' and 'tupper', a script .py file was created named check
  * $ gdd temperatures.csv tbase tupper
  * store output
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
