# -*- coding: utf-8 -*-
import segyio
import math
import numpy as np 
#read information of seismic data
###############################################################################

def getSEGYInformation(filename):
    print("### Get Datafile Informaton:")
    print("    Data file --> [%s]"%(filename))
  
    mTrace = 0
    nTrace = 0
    nSample = 0
    startT = 0
    deltaT = 0
    sortCode = 0
    formatFlag = 0
    
    with segyio.open(filename,"r",ignore_geometry = True) as f:
        f.mmap()
        mTrace = f.tracecount
        nTrace = f.bin[segyio.BinField.Traces]
        nSample = f.bin[segyio.BinField.Samples]
        deltaT = f.bin[segyio.BinField.Interval]
        sortCode = f.bin[segyio.BinField.SortingCode]
        formatFlag = f.bin[segyio.BinField.Format]
        f.close()
        
    return (mTrace,nTrace,nSample,startT,deltaT,sortCode,formatFlag)
#End of getSEGYInformation

#read Seismic Data
###############################################################################
def readSEGYData(filename):
    print("### Reading SEGY-formatted Seismic Data:")
    print("    Data file --> [%s]" % (filename))
    
    nTrace = 0
    nSample = 0
    startT = 0
    deltaT = 0
    
    with segyio.open(filename,"r",ignore_geometry = True) as f:
        f.mmap()
        nTrace = f.tracecount
        nSample = f.bin[segyio.BinField.Samples]
        deltaT = f.bin[segyio.BinField.Interval]
        
        print("### Number of Trace   = %d" %(nTrace))
        print("### Number of Samples = %d" %(nSample))
        print("### Start Sample      = %d" %(startT))
        print("### Sampling Rate     = %d" %(deltaT))
              
        print("====================================")
        print("    Trace    X-coord    Y-coord")
        print("====================================")
        for i in range(0,nTrace,math.floor(nTrace/10)):
            id = f.header[i][segyio.TraceField.TRACE_SEQUENCE_LINE]
            x = f.header[i][segyio.TraceField.GroupX]
            y = f.header[i][segyio.TraceField.GroupY]
            print("    %8d%12.2f%12.2f"%(id,x,y))
        print("====================================")
        
        mySeis = np.zeros((nTrace,nSample),dtype = np.float32)
        for i in range(nTrace):
            for j in range(nSample):
                mySeis[i][j] = f.trace[i][j]
        f.close()
        
    return (mySeis)
#End of readSEGYData