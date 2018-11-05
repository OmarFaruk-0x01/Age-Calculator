"""Coder Omar Faruk (Bignner)
contact info:
Facebook:https://www.facebook.com/omfaruk.om
Github:https://github.com/omof

simple age calculator and date storage
My frist OOP program
"""

import datetime
import calendar
class BirthDay:
	"""Main class of this program
	Its convert and find all dates and times """
	def __init__(self,bd):
    	#today info
		self.td=datetime.datetime.now()
		self.td_y=self.td.year
		self.td_m=self.td.month
		self.td_d=self.td.day

	#	important var
		self.days=0
		self.lip=0
		self.month_count=0
		self.next_y=self.td_y+1
		self.m_d_list=calendar.mdays
		self.lipyear_list=[]
		
		#dirthday info
		self.bd=bd.split('/')
		self.bd_y=int(self.bd[-1])
		self.bd_m=int(self.bd[1])
		self.bd_d=int(self.bd[0])
		self.bd_d_name=datetime.date(self.bd_y,self.bd_m,self.bd_d).strftime("%A")
		self.nxbd_d_name=datetime.date(self.next_y,self.bd_m,self.bd_d).strftime("%A")
		#call func
		self.lip_count()
		self.tTOb()
		self.count_times()

	def lip_count(self):
		"""Find & count all leap year from DoB to NOw"""
		for i  in range(self.bd_y,self.td_y+1):
			if i % 4 == 0:
				self.lip+=1
				self.lipyear_list.append(i)
		return self.lip
	def tTOb(self):
		#important method!!!!!!!!!
		#count how many days for next birthday and also count month
		for i in range(1,13):
			if i >= self.td_m:
				self.month_count+=1
				self.days+=self.m_d_list[i]
				if i >= 12:
					for j in range(1,self.bd_m):
						self.days+=self.m_d_list[j]
						self.month_count+=1
		self.days=(self.days+self.bd_d)-self.td_d
		return self.month_count, self.days
	def count_times(self):
		"""Count & convert all time into year , month , days , hour , minite , sceond and also find how many heartbits from bron to now"""
		from datetime import datetime
		td_n=datetime.now()
		self.totalyear, self.age=abs(self.bd_y-self.td_y),abs(self.bd_y-self.td_y)
		self.totaldays=(self.age*365)+self.lip+(365-self.days)
		self.totalmonth=(self.age*12)+(12-self.month_count)-1#-1 for last month is not be counted
		self.totalhour=(self.totaldays*24)+(24-td_n.hour)
		self.totalmin=self.totalhour*60+(((24-td_n.hour)*60)+td_n.minute)
		self.totalsc=self.totalmin*60+((((24-td_n.hour)*60)*60)+td_n.second)
		#week info
		self.week=str(self.totaldays/7)
		self.totalweek=int(float(self.week[0:self.week.find('.')]))
		self.week_day=int(float('{0:.2f}'.format(float(self.week[self.week.find('.'):])*7)))
		#age info
		self.age_day=(self.m_d_list[self.td_m]-abs(self.td_d-self.bd_d))+1
		self.age_month=abs(self.td_m-self.bd_m)-1
		
		#breath info
		#per sceond
		self.breath_s_mi='{0:.2f}'.format(self.totalsc*0.2)
		self.breath_s_mx='{0:.2f}'.format(self.totalsc*0.33)
		self.breath_s=f'{self.breath_s_mi} - {self.breath_s_mx}'
		
		#per min 
		self.breath_m_mi=f'{self.totalmin*12}'
		self.breath_m_mx=f'{self.totalmin*20}'
		self.breath_m=f'{self.breath_m_mi} - {self.breath_m_mx}'
		
		#per hour
		self.breath_h_mi=f'{self.totalhour*(12*60)}'
		self.breath_h_mx=f'{self.totalhour*(20*60)}'
		self.breath_h=f'{self.breath_h_mi} - {self.breath_h_mx}'
		
		#per day
		self.breath_d_mi=f'{self.totaldays*((12*60)*24)}'
		self.breath_d_mx=f'{self.totaldays*((20*60)*24)}'
		self.breath_d=f'{self.breath_d_mi} - {self.breath_d_mx}'
		
		#per year
		self.breath_y_mi=f'{self.totalyear*(365*((12*60)*24))}'
		self.breath_y_mx=f'{self.totalyear*(365*((20*60)*24))}'
		self.breath_y=f'{self.breath_y_mi} - {self.breath_y_mx}'
	def show(self):
		"""Show all times as converted from"""
		print(f'Today: {self.td}')
		print(f'Your age:{self.age} year {self.age_month} month {self.age_day} days')
		print(f'\nYou stay in world::\n\tDoB to Now:\n\t\t{self.totalyear} year\n\t\t{self.totalmonth} month\n\t\t{self.totaldays} days\n\t\t{self.totalhour} hour\n\t\t{self.totalmin} minute\n\t\t{self.totalsc} second')
		print(f'Health Report:\nDoB to Now:\n\tHeart Bits:{self.breath_s} in second')
		print(f'')
		print(f'')
		print(f'')
		return ''
	def nexbd(self):
		#find how many days , year , months , hour , minite , sceond
		tn=datetime.datetime.now()
		y="{0:.2f}".format(self.days/365)
		m="{0:.2f} (avrage)".format(self.days/30)
		d=self.days
		h=(self.days*24)-tn.hour
		mi=(h*60)-tn.minute
		sc=(mi*60)-tn.second
		day_name=self.nxbd_d_name
		print(f"Your Next Brith day at {self.bd_d}/{self.bd_m}/{self.next_y} {day_name}")
		print(f'\nNow to Next Birthday:\n\t{y} year\n\t{m} month\n\t{d} days\n\t{h} hour\n\t{mi} minute\n\t{sc} second\n')
	def show_more(self,n):
		"""Same as show() method its for all Birthdays of DateStorage"""
		print(f'Today:{self.td}')
		print(f'{n} age:{self.age} year {self.age_month} month {self.age_day} days')
		print(f'You stay in world::|\nDoB to Now:\n\t{self.totalyear} year\n\t{self.totalmonth} month\n\t{self.totaldays} days\n\t{self.totalhour} hour\n\t{self.totalmin} minute\n\t{self.totalsc} second')
		print(f'Health Report:\nDoB to Now:\n\tHeart Bits:{self.breath_s} in second')
		print("All lyper from DoB to Now:")
		for i,j in enumerate(self.lipyear_list):
			print(f"\t\t{i+1}.{j}")
		print()
		print(f'')
	def agefinder(self,y):
		return abs(y-self.td_y)