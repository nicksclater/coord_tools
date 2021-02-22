import tkinter as tk
from mgrspy import mgrs as m
import OSGridConverter as OS
from math import modf
import re

class App:

	def __init__(self, master):

		self.master = master
		master.title('Coord Converter')
		master.option_add("*Font", 'arial 18')
		master.option_add('*justify', 'center')
		
		self.options = ['to dm.m', 'to bng', 'to mgrs', 'to dms', 'to dd.dd',]
		self.req_format = tk.StringVar()
		self.req_format.set('select format')
		self.input = tk.StringVar()
		self.result = tk.StringVar()
		self.result.set('')

		self.label1 = tk.Label(master, text='Enter Coord:')
		self.label1.grid(row=0, column=0, padx=(10,0), pady=(1,1))
		self.ent1 = tk.Entry(master, textvariable=self.input)
		self.ent1.grid(row=0, column=1, padx=(0,10), pady=(1,1))

		self.for_menu = tk.OptionMenu(master, self.req_format, *self.options)
		self.for_menu.grid(row=1, column=0, columnspan=2, sticky='EW', padx=(10,10), pady=(1,1))

		self.convert_btn = tk.Button(master, text='convert', command=self.convert_btn_pressed)
		self.convert_btn.grid(row=2, column=0, columnspan=2, sticky='EW', padx=(10,10), pady=(1,1))

		self.result_label = tk.Label(master, textvariable=self.result, bg='gray100')
		self.result_label.grid(row=3, column=0, columnspan=2, sticky='EW', padx=(10,10), pady=(1,1))

	
	def convert_btn_pressed(self):

		wgs84 = self.convert2wgs84()

		try:

			if self.req_format.get() in ['to dm.m', 'to dms']: 

				ans = self.convert2latlon(wgs84)

			elif self.req_format.get() == 'to mgrs':
				
				ans =  self.convert2mgrs(wgs84)

			elif self.req_format.get() == 'to bng':
				
				ans = str(self.convert2bng(wgs84))

			else:
				ans =  f'{round(wgs84[0],5)}  {round(wgs84[1],5)}'

			self.result.set(ans)
	
		except:
			pass


	def convert2wgs84(self):
		
		try:
			wgs84 = m.toWgs(self.input.get())
			print('mgrs')
			return wgs84
		except:
			pass

		try:
			tmp = OS.grid2latlong(self.input.get())
			wgs84 = (tmp.latitude, tmp.longitude)
			print('bng')
			return wgs84
		except:
			pass

		try:
			tmp = self.input.get().split()
			n,e = tmp[0], tmp[1]
			print('dm')
			print(n,e)
			_n, _e = int(n[1:3]) + (float(n[3:]) / 60), int(e[1:3]) + (float(e[3:]) / 60)
			print(_n,_e)

			_n = _n * -1 if re.search('[Ss-]', n) else _n
			_e =_e * -1 if re.search('[Ww-]', e) else _e
			print(_n,_e)

			ans = (_n,_e)
			print(ans, type(ans))

			return ans

		except:
			pass

	
	def convert2latlon(self, wgs84):
		
		n,e = wgs84[0], wgs84[1]

		if self.req_format.get() == 'to dm.m':

			n,e = self.convert_dd2dm(n), self.convert_dd2dm(e)
		
		elif self.req_format.get() == 'to dms':

			n,e = self.convert_dd2dms(n), self.convert_dd2dms(e)

		n = 'S' + n if wgs84[0] < 0 else 'N' + n
		e = 'W' + e if wgs84[1] < 0 else 'E' + e
		
		return f'{n}  {e}'

	def convert2mgrs(self, wgs84):
		
		ans = m.toMgrs(wgs84[0],wgs84[1])
		ans = ans[:3]+' '+ ans[3:5] + ' ' + ans[5:10] + ' ' + ans[10:]
		return ans
		
	
	def convert2bng(self, wgs84):
		
		ans = str(OS.latlong2grid(wgs84[0], wgs84[1]))
		return ans

	
	def convert_dd2dm(self, x):

		x = abs(round(x,4))
		mm, dd = modf(x)
		mm = round(mm * 60, 2)
		xm, mm = modf(mm)
		dd, mm, xm = int(dd), int(mm), int(xm * 100)
		
		return f'{str(dd).zfill(2)}:{str(mm).zfill(2)}.{str(xm).zfill(2)}'


	def convert_dd2dms(self, x):

		x = abs(round(x,4))
		mm, dd = modf(x)
		mm = round(mm * 60, 2)
		xm, mm = modf(mm)
		ss = round(xm * 60)
		dd, mm, ss = str(int(dd)).zfill(2), str(int(mm)).zfill(2), str(int(ss)).zfill(2)

		return f'{dd}:{mm}:{ss}'



root = tk.Tk()
my_app = App(root)

root.mainloop() 