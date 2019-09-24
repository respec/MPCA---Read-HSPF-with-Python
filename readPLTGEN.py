import pandas as pd
import numpy as np
import datetime

def readPLTGEN(filename):
    ''' Reads HSPF PLTGEN files and creates a DataFrame that can be plotted like HSP2'''

    foundcols = False
    cols = []
    lst = []
    with open(filename) as f:
        for i, line in enumerate(f):
            if i < 25 and 'LINTYP' in line:
                foundcols = True
            elif i < 25 and line[5:].startswith('Time series'):
                foundcols = False
            elif i < 25 and foundcols:
                header =  line[4:30].strip()
                if not header:
                    foundcols = False
                else:
                    cols.append(header)

            if i > 25:
                y, mm, d, h, m = line[4:22].split()
                if int(h) == 24:
                    d = [datetime.datetime(int(y), int(mm), int(d), tzinfo=None)]
                else:
                    d = [datetime.datetime(int(y), int(mm), int(d), int(h)-1, int(m), tzinfo=None)]
                data = [float(x) for x in line[23:].split()]
                lst.append(d + data)

    df = pd.DataFrame(lst)
    df.columns = ['Date'] + cols
    df = df.set_index(['Date'])
    return df