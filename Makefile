TBASE = 10
TUPPER = 30
EXAMPLEDATA = ../Input/

all: report.pdf

report.pdf: plot
	pdflatex Report/report.tex
	@mv report.* Output/ 

plot: gdd
	python Scripts/create_plots.py

gdd:
	@mkdir Output/  
	python Scripts/gdd.py $(TBASE) $(TUPPER) $(EXAMPLEDATA)

#data.csv:
#	curl -o data.csv http://climate.weather.gc.ca/climate_data/bulk_data_e.html?format=csv&stationID=50089&Year=2016&timeframe=2&submit=Download+Data

#plot.png: data.csv
#	python plot.py data.csv

#report.pdf: report.tex plot.png
#	pdflatex report.tex

#%_plot.png: %_gdd.csv
#	python temperature_plot.py

#%_gdd.csv: %_temp.csv 
#	bash gdd.sh $(TBASE) $(TUPPER) 


#### EXAMPLE ##########

#example: example_report.pdf

#example_report.pdf: example_plot
#	pdflatex example_report.tex

#example_plot: example_gdd
#	python temperature_plot.py $(EXAMPLEDATA)

#example_gdd:  
#	python gdd.py $(TBASE) $(TUPPER) $(EXAMPLEDATA)

#######################

clean:
	rm -f Report/report.log Report/report.aux Report/report.pdf Report/report.out Report/report.toc
	rm -f report.log report.aux report.pdf report.out report.toc
	rm -rf Output/
