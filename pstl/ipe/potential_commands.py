import basic.basic_plt as bplt

import potential_commands_extentions as pce
import helpprint as h



def potential_commands(ax,s,x,y,cnt=True):

    # skip
    if s == "":
        cnt = False

    # call help
    elif s == "h" or s=="help":
        h.printhelp()

    # add title
    elif s == "t" or s == "title":
        title = input("\tPlease enter title\n\t>>")
        ax = bplt.change_title(ax,title,save=None,close=False)

    # add vertical line
    elif s =="v" or s=="vertical-line":
        v = float(input("\tPlease enter x-location for vertical line\n\t>>"))
        l = input("\tPlease enter label for legend\n\t>>")
        ax = bplt.add_vertical(ax,v,label=l,save=None,close=False)

    # Change Axes limits
    elif s == "c":
        h.printhelplimits()
        ax = pce.potential_commands_axes_limits(ax)

    # Add fitted Line
    elif s == "a" or s == "add-fit":
        # extra options (update in the future)
        h.printhelpfits()
        ax = pce.potential_commands_add_fits(ax,x,y)

    # Add xlabel
    elif s == "x" or s == "xlabel":
        xlabel = input("\tPlease enter xlabel \n\t>>")
        ax = bplt.change_xlabel(ax,xlabel,save=None,close=False)

    # Add ylable
    elif s == "y" or s == "ylabel":
        ylabel = input("\tPlease enter ylabel \n\t>>")
        ax = bplt.change_ylabel(ax,ylabel,save=None,close=False)

    # Change Axes Scales
    elif s == "s" or s == "scale":
        h.printhelpscales()
        ax = pce.potential_commands_change_scales(ax)

    # InCase of Input error
    else:
        print()
        print("'%s' is an unknown command please try again."%(s))
        print("Enter h for help or enter nothing to exit.")
    return ax,cnt
