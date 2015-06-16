#!/usr/bin/env python

import sys, time
import socket
import subprocess
import threading
import MySQLdb

from daemon import Daemon
from datetime import datetime

def tell_me_somth():
	pass

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


def wait_take_it_easy():
	while True:
		sock = socket.socket()
		sock.bind(('', 9090))
	    	sock.listen(1)
		conn, addr = sock.accept()
		print 'connected:', addr
		while True:
			data = conn.recv(1024)
			if not data:
				break
			try:
				str(data)
			except:
				conn.send("Bad parametr")
				break
			#doing somth.
			if str(data) == "CPU":
				pass
			elif str(data) == "HDD":
				pass
			else:
				conn.send("Parametr Does exist")
				conn.close()
		time.sleep(1)

def shut_up_and_write():
	pass

class MyDaemon(Daemon):
	def run(self):
		t1 = threading.Thread(target=wait_take_it_easy, args=())
		t2 = threading.Thread(target=scan_me_all, args=())
#		sock = socket.socket()
#		sock.bind(('', 9090))
#		sock.listen(1)
#		conn, addr = sock.accept()
#		print 'connected:', addr
#		while True:
#			while True:
#				data = conn.recv(1024)
#				if not data:
#					break
#				conn.send(data.upper())
#			conn.close()
#			time.sleep(1)
		t1.start()
		t2.start()

if __name__ == "__main__":
	daemon = MyDaemon('/tmp/PIDsprint.pid')
	if len(sys.argv) == 2:
		if 'start' == sys.argv[1]:
			daemon.start()
		elif 'stop' == sys.argv[1]:
			daemon.stop()
		elif 'restart' == sys.argv[1]:
			daemon.restart()
		else:
			print "Unknown command"
			sys.exit(2)
		sys.exit(0)
	else:
		print "usage: %s start|stop|restart" % sys.argv[0]
		sys.exit(2)
