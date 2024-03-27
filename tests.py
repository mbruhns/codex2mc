import os 
from pathlib import Path
from operator import itemgetter
import argparse
import logging
from argparse import ArgumentParser as AP
from os.path import splitext
from pathlib import Path

parser=argparse.ArgumentParser()
cycles_dir=Path('C:/Users/vp232003/repos/test_data/macsima_v2')
 
def pull_all_cycles( cycles_path=cycles_dir):
    folders=list(filter(lambda x: 'Cycle' in x ,os.listdir( cycles_path )))
    aux_list={ int(f.split('Cycle_')[-1]):f for f in folders } 
    folders=dict( sorted(aux_list.items(),reverse=False) )  
    #aux_list=sorted(aux_list,key=itemgetter(1),reverse=False)
    return folders

cycles_list=pull_all_cycles(cycles_dir)

def cycle_info(cycle_no=1,cycles_path=cycles_dir ,cycles=cycles_list,ref_marker='DAPI'):

    workdir=cycles_path / cycles[cycle_no]
    images=list(filter(lambda x: x.endswith('.tif'),os.listdir(workdir)))
    signal_images=list( filter(lambda x: '_S_' in x ,images) )
    bleach_images=list( filter(lambda x: '_B_' in x ,images) )
    print(signal_images)
    print(bleach_images)
    

    cycle_info={'img_full_path':[],
                'image':images,
                'marker':[],
                'filter':[],
                'rack':[],
                'well':[],
                'roi':[],
                'fov':[],
                'exposure':[]
               }

#cycle_info()

parser.add_argument(
        "-a",
        "--autotune",
        dest="autotune",
        action="store_true",
        required=False,
        help="Flag to autotune the parameters [default=True].")

args=parser.parse_args()



#name='C-001_S-000_S_DAPI_R-01_W-A01_ROI-01_A-DAPI.tif'
#full_name=name.replace('_S_','_B_')
print(args.autotune)









































































































































































































































































































