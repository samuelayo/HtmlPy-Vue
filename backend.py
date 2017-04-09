                    
import htmlPy
import json
import sqlite3
sqlite_file = 'my_db.sqlite'
conn = sqlite3.connect(sqlite_file)
c = conn.cursor()
c.execute('''
    CREATE TABLE IF NOT EXISTS contacts(id INTEGER PRIMARY KEY AUTOINCREMENT, firstname TEXT, lastname TEXT,
                       phone TEXT, notes TEXT)
''')
conn.commit()

class BackEnd(htmlPy.Object):

    def __init__(self, app):
        super(BackEnd, self).__init__()
        self.app = app

    @htmlPy.Slot(str, result=str)
    def add_contact(self, json_data):
        # @htmlPy.Slot(arg1_type, arg2_type, ..., result=return_type)
        # This function can be used for GUI forms.
        #
        form_data = json.loads(json_data)
        statement = """
            INSERT INTO contacts (firstname, lastname, phone, notes) VALUES(?, ?, ?, ?)
        """  
        params = (form_data['firstname'], form_data['lastname'], form_data['phone'], form_data['notes'])

        c.execute(statement, params)
        conn.commit()
        c.execute("SELECT * from contacts")
        all_rows = c.fetchall()
        return str(json.dumps(all_rows))
    
    @htmlPy.Slot(str, result=str)
    def delete_contact(self, json_data):
        form_data = json.loads(json_data)
        id = form_data['id']
        statement = """
            DELETE FROM contacts where id = ?
        """
        params = (id,)
        c.execute(statement, params)
        conn.commit()
        c.execute("SELECT * from contacts")
        all_rows = c.fetchall()
        return str(json.dumps(all_rows))


    
