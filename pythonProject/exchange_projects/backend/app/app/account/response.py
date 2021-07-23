
def fetch_multiple(sql,cursor):
    l=[]
    cursor.execute(sql)
    rows = cursor.fetchall()
    columns = [column[0] for column in cursor.description]
    for i in rows:
        l.append(dict(zip(columns, i)))

    while (cursor.nextset()):
        rows = cursor.fetchall()
        columns = [column[0] for column in cursor.description]
        for i in rows:
            l.append(dict(zip(columns, i)))
    return l
