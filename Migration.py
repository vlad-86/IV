import os
import sqlite3
import subprocess
"""Decide whether it'll be module, package .self needed? """


class Migration:



    def init_sql_lite_db(self):
        con = sqlite3.connect("d:\Share\FEATURES\IV\databasefile.db")
        # TODO: define variable path_to_sql_lite_db

        return

    def init_sybase_db():
        # TODO: implement init DB by subprocess.call("dbisql.exe"), start engine?
        # echo Start engine
        # start "db" "%SYPATH%\bin64\dbeng16.exe"  -n %SYNAME% -x tcpip(PORT=%SYPORT%;) iv_etalon.db
        # Execute scripts to create DB
        # "%SYPATH%\bin64\dbisql.exe" -q -d1 -nogui -c "UID=dba;PWD=sql;ENG=%SYNAME%;links=tcpip{PORT=%SYPORT%;}"*.sql
        sybase_path = os.environ['SQLANY16']
        syspath = os.path.join(sybase_path, 'bin64')
        port = 45163
        db_name = 'VP_1'
        os.chdir(syspath)
        sql_query = "UPDATE VPSecuritySettings SET LdapAuthentication='Y'; commit;"
        query_result = subprocess.call(["dbisql.exe", "-q", "-d1", "-nogui", "-c", "UID=dba;PWD=sql;ENG=VP_1;links=tcpip{PORT=45163;}", sql_query])

        return print("Exit code of execution is - "+str(query_result))

    def execute_sql_lite(self, querydb):
        # TODO: implement cursor.execute from sqlite3 module
        #
        # con.execute()
        return 0

    def execute_sybase(query_sybase):
        # TODO: implement execute sql query by subprocess.call("dbisql.exe")
        return query_sybase

    def run_validator(self):
        # TODO: define running tool with or w\o parameters
        return 0
    def tear_down(self):
        # TODO: define postconditions here: revert made changes to DB
        # cursor.close() # close db connection
        return 0
