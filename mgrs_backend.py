#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  8 18:40:02 2020

@author: nicksclater1
"""
import numpy as np
from mgrs import MGRS
m = MGRS()


def convert_mgrs_ddxdd(mgrs_str: str) -> tuple:
  string = mgrs_str.replace(' ','')
  pre = string[:5]
  dig = string[5:]
  
  if len(pre) == 5 and pre[:2].isnumeric() and pre[2:].isalpha()\
      and dig.isnumeric() and len(dig) % 2 == 0:
    east = dig[:int(len(dig)/2)]; north = dig[int(len(dig)/2):]
    
    while len(dig) < 10:
      east = east + '0'
      north = north + '0'
      dig = east + north
    string = pre + east + north
    
    
    try:
      result = m.toLatLon(string.encode('utf-8'))
      return result
    
    except:
      return 'invalid position'
  
  else:
    return 'input format error'
    


def convert_ddxdd_ddmm(lat_lon: tuple) -> [str]:
  ddmm = []
      
  try:
      
    for i in lat_lon:
        
      string = str(abs(int(np.trunc(i)))) + ':' + str(round(abs(i - np.trunc(i))*60,2))
      ddmm.append(string)
  
    while len(ddmm[1].split(':')[0]) < 2:
        
      ddmm[1] = '0' + ddmm[1]
    
    result = ['N' + ddmm[0] if lat_lon[0] >= 0 else 'S' + ddmm[0]]
    
    result.append('E' + ddmm[1] if lat_lon[1] >= 0 else 'W' + ddmm[1])

    return result
  
  except:
      
    return lat_lon 



def convert_ddxdd_ddmmss(lat_lon: tuple) -> [str]:
  
  ddmmss = []
      
  try:
      
    for i in lat_lon:
        
      string = str(abs(int(np.trunc(i))))\
          + ':' + str(int(np.trunc(abs(i - np.trunc(i)) * 60)))\
              + ':' + str(round(abs((i - np.trunc(i)) * 60 - np.trunc((i - np.trunc(i)) * 60)) * 60 , 1))
      
      
      ddmmss.append(string)
    
    while len(ddmmss[1].split(':')[0]) < 2:
        
      ddmmss[1] = '0' + ddmmss[1]
    
    result = ['N' + ddmmss[0] if lat_lon[0] >= 0 else 'S' + ddmmss[0]]
    
    result.append('E' + ddmmss[1] if lat_lon[1] >= 0 else 'W' + ddmmss[1])

    return result
  
  except:
      
    return lat_lon 





    
# tesing
  
test1 = '30UXD15123 95123'
test2 = '30UXD15123 95123'
error1 = '30uxd123456789'
error2 = '20ux3123456'
error3 = ''
error4 = '12uad123123'


x1 = convert_ddxdd_ddmm(convert_mgrs_ddxdd(test1))
x2 = convert_ddxdd_ddmmss(convert_mgrs_ddxdd(test2))
x3 = convert_ddxdd_ddmm(convert_mgrs_ddxdd(error1))
x4 = convert_ddxdd_ddmm(convert_mgrs_ddxdd(error2))
x5 = convert_ddxdd_ddmm(convert_mgrs_ddxdd(error3))
x6 = convert_ddxdd_ddmm(convert_mgrs_ddxdd(error4))
    
   