''' Copyright 2017 by RESPEC, INC. - see License.txt with this HSP2 distribution
Author: Robert Heaphy, Ph.D. '''


import sys
import platform
import pandas
import importlib
import datetime

def versions(import_list):
    '''input list of imports, return their versions in a pandas Dataframe'''
    names = ['Python', '']
    data  = [sys.version, ' ']
    for import_ in import_list:
        imodule = importlib.import_module(import_)
        names.append(import_)
        data.append(imodule.__version__)
    names.extend(['', 'os', 'processor', 'Date/Time'])
    data.extend([' ', platform.platform(), platform.processor(),
                 str(datetime.datetime.now())[0:19]])
    return pandas.DataFrame(data, index=names, columns=['version'])