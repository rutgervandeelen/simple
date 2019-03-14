#!/usr/bin/env python

"""
Experimental code
"""

import os
import json
import logging

def add(a, b):
    """ Add two numbers """
    return a + b

def write_settings(settings, output_file):
    """ Write the settings to a JSON file

    Args:
       settings: dictionary with configuration settings
       output_file: string with output filename

    """
    fop = open(output_file, 'w')
    contents = json.dumps(settings, indent=4)
    fop.write(contents)
    fop.close()

def main():
    """ Main function """

    # Remove the old log file if it exist
    log_filename = 'log.txt'
    if os.path.exists(log_filename):
        os.remove(log_filename)

    # Setup logging
    logger = logging.getLogger('simple')
    logger.setLevel(logging.INFO)

    # Set the format
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s %(message)s',
                                  '%Y-%m-%d %H:%M:%S')

    # Set the streamhandler
    streamhandler = logging.StreamHandler()
    streamhandler.setLevel(logging.INFO)
    streamhandler.setFormatter(formatter)

    # Set the filehandler
    filehandler = logging.FileHandler(log_filename)
    filehandler.setLevel(logging.INFO)
    filehandler.setFormatter(formatter)

    # Add the streamhandler and filehandler to the logger
    logger.addHandler(streamhandler)
    logger.addHandler(filehandler)

    # Create the configuration settings
    msg = "Creating settings"
    logger.info(msg)
    settings = {
        'name' : 'test_machine',
        'num_units' : add(2, 3)
    }

    # Write the settings to a JSON file
    output_file = 'test.json'
    msg = "Writing '%s'" % os.path.basename(output_file)
    logger.info(msg)
    write_settings(settings, output_file)

if __name__ == "__main__":
    main()
