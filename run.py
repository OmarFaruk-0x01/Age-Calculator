"""Coder Omar Faruk (Bignner)
contact info:
Facebook:https://www.facebook.com/omfaruk.om
Github:https://github.com/omof

simple age calculator and date storage
My frist OOP program
"""


import DoB 
import os
from datetime import datetime
import calendar
import json
nme=input('Input Name:')
dob=input('Input DoB:')
# chack file is exist or not in not then create a database file 
if os.path.exists('DataBase'):
	if os.path.exists('DataBase/dob.json'):
		pass
	else:
		os.system('touch DataBase/dob.json')
		file=open("DataBase/dob.json",'w')
		file.write('{}')
		file.close()
else:
	os.system('mkdir DataBase')
	os.system('touch DataBase/dob.json')
	file=open("DataBase/dob.json",'w')
	file.write('{}')
	file.close()
# create a classs
class Run:
	"""it help to comunicate with another class of another file
	it take a class object and create some instances for using in program
	"""
	def __init__(self,obj):
		
		"""Create Some instances of another class ojbect"""
		self.cal=calendar
		self.obj=obj
		self.file=open("DataBase/dob.json",'r')
		self.j_data=json.load(self.file)
		self.bd_d_name=self.obj.bd_d_name
		self.days=self.obj.days
		self.totaldays=self.obj.totaldays
		self.totalmonth=self.obj.totalmonth
		self.totalyear=self.obj.totalyear
		self.totalweek=self.obj.totalweek
		self.totalhour=self.obj.totalhour
		self.totalmin=self.obj.totalmin
		self.totalsc=self.obj.totalsc
		self.age=self.obj.age
		self.age_day=self.obj.age_day
		self.age_month=self.obj.age_month
		self.today=datetime.now()
		self.lip=self.obj.lip
		self.lipyear_list=self.obj.lipyear_list
		#func
		self.nexbd=self.obj.nexbd
		self.data_create()
	def helpp(self):
		# """Help Menu for consoel"""
		print("\t[help()]\t\t -->Show Help Menu",
		"\n\t[Show()]\t\t -->Show DoB to Now Time Chart",
		"\n\t[cls or clear]\t\t -->Clear the screen",
		"\n\t[hostname -(name)]\t -->Change Your Name",
		"\n\t[hostdate -(date)]\t -->Change BirthDay Date",
		"\n\t[@exit]\t\t\t -->Exit console",
		"\n\t[-td or @today]\t\t -->Show Date and Time of Now",
		"\n\t[-bd or @birthday]\t -->Show Your Brithbay",
		"\n\t[-nxbd or @nextBrithday] -->Show how many days of your next brithday",
		
		"\n\t[-y or @year]\t\t -->Show how many years DoB to Now",
		"\n\t[-m or @month]\t\t -->Show how many months DoB to Now",
		"\n\t[-d or @day]\t\t -->Show how many days DoB to Now",
		"\n\t[-h or @hour]\t\t -->Show how many hours DoB to Now",
		"\n\t[-min or @minite]\t -->Show how many minites DoB to Now",
		"\n\t[-sce or @sceond]\t -->Show how many seconds DoB to Now",
		"\n\t[-wk or @week]\t\t -->Show how many weeks DoB to Now",
		"\n\t[-ag or @age]\t\t -->Show your Age",
		"\n\t[-lip or @liyear]\t -->Show how many lipyer and which year was lipyer",
		"\n\t[-bits or @heartbit]\t -->Show total Heartbit from DoB to NOW",
		"\n\t[add -bd]\t\t -->Add Birthday from Date Storage",
		"\n\t[del -bd]\t\t -->Delete Birthday from Date Storage",
		"\n\t[lis -bd]\t\t -->Show Birthday list from Date Storage",
		"\n\t[cls -bd]\t\t -->Remove all Birthday from Date Storage",
		"\n\t[show **more]\t\t -->Show More Detalis about birthdays from storage")
	def brithday(self):
		#show your brith day in console with day name and month name
		day=self.obj.bd_d
		month=self.obj.bd_m
		year=self.obj.bd_y
		day_name=self.bd_d_name
		month_name=self.cal.month_name[month]
		print(self.h_p(f"{day_name} {day}/{month_name}/{year}"))
	def h_p(self,obj):
		#this method help to print with some exprension
		return "\n\t"+str(obj)+"\n"
	def extract_info(self,n):
		"""Extract Data From Dict which is loaded by Json data file
		And Show more info in console"""
		for i in self.j_data.keys():
			if i==n:
				x=DoB.BirthDay(self.j_data.get(i))#call the main class of DoB module for print new info by Birthdates
				x.show_more(i)
	def bd_db(self,data):
		#Open file for writw data in Json file
		with open('DataBase/dob.json','w') as dj:#open data file and write data
				json.dump(data,dj)
				dj.close()
		
	def bd_db_read(self):
		"""Read Data From Json file and print that data in a stuctured way"""
		print('\nBirthDates List:\n')
		for p,da in enumerate(self.j_data.items()):
			y=da[1].split('/')
			print(f'\t{p+1}.{da[0]} --> {da[1]} | {self.obj.agefinder(int(y[-1]))} year')
		print('\nYou can Find More Details in console by typeing "show **more"\n')
	def data_add(self):
		#Simple method for adding data in dict
		uname=input('Enter Name:')
		date=input('Enter Date:')
		if  uname not in self.data_dict.keys():#check geven name is exist in dict or not
			self.data_dict[uname]=date
			print(self.h_p('Date Added'))
		else:
			print(self.h_p('!!Name is Alredy Exciest'))
	def data_delete(self):
		#delet data from dict
		uname=input("Enter name:")
		if uname in self.data_dict.keys():
    			
				self.data_dict.pop(uname)
				print(rn.h_p("Removed Date"))
				
		else:
    			print(f"{uname} is not in storage")
	def userask(self):
		"""A method for asking manegment options from user """
		print(self.h_p("BirthDay Mangement"))
		ask3=input('1.Add Birthday\n2.Remove Birthday\n3.View List\n4.Clear All\n\ninput:')
		if ask3=='1':
			try:
				self.data_add()#frist call data_add func for adding data in a dict  
				self.bd_db(self.data_dict)#call another func for dumping data in a json file
			except Exception as ex:
				print(ex)
		elif ask3=='2':
			try:
				self.data_delete()#frist call data_remove func for removing data from dict 
				self.bd_db(self.data_dict)#call another func for adjusting data with that dict 
				print(self.h_p("Removed Date"))
			except Exception as ex:
				print(ex)
		elif ask3=='3':
			try:
				self.bd_db_read()#data read func for read and print data
			except Exception as ex:
				print(ex)
		elif ask3=="4":
			try:
				ask4=input("Are you sure?[y/n]>")
				if ask4=="y" or ask4=="Y":
					file=open('DataBase/dob.json','w')#again data file open and remove all data and add a empty dict
					json.dump({},file)
					print(self.h_p("All Dates Removed"))
				else:
					pass
			except Exception as ex:
				print(ex)
	def data_create(self):
		"""Important method for this program bq when this class will call this method will load all data from file and save it a variable as a dict
		other wise data will permanently remove after closeing this program"""
		file=open('DataBase/dob.json','r')
		self.data_dict=json.load(file)
		file.close()
			
