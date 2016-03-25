import sqlite3
#import Syb

con = sqlite3.connect("d:\Share\FEATURES\IV\databasefile.db")
print('Opened connection successfully')

cursor = con.execute("DELETE FROM VPM_DEPARTMENT")
cursor = con.commit()
cursor = con.execute("INSERT INTO VPM_DEPARTMENT ('@ID', NAME, DESCRIPTION) VALUES (222, 'batch_call2', 'tryIT')")
cursor = con.commit()
cursor = con.execute("SELECT * FROM VPM_DEPARTMENT")

for row in cursor:
    print("@ID = ", row[0])
    print("NAME = ", row[1])
    print("DESCRIPTION = ", row[2])


con.close()
print("Connection is closed")
"""
Ultrasound Multi-frame Image Storage
1.2.840.10008.5.1.4.1.1.3.1
Ultrasound Multi-Frame Image Storage (Retired)
1.2.840.10008.5.1.4.1.1.3
Ultrasound Image Storage
1.2.840.10008.5.1.4.1.1.6.1
Ultrasound Image Storage (Retired)
1.2.840.10008.5.1.4.1.1.6
Secondary Capture Image Storage
1.2.840.10008.5.1.4.1.1.7
X-Ray Angiographic Image Storage
1.2.840.10008.5.1.4.1.1.12.1
X-Ray Radiofluoroscopic Image Storage
1.2.840.10008.5.1.4.1.1.12.2
Basic Text SR Storage
1.2.840.10008.5.1.4.1.1.88.11
Enhanced SR Storage
1.2.840.10008.5.1.4.1.1.88.22
Comprehensive Structured Reporting SOP Class
1.2.840.10008.5.1.4.1.1.88.33
Positron Emission Tomography Image Storage
1.2.840.10008.5.1.4.1.1.128
Computed Radiography Image Storage
1.2.840.10008.5.1.4.1.1.1
CT Image Storage
1.2.840.10008.5.1.4.1.1.2
Study Root Query/Retrieve Information Model – MOVE
1.2.840.10008.5.1.4.1.2.2.2
"""
# modified on home PC