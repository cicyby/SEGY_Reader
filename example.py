# -*- coding: utf-8 -*-
import time
from kernel import reader
from kernel import shower

if __name__=='__main__':
    x0 = 60
    y0 = 32
    Width = 1000
    Height = 600
    scale = 3.0
    
    mySeisFile = './TestData/z_ffid7.segy'
    myPlot = "SEIS.html"
    myTitle = "Seismic Section"
    
    start = time.time()
    
    (mTrace,nTrace,nSample,t0,dt,sort,kfc) = reader.getSEGYInformation(mySeisFile)
    seis = reader.readSEGYData(mySeisFile)
#    print("### Seismic Dataset Parameters:")
#    print("    Number of  Traces  = %d(%d)"%(mTrace,nTrace))
#    print("    Number of  Samples = %d"%(nSample))
#    print("    Start Sample  (ms) = %d"%(t0))
#    print("    Sampling Rate (us) = %d"%(dt))
#    print("    Sorting Code       = %d"%(sort))
#    print("    Format  Code       =%d"%(kfc))
    
    shower.outputSeisSVG(myPlot,nTrace,nSample,t0,dt,seis,x0,y0,Width,Height,scale,1)
    shower.plotSeismicMap(myTitle,nTrace,nSample,t0,dt,seis,Width,Height,scale,0)
    shower.plotSeismicMap(myTitle,nTrace,nSample,t0,dt,seis,Width,Height,scale,1)
    
    now = time.time()
    dtime = now - start
    print("### Elapsed time = %.1f seconds"%(dtime))
