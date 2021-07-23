from .route import account
from ..shared.db import  return_connection

@account.post('/dynamic response')
async def dynamic_response(Parameter1,Parameter2):
    try:
        list = []
        conn=return_connection()
        cursor=conn.cursor()
        sql = f"EXEC SP_Test '{Parameter1}',{Parameter2} "
        print('printing')
        cursor.execute(sql)

        rows=cursor.fetchall()
        print(rows,"printing")
        columns=[column[0] for column in cursor.description]
        for i in rows:
            list.append(dict(zip(columns,i)))


        while (cursor.nextset()):
            rows = cursor.fetchall()
            columns = [column[0] for column in cursor.description]
            for i in rows:
                list.append(dict(zip(columns, i)))
        conn.commit()
        return list

        #print(dict)


        #print(dict(zip(columns,rows)))
        #list.append(columns)
        #list.append(rows)
        print(list)





    except Exception as e:
        print(e)




        # for i in cursor:
        # list.append(i)
        # return list