# CarbideCopperGcodeConverter
Prepares Carbide Copper gcode for use with Easel (Carvey)<br />
<a href="http://copper.carbide3d.com/">Carbide Copper</a> has some limitations for use with Carvey. 1) Gcode output is contained in one file with toolchange codes, which Easel can't do. 2) Given copper blank thickness of 1.58mm Z-depth is fixed at -0.2mm and can't be modified whereas I find that is too deep for Carvey and needs to be more like -0.01 or -0.02mm. Note: This software assumes gcode from Carbide Copper is generated in mm not inches!<br />
Also note: This software is provided as is and you should test in Easel under controlled conditions before putting bits to blanks you don't want to waste.
Run from terminal this software:
1) opens downloaded 'copper.nc' gcode file (must be in same folder) and copies all but toolchange codes into new text file
2) copies initial settings gcode into 4 new files; isolation.gcode, rubout.gcode, drilling.cgode, cutout.gcode.
3) finds toolpaths for each file in the gcode.txt file and copies it into the appropriate gcode file.
4) I find Carbide Copper sets the ZDepth for isolation and rubout toolpaths too deep for me on the Carvey--either -0.100 or -0.200--so in copying isolation and rubout gcode user is given the option to change them just for those two. For me -0.010 is better.
