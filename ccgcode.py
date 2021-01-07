#!/usr/bin/python
filenames = ['isolation.gcode','drill.gcode','rubout.gcode','cutout.gcode']
tools = ['Contour','Drilling','Rubout','Routing']

# copies contents of Carbide Copper excluding tool change codes, into
# a gcode file 
def deleteToolchange():
	with open('copper.nc') as filein, open('gcode.txt', 'w') as fileout:
		for line in filein:
			# replaced variable holding string with the string -> don't need to store 1 time use variable
			# if see this string remove it but add the rest of the line (otherwise error)
			if "G01F200" in line:
				fileout.write(line[7:])
			elif "M06" not in line:
				fileout.write(line)

# copies initial state gcode into separate file for each toolpath
def copyStates(gcode,splitGcode):
	with open(gcode) as filein, open(splitGcode,'w') as fileout:
		for line in filein:
			# same as above to save memory
			if "(  )" not in line:
				fileout.write(line)
			else:
				break

# copies gcode for each toolpath into corresponding toolpath file
# replaces default Zdepth with new ZDepth if user wants
def copyGcode(gcode,splitGcode,tool):
	# ZDepth of isolation & rubout toolpaths I found through testing various
	# settings will either be set by CC to -0.100 or -0.200mm.
	# Both are too deep for me on the Carvey so below I give the option to change
	# thorugh user input
	zDepthFound = False
	oldZDepth1 = "Z-0.100"
	oldZDepth2 = "Z-0.200"
	newZDepth = "Z" #will be set based on user input
	with open(gcode) as filein, open(splitGcode,'a') as fileout:
		for line in filein:
			if tool in line:
				fileout.write(line)
				for line in filein:
					if '(' in line or 'M30' in line: break
					if oldZDepth1 in line:
						if not zDepthFound:
							print ("Current Z-depth in your " + splitGcode +" file is set to " + oldZDepth1 + ".")
							changeZ = input("Would you like to change it? (yes or no) ")
							if changeZ == "yes":
								newZ = input("Type value including -. ")
								newZDepth = newZDepth + newZ
							else:
								newZDepth = oldZDepth1
							zDepthFound = True
						line= line.replace(oldZDepth1, newZDepth)
					if oldZDepth2 in line:
						if not zDepthFound:
							print ("Current Z-depth in your " + splitGcode +" file is set to " + oldZDepth2 + ".")
							changeZ = input("Would you like to change it? (yes or no) ")
							if changeZ == "yes":
								newZ = input("Type value including -. ")
								newZDepth = newZDepth + newZ
							else:
								newZDepth = oldZDepth2
							zDepthFound = True
						line= line.replace(oldZDepth2, newZDepth)
					fileout.write(line)
		fileout.write("M30")

deleteToolchange()
for files in filenames:
	copyStates("gcode.txt",files)
for tool,filename in zip(tools,filenames):
	copyGcode('gcode.txt',filename,tool)
