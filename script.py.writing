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
	pass

def wait_take_it_easy():
	pass

def shut_up_and_write():
	pass

class MyDaemon(Daemon):
	def run(self):
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
				conn.send(data.upper())
			conn.close()
			time.sleep(1)

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
