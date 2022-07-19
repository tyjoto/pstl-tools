def printhelp():
    print("\n\
 t, title\t\tAdd title of plot\n\
 v, vertical-line\tAdd vertical line\n\
 h, horizontal-line\tAdd horizontal line\n\
 c, change-axes\t\tChange axes limits\n\
 a, add-fit\t\tAdd linear, semilog, log fits (auto -- style line)\n\
 l, legend\t\tLegend location\n\
 x, xlabel\t\tDefine Xlabel\n\
 y, ylabel\t\tDefine Ylabel\n\
 s, scale\t\tChange axes scale\n\
")

def printhelplimits():
    print("\n\
	 x\tEdit only the x limits\n\
	 y\tEdit only the y limits\n\
	 xy\tEdit both x and y limits\n\
     ")

def printhelpfits():
    print("\n\
	 l, linear\tLinear fit\n\
	 y, semilogy\tSemilogy fit\n\
	 x, semilogx\tSemilogx fit\n\
	 e, logfit\tLog fit\n\
     ")

def printhelpscales():
    print("\n\
     x, xscale\tChange x-scale\n\
     y, yscale\tChange y-scale\n\
         \tl, linear\n\
         \te, log\n\
    ")
