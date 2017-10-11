#-*- coding:utf8 -*-

from conf.sysconf import DB_CONF
import pymysql
import socket

def conn_db():
    try:
        conn = pymysql.connect(**DB_CONF)
    except pymysql.err.OperationalError:
        conn = pymysql.connect(**DB_CONF)
    return conn


def excute_sql(sql, val_tuple):
    res = None
    try:
        conn = conn_db()
        with conn.cursor() as cursor:
            data = cursor.execute(sql, val_tuple)
            print(data)
            res = cursor.fetchall()
        return res
    except socket.timeout as e:
        conn = conn_db()
        with conn.cursor() as cursor:
            data = cursor.execute(sql, val_tuple)
            print(data)
            res = cursor.fetchall()
        return res
    except:
        import traceback;traceback.print_exc()
    finally:
        conn.close()

def chaxun():
    sql =  "select count(*) from `friendscircle_article`"
    res = excute_sql(sql, ())
    print(res)