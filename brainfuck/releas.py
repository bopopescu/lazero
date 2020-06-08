import sqlite3
# how do you read a book? how do you execute a command?
# def init():
# try debugging?
# why so many shits?
# not reading correct programs.
# what does it mean really?
# nothing. believe it or not, there's only one thing over there. it is always right.
def createMain():
    conn = sqlite3.connect('Monitor.db', timeout=45)
    conn.text_factory=str
    c = conn.cursor()
    sql = "CREATE TABLE IF NOT EXISTS projects ( \
    ts float NOT NULL, \
    op_type text NOT NULL, \
    op_output text NOT NULL \
);"
    c.execute(sql)
    conn.commit()
    # this thing must be done after every execute.
    conn.close()
# i do not care about internal logic. all i need is to fuck it up.