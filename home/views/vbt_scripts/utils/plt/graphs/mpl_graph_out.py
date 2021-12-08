import matplotlib.pyplot as plt
from io import StringIO
import numpy as np

def return_graph():

    x = np.arange(0,np.pi*3,.1)
    y = np.sin(x)

    fig = plt.figure()
    plt.plot(x,y)

    imgdata = StringIO()
    fig.savefig(imgdata, format='svg')
    imgdata.seek(0)

    data = imgdata.getvalue()
    return data


"""
This one can be called by some other function
using and rendering the image returned by return_graph():
_________________________________________________________

(views.py)

def home(request):
    context['graph'] = return_graph() #import method to make graph
    return render(request, 'x/dashboard.html', context)
_________________________________________________________

And in the dashboard.html file,
the graphic is embedded by the following command:

(template.html)

{{ graph|safe }}



"""
