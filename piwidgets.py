#piconwidgets.py

import math
from tkinter import *
	
#guage	
def cpiguage(cfg):
		canvas = cfg.canvas
		cx, cy, grad = cfg.cx, cfg.cy, cfg.grad
		vlow, vhigh, deglow, deghigh  = cfg.vlow, cfg.vhigh, cfg.deglow, cfg.deghigh
		colorrim, colorface = cfg.colorrim, cfg.colorface
		deglow, deghigh = cfg.deglow, cfg.deghigh
		name = cfg.name
		tag, gtag = cfg.tag, cfg.gtag
		ginr = grad-5
		canvas.create_oval(cx-grad, cy-grad, cx+grad, cy+grad,fill=colorrim, tag=gtag)
		canvas.create_oval(cx-ginr, cy-ginr, cx+ginr, cy+ginr, fill=colorface, tag=gtag)
		canvas.create_oval(cx-2,cy-2,cx+2, cy+2,fill='red', tag=gtag)
		if deglow > deghigh:
			degspan = (360-deglow) + deghigh
		else:
			degspan = deghigh - deglow	
		xceil, vmult, incr = getscale(vlow,vhigh)
		if xceil == 1:  vmult = ' '
		dincr = degspan / incr
		ptrad = grad -12
		ptrad2 = ptrad+5
		txtrad = grad - 20
		radsPD = math.pi / 180
		xdeg = deglow
		xprog = 0
		canvas.create_text(cx,cy+25,text=name, tag = gtag)
		canvas.create_text(cx,cy+37,text=vmult, tag = gtag)
		vbase = vlow
		while xprog <= incr:
			px1 = int(round(ptrad * math.sin(xdeg * radsPD)))
			py1 = int(round(ptrad * math.cos(xdeg * radsPD)))
			px2 = int(round(ptrad2 * math.sin(xdeg * radsPD)))
			py2 = int(round(ptrad2 * math.cos(xdeg * radsPD)))
			px3 = int(round(txtrad * math.sin(xdeg * radsPD)))
			py3 = int(round(txtrad * math.cos(xdeg * radsPD)))
			px1 = cx + px1
			py1 = cy - py1
			px2 = cx + px2
			py2 = cy - py2
			px3 = cx + px3
			py3 = cy - py3
			canvas.create_line(px1, py1, px2, py2, width=2, fill='black', tag=gtag)
			ptxt = str(int(vbase/xceil))
			canvas.create_text(px3,py3,text=ptxt, tag=gtag)
			xdeg += dincr
			vbase += xceil
			xprog += 1
		
		
def cpisetguage(cfg):
		canvas = cfg.canvas
		cx,cy,grad = cfg.cx, cfg.cy, cfg.grad
		deglow, deghigh, vlow, vhigh = cfg.deglow, cfg.deghigh, cfg.vlow, cfg.vhigh
		setcolor,setlen, setwidth = cfg.setcolor, cfg.setlen, cfg.setwidth
		pval = cfg.pval
		tag = cfg.tag
		if deglow > deghigh:
			degspan = (360-deglow) + deghigh
		else:
			degspan = deghigh - deglow
		valspan = vhigh - vlow
		valdeg = degspan / valspan
		ptrdeg = (pval - vlow)* valdeg
		ptrdeg = deglow + ptrdeg
		if ptrdeg > 360:
			ptrdeg = ptrdeg-360
		radsPD = math.pi / 180
		grad = setlen
		px = int(round(grad * math.sin(ptrdeg * radsPD)))
		py = int(round(grad * math.cos(ptrdeg * radsPD)))
		canvas.delete(tag)
		canvas.create_line(cx,cy, cx+px, cy-py, fill=setcolor,width=setwidth, tag = tag)

def getscale(vlow, vhigh):
		vspan = abs(vhigh - vlow)
		xceil = 100000
		while vspan <= xceil:
			priorxceil = xceil
			xceil /= 10
		if vspan / xceil < 3:
			xceil /= 10
		if (xceil * 10) - (int(xceil)*10) == 0:
			xceil = int(xceil)
		vmult = '(x '+str(xceil)+')'
		incr = vspan / xceil
		incr = int(round(incr))
		return xceil, vmult, incr
		
def cpidisplay(cfg):
		canvas = cfg.canvas
		cx,cy,sx,sy = cfg.cx, cfg.cy, cfg.sx, cfg.sy
		dx,dy = cfg.dx,cfg.dy
		cy += dy
		cx += dx
		font, fsize = cfg.font, cfg.fsize
		tag = cfg.tag
		gtag = cfg.gtag 
		text = cfg.text
		if sx:
			canvas.create_rectangle(cx-sx,cy-sy,cx+sx,cy+sy, tag=tag)
			canvas.create_text(cx,cy, text=text, font=(font,fsize),tag=tag)
		
def cpibutton(cfg):
		cx, cy = cfg.cx, cfg.cy
		canvas = cfg.canvas
		name = cfg.name
		sizex, sizey = cfg.sizex, cfg.sizey
		font, fsize, shape = cfg.font, cfg.fsize, cfg.shape
		color = cfg.color
		buttonid = cfg.buttonid
		if shape == 'square':
			objbtn = canvas.create_rectangle(cx,cy,cx+sizex,cy+sizey,fill=color,tag=buttonid)
			objtxt = canvas.create_text(cx+(sizex/2),cy+(sizey/2),text=name, font=(font,fsize),tag=buttonid)
		else:
			szx, szy = sizex/2, sizey/2
			objbtn = canvas.create_oval(cx-szx, cy-szy, cx+szx, cy+szy,fill=color,tag=buttonid)
			objtxt = canvas.create_text(cx,cy,text=name, font=(font,fsize),tag=buttonid)

