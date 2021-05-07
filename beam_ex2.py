from beam import Cantilever
import pprint

L = 1000  # mm
matname = 'AL7010'
h, tw, blf, tlf, buf, tuf = 140, 2.5, 60, 5, 60, 5   # mm
forces = (6000, -10000)  # N

beam = Cantilever(matname, L, h, tw, blf, tlf, buf, tuf)
res = beam.analyse(forces)
pprint.pprint(res)  
