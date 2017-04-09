import htmlPy
import os
from backend import *
import json
import sqlite3


sqlite_file = 'my_db.sqlite'
conn = sqlite3.connect(sqlite_file)
c = conn.cursor()




app = htmlPy.AppGUI(title=u"MY ADDRESS BOOK", maximized=False)

app.template_path = os.path.abspath(".")
app.static_path = os.path.abspath(".")
app.bind(BackEnd(app))

c.execute("SELECT * from contacts")
all_rows = json.dumps(c.fetchall())

app.template = ("index.html",{'contacts':all_rows})

app.start()
