from beam import Cantilever
import pprint

L = 1000  # mm
matname = 'AL7010'
h, tw, blf, tlf, buf, tuf = 140, 2.5, 60, 2.5, 60, 2.5   # mm
F = 1000  # N

# instantiate a beam
beam = Cantilever(matname, L, h, tw, blf, tlf, buf, tuf)
# get response for single load case: a dictionary
res = beam.analyse_single(F)
# print
pprint.pprint(res)  
