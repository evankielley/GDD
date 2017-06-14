TBASE = 10
TUPPER = 30
INPUT = -if ./Input/ -of ./Output/
OUTPUT = ./Output/
REPORT = ./Report/
SCRIPTS = ./Scripts/

all: report.pdf
	@printf "\nDone\n\n"

report.pdf: plot
	@printf "\nMaking LaTeX report...\n"
	@pdflatex -interaction=batchmode $(REPORT)report.tex
	@printf "\nMoving report output to output folder...\n"
	@mv report.* $(OUTPUT)

plot: gdd
	@printf "\n Unzip input file...\n"
	@tar xvzf ./Input/canadaMean.csv.tar.gz -C ./Input/
	@printf "\nMaking plots...\n"
	@python $(SCRIPTS)create_plots.py

gdd:
	@printf "\nMaking output folder...\n"
	@mkdir Output/
	@printf "\nCalculating GDD...\n"
	@python $(SCRIPTS)gdd.py $(TBASE) $(TUPPER) $(INPUT)

clean:
	@printf "\nCleaning...\n"
	@rm -rf $(OUTPUT)
	@printf "\nAll clean\n\n"

#data.csv:
#	curl -o data.csv http://climate.weather.gc.ca/climate_data/bulk_data_e.html?format=csv&stationID=50089&Year=2016&timeframe=2&submit=Download+Data
