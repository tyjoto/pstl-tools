import numpy as np

import basic.basic_plt as bplt
import basic.basic_fit as bfit

import helpprint as h

def potential_commands_axes_limits(ax):

    repeat = True
    while repeat:
        repeat = False
        s = input("\tPlease enter which axes to change\n\t>>")
        if s == "x":
            xmin = float(input("\tPlease enter xmin\n\t>>"))
            xmax = float(input("\tPlease enter xmax\n\t>>"))
            xlim = np.array([xmin,xmax])
            ax = bplt.change_limits(ax,xlim=xlim,save=None,close=False)
        elif s == "y":
            ymin = float(input("\tPlease enter ymin\n\t>>"))
            ymax = float(input("\tPlease enter ymax\n\t>>"))
            ylim = np.array([ymin,ymax])
            ax = bplt.change_limits(ax,ylim=ylim,save=None,close=False)
        elif s =="xy":
            xmin = float(input("\tPlease enter xmin\n\t>>"))
            xmax = float(input("\tPlease enter xmax\n\t>>"))
            xlim = np.array([xmin,xmax])
            ymin = float(input("\tPlease enter ymin\n\t>>"))
            ymax = float(input("\tPlease enter ymax\n\t>>"))
            ylim = np.array([ymin,ymax])
            ax = bplt.change_limits(ax,xlim=xlim,ylim=ylim,save=None,close=False)
        elif s == "":
            pass
        elif s == "h" or "help":
            h.printhelplimits()
            repeat = True
        else:
            print("\n\t'%s' is an unknown command please try again."%(s))
            print("\tEnter h for help or enter nothing to exit.\n")
            repeat = True
    return ax

def getpart(x,y):
    xmin = float(input("\tPlease enter xmin\n\t>>"))
    xmax = float(input("\tPlease enter xmax\n\t>>"))

    # INSERT HERE algo to find indices
    imin = np.where(x>=xmin)[0][0]
    imax = np.where(x<=xmax)[0][-1]

    # INSERT HERE make fit
    xpart = x[imin:imax]
    ypart = y[imin:imax]

    return xpart,ypart

def potential_commands_add_fits(ax,x,y):

    plot = True
    repeat = True

    while repeat:
        repeat = False
        s = input("\tPlease enter which type of fit\n\t>>")
        if s == "l":
            # linear fit
            xpart,ypart = getpart(x,y)
            fit = bfit.linearfit(xpart,ypart)
        elif s == "y":
            # semilogy fit
            xpart,ypart = getpart(x,y)
            fit = bfit.semilogyfit(xpart,ypart)
        elif s =="x":
            # semilogx fit
            xpart,ypart = getpart(x,y)
            pass # (future update)
        elif s =="e":
            # log fit
            xpart,ypart = getpart(x,y)
            pass # (future update)
        elif s == "":
            plot = False
            pass
        elif s == "h" or s == "help":
            h.printhelpfits()
            plot = False
            repeat = True
        else:
            print("\n\t'%s' is an unknown command please try again."%(s))
            print("\tEnter h for help or enter nothing to exit.\n")
            plot = False
            repeat = True
    if plot:
        xfit = fit['xfit']
        yfit = fit['yfit']
        label = fit['label']
        ax = bplt.add_data(ax,xfit,yfit,label=label,save=None,close=False)

    return ax

def getscaletype():
    # get scale type
    redo = True
    while redo:
        redo = False
        stype = input("\tPlease enter scale type\n\t>>")
        if stype == "l" or stype == "linear":
            scale = 'linear'
        elif  stype == "e" or stype == "log":
            scale = 'log'
        elif stype == "":
            scale = None
            pass
        elif stype == "h" or stype == "help":
            h.printhelpscales()
            redo = True
        else:
            print("\n\t'%s' is an unknown command please try"+\
                    "again."%(stype))
            print("\tEnter h for help or enter nothing to exit.\n")
            redo = True
    return scale


def potential_commands_change_scales(ax):

    repeat = True

    while repeat:
        repeat = False
        s =  input("\tPlease enter which scale to change\n\t>>")

        # scale type and axes given
        if s == "xl" or s == "xe":
            if s == "xl":
                scale = 'linear'
            elif s == "xe":
                scale = 'log'
            else:
                print("ERROR in potential_commands_change_scales")
            ax = bplt.change_xscale(ax,scale,save=None,close=False)
        elif s == "yl" or s == "ye":
            if s == "yl":
                scale = 'linear'
            elif s == "ye":
                scale = 'log'
            else:
                print("ERROR in potential_commands_change_scales")
            ax = bplt.change_yscale(ax,scale,save=None,close=False)
        elif s == "xyl" or s == "xye":
            if s == "xyl":
                scale = 'linear'
            elif s == "xye":
                scale = 'log'
            else:
                print("ERROR in potential_commands_change_scales")
            ax = bplt.change_xscale(ax,scale,save=None,close=False)
            ax = bplt.change_yscale(ax,scale,save=None,close=False)

        # axes given, scale was not
        else:
            if s == "x"  or s == "xscale":
                # changing the x-scale only
                scale = getscaletype()
                if scale is not None:
                    ax = bplt.change_xscale(ax,scale,save=None,close=False)
            elif s == "y" or s == "yscale":
                # changing the y-scale only
                scale = getscaletype()
                if scale is not None:
                    ax = bplt.change_yscale(ax,scale,save=None,close=False)
            elif s == "xy":
                # changing the x AND y scales
                scale = getscaletype()
                if scale is not None:
                    ax = bplt.change_xscale(ax,scale,save=None,close=False)
                    ax = bplt.change_yscale(ax,scale,save=None,close=False)
            elif s == "":
                pass
            elif s == "h" or s == "help":
                h.printhelpscales()
                repeat = True
            else:
                print("\n\t'%s' is an unknown command please try again."%(s))
                print("\tEnter h for help or enter nothing to exit.\n")
                repeat = True

    return ax
