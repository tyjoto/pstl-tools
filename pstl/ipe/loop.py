import numpy as np
import matplotlib.pyplot as plt

import basic.basic_plt as bplt
import basic.numpy_read as bnpr


import potential_commands as pcmd
import helpprint as h

def loop(fname,sname,delimiter,skiprows):

    # check if filename was passed in
    if fname is None:
        fname = input("Please enter path to file name i.e. your/path/to/file.csv\n>>")
    #print("Reading in %s"%(fname))
    #data = readCSV(fname,delimiter,skiprows)
    data = bnpr.importCSV(fname,skiprows,delimiter)
    print("done!")

    # Determine size of data
    # (future update)
    x = data[:,0]
    y = data[:,1]

    # make initial plot
    ax = bplt.setup_standard(x,y,label="Data",save=None,close=False)
    plt.show(block=False)

    # show possible commands
    h.printhelp()

    # Start while loop
    cnt = True
    while cnt:
        s = input("\nPlease enter command or enter nothing to exit\n>>")
        ax,cnt = pcmd.potential_commands(ax,s,x,y)
        plt.draw()

    # end ask to save
    repeat = True
    while repeat:
        repeat = False
        s = input("\nWould you like to save the figure?\n(Y/n)>>")
        if s == "Y":
            if sname is None:
                sname = input("\tPlease enter path/to/file/name.extentions\n\t>>")
            ax = bplt.save_fig(ax,save=sname,close=True)
        elif s == "n":
            s = input("\nAre you sure?\n(Y/n)>>")
            if s == "Y":
                pass
            else:
                repeat = True
        else:
            print("\n\t'%s' is an unknown command please try again."%(s))
            print("\tRetrying.")
            repeat = True

