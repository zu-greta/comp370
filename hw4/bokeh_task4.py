from bokeh.io import curdoc
from bokeh.layouts import column
from bokeh.models import Select, ColumnDataSource
from bokeh.plotting import figure
import pandas as pd

data = pd.read_csv('task4_2.csv')

data['month'] = pd.to_datetime(data['month'], format='%Y-%m')

source = ColumnDataSource(data=dict(month=[], all_data=[], zip1_data=[], zip2_data=[])) # Create a ColumnDataSource

# init figure for plotting
plot = figure(x_axis_type='datetime', title="Monthly Average Response Time (Hours)",
              width=800, height=400)  # Adjust width and height as needed
plot.line(x='month', y='all_data', source=source, color='blue', legend_label='All 2020 Data')
plot.line(x='month', y='zip1_data', source=source, color='green', legend_label='Zipcode 1')
plot.line(x='month', y='zip2_data', source=source, color='red', legend_label='Zipcode 2')
plot.legend.title = 'Legend'
plot.xaxis.axis_label = 'Month'
plot.yaxis.axis_label = 'Avg Response Time (Hours)'

# dropdowns for selecting zipcodes
zipcodes = sorted(data['zipcode'].unique().astype(str))
zip1_select = Select(title="Select Zipcode 1", value=zipcodes[0], options=zipcodes)
zip2_select = Select(title="Select Zipcode 2", value=zipcodes[1], options=zipcodes)

# update the plot based on the selected zipcodes
def update_plot():
    zip1 = zip1_select.value
    zip2 = zip2_select.value
    
    # Filter data for the selected zipcodes 
    all_data_avg = data.groupby('month')['avg_response_time_hours'].mean().reset_index()
    # Compare zip codes as strings
    zip1_data_avg = data[data['zipcode'].astype(str) == zip1].groupby('month')['avg_response_time_hours'].mean().reset_index()
    zip2_data_avg = data[data['zipcode'].astype(str) == zip2].groupby('month')['avg_response_time_hours'].mean().reset_index()

    # Update the source 
    source.data = dict(
        month=all_data_avg['month'],
        all_data=all_data_avg['avg_response_time_hours'],
        zip1_data=zip1_data_avg['avg_response_time_hours'],
        zip2_data=zip2_data_avg['avg_response_time_hours'],
    )

# Call update_plot whenever the dropdowns are changed
zip1_select.on_change('value', lambda attr, old, new: update_plot())
zip2_select.on_change('value', lambda attr, old, new: update_plot())

# Layout the widgets and the plot
layout = column(zip1_select, zip2_select, plot)

# Add the layout to the current document
curdoc().add_root(layout)
curdoc().title = "NYC 311 Complaints Dashboard"

# Initial plot update
update_plot()