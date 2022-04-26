EXTERNAL LIBRIRIES
In mydig, I use dns.message, dns.query, dns.exception, and time libraries. 
In mydig_output, I use numpy, pandas,  matplotlib.pyplot, pandas.plotting and plotly.graph_objects libraries to draw the output plots.

INSTRUCTIONS:
When running mydig, the console will ask the users input the domain they want to query, and return in the format with the information about the query result.

When running mydig_output, there is a part of commanded code. These code can be uncommand to draw the single plot of each website and have the information about  median, 25th percentile and 75th percentile values at right-top corner of the plot. But just input different website name in the brackets in the following statement 'df = pd.DataFrame()', and change the title name. 

Except these single websites plot, I also provided the code that can draw all website query time information in the same plot.