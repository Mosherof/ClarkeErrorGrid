import ClarkeErrorGrid as EGA
import random
import math
import numpy as np

def make_data():
    #Generates Random CGM and and Reference data
    #Creates an array of about 300 data points and uses log scale to create a clustering 
    cgm=[np.random.uniform(0,400)/math.log(n+2) + 45 for n in range(300)]
    cgm_temp=[]
    for i in cgm:
        if i < 400:
            cgm_temp.append(i)
    cgm=cgm_temp
    
    #Adds noise to CGM array to create reference
    reference = []
    for n in range(len(cgm)):
        reference.append(np.random.normal(loc=cgm[n], scale=cgm[n]**.6, size=None))
    return [cgm, reference]

data = make_data()
fig, zone = EGA.clarke_error_grid(data[0], data[1], "CGM")
fig.savefig("example_EGA.png")
