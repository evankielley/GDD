all: report.pdf

data.csv:
	curl -o data.csv http://climate.weather.gc.ca/climate_data/bulk_data_e.html?format=csv&stationID=50089&Year=2016&timeframe=2&submit=Download+Data

plot.png: data.csv
	python plot.py data.csv

report.pdf: report.tex plot.png
	pdflatex report.tex
	pdflatex report.tex
	#bibtex report
	pdflatex report.tex

clean:
	rm -f report.log report.aux report.pdf
	rm -f data.csv plot.png
