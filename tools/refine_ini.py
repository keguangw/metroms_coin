#!/usr/bin/python

import os
from netCDF4 import Dataset as nc

app = 'barents-2.5km'
initdir = os.environ.get('METROMS_TMPDIR') + '/' + app + '/cice/rundir/restart'

infile = initdir + '/ice.restart_file'
inifile = open(infile).readline().strip()

print inifile

f = nc(inifile,'r+')
aicen_id = f.variables['aicen']
vicen_id = f.variables['vicen']
vsnon_id = f.variables['vsnon']

aicen = aicen_id[:]
vicen = vicen_id[:]
vsnon = vsnon_id[:]

aicen[vicen < 0.001] = 0.
vicen[vicen < 0.001] = 0.
vsnon[vicen < 0.001] = 0.
vsnon[vsnon < 0.001] = 0.

aicen_id[:] = aicen
vicen_id[:] = vicen
vsnon_id[:] = vsnon

f.close()

