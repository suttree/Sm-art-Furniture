from daemon import Daemon

import os, sys, getopt
import random
import signal

def usage():
  print "sf.py -h (help) -d (debug) -s (startup)"

def main(argv):
    full_path = os.path.realpath(__file__)
    sf = smartFurniture(os.path.dirname(full_path) + '/' + 'sf.pid')
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

    def _handle_sigterm(self, signum, frame):
        """Handles SIGTERM and SIGINT, which gracefully stops the agent."""
        log.debug("Caught sigterm. Stopping run loop.")
        self.run_forever = False

        if self.collector:
            self.collector.stop()
        log.debug("Collector is stopped.")

    def _handle_sigusr1(self, signum, frame):
        """Handles SIGUSR1, which signals an exit with an autorestart."""
        self._handle_sigterm(signum, frame)
        self._do_restart()

    def _handle_sighup(self, signum, frame):
        """Handles SIGHUP, which signals a configuration reload."""
        log.info("SIGHUP caught! Scheduling configuration reload before next collection run.")
        self.reload_configs_flag = True

    def run(self):
        # Gracefully exit on sigterm.
        signal.signal(signal.SIGTERM, self._handle_sigterm)

        # A SIGUSR1 signals an exit with an autorestart
        signal.signal(signal.SIGUSR1, self._handle_sigusr1)

        # Handle Keyboard Interrupt
        signal.signal(signal.SIGINT, self._handle_sigterm)

        # A SIGHUP signals a configuration reload
        signal.signal(signal.SIGHUP, self._handle_sighup)

        # Run the main loop.
        while self.run_forever:
	    print "hey"

	print "Exiting. Bye bye."
        sys.exit(0)

if __name__ == "__main__":
  main(sys.argv[1:])
