#!/usr/bin/python3

db = "appdev"
# all content in temp_db will be DELETED!
temp_db = "spielwiese"


TODO pseudocode!

# create DB (folder must not exist before)
/usr/lib/postgresql/9.4/bin/initdb -D /tmp/asdf
pg_conftool /tmp/asdf/postgresql.conf set unix_socket_directories /tmp/asdf
# start postgres server
/usr/lib/postgresql/9.4/bin/postgres  -p 37731 -D /tmp/asdf

# TODO connect, create temp_db



# import dump (only from selected db, ignore other dbs in dump)
psql_process = subprocess.call("psql -d {}".format(temp_db), STDIN=todo)
psql = TODO stdin

skip_content = True # wait until next db
for line in open("./dump","r"):
    if line.startswith("\connect"):
        skip_content = (line == r"\connect {}".format(db))
        continue
    
    if skip_content:
        # wait until \connect <DATABASE>
        continue
    out.write(line)
out.close()

psql.write("UPDATE res_users SET password_crypt='';")

TODO dump > anon_dump

TODO stop postgres, delete tempfolder (finally...)
