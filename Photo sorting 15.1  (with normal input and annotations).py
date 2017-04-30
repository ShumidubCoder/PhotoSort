"""
for python 3

 PROGRAM'S GOAL:  automatise move jpeg and raw files from sd card, and give uniq name for all files

- Make project diretory (unic name with date code)
- Copy RAW and JPG to project directory (with name test and dublicates list). Copy can repeat.
- New uniq name (equal for JPG and RAW), with name test
"""

""" INTRO """
def introLigth():
	print (' \n>> Press 1,2 or 3 - for what you need. Or exit program.')
	intro_answer=int(input())

	if intro_answer == 1:
		step_one_pr_dr_name()
		step_one_mk_dr()
	elif intro_answer == 2:
		test_for_blank_fullname()
		step_two_copy_files()
	elif intro_answer == 3:
		step_three_new_name_test()
	else:
		print ("Press 1,2, or 3 - for what you need. Or exit program.")

	introLigth()

def intro():
	print (" \n    1. For make project dir - press 1 \n    2. For copy files from sdcard - press 2 \n    3. For new name for files in project dir - press 3\n \n    >> For exit program close it\n    >> For note - IMG = R+J, Img = J, img = R\n    >> And please test your sdcard for workability\n \n  ")
	intro_answer=int(input())

	if intro_answer == 1:
		step_one_pr_dr_name()
		step_one_mk_dr()
	elif intro_answer == 2:
		test_for_blank_fullname()
		step_two_copy_files()
	elif intro_answer == 3:
		step_three_new_name_test()
	else:
		print ("Press 1,2 or 3 - for what you need. Or exit program.")

	introLigth()

""" imports"""
import datetime
import os
import time
import shutil

""" blanks """
datepr = datetime.datetime.today()
date= datepr.strftime("%Y.%m.%d")
pn= "BLANKS PROJECT " + date
fullname= os.path.join(r'D:\01.Photos', pn)
namedir = {}
foulder = ["jpeg", "raw"] 

def createfoulder(path):
		if not os.path.exists(path):
			os.mkdir(path)

""" 1. MAKE PROJECT DIRECTORY """
def step_one_pr_dr_name(): 
	print ("Step 1. Make project directory")

	proj_name=input("Write the project name:")
	n=int(input("How many days before was project:"))
	
	global datepr
	datepr=datetime.datetime.today() + datetime.timedelta(-n)
	global date
	date = datepr.strftime("%Y.%m.%d")
	global pn
	pn=date+"  "+proj_name
	global fullname
	fullname=os.path.join(r'D:\01.Photos', pn)

def step_one_mk_dr():
	
	createfoulder (fullname)   # create project directory

	for f in foulder:
		createfoulder(os.path.join(fullname, f)) #create foulders for jpeg and raw files 

	print ("Project directory %s have maked\nStep 1 is Done.\n  " %pn)
	

""" 2. COPY FILES """
def test_for_blank_fullname():
	global fullname
	if fullname == os.path.join(r'D:\01.Photos', ("BLANKS PROJECT " + date)):
		z= input("Project directory is not created. Now use directory %s\n For use current directory press 1\n If you want use have created directory early - past path to one or press 2\n OR if you want create new directory - press 3" %fullname)

		if str(z) == "1":
			if not os.path.exists(fullname):
				os.mkdir(fullname)
			for f in foulder:
				createfoulder(os.path.join(fullname, f))

		elif os.path.isdir(z): 
			fullname=z
			for f in foulder:
				createfoulder(os.path.join(fullname, f))  #test

		elif str(z) == "2":
			r=input("Paste path to directory:")
			fullname=z
			for f in foulder:
				createfoulder(os.path.join(fullname, f))

		elif str(z) == "3":
			step_one_pr_dr_name()
			step_one_mk_dr()

		else:
			print (">>> Press 1,2 or 3, depending on what you want")


