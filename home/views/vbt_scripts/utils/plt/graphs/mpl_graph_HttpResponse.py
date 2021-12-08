import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_agg import FigureCanvasAgg
from django.http import HttpResponse


# https://plotly.com/python/renderers/

def plot(request):
    # Data for plotting
    t = np.arange(0.0, 2.0, 0.01)
    s = 1 + np.sin(2 * np.pi * t)

    fig, ax = plt.subplots()
    ax.plot(t, s)

    ax.set(xlabel='time (s)', ylabel='voltage (mV)',
           title='About as simple as it gets, folks')
    ax.grid()

    response = HttpResponse(content_type = 'image/png')
    canvas = FigureCanvasAgg(fig)
    canvas.print_png(response)
    return response

"""
https://plotly.com/python/renderers/

You can easily return plot using django HttpResponse instead using
some extra libs. In the matplotlib there is a FigureCanvasAgg which
 gives you access to canvas where plot is rendered. Finaly you can
 simple return it as HttpResonse. Here you have very basic example.


"""
# BETTER OPTION: https://stackoverflow.com/questions/49542459/error-in-django-when-using-matplotlib-examples
# At the moment, matplotlib's writing functions require the seek ducktype to use
# the response at a file. You can write to a buffer, like this:

def mplimage(request):
    f = matplotlib.figure.Figure()

    # Code that sets up figure goes here; in the question, that's ...
    FigureCanvasAgg(f)

    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    plt.close(f)
    response = HttpResponse(buf.getvalue(), content_type='image/png')
    return response

"""
https://stackoverflow.com/questions/49542459/error-in-django-when-using-matplotlib-examples

You can just replace the response with a buffer and then add the buffer to the
response. This will give an appropriate object to canvas.print_png() and keep
code changes to a minimum.

"""

def mplimage(request):
    f = matplotlib.figure.Figure()
    buf = io.BytesIO()
    canvas = FigureCanvasAgg(f)
    canvas.print_png(buf)
    response=HttpResponse(buf.getvalue(),content_type='image/png')
    # if required clear the figure for reuse
    f.clear()
    # I recommend to add Content-Length for Django
    response['Content-Length'] = str(len(response.content))
    #
    return response