def main(name,d):#main func
	try:
		os.system('clear')
		ac=DoB.BirthDay(d)
		rn=Run(ac)
		print(f'{name} Welcome To Age Calc.\nEnter Your Choise:\n\t1]-Age Calculate chart\n\t2]Find Age\n\t3]-Console\n\t4]-BirthDates\n\t5]-Exit')
		ask=input('input:')
		if ask=='1':
			os.system('clear')
			ac.show()
		elif ask=='2':
			os.system('clear')
			print(f'{name} you age is \n\t{ac.age} year {ac.age_month} month {ac.age_day} days')
		elif ask=='5':
			print(rn.h_p("Good Bye See you Soon"))
			quit()
		elif ask=='3':
			os.system('clear')
			print(f'Hello {name}!! Welcome to Age console.You can type "help()" for better understanding....')
			while True:
				con=input(f'DoB@{name}|~$')
				if con=="help()":
					rn.helpp()
				elif con=="show()":
					rn.obj.show()
				elif con=="cls" or con=="clear":
					os.system('clear')
				elif "hostname" in con:
					if len("hostname")==len(con):
						print(rn.h_p(name))
					elif len(con)>len("hostname"):
							name=con[len("hostname")+1:]
				elif "hostdate" in con:
					if len("hostdate")==len(con):
						print(rn.h_p(d))
					elif con[len("hostdate")+1:]==" "*len(con[len("hostdate")+1:]):
						print('Enter a date for change hostdate or Birthday')
						continue
					elif len(con)>len("hostdate") and con!=" "*len(con[len("hostdate")+1:]):
						d=con[len("hostdate")+1:]
						ac=DoB.BirthDay(d)
						rn=Run(ac)
				elif con=="@exit":
					print("Good Byeee See You soon!!!!!!!!!")
					break
				elif con=="-td" or con=="@today":
					print("\n",rn.today,"\n")
				elif con=="-bd" or con=="@birthday":
					rn.brithday()
				elif con=="-nxbd" or con=="@nextbirthday":
					rn.nexbd()
    					
				elif con=='-m' or con=="@month":
					print(rn.h_p(f'{rn.totalmonth} month'))
				elif con=="-y" or con=="@year":
					print(rn.h_p(f'{rn.totalyear} year'))
				elif con=="-d" or con=="@day":
					print(rn.h_p(f'{rn.totaldays} days'))
				elif con=="-min" or con=="@minite":
					print(rn.h_p(f'{rn.totalmin} minite'))
				elif con=="-h" or con=="@hours":
					print(rn.h_p(f'{rn.totalhour} hour'))
				elif con=="-sec" or con=="@sceond":
					print(rn.h_p(f'{rn.totalsc} sceond'))
				elif con=="-w" or con=="@week":
					print(rn.h_p(f'{rn.totalweek} week'))
				elif con=="-ag" or con=="@age":
					print(rn.h_p(f"{rn.age} year {rn.age_month} month {rn.age_day} days"))
				elif con=="add -bd":
					rn.data_add()
					rn.bd_db(rn.data_dict)
				elif con=="del -bd":
					rn.data_delete()
					rn.bd_db(rn.data_dict)
				elif con=="lis -bd":
					for p,da in enumerate(rn.j_data.items()):
						y=da[1].split('/')
						print(f'\t{p+1}.{da[0]} --> {da[1]} | {rn.obj.agefinder(int(y[-1]))} year')
				elif con=="show **more":
					ask5=input('Enter Name:')
					if ask5 in rn.data_dict.keys():
    						rn.extract_info(ask5)
					else:
    						print(f"{ask5} is not in storage.Yoy have to add it")
				elif con=="cls -bd":
					ask4=input("Are you sure?[y/n]>")
					if ask4=="y" or ask4=="Y":
						file=open('DataBase/dob.json','w')
						json.dump({},file)
						print(rn.h_p("All Dates Removed"))
					else:
						pass
				elif ("-bits" in con) or ("@heartbit" in con):
					print(rn.h_p(f'{rn.totalmin*15} in min (Almost)'))
				elif con=="-lip" or con=="@lipyear":
					if rn.obj.td_y%4==0:
						print(rn.h_p("This Year is Lipyear."))
						print("All lyper from DoB to Now:")
						for i,j in enumerate(rn.lipyear_list):
							print(f"\t\t{i+1}.{j}")
					else:
						print(rn.h_p("This Year is not Lipyear."))
						print("All lyper from DoB to Now:")
						for i,j in enumerate(rn.lipyear_list):
							print(f"\t\t{i+1}.{j}")
					
				else:
					if con:
						if con[0]!="@" or con[0]!="-":
							print("Missing '@' or '-' please check with help()")
						if ("help" in con) and ("()" not in con):
							print("Missing () in help commad ")
					else:
						pass
		elif ask=="4":
			rn.userask()
	except KeyboardInterrupt:
		pass
	except Exception as ex:
		print(ex)
		quit()
if __name__=='__main__':
	while True:
		main(nme,dob)
		input("\nPress Enter to Continue")