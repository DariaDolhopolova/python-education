"""Example of using ReGex functionality and logging it instead of printing"""
import re
import logging

logger = logging.getLogger(__name__)
# Create handlers
c_handler = logging.StreamHandler()
f_handler = logging.FileHandler('file.log')
c_handler.setLevel(logging.DEBUG)
f_handler.setLevel(logging.INFO)

# Create formatters and add it to handlers
c_format = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
f_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
c_handler.setFormatter(c_format)
f_handler.setFormatter(f_format)

# Add handlers to the logger
logger.addHandler(c_handler)
logger.addHandler(f_handler)


logger.warning('This is a warning')
logger.error('This is an error')

# ReGex part starts here
TXT = 'My cat is 20 years old, did you know?!'
logger.debug("Message added to TXT variable: %(TXT)s")
begins_ends = re.search('^My.*!$', TXT)
logger.info("Match object created after search: %(begins_ends)s")
find_a_to_f = re.findall('[a-f]', TXT)
logger.info("Letters found in TXT from a to f: %(find_a_to_f)s")
numbers = re.search(r'\d', TXT)
logger.info("Match object created after search: %(numbers)d")
logger.info("The position of digits in the txt: %(numbers.span())s")
words = re.split(r'\s', TXT)
logger.info("Split by spaces: %(words)s")
