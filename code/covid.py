# First we import packages for plotting and working with data
from matplotlib.pyplot import *
from numpy import *


# We load our data
IRD_feb = loadtxt('../data/feb.txt',dtype=int)
IRD_mar = loadtxt('../data/mar.txt',dtype=int)
IRD_apr = loadtxt('../data/apr.txt',dtype=int)
IRD_may = loadtxt('../data/may.txt',dtype=int)

# Let us isolate infected, recovered, deceased cases
# Remark: \ is for multiline code separation
act_num = concatenate((IRD_feb[:,0], IRD_mar[:,0], \
            IRD_apr[:,0], IRD_may[:,0]))
rec_num =  concatenate((IRD_feb[:,1], IRD_mar[:,1], \
            IRD_apr[:,1], IRD_may[:,1]))
dec_num =  concatenate((IRD_feb[:,2], IRD_mar[:,2], \
            IRD_apr[:,2], IRD_may[:,2]))



# How many more infections each day?
dact_num = (act_num[2:] - act_num[:-2])/2

# How many more recovered each day?
drec_num = (rec_num[2:] - rec_num[:-2])/2

# How many more deceased each day?
ddec_num = (dec_num[2:] - dec_num[:-2])/2


# How is the increase or decrease of infections per day changing?
ddact_num =  (-2*act_num[1:-1] + act_num[:-2] + \
                act_num[2:])


# Is the rate of change of recovered/deceased related to infection 
# numbers?
drec_act = drec_num/act_num[1:-1] 
ddec_act = ddec_num/act_num[1:-1]



