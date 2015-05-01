import requests
import sys
from djangopkg.main.conf import CONFIG

def sample():
    env = CONFIG.ENVIRONMENT_NAME
    args = ' '.join(sys.argv[1:])
    print "Running sample script in environment '{}', with args: {}".format(env, args)

