#!/usr/bin/python3


import os

import jk_logging
from jk_testing import Assert

from jk_packunpack import *




log = jk_logging.ConsoleLogger.create(logMsgFormatter=jk_logging.COLOR_LOG_MESSAGE_FORMATTER)



resultFilePath = Packer.compressFile("testdata/myfile.txt", "gz", False, log)
Assert.isEqual(resultFilePath, os.path.abspath("testdata/myfile.txt.gz"))

resultFilePath2 = Unpacker.uncompressFile(resultFilePath, "output2/myfile.txt", False, log)
Assert.isEqual(resultFilePath2, "output2/myfile.txt")

log.success("Success.")





