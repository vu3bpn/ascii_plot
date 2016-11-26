# -*- coding: utf-8 -*-
"""
Created on Sat Nov 26 12:16:47 2016

@author: BIPIN
ascii plot
"""
import numpy as np
class cursor:
    def __init__(self,pos,colour):
        self.pos = [pos]
        self.colour = [colour]
        
    def __repr__(self):
        str1 = ''
        p0 = 0 
        pos_colour = zip(self.pos,self.colour)
        pos_colour.sort()
        for (p1,c1) in pos_colour:
            if c1 < 0:
                str1 += ' '*(p1-p0)   
            else:
                str1 += ' '*(p1-p0)+'\x1b[1;{0}m'.format(30+c1%6)+['+','*','#','%','&','a','@'][c1/7]+'\x1b[0m'
            p0 = p1
        return str1
        
    def __str__(self):
        return self.__repr__()
        
    def __iadd__(self,c2):
        self.pos += c2.pos
        self.colour += c2.colour
        return self
    def __add__(self,c2):
        c3 = cursor(0,0)
        c3.pos = self.pos + c2.pos
        c3.colour = self.colour + c2.colour
        return c3
        
      
class ascii_plot:
    def __init__(self):
        self.max_val = 0
        self.min_val = 0
        self.max_div = 100
        
    def plot_val(self,vect):
        self.max_val =  max(vect+[self.max_val])
        self.min_val = min(vect+[self.min_val])
            
        cur_idx = 1
        scale = float(self.max_div)/(self.max_val-self.min_val)
        c1 = cursor(self.max_div ,-1)
        #c1 = cursor(0 ,-1)
        for v1 in vect:
            c1 += cursor(int((v1-self.min_val)*scale),cur_idx)
            cur_idx+= 1
        print '{0}['.format(self.min_val)+c1.__str__()+']{0}'.format(self.max_val)
            
         
        
        
    def test_all_colours(self):
        for i1 in range(8):
            print '\n',
            for i2 in range(30,38):
                for i3 in range(40,48):
                    print '\x1b[{0};{1}m hello {0}-{1}-{2} \x1b[0m'.format(i1,i2,i3),
                print '\n',
if __name__ =='__main__':
    ap1 = ascii_plot()
    #ap1.test_all_colours()
    for k in range(50):
        c1 = cursor(20 + np.sin(k*np.pi/25)*20,1)
        c1 += cursor(20 + np.cos(k*np.pi/25)*20,20) 
        c1 += cursor(20 - np.sin(k*np.pi/25)*20,10) 
        
        print c1
        
    for k in range(50):
        ap1.plot_val([k,k+10%50,50-k])
        
