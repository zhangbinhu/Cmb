'''
Description: 
version: 0.0.1
Author: binhu.zhang@gdchina.com
Date: 2021-11-11 11:20:56
LastEditors: zbh
LastEditTime: 2021-11-11 13:54:06
'''

import time
import os
import re

BIN_EXT = ".bin"
TEXT_EXT = ".txt"
XML_EXT = '.xml'

g_bWriteDCFile = True
g_bEncryptGPF = True
g_CMBFileRestring = r"^P[0-9a-zA-Z]{1,}.*"
g_CMBDeCryptoDgi = ['pboc8000']
g_CMBFileInfoArray = []
g_CMBProjectName = r'CMB_Debit_PBOC.prj'
g_CMBKek = '9DDFCD8B37D74CFCE9C269D6DF5F2ABF'


def runTime(method):
    @wraps(method)
    def wrapper(*args, **kwargs):
        ts = time.time()
        result = method(*args, **kwargs)
        te = time.time()
        # log.info("%r (%r, %r) %2.2f sec" % (method.__name__, args, kw, te-ts))
        print(f"{method.__name__} => {(te-ts)}ms")

        return result

    return wrapper
