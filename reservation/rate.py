'''
Created on 12/01/2015

@author:    Richard Lares 11-10508
            Patricia Reinoso 11-10851
'''

from decimal import Decimal
from datetime import datetime
from datetime import timedelta

class rate():    
    def __init__(self,day,night):
        assert(day>0 and night>0)
        self._day=Decimal(day)
        self._night=Decimal(night)
    
    def GetDay(self):
        return self._day
    
    def GetNight(self):
        return self._night
    
def rateCompute(dateI,dateO, r):
    if dateI>=dateO:
        raise AssertionError
    if (dateO<dateI+timedelta(minutes=15)):
        raise AssertionError
    if (dateO>dateI+timedelta(days=3)):
        raise AssertionError
    totalRate=0
    tempA=dateI
    while tempA<dateO:
        tempB=tempA+timedelta(hours=1)
        if tempB.hour>dateO.hour and tempB>dateO:
            tempB=tempB-timedelta(hours=1)
        if (tempA.hour<6 and tempB.hour>=6) or (tempA.hour<18 and tempB.hour>=18):
            totalRate+=max(r.GetDay(),r.GetNight())
        else:
            if tempA.hour<6 or tempA.hour>=18:
                totalRate+=r.GetNight()
            else:
                totalRate+=r.GetDay()
        tempA=tempA+timedelta(hours=1)
    return Decimal(totalRate)

# Prueba cualquiera

dateA=datetime(2015,7,5,5,44,0,0)
dateB=datetime(2015,7,5,5,59,0,0)

r=rate(7,5)
print(rateCompute(dateA,dateB,r))