#!/usr/bin/env python

# Dakota will execute this script as
#   dakotabeam.py params.in results.out
# The command line arguments will be extracted by dakota.interfacing automatically.

import sys
sys.path.append("c:/tools/dakota-6.13.0/share/dakota/Python")
sys.path.append("c:/users/oliver/dakota_gui_workspace/beam")
from beam import Cantilever
# necessary python modules
import dakota.interfacing as di
import math

# Parse Dakota parameters file
params, results = di.read_parameters_file()

# Convert and send to application
beam = Cantilever(params['matname'], 
                  params['L'], 
                  params['h'],
                  params['tw'],
                  params['blf'],
                  params['tlf'],
                  params['buf'],
                  params['tuf'])

# fixed parameters - could read these from a config file
loads = [params['Fdown'], params['Fup']]
res = beam.analyse(loads)  

# for optimisation: g(x) <= 0
res['g_t_uf'] = 1/res['rf_t_uf'] - 1
res['g_t_lf'] = 1/res['rf_t_lf'] - 1
res['g_c_uf'] = 1/res['rf_c_uf'] - 1
res['g_c_lf'] = 1/res['rf_c_lf'] - 1
res['g_lb_uf'] = 1/res['rf_lb_uf'] - 1
res['g_lb_lf'] = 1/res['rf_lb_lf'] - 1
res['g_s_web'] = 1/res['rf_s_web'] - 1
res['g_wb'] = 1/res['rf_wb'] - 1
res['g_lat'] = 1/res['rf_lat'] - 1

# multiobjective: optimise log mass, cost
res['log_mass'] = math.log(res['mass'])
res['log_cost'] = math.log(res['cost'])

# print("Beam analysis complete.")                                                                

# Return the results to Dakota
for key in results:
    results[key].function = res[key]
results.write()


