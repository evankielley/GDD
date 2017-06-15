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
	@pdflatex -interaction=batchmode $(REPORT)report.tex
	@printf "\nMoving report pdf to output folder...\n"
	@mv report.pdf $(OUTPUT)
	@printf "\nRemove remaining report files...\n"
	@rm -rf report.*

plot: gdd
	@printf "\nMaking plots...\n"
	@python $(SCRIPTS)create_plots.py

gdd: prep
	@printf "\nCalculating GDD...\n"
	@python $(SCRIPTS)gdd.py $(TBASE) $(TUPPER) $(INPUT)

prep:
	@printf "\nMaking output folder...\n"
	@mkdir Output/
	@printf "\nUnzipping input files...\n"
	@tar xvzf ./Input/InputData.tar.gz -C ./Input/

clean:
	@printf "\nCleaning...\n"
	@rm -rf $(OUTPUT)
	@rm -rf ./Input/*.csv
	@printf "\nAll clean\n\n"

#data.csv:
#	curl -o data.csv http://climate.weather.gc.ca/climate_data/bulk_data_e.html?format=csv&stationID=50089&Year=2016&timeframe=2&submit=Download+Data
