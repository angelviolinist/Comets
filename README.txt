Hello, this is an overview of the contents of this folder and what the scripts should do

First part of the project, all the JPL HORIZONS files, are everything besides the icosahedron directory.
My workflow was JPL HORIZONS email/telnet --> save as .txt from email --> use .txt file in one of many python scripts that would output a graph or excel sheet
At first the criteria was JFCs (jupiter family comets) between years 2025-2038, but later on criteria became halley type comets and long period comets between 1990-2020.
filepaths must all be changed for program to run!!

jupiter_family
	The .txt files (except for full_comet_list.txt) are copied online from a full list of all jupiter family comets.
	get_comets.py script was used to extract just the comet names from these .txt files.
	full_comet_list.txt was used for my input for the HORIZONS email interface.
	table_approaches.xlsx was first version of excel file, please ignore.
	
halley_type
	Halley_list.txt is copied online from full list of halley type comets.
	
long_period
	list.txt is copied online from full list of long period comets.
	analyze_list.py was used to get input for the HORIZONS email interface.
	
emails
	Meant for close_approaches_plot.py, these are raw .txt files that store data for the three classes of comets. 1.5_jupiter is for JFCs that come within 1.5 AU of Earth while jupiter is for JFCs that come within 1 AU of Earth.
	
telnet
	Meant for all_approaches_plot.py, these are raw .txt files that store data for the three classes of comets.
	
position
	Meant for orbit_2D_plot.py and orbit_2D_plot.py, these are raw .txt files that store data for the three classes of comets.
	
big_email.txt
	This is a messy .txt file that has the general format of what my queries to the HORIZONS email interface look like.

find_all.py
	This script looks through the emails/jupiter .txt files to find all close approaches of a JFC (since JFCs have smaller orbits, multiple close approaches can occur within the time range) and save the distances if the minimum is within 1 AU.

inclination.py
	Meant for long period comets only, outputs a plot of each comet's close approach date and inclination angle.
	Command from terminal is "python3 inclination.py"

all_approaches_plot.py
	This python script plots each comet's close approach rate (logscale) to their distance from Earth or Sun, depending on what the query for HORIZONS was. Each comet has data for 6 months before and after closest approach.
	Command from terminal is "python3 all_approaches_plot.py [comet name or 'all' to select all comets in one class] [comet class] [optional: logspace or linspace axes]"
	ex. python3 all_approaches_plot.py all jupiter
	
close_approaches_plot.py
	This python script plots each comet's close approach date to their distance from Earth or Sun, depending on what the query for HORIZONS was.
	Command from terminal is "python3 close_approaches_plot.py [comet name or 'all' to select all comets in one class] [comet class (jupiter, halley, long)] [optional: logspace or linspace axes]"
	ex. python3 close_approaches_plot.py all halley
	
orbit_2D_plot.py
	This python script plots the orbits of comets projected on the ecliptic plane. Script was misbehaving when I last tried the all comets option right before my symposium, so I haven't had time to debug that. It worked perfectly fine with the all comets and single comet options before, unsure what changed.
	Command from terminal is "python3 orbit_2D_plot.py [comet name or 'all' to select all comets in one class] [comet class (jupiter, halley, long)]". Axes are in units of AU.
	ex. python3 orbit_2D_plot.py all halley"
	
orbit_3D_plot.py
	A work in progress, didn't really have a use for it so was discarded. Idea is to do a 3D plot of the orbit. Couldn't get orbits of multiple comets at once, but single comet plots worked.
	
table_generator.py
	This python script takes all the data from a single directory and outputs relevant data as a spreadsheet.
	Command from terminal is "python3 table_generator.py [comet class (jupiter, halley, long)]"
	ex. python3 table_generator.py long
	
1.5_jupiter comet table 2021-03-05 15:55:25.xlsx
clean_1.5_jupiter comet table 2021-03-05 15:55:41.xlsx
jupiter comet table 2021-02-18 18:11:12.xlsx
halley_full comet table 2021-03-05 15:59:01.xlsx
long comet table 2021-02-18 18:11:00.xlsx
	These are all excel spreadsheets generated from table_generator.py. 1.5_jupiter comet table is a sheet where the criteria is within 1.5 AU of Earth instead of 1 AU (that would be jupiter comet table). clean_1.5_jupiter is content wise same as 1.5_jupiter, except the repeating comet names are removed for less repetition.

archive
	Old files, not used.
____________________________________________________________________
Second part of the project is all in the icosahedron directory.

PLEASE NOTE: to run the part of the program that generates .vtk files, jigsawpy has to be installed somehow, refer to https://github.com/dengwirda/jigsaw-python for details. I used a conda environment. Paraview is a free software that can view .vtk files.

icosahedron
	out and tmp directories are left over from the github repository, some files are automatically saved to those directories after the program runs. the mesh.msh file is where I get my information on vertice locations.
	
ico.vtk, ico1.vtk, elip_2_15_15.vtk
	ico files are icosahedral (like sphere) while the elip .vtk file is an ellipsoid.
	
run.py
	This script has to be run with jigsawpy installed. Line 20 are the radii values. The numbers at ines 31 and 32 have to be changed for different mesh resolutions.
	
parse_points.py
	Formula from here: https://www.aanda.org/articles/aa/full_html/2016/04/aa27889-15/aa27889-15.html
	This script has many parts. First is getting location information on all verticies and faces. Next, I get normal vectors from all the faces and make sure they're pointing outwards. Next secion is completely commented out, it was only used to make sure the mesh and normal vectors are what you expect them to be. After that is the assumed sun direction, can be easily modified if necessary. Then some spherical harmonics calculation (had to hardcode all the formulas). Last, it puts all the data on a heatmap. No one has checked my work for this, so please please make sure the data points map to where you expect them to be on a heatmap.
	
____________________________________________________________________
Symposium.pptx
	My slides for the Virtual Intern Symposium
	
	
If you have any questions, feel free to contact me at angelviolinist718@gmail.com
	