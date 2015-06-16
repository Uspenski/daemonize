import sys, time
import socket
import subprocess
import threading
import MySQLdb

from datetime import datetime

def scan_me_all():
    while True:
        now=datetime.now()
        now_time='(%s:%s:%s)' % (now.hour, now.minute, now.second)
        now_date='(%s:%s:%s)' % (now.day, now.month, now.year)
        p=subprocess.Popen("ps -aux | awk '{sum[$1] += $3}END {for(i in sum)print i \":\"sum[i]}'", shell=True, stdout=subprocess.PIPE)
        a=[]
        db = MySQLdb.connect(host="localhost", user="sprint", passwd="sprint", db="spirit", charset='utf8')
        cursor = db.cursor()
        while True:
            strin_answ=p.stdout.readline()
            if not strin_answ: break
            a.append(strin_answ.split(":"))
        for elem in a:
            sql = """INSERT INTO cpu(time, date, user, cpu) VALUES ('%(time)s', '%(date)s', '%(user)s', '%(cpu)s')"""%{"time":(str(now_time)), "date":(str(now_date)), "user":str(elem[0]), "cpu":str(elem[1])}
            cursor.execute(sql)
        db.commit()
        db.close()
        time.sleep(10)
        
scan_me_all()