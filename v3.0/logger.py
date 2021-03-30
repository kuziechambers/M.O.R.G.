import logging
import logging.handlers as handlers


morg_log = logging.getLogger('MORGlogger')
morg_log.setLevel(logging.INFO)
log_handler = handlers.RotatingFileHandler('/home/pi/M.O.R.G./logs/MORG.log', mode='a+', maxBytes=10000*1024, backupCount=1)
log_handler.setLevel(logging.INFO)
morg_log.addHandler(log_handler)




