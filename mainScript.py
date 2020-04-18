import os                                                                       
from multiprocessing import Pool                                                
                                                                                
                                                                                
processes = ('cameraTest2.py','lightsAmbulanceTest.py')
                                                                                
def run_process(process):                                                             
    os.system('python3 {}'.format(process))                                       
                                                                                
print("Starting....")                                                     
pool = Pool(processes=2)
print("Running....")
pool.map(run_process, processes)
