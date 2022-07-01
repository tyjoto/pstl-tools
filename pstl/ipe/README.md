# Interactive Plot Editor (IPE)
Allows one to:
1. Read in a csv file
2. Shows Plot
3. Input command to edit file/or quit (go to step 6)
4. Add edits via pre-organized algrithms
5. Return to step 2
6. Save file(Y/n)/Where?

## Required Packages
- numpy (numpy.loadtxt() is used to read in csv)
- basic-plts (see tyjoto/basic-plts.git)


## How to run

```
python -m ipes.py <-additional flags> [options]
```

### Optional flags
- -f, --filename	Data file to use
- -s, --savename	Save plot and new csv with this name
- -d, --delimiter	Deliminatior for csv file
- -r, --skiprows	Skip # of rows


## Potential Commands
- t, title		Title of plot
- v, vertical-line	Add vertical line
- h, horizontal-line	Add horizontal line
- c, change-axes	Change axes limits
	- x		Edit only the x limits
	- y		Edit only the y limits
	- xy		Edit both x and y limits
- a, add-fit		Add linear, semilog, log fits (auto -- style line)
	- l, linear	Linear fit
	- y, semilogy	Semilogy fit
	- x, semilogx 	Semilogx fit
	- e, logfit	Log fit
- l, legend		Legend location
- x, xlabel		Define Xlabel
- y, ylabel		Define Ylabel



