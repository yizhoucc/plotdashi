
import pymysql
# import torch

def conn(dbconf=None, user=None, password=None,charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor):
    if dbconf is None:
        dbconf={
            'host':'localhost',
            'user':'testbot',
            'db':'plot_test',
            'password':'testbot',
            'charset':'utf8mb4',
            'cursorclass':pymysql.cursors.DictCursor,
        }
    connection = pymysql.connect(**dbconf)
    return connection

def writedata(conn,data):
    con=conn()
    try:
        with con.cursor() as cur:
            sql='INSERT INTO test (x) VALUES ({});'.format(str(data))
            print(sql)
            cur.execute(sql) 
            con.commit()
    finally:
        con.close()

def fakedata():
    return 10.0001

def writetest(conn):
    code=1
    try:
        for i in range(50):
            data=fakedata()
            print(data)
            code=writedata(conn,data)
        code=0   
    except:
        pass     
    return code

def readdata(conn,process=False):
    con=conn()
    try:
        with con.cursor() as cur:
            sql='select x, dt from test'
            print(sql)
            cur.execute(sql) 
            results=cur.fetchall()
            con.close()
            if process:
                tslist,datalist=tsdata(results)
                return tslist,datalist
            else:
                return results
    except:
        return None

def tsdata(results):
    tslist=[]
    datalist=[]
    for onedict in results:
        tslist.append(onedict['dt'])
        datalist.append(onedict['x'])
    return tslist,datalist


if __name__ == "__main__":
    # code=writetest(conn)
    # print(code)
    
    # ts,data=readdata(conn,process=True)
    # print(ts)
    # print(data)

