# First we import packages for plotting and working with data
from matplotlib.pyplot import *
from numpy import *


# We load our data
IRD_feb = loadtxt('../data/feb.txt',dtype=int)
IRD_mar = loadtxt('../data/mar.txt',dtype=int)
IRD_apr = loadtxt('../data/apr.txt',dtype=int)
IRD_may = loadtxt('../data/may.txt',dtype=int)

# Let us isolate infected cases
# Remark: \ is for multiline code separation
act_num = concatenate((IRD_feb[:,0], IRD_mar[:,0], \
            IRD_apr[:,0], IRD_may[:,0]))



