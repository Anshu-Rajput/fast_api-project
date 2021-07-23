# from .route import account
# from ..shared.db import return_connection
# import pandas as pd
#
#
#
# conn=return_connection()
# sql = f"EXEC SP_Test"
#
# cursor = conn.cursor()
# df_list = []
#
# # get First result
# cursor.execute(sql)
# rows=cursor.fetchall()
# columns = [column[0] for column in cursor.description]
# df_list.append(pd.DataFrame.from_records(rows, columns=columns))
#
# # check for more results
# while (cursor.nextset()):
#    rows = cursor.fetchall()
#    columns = [column[0] for column in cursor.description]
#    df_list.append(pd.DataFrame.from_records(rows, columns=columns))
#
# cursor.close()
