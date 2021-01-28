import logging
import logging.handlers

logger = logging.getLogger('')
logger.setLevel(logging.INFO)

# handler = logging.handlers.SysLogHandler('/run/systemd/journal/syslog')
# Enter IP and port where your Vector sink is running
handler = logging.handlers.SysLogHandler(address=('192.168.101.29', 5514), facility=19)
logger.addHandler(handler)

logger.info("Hello World")
