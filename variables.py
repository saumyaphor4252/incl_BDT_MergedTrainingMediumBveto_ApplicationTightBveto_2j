# variables
variables['BDTOutput'] = {
     'name': 'WW_against_top_bg_2j(Entry$,0)',
     'range' : ([-1.0,-0.5,-0.25,0.,0.25,0.5,1.0],),
#     'range' : (10,-1,1),
     'xaxis' : 'MVA discriminant WW',
     'fold' : 3,
     'linesToAdd' : ['.L /afs/cern.ch/user/s/ssaumya/Projects/WW_Analysis_Work/WW_Cuts_Optimization/CMSSW_11_1_3/src/PlotsConfigurations/Configurations/WW/FullRunII/Full2017_v7/Systematics_BDT_MergedTrainingWithMediumBveto_ApplicationTightBveto_2j/WW_against_top_bg_2j.C+']
}  #change the path of macro

variables['events']  = {   'name': '1',      
                        'range' : (1,0,2),  
                        'xaxis' : 'events', 
                        'fold' : 3
                        }

variables['mll']  = {   'name': 'mll',
                        'range' : (20, 80,200),
                        'xaxis' : 'm_{ll} [GeV]',
                        'fold' : 3
                        }

variables['mth']  = {   'name': 'mth',
                        'range' : (20, 60,300),
                        'xaxis' : 'm_{T}^{WW} [GeV]',
                        'fold' : 3
                        }

