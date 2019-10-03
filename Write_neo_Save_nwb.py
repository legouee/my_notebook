import neo
from neo import *
from neo.core import (Block, Segment, ChannelIndex, AnalogSignal)
from quantities import nA, kHz
import quantities as pq
import numpy as np

# Create a Block with 3 Segment and 2 ChannelIndex objects
blk = Block()
for ind in range(3):
    seg = Segment(name='segment %d' % ind, index=ind)
    print("seg = ", seg)
    blk.segments.append(seg)

for ind in range(2):
    chx = ChannelIndex(name='Array probe %d' % ind, index=np.arange(64))
    blk.channel_indexes.append(chx)

# Populate the Block with AnalogSignal objects
for seg in blk.segments:
    for chx in blk.channel_indexes:
        a = AnalogSignal(signal=[1, 2, 3], units='V', t_start=np.array(3.0)*pq.s, sampling_rate=1*pq.Hz)
        print("a = ", a)
        print("chx.name = ", chx.name) # ChannelIndex
        print("seg.name test = ", seg.name) # Segment
        print("a.name test = ", a.name) # AnalogSignal
        chx.analogsignals.append(a)
        seg.analogsignals.append(a)
        

# Save the file
# Create a reader
filename = '/home/elodie/env_NWB_py3/my_notebook/my_first_test_neo_to_nwb.nwb'
w_file = neo.io.NWBIO(filename, 'w')
print("w_file = ", w_file)
w_file.write_block(blk)


