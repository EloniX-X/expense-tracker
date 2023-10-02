#budget 
#new money
#expenses 
#spent - bal

import jsonpickle
import sqlite3
con = sqlite3.connect("table.db")

cur = con.cursor()

def stringify(str):
    special_characters=['(',')',',',"'", '[',']']
    normal_string=str
    for i in special_characters:
    # Replace the special character with an empty string
        normal_string=normal_string.replace(i,"")
    return(normal_string)
#stringify('he443#')


#cur.execute("CREATE TABLE mon (id INTEGER PRIMARY KEY, bal, name, inc)")

def gettrans():
    print('running')
    cur.execute("SELECT id, bal, name, inc FROM mon ORDER BY id")
    result_set = cur.fetchall()
    list = []
    for row in result_set:
        #{'bal': 50, 'name': 'hi', 'inc':+12},
        id = row[0]
        bal = row[1]
        name = row[2]
        inc = str(row[3])
        testdict = {'id': id, 'bal': bal, 'name': name, 'inc': inc}
        list.append(testdict)
    
    #list = [testdict]
    #testdict = jsonpickle.encode(testdict)
    
    return list

def getidlist():
    cur.execute("select id from mon")
    x = []
    ids = cur.fetchall()
    for row in ids:
        x.append(row)
    return x

def getids():
    cur.execute("select id from mon")
    ids = cur.fetchall()
    return ids


def test():
    a = {'name': 'yo', 'age': 21}
    b = 'yo'
    return a, b

def getbal():
    idcurnum = 0
    bal = []
    ids = getids()
    idstringed = str(ids)
    idstr = stringify(idstringed)
    idnum = len(idstr.split())
    
    while idcurnum < idnum: 
        curid = ids[idcurnum]
        cur.execute("SELECT bal FROM mon where id = ?", (curid))
        idcurnum = idcurnum + 1
        bal.append(cur.fetchone())

    return bal
    
def getmaxid():
    maxid = cur.execute("select max(id) from mon")
    resmaxid = maxid.fetchone()
    resmaxid = str(resmaxid)
    resmaxid = stringify(resmaxid)
    return resmaxid

def recbal():
    rec = getmaxid()
    recbal = cur.execute("SELECT bal from mon where id = ?",(rec,))
    recbal = cur.fetchone()
    recbal = str(recbal)
    recbal = stringify(recbal)
    print(recbal)
    return recbal




def newtrans(name, inc):
    maxid = cur.execute("select max(id) from mon")
    print('prefetching')

    resmaxid = maxid.fetchone()
    resmaxid = str(resmaxid)
    resmaxid = stringify(resmaxid)

    print(resmaxid)
    
    prevbal = cur.execute("select bal from mon where id = ?", (resmaxid,))
    prevbal = prevbal.fetchone()
    prevbal = str(prevbal)
    prevbal = stringify(prevbal)
    inc = int(inc)
    prevbal = int(prevbal)
    newbal = prevbal + inc
    newbal = str(newbal)
    newbal = stringify(newbal)
    cur.execute("INSERT INTO mon (bal, name, inc) VALUES (?, ?,?)",(newbal, name, inc))
    con.commit()

def deltrans(sel2rem):
    print(sel2rem)
    cur.execute("DELETE FROM mon WHERE id = ?", (sel2rem,))
    con.commit()
    print('commited')
    
def getmaxidlist():
    maxid = cur.execute("select max(id) from mon")

    resmaxid = maxid.fetchone()
    resmaxid = str(resmaxid)
    resmaxid = stringify(resmaxid)
    print(resmaxid)
  #  i = 0
  #  maxid = int(resmaxid)
  #  x = []
  #  while i < maxid:
  #      i = i + 1
  #      x.append(i + 1)
  #  return x



#INSERT INTO mon  (bal, name, inc) VALUES (500, 'money example',  +500)