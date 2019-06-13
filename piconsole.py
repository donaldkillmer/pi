# new piconsole parameterized

import math, time
from tkinter import *
from tkinter.messagebox import *
from piwidgets import *

# test basic Guage class
win = Tk()
canvas = Canvas(win,width=700, height=400)
canvas.pack(side=TOP)
canvas.config(bg='white')

def sendmail(text,cfg):
	alertto = cfg.alertto
	name = cfg.name
	print ('alert for '+name+': '+text+' sent to '+alertto)
	
def onPress1():  #reset guage 1 to 0
	Guage1.colorface = 'white'
	if Guage1.alarm:
		ttt=newtime()
		text = Guage1.name + ' has been reset: '+ttt
		if Guage1.alertmail:
			sendmail(text,Guage1)
		else:
			print (text)
	Guage1.alarm = 0
	cpiguage(Guage1)
	g1.set(50)
	btn1.config(bg='pink')
	
def onPress2():
	cfg = Guage1
	g1.set(round(cfg.pval + cfg.samplestep, cfg.vrnd))
	
def onPress3():   #preset guage2 to 0
	Guage2.colorface = 'white'
	if Guage2.alarm:
		ttt = newtime()
		text = Guage2.name + ' has been reset: '+ttt
		if Guage2.alertmail:
			sendmail(text,Guage2)
		else:
			print (text)
	Guage2.alarm = 0
	cpiguage(Guage2)
	g2.set(0)
	btn3.config(bg='pink')
	
def onPress4():
	g2.set(round(Guage2.pval + Guage2.samplestep, Guage2.vrnd))
	
def alert(cfg):   # display  email alert that guage has exceeded limits
	vlow, vhigh, pval = cfg.vlow, cfg.vhigh, cfg.pval
	name = cfg.name
	ttt=newtime()
	if pval == vlow:
		text = name + ' has exceeded low limit: '+ttt
	else:
		text = name + ' has exceeded high limit: '+ttt
	if cfg.alertmail:
		sendmail(text,cfg)
	else:
		print (text)
	if cfg.tag == 'g1':
		btn1.config(bg = 'red')
	else:
		btn3.config(bg = 'red')
	
def newtime():
	t =time.time()
	tt=time.localtime(t)
	fmt = '%a %d %b %H:%M:%S'
	ttt = time.strftime(fmt,tt)
	return ttt

toolbar = Frame(win)
toolbar.pack(side=LEFT, expand=YES, fill=X)
bfont = ('arial',9,'bold')

btn1 = Button(toolbar,text='RESET 1',font = bfont,command=onPress1)
btn1.pack(side=LEFT)
btn1.config(width=10,height=2, bg='pink')

btn2 = Button(toolbar,text='TEST 1',font=bfont,command=onPress2)
btn2.pack(side=LEFT)
btn2.config(width=10, height=2, bg='lightblue')

tlabel = Label(toolbar)
tlabel.config(width=20, height=2, text='date', bg='silver', bd=2)
tlabel.config(relief = SUNKEN)
tlabel.pack(side=RIGHT)

btn4 = Button(toolbar,text='TEST 2',font=bfont,command = onPress4)
btn4.pack(side=RIGHT)
btn4.config(width=10, height=2, bg='lightblue')

btn3 = Button(toolbar,text='RESET 2',font=bfont,command=onPress3)
btn3.pack(side=RIGHT)
btn3.config(width=10,height=2,bg='pink')

class WBase:
	canvas = canvas
	setcolor, setlen, setwidth = 'red', 60, 2
	sx = sy = dx = dy = pval = 0
	font, tag, gtag   = 'arial', 'base', 'base'
	colorrim, colorface = 'silver', 'white'
	samplerate = samplestep = 0
	
class Guage1(WBase):
	cx, cy, grad  = 200, 200, 90
	deglow, deghigh = 240,120
	vlow, vhigh, vrnd = 0,110,2
	type, name, tag =  'guage','Sensor 1','g1'
	dx, dy, sx, sy = 0,110,70,15
	fsize = 22
	alarm = 0
	samplerate, samplestep = 4000, -2.23
	alertmail, alertto = 1, 'dek@creativesoftwaresys.com'
 
class Guage2(Guage1):
	cx, cy, grad = 500,200,90
	deglow, deghigh = 270, 90
	vlow, vhigh, vrnd = -200,1200,3
	name, tag = 'Sensor 2', 'g2'
	pval = 0
	alarm = 0
	samplerate, samplestep = 5000, 18.717 
	alertmail, alertto = 1, 'dek@creativesoftwaresys.com'

class Title(WBase):
	cx, cy = 350,20
	text = 'Raspberry Pi PLC'
	type = 'display'
	fsize = 18
	
class Widget:
	def __init__(self, cfg):
		self.cfg = cfg
		self.type = cfg.type
		self.samplerate = cfg.samplerate
		self.samplestep = cfg.samplestep
	def draw(self):
		type = self.type
		cfg = self.cfg
		if type == 'guage':
			cpiguage(cfg)
		elif type == 'display':
			cpidisplay(cfg)
	def set(self,pval):
		type = self.type
		cfg = self.cfg
		if cfg.alarm:
			return
		vlow, vhigh = cfg.vlow, cfg.vhigh
		if pval < vlow or pval > vhigh:
			cfg.alarm = 1
			if pval < vlow:
				pval = vlow
			else:
				pval = vhigh
		cfg.pval = pval
		cfg.text=str(pval)
		if cfg.alarm:
			cfg.colorface = 'pink'
			cpiguage(cfg)
			alert(cfg)
		tag = cfg.tag
		canvas.delete(tag)
		cpisetguage(cfg)
		cpidisplay(cfg)

d1 = Widget(Title)
g1 = Widget(Guage1)
g2 = Widget(Guage2)

d1.draw()
g1.draw()
g2.draw()

g1.set(54.8)
g2.set(3.75)
 
win.title('Raspberry Pi PLC')

# timed routines update guages and current date/time
def sample1():
	onPress2()
	win.after(g1.samplerate,sample1)
	
def sample2():
	onPress4()
	win.after(g2.samplerate,sample2)
	
def tfresh():
	ttt = newtime()
	tlabel.config(text = ttt, font=('arial',11,'bold'))
	win.after(1000,tfresh)
	
sample1()
sample2()
tfresh()

win.mainloop()


		
