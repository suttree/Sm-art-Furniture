from daemon import Daemon

import os, sys, getopt, time
import webbrowser
import datetime
import logging
import random
import signal
import noise

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

# for screen dimming
dimmer = 1

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
	i = 0.0
	launch_processing(True)

        # Run the main loop
        while self.run_forever:
	    if (random.randint(0,9) > 8):
		dim_screen()
		launch_processing()
		p = int(noise.pnoise1(i) * 100)
		try:
		    time.sleep(p)
		except IOError:
		    pass
	    i += 0.1

        print "This is an exit"
        sys.exit(0)

def dim_screen():
    global dimmer
    hour = datetime.datetime.now().hour
    log.info("Hour: %d, Dimmer: %f", hour, dimmer)
    if hour >= 20 or hour <= 6:
	if hour >= 20:
	    # dim screen
	    dimmer -= 0.01
	elif hour <= 6:
	    # wake up
	    dimmer += 0.01

	if dimmer > 0.0:
	    os.system("bin/brightness {}".format(dimmer))

# Launch p5, select a script and suply with random args?
def launch_processing(startup = False):
    # From https://stackoverflow.com/questions/12211781/how-to-maximize-window-in-chrome-using-webdriver-python
    #ChromeOptions chromeOptions = new ChromeOptions();
    #chromeOptions.addArguments("--kiosk");
    #driver = new ChromeDriver(chromeOptions);

    if (random.randint(0,9) > 8) or startup:
	page = random.choice(['index11.html', 'index12.html'])
	log.info("Launching p5: %s", page)
	webbrowser.open("http://0.0.0.0:8000/{}".format(page) , new = 0)

if __name__ == "__main__":
    main(sys.argv[1:])
