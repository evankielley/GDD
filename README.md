# :octocat: Growing Degree Days in Canada - Data Project 

* This project aimed to gain experience with computational workflow for a scientific problem in which data was retrived from    the Historial Climate Data from the Government of Canada to calculate the growing degree days (GDD) in three cities: Montreal, Ottawa and Victoria. The GDD is a heat index (heat accumulation) that describes the best timing of biological process such as when a crop will reach maturity, when a flower will bloom, or even when animals will migrate. It is calculated through the formula GDD = [(Tmax + Tmin)/2] - Tbase, in which Tmax and Tmin are the daily maximum and minimum temperatures, and Tbase is the base temperature [1].

## Presentation
* To see our presentation online, please click on this [link](https://evankielley.github.io/GDD/Presentation/presentation.html#1).
 
## Build
* The entire workflow of this project is done by calling 'make all', which runs the *Makefile* and all the scripts to generate the outputs required for this project. 

## Primary Tasks
* The data retrieved from http://climate.weather.gc.ca on Jun 5th, 2017, contains the annual temperatures of 2015 for 3 cities in Canada: Montreal, Victoria and Ottawa (downloaded as 2015_city_temp.csv files).
* The .csv files contain extra information that are not used in this task. Therefore, we created a script file called `gdd.py` to run the data from the .csv files into more readable and useful information to create the plots, thus containing only the days, min/max daily temperatures and the cumulative GDD (growing degree days) already calculated for each city. These files were then named 2015_city_gdd.csv. The data obtained was used to create plots showing the annual cycle of min/max daily temperatures for each city and the accumulation GDD. The files obtained when using the `gdd.py` script were also used to calculate the GDD by calling the 'tbase' and 'tupper' as arguments that were set up to be 10 and 30, respectively.  
  * $ gdd temperatures.csv tbase tupper
  
* The script `create_plots.py` was used to create the plots for max and min temperatures for each city and the accumulated GDD. In the former, we compared the temperatures for the three cities represented in 3 plots of min and max temperatures for each city. Moreover, the accumulate GDD is shown in one plot for the 3 cities. Figures are found in the Outputs folder and named as CompareMaxMinTemp and CumulativeGDD, respectively. 

* The plot below is showing the accumulated GDD vs time for selected cities: 
![alt text](https://raw.githubusercontent.com/evankielley/GDD/master/Output/CumulativeGDD.png?token=Abv3GRtFi3qHnLJFDwGDdtJajOOyqtUZks5ZSBtRwA%3D%3D)

## LaTex Report
* The LaTex report generates a PDF file containing the summarized results for this project.

## Test Suite
* When running the script `test_gdd.py` one can test if the calculation for the GDD is working as expected (see Testing folder).

## Secondary Tasks
* *For question 1*: A script called `nl_effective_gdd.py` was created to
* *For question 3*: Importing `calc_gdd.py` script we created another script called `analyze_tbase.py` to calculate GDD using different base temperatures (Tbase = 8, 9, 11, 12) to show how the cumulative growing degree days changes depending on the base temperature chosen. As
* *For questions 4 and 5*: By running the script `bokeh_plots.py`, a html file based in our presentation is created. The scripts `bokeh_serve_tempy.py` and `bokeh_serve_gdd.py` shows interactively the minimum and maximum temperatures and the cumulative GDD for each capital city in Canada in 2015. To run the last two scripts mentioned, one should type in the bash shell 'bokeh serve --show <script's name>'.

## Final Task

## References
* (1) Growing degree-days: one equation, two interpretations http://digitalcommons.unl.edu/cgi/viewcontent.cgi?article=1086&context=usdaarsfacpub 


:octocat:
