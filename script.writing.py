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
	while True
		p=subprocess.Popen("ps -aux | awk '{sum[$1] += $3}END {for(i in sum)print i \":\"sum[i]}'", shell=True, stdout=subprocess.PIPE)
		a=[]
		b=0
		while True:
 			b+=        strin_answ=p.stdout.readline()
        if not strin_answ: break
        a.append(strin_answ.split(":"))
    for elem in a:
       print "element1 = %s, element2 = %s" % (elem[0], elem[1])
    print "length = %s, tries = %s" % (len(a), b)
daemon_scanner()

def wait_take_it_easy():
	sock = socket.socket()
        sock.bind(('', 9090))
        sock.listen(1)
        conn, addr = sock.accept()
        print 'connected:', addr
        while True:
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
			else
				conn.send("Parametr Does exist")
                conn.close()
	        time.sleep(1)

def shut_up_and_write():
	pass

class MyDaemon(Daemon):
	def run(self):
		t1 = threading.Thread(target=wait_take_it_easy, args=())
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
