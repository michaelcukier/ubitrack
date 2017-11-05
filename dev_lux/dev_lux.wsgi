#!/usr/bin/python
import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"/var/www/dev_lux/")

from dev_lux import app as application
application.secret_key = 'cukier'
