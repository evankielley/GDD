TBASE = 10
TUPPER = 30
INPUT = ../Input/
OUTPUT = ./Output/
SCRIPTS = ./Scripts/

all: report.pdf

report.pdf: plot
	pdflatex Report/report.tex
	@mv report.* $(OUTPUT) 

plot: gdd
	python $(SCRIPTS)create_plots.py

gdd:
	@mkdir Output/  
	python $(SCRIPTS)gdd.py $(TBASE) $(TUPPER) $(INPUT)

clean:
	rm -rf $(OUTPUT)

#data.csv:
#	curl -o data.csv http://climate.weather.gc.ca/climate_data/bulk_data_e.html?format=csv&stationID=50089&Year=2016&timeframe=2&submit=Download+Data


