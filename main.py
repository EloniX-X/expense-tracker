from nicegui import ui
from serv import gettrans, newtrans, deltrans, getids, recbal, stringify
from graph import test

def input():
    with ui.row():
        name = ui.input(label='name', placeholder='name')
        inc = ui.input(label='+/-', placeholder='+num/-num')
        ui.button('Submit Transaction', on_click=lambda: processinputbutton(name, inc))

def processinputbutton(name, inc):
    resname = name.value
    resinc = inc.value
    resname = str(resname)
    resinc = str(resinc)
    newtrans(resname, resinc)
    displaytrans.refresh()
    displaymoney.refresh()
    #return restxt

@ui.refreshable
def displaytrans():
    a = gettrans()  
    columns = [
        {'name': 'id', 'label': 'id', 'field': 'id'},
        {'name': 'bal', 'label': 'bal', 'field': 'bal', 'sortable': True},
        {'name': 'name', 'label': 'Name', 'field': 'name', 'required': True, 'align': 'left'},
        {'name': 'inc', 'label': 'inc', 'field': 'inc', 'sortable': True},
    ]
    
    rows = a
 
    ui.table(columns=columns, rows=rows, row_key='name').style('width: 40%')

@ui.refreshable
def removetrans():
    select = ui.select([item[0] for item in getids()], value=1)
    ui.button('delete', on_click=lambda: processremovetrans(select))

def processremovetrans(sel):
    select = sel.value
    select = str(select)
    deltrans(select)
    removetrans.refresh()
    displaytrans.refresh()
    displaymoney.refresh()


def plotly():
    fig = test()
    fig = fig.update_layout(margin=dict(l=0, r=0, t=0, b=0))
    ui.plotly(fig).classes('w-13 h-13  scale-50 absolute inset-y-0 right-0 ')


@ui.refreshable
def displaymoney():
    with ui.element('div').classes('p-2 bg-blue-100'):
        ui.label(recbal())

displaymoney()
input()
displaytrans()
plotly()
removetrans()
ui.run()