def step_two_copy_files(): 


	print ("Step 2. Make lists of files and copy files to project folder")



	def copyfun():
		# sdcard=input("Step 2. Write the sdcard drive:")
		sdcard=r"D:\01.Photos\01"

		sdcardfiles=[]   #  список всех файлов с подпапками
		dirsfiles={}

		for d, dirs, files in os.walk(sdcard):
			for f in files:
				sdcardfiles.append(os.path.join(d, f))
				dirsfiles[(os.path.join(d, f))]=d

		jpeglist = filter(lambda x: x.endswith ((".jpg", ".JPG")), sdcardfiles)
		neflist =filter(lambda x: x.endswith ((".nef", ".NEF")), sdcardfiles)
		arwlist=filter(lambda x: x.endswith ((".arw", ".ARW")), sdcardfiles)

		myjpeg=[] # list for added jpeg files with full path 
		myraw=[]  # list for added raw files with full path 

		for f in jpeglist:
			myjpeg.append(f)

		for f in neflist:
			myraw.append(f)

		for f in arwlist:
			myraw.append(f)


		dub_one_jpg=[]
		dub_one_raw=[]
		
		coin_copy=0
    
		for d, dr, files in os.walk(sdcard): 
			for f in filter(lambda x: x.endswith ((".jpg", ".JPG")), files):
				j = d + "\\" + f
				if not os.path.isfile(fullname +"\\"+ "jpeg" +"\\"+ f):
					shutil.copy(j, os.path.join(fullname, "jpeg"))   #copy jpg to project folder from myjpeg
					coin_copy+=1
				elif os.path.isfile(fullname +"\\"+ "jpeg" +"\\"+ f):
					dub_one_jpg.append(j)


		for d, dr, files in os.walk(sdcard): 
			t = filter(lambda x: x.endswith ((".nef", ".NEF")), files)
			v = filter(lambda x: x.endswith ((".arw", ".ARW")), files)
			k=[]
			for i in t:
				k.append(i)
			for i in v:
				k.append(i)


			for f in k:
				j = d + "\\" + f
				if not os.path.isfile(fullname +"\\"+ "raw" +"\\"+ f):
					shutil.copy(j, os.path.join(fullname, "raw"))   #copy raw to project folder from myjpeg
					coin_copy+=1
				elif os.path.isfile(fullname +"\\"+ "raw" +"\\"+ f):
					dub_one_raw.append(j)

		print ("Copy %d files" %coin_copy)
		

		print ("Dublicates (none or bellow):")
		for d in dub_one_jpg:
			print (d)
		for d in dub_one_raw:
			print (d)
		print ('Step 2 "Copy" Done.\n ')

		
	copyfun()


	namejpeg = os.listdir(os.path.join(fullname, "jpeg"))  #список файлов без пути (только имя и расширение)
	nameraw = os.listdir(os.path.join(fullname, "raw"))

	namejpeglist=[] #name of files without extensions (adding code bellow)
	namerawlist=[]
	totallist=[] #and raw and jpeg

	for n in namejpeg:
	    name, ext = os.path.splitext(n)
	    namejpeglist.append(name)
	    totallist.append(name)
	    
	for r in nameraw:
	    name, ext = os.path.splitext(r)
	    namerawlist.append(name)
	    totallist.append(name)


	abc="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
	abcdir={}
	for i in range(1,53):
		abcdir[i]=abc[i-1]

	Y=int(datepr.strftime("%Y"))-2000
	M=int(datepr.strftime("%m"))
	D= int(datepr.strftime("%d"))
	dater= abcdir[Y]+abcdir[M]+abcdir[D]

	global namedir
	namedir={}  # dic for rename files, for example "08: IMG(2049)..."
	coin=1001

	for t in totallist:
		if t in namejpeglist and t in namerawlist:
			namedir[t]="IMG"+ ("(%s)_"% dater) + str(coin)
			coin+=1
		elif t in namejpeglist and t not in namerawlist:
			namedir[t]="Img"+ ("(%s)_"% dater) + str(coin)
			coin+=1
		elif t not in namejpeglist and t in namerawlist:
			namedir[t]="img"+ ("(%s)_"% dater) + str(coin)
			coin+=1

		
	
""" 3. NEW NAME """

def step_three_new_name_test():
	if not os.path.isdir(os.path.join(fullname, "jpeg")):
		print ("First done step 1 and 2")
	else:
		step_three_new_name()

def step_three_new_name():

	print ("Step 3. New name")
	
	dublicats=[]

	coin_rename=0

	for d, dirs, files in os.walk(os.path.join(fullname, "jpeg")):
		for f in files:
			name, ext = os.path.splitext(f)
			if not os.path.isfile(d+ "\\"+namedir[name]+ext):
				os.rename(d + "\\" + f, d+ "\\"+namedir[name]+ext)
				coin_rename+=1
			elif (namedir[name]+ext) in d:
				dublicats.append(d + "\\" + f)
				
	for d, dirs, files in os.walk(os.path.join(fullname, "raw")):
		for f in files:
			name, ext = os.path.splitext(f)
			if not os.path.isfile(d+ "\\"+namedir[name]+ext):
				os.rename(d + "\\" + f, d+ "\\"+namedir[name]+ext)
				coin_rename+=1
			elif (namedir[name]+ext) in d:
				dublicats.append(d + "\\" + f)
	
	print ("Rename %d files" %coin_rename)			
	print ("Dublicats (none or bellow):") 
	for d in dublicats:
		print (d)	

	print ('Step 3 "New Name" is Done.\n ')


intro() #run all code



