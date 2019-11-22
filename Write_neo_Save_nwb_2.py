import neo
from neo import *
import quantities as pq
import numpy as np


#blocks = []
#num_segment=1 # number of segment
#segment_durations = [5*pq.s, 13*pq.s]
#
#for ind in range(2): # loop on blocks
#    blk = Block(name='block_%s' %ind)            
#
#    for seg_num in range(num_segment): # loop on segments
#        seg = Segment(name=f'Seg {seg_num}')                
#        blk.segments.append(seg)
#
#        for seg_index in range(num_segment): # loop on ChannelIndex
#            sampling_rate = 80*pq.Hz
#            num_channel = 2
#            duration = segment_durations[seg_index]
#            length = int((sampling_rate*duration).simplified)
#            np_sig = np.random.randn(length, num_channel).astype('float32')
#
#            anasig = AnalogSignal(np_sig, units='cm', sampling_rate=sampling_rate)                    
#            anasig.annotate(data_type='tracking')
#            anasig.array_annotate(channel_names=['lfp_{}'.format(ch) for ch in range(num_channel)])
#            blk.segments[seg_index].analogsignals.append(anasig) #   
#        blocks.append(blk)






blocks = []
for ind in range(2): # 2 blocks
    blk = neo.Block(name='%s' %ind)
    blocks.append(blk) ########
    
    for ind in range(3): # 3 Segment
        seg = Segment(name='segment %d' % ind, index=ind)
        blk.segments.append(seg)
    
    for ind in range(2):  # 2 ChannelIndex
     chx = ChannelIndex(name='Array probe %d' % ind, index=np.arange(64))
     blk.channel_indexes.append(chx)
    
    for seg in blk.segments: # AnalogSignal objects
        for chx in blk.channel_indexes:
         a = AnalogSignal(np.random.randn(10000, 64)*pq.nA, sampling_rate=10*pq.kHz)
         chx.analogsignals.append(a)
         seg.analogsignals.append(a)

blocks





# Save the file
filename = '/home/elodie/env_NWB_py3/my_notebook/my_first_test_neo_to_nwb_test_NWBIO.nwb'
w_file = NWBIO(filename=filename, mode='w') # Write the .nwb file
print("w_file = ", w_file)
blocks = w_file.write(blk)
#print("blocks = ", blocks)

print("   ")

r_file = NWBIO(filename, mode='r')
print("r_file = ", r_file)
print("r_file.read() = ", r_file.read())
