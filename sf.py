from daemon import Daemon

import os, sys, getopt, time
import datetime
import logging
import random
import signal

# Setup logging
log = logging.getLogger(__name__)
log.setLevel(logging.INFO)

# create a file handler
handler = logging.FileHandler('log/sf.log')
handler.setLevel(logging.INFO)

# create a logging format
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

# add the handlers to the logger
log.addHandler(handler)

# Setup PID file
full_path = os.path.realpath(__file__)
PID_FILE = os.path.dirname(full_path) + '/pid/' + 'sf.pid'

# dim the screen after 10pm, and vie versa

def usage():
    print "sf.py -h (help) -d (debug) -s (startup)"

def main(argv):
    full_path = os.path.realpath(__file__)
    sf = smartFurniture(PID_FILE)
    sf.start()

# Mostly taken from:
#   https://github.com/serverdensity/sd-agent/blob/master/agent.py
#   https://github.com/serverdensity/python-daemon
#   https://dpbl.wordpress.com/2017/02/12/a-tutorial-on-python-daemon/
class smartFurniture(Daemon):
    """
    This class manages the overall hardware process
    """

    def __init__(self, pidfile):
        Daemon.__init__(self, pidfile)
        self.run_forever = True

    def run(self):
        # Run the main loop.
        while self.run_forever:
	    # Schedule periodic processing changes
	    # TODO use perlin noise on the interval
	    dim_screen()
	    launch_processing()
	    time.sleep(5)

        print "This is an exit"
        sys.exit(0)

def dim_screen():
    hour = datetime.datetime.now().hour
    log.info("Hour: %d", hour)
    if hour >= 20 or hour <= 6:
	if hour > 20:
	    # dim screen
	    bvar -= 0.1
	elif hour < 6:
	    # wake up
	    bvar += 0.1

	os.system("bin/brightness %d", bvar)

def launch_processing():
    log.info("hey")

if __name__ == "__main__":
    main(sys.argv[1:])
