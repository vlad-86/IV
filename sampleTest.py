import sqlite3
import Syb

con = sqlite3.connect("d:\Share\FEATURES\IV\databasefile.db")
print('Opened connection successfully')

cursor = con.execute("DELETE FROM VPM_DEPARTMENT")
cursor = con.commit()
cursor = con.execute("INSERT INTO VPM_DEPARTMENT ('@ID', NAME, DESCRIPTION) VALUES (222, 'pycharm_successful', 'descr_filled')")
cursor = con.commit()
cursor = con.execute("SELECT * FROM VPM_DEPARTMENT")

for row in cursor:
    print("@ID = ", row[0])
    print("NAME = ", row[1])
    print("DESCRIPTION = ", row[2])


con.close()
print("Connection is closed")
