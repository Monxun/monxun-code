# fig is plotly figure object and graph_div the html code for displaying the graph
graph_div = plotly.offline.plot(fig, auto_open = False, output_type="div")
# pass the div to the template

"""
<div style="width:1000;height:100">
{{ graph_div|safe }}
</div>

"""
