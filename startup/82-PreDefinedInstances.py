from ophyd import EpicsMotor
import collections
import time
import math


#Definition of SIX specific classes
    

class DiagAndSingleAxisMaskClass(PreDefinedPositions):
    '''
    A class that is used to defien diagnostic untis and single axis mask units. It is a child of the 
    PreDefinedPositions class which allows for defining a set of pre-defined positions, in addition 
    these have a single, "y", axis that is used to move to the different locations.
    '''

    y = Cpt(EpicsMotor, '')

class OpticsWheelClass(PreDefinedPositions):
    '''
    A class that is used to defien diagnostic untis and single axis mask units. It is a child of the 
    PreDefinedPositions class which allows for defining a set of pre-defined positions, in addition 
    these have a single, "y", axis that is used to move to the different locations.
    '''
    
    th = Cpt(EpicsMotor, '')



#Definition of Devices
    
            
m5mask = DiagAndSingleAxisMaskClass('XF:02IDD-ES{Msk:Mir5-Ax:Y}Mtr',
                         locations = {'open':['y',54], 'thin':['y',34], 'wide':['y',21], 'thru':['y',8],},
                         vis_path_options={'fig_size':[10,10],'axis_labels':['arbitrary axis','m5mask_y'],
                                           'pos':{'open':[0,54],'thin':[0,34],'wide':[0,21],'thru':[0,8]}},
                         name = 'm5mask')

m3diag = DiagAndSingleAxisMaskClass('XF:02IDC-OP{Mir:3-Diag:12_U_1-Ax:1}Mtr',
                         locations = {'diode':['y',-76.4],'grid':['y',-97.5], 'out':['y',-1],
                                      'yag':['y',-49.4,'cam.roi1_minx',582,'cam.roi1_sizex',44,'cam.roi1_miny',
                                             540,'cam.roi1_sizey',225]},
                         vis_path_options={'fig_size':[10,10],'axis_labels':['arbitrary axis','m3diag_y'],
                                           'pos':{'diode':[0,-76.4],'grid':[0,-97.5],'out':[0,-1],'yag':[0,-49.4]}},
                         cam_list = [m3_diag_cam], qem_list = [qem05],
                         name = 'm3diag')

gcdiag = DiagAndSingleAxisMaskClass('XF:02IDC-OP{Mir:4-Diag:16_U_1-Ax:1}Mtr',
                         locations = {'diode':['y',-71.4], 'yag':['y',-43.4], 'grid':['y',-95.4], 'out':['y',-1]},
                         vis_path_options={'fig_size':[10,10],'axis_labels':['arbitrary axis','gcdiag_y'],
                                           'pos':{'diode':[0,-71.4],'grid':[0,-95.4],'out':[0,-1],'yag':[0,-43.4]}},
                         cam_list = [gc_diag_cam], qem_list = [qem07],  
                         name = 'gcdiag')

espgmmask = DiagAndSingleAxisMaskClass('XF:02IDD-ES{Msk:Mono2-Ax:Y}Mtr',
                         locations= {'yag':['y',-43.4],'out':['y',0]},
                         vis_path_options={'fig_size':[10,10],'axis_labels':['arbitrary axis','espgm_y'],
                                           'pos':{'out':[0,0],'yag':[0,-43.4]}},
                         cam_list = [sc_4],
                         name='espgmmask')

ow = OpticsWheelClass('XF:02IDD-ES{Mir:5-Ax:S1_2T}Mtr',
                         locations={'m5in':['th',-30],'m5out':['th',-90],'yag_reflected':['th',100.3],
                                    'yag_postcryo':['th',-26.5],'yag_precryo':['th',-209.7],'door':['th',113],
                                    'diode':['th',68.9]},
                         vis_path_options={'fig_size':[20,20],'axis_labels':['cryo_x','cryo_z'],
                                           'pos': {'diode': [-0.14953534344370978, 0.9887563810470058],
                                           'door': [-0.7954734808548956, 0.6059884002657115],
                                           'm5in': [0.9999862922474267, -0.005235963831419821],
                                           'm5out': [0.4954586684324072, -0.8686315144381914],
                                           'yag_postcryo': [0.998440764181981, 0.05582150499316376],
                                           'yag_precryo': [-1.0, 0.0],
                                           'yag_reflected': [-0.6427876096865393, 0.7660444431189781]} },
                         name='ow')
    
#defining some parameters for the visulization of the paths

###BELOW IS USED TO GENERATE THE VIS_PATH_OPTIONS "POS" DICTIONARY FOR THE OW
#new_dict={}
#for key in ow.locations.keys():
#    new_dict[key]=[-1* math.cos(math.radians(ow.locations[key][1]+209.7)),math.sin(math.radians(ow.locations[key][1]+209.7))]



#Definition of Device Groups

diagnostics = PreDefinedPositionsGroup([m3diag,gcdiag],{'test_location':['m3diag','out','gcdiag','out']},name='diagnostics')








#Below is some carry over definitions for devices that should be defined above but which are yet to be.


m4_diag1 = EpicsMotor('XF:02IDC-OP{Mir:4-Diag:17_U_1-Ax:1}Mtr',name='m4_diag1')
m4_diag2 = EpicsMotor('XF:02IDC-OP{Mir:4-Diag:17_U_1-Ax:2}Mtr',name='m4_diag2')
m4_diag3 = EpicsMotor('XF:02IDC-OP{Mir:4-Diag:17_U_1-Ax:3}Mtr',name='m4_diag3')

m5_RPD = EpicsMotor('XF:02IDD-ES{Mir:5-Ax:RPD}Mtr', name='m5_RPD')

SC_QPD = EpicsMotor('XF:02IDD-ES{SC:1-Ax:QPD}Mtr', name='SC_QPD')
SC_IO = EpicsMotor('XF:02IDD-ES{SC:1-Ax:IO}Mtr', name='m5_RPD')
