import os
import time
import os
import sys

pid = str(os.getpid())
pidfile = "/tmp/mydaemon.pid"
logfile = open(pidfile,"w").write(pid)


os.unlink(pidfile)