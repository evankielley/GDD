def bokeh_plot_gdd_years():

	data_frame=pd.read_csv("..\Input\Ottawa_grouped_gdd.csv") ## To be replaced with fname
	data1 = data_frame.transpose()
	#print (data)
	Mean = [None]*365
	fifth_percentile = [None]*365
	ninety_fifth_percentile = [None]*365
	twenty_fifth_percentile = [None]*365
	seventy_fifth_percentile = [None]*365
	xaxisTickNames = [None]*365
	numOfYearsGDDRecorded = (len(list(data1[0][ 1:])))
	fivepercentile = round((5/100) * numOfYearsGDDRecorded)
	ninetyfivepercentile = round((95/100) * numOfYearsGDDRecorded)
	twentyfivepercentile = round((25/100) * numOfYearsGDDRecorded)
	seventyfivepercentile = round((75/100) * numOfYearsGDDRecorded)
	i=0
	j=0
	xHeader = [ "Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec", ""]
	for day in data['index']:
		sorteddata = list(data1[i][ 1:])
		sorteddata.sort()
		Mean[i]=data1[i][ 1:].mean()
		fifth_percentile[i] = sorteddata[fivepercentile]
		ninety_fifth_percentile[i] = sorteddata[ninetyfivepercentile]
		twenty_fifth_percentile[i] = sorteddata[twentyfivepercentile]
		seventy_fifth_percentile[i] = sorteddata[seventyfivepercentile]
		'''if (i % 30 == 0):
			xaxisTickNames[i] = xHeader[j]
			j = j+1
			#print (j)
			#print(i)
		else:
			xaxisTickNames[i] = ""
			#print(i)'''
		i+=1

	source1 = ColumnDataSource(dict(
	left=np.arange(0.5, 365.5, 1),
	top= ninety_fifth_percentile,
	right=np.arange(1.5, 366.5, 1),
	bottom=fifth_percentile,
	)
	)
	source2 = ColumnDataSource(dict(
	left=np.arange(0.5, 365.5, 1),
	top= seventy_fifth_percentile,
	right=np.arange(1.5, 366.5, 1),
	bottom=twenty_fifth_percentile,
	)
	)
	plot = figure(x_axis_type="datetime", plot_width=400, tools="", toolbar_location=None)
	plot.quad(top='top', bottom='bottom', left='left',right='right',source=source1,color="#000000", legend="Percentile 5-95")
	plot.quad(top='top', bottom='bottom',left='left',right='right', source=source2,color="#66ccff",legend="percentile 25-75")
	plot.line(np.arange(1,365,1),Mean,source=source,line_color='Red', line_width=0.5, legend='AverageTemp')
	plot.border_fill_color = "whitesmoke"
	plot.xaxis.axis_label = "GDD/Days over years"
	plot.yaxis.axis_label = "Temperature (C)"
	plot.axis.major_label_text_font_size = "10pt"
	plot.axis.axis_label_text_font_size = "12pt"
	plot.axis.axis_label_text_font_style = "bold"
	plot.x_range = DataRange1d(range_padding=0.0, bounds=None)
	plot.grid.grid_line_alpha = 0.3
	new_fname =  os.path.dirname(os.path.realpath(__file__)) + "/../Output/" + "bokeh_temp.html"
	output_file(new_fname, title="OptionalTask1GDDPlot")
	save(plot)
