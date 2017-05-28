from daemon import Daemon

import os, sys, getopt
import sched, time
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

scheduler = sched.scheduler(time.time, time.sleep)

# run a p5.js script every 30 minutes/rand
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

#    def _handle_sigterm(self, signum, frame):
#        """Handles SIGTERM and SIGINT, which gracefully stops the agent."""
#        log.debug("Caught sigterm. Stopping run loop.")
#	log.error('sigterm backtrace', exc_info=True)
#        self.run_forever = False
#	self._remove_pidfile()

#    def _handle_sigusr1(self, signum, frame):
#        """Handles SIGUSR1, which signals an exit with an autorestart."""
#        self._handle_sigterm(signum, frame)
#        self._do_restart()

#    def _handle_sighup(self, signum, frame):
#        """Handles SIGHUP, which signals a configuration reload."""
#        log.info("SIGHUP caught! Scheduling configuration reload before next collection run.")
#	log.error('sighup backtrace', exc_info=True)
#	self._remove_pidfile()

#    def _do_restart(self):
#	log.info("on Restart.")

#    def _remove_pidfile(self):
#        try:
#            os.remove(PID_FILE)
#	except Exception: 
#	    pass

    def run(self):
#        # Gracefully exit on sigterm.
#        signal.signal(signal.SIGTERM, self._handle_sigterm)

#        # A SIGUSR1 signals an exit with an autorestart
#        signal.signal(signal.SIGUSR1, self._handle_sigusr1)

#        # Handle Keyboard Interrupt
#        signal.signal(signal.SIGINT, self._handle_sigterm)

#        # A SIGHUP signals a configuration reload
#        signal.signal(signal.SIGHUP, self._handle_sighup)

        # Schedule periodic processing changes
        # TODO use perlin noise on the interval
        periodic(scheduler, 5, launch_processing)

        # Run the main loop.
        while self.run_forever:
            pass

        print "This is an exit"
#	self._remove_pidfile()
        sys.exit(0)

def periodic(scheduler, interval, action, actionargs=()):
    print "1"	
    log.info("1")
    scheduler.enter(interval, 1, periodic, (scheduler, interval, action, actionargs))
    action(*actionargs)

def launch_processing():
    print "2"
    log.info("2")
    log.info("hey")


if __name__ == "__main__":
    main(sys.argv[1:])
