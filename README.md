# :octocat: Growing Degree Days in Canada - Data Project :octocat:

This project aimed to gain experience with computational workflow for a scientific problem in which data was retrived from the Historial Climate Data from the Government of Canada to calculate the Growing Degree Days (GDD) in three cities: Montreal, Ottawa and Victoria. The GDD is a heat index (heat accumulation) that describes the best timing of biological process such as when a crop will reach maturity, when a flower will bloom, or even when animals will migrate. It is calculated through the formula GDD = [(T<sub>max</sub> + T<sub>min</sub>)/2] - T<sub>base</sub>, in which T<sub>max</sub> and T<sub>min</sub> are the daily maximum and minimum temperatures, and T<sub>base</sub> is the base temperature [1].

## Installation Instructions 
The entire workflow of this project is done by calling 'make all', which runs the *Makefile* and all the scripts to generate the outputs required for this project. 
1. Clone this repo.
2. In the bash shell:
```
make clean
make all

```
## Primary Tasks
* The data retrieved from [Climate Weather Canada](http://climate.weather.gc.ca) on Jun 5th, 2017, contains the annual temperatures of 2015 for 3 cities in Canada: Montreal, Victoria and Ottawa (downloaded as 2015_city_temp.csv files).
* The .csv files contain extra information that are not necessary in this task. Therefore, we created the script `gdd.py` to run the data from the .csv files into more readable and useful information. The output files generated contain only the days, min/max daily temperatures and the cumulative GDD (growing degree days) which are already calculated for each city. These files were named 2015_city_10_30_gdd.csv (found in the Outputs folder). The data obtained was used to create plots showing the annual cycle of min/max daily temperatures for each city and the accumulation GDD. The files obtained when using the `gdd.py` script were also used to calculate the GDD by calling the 'tbase' and 'tupper' as arguments that were set up to be 10 and 30, respectively. 
```
gdd temperatures.csv tbase tupper
``` 
* The script `create_plots.py` is used to create all the plots in this project. Therefore, everytime that both scripts `gdd.py` and `create_plots.py` run, the script `calc_gdd.py` is used as a module/tool to calculate the GDD. The script `create_plots.py` also requires another script to run called `station_info.py`, in which has the stations IDs defined for each city.  
* For this task, 4 plots created are shown in 2 figures: 1) 3 plots showing the max and min temperatures for each city and 2) 1 plot showing the accumulated GDD for the three cities.  Figures are found in the Outputs folder and named as CompareMaxMinTemp.png and CumulativeGDD.png, respectively. 
* The functions defined are:
```
max_min_plot(names)
gdd_plot(names)
```
* The plot below is showing the accumulated GDD vs time for selected cities: 
![alt text](https://raw.githubusercontent.com/evankielley/GDD/master/Output/CumulativeGDD.png?token=Abv3GRtFi3qHnLJFDwGDdtJajOOyqtUZks5ZSBtRwA%3D%3D)

## Secondary Tasks
For all plots generated in this task, the script `create_plots.py` is called, except for question 5.
* *Question 1*: 
* *Question 2*: The input .csv files to solve this question are found in the Input folder (TempMax, TempMean, TempMin). The map of Canada shows the effective GDD of the country distributed by colours, in which as redder the area is, higher the GDD cumulation is.  
```
map_plot_nl_gdd()
```
* *Question 3*: Calculating the GDD by using different base temperatures (T<sub>base</sub> = 8, 9, 11, 12) for **city's name** in 2015. This plot shows how the cumulative growing degree days change depending on the base temperature chosen. The default for the base temperature is 10, so if Tbase is increased by 12 for example, then a higher GDD curve is seen because more temperature is accumulated along the days.
```
analyze_tbase()
```
* *Questions 4*: This bokeh plot shows interactively the T<sub>max</sub> and T<sub>min</sub> and the cumulative GDD for each capital city in Canada in 2015. To run the last two scripts mentioned, one should type in the bash shell 'bokeh serve --show <script's name>'.
* Functions defined as:
```
bokeh_plot_temp(fname)
bokeh_plot_gdd(fname)
```
* *Question 5*: By calling the script `bokeh_serve_gdd.py`, one can check the accumulated GDD for the 14 capital cities in Canada, including Montreal. 
* *Question 6*: 
```
plot_lin_reg(city,startYear, endYear,tbase,tupper): 
```

## Final Task

## LaTex Report
The LaTex report generates a PDF file containing the summarized results for this project.

## Test Suite
When running the script `test_gdd.py` one can test if the calculation for the GDD is working as expected (see Testing folder).

## Presentation
To see our presentation online, please click [here](https://evankielley.github.io/GDD/Presentation/presentation.html#1).

## References
(1). Growing degree-days: one equation, two interpretations http://digitalcommons.unl.edu/cgi/viewcontent.cgi?article=1086&context=usdaarsfacpub 


:octocat: Thank you.
