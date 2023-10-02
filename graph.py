import plotly.express as px 
from serv import getbal, getids, getidlist, stringify

def listify(inp):
    stag0 = str(inp)
    stag1 = stringify(stag0)
    res = [int(i) for i in stag1.split() if i.isdigit()]
    return res





def test():
    # make figure instance
    print('input')
    x = listify(getidlist())
    y = listify(getbal())
    print(x)
    print("y /n")
    print(y)
    fig = px.line(x=x, y=y) 
    return fig

test()
