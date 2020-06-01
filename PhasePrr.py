import math
import ast
from math import e
from decimal import *
getcontext().prec = 28



#first we have defined funcyions to access signals and vehicles data
def permutation(lst):
    if len(lst) == 0:
        return []
    if len(lst) == 1:
        return [lst]

    l = []

    for i in range(len(lst)):
        m = lst[i]
        remLst = lst[:i] + lst[i + 1:]
        for p in permutation(remLst):
            l.append([m] + p)
    return l
def factorial(f):
    if f == 0:
        return 1
    else:
        return f * factorial(f-1)

def toList(NestedTuple):
    return list(map(toList, NestedTuple)) if isinstance(NestedTuple, (list, tuple)) else NestedTuple


def Init():
    global vehTypesEquipped
    global vehTypesSpecial
    global vehsAttributes
    global vehsAttNames
    
    vehsAttributes = []
    vehsAttNames = []
    vehTypesAttributes = Vissim.Net.VehicleTypes.GetMultipleAttributes(['No', 'IsConnected', 'IsSpecial'])
    vehTypesEquipped = [x[0] for x in vehTypesAttributes if x[1] == True]
    vehTypesSpecial = [x[0] for x in vehTypesAttributes if x[2] == True]


    global SigCritical11    
    Sig11Atributes =  Vissim.Net.SignalControllers.ItemByKey(11).SGs.GetMultipleAttributes(['No', 'CriticalPhase'])
    SigCritical11 = [x[0] for x in Sig11Atributes if x[1] == True]

    global SigCritical10    
    Sig10Atributes =  Vissim.Net.SignalControllers.ItemByKey(10).SGs.GetMultipleAttributes(['No', 'CriticalPhase'])
    SigCritical10 = [x[0] for x in Sig10Atributes if x[1] == True]

    global SigCritical9    
    Sig9Atributes =  Vissim.Net.SignalControllers.ItemByKey(9).SGs.GetMultipleAttributes(['No', 'CriticalPhase'])
    SigCritical9 = [x[0] for x in Sig9Atributes if x[1] == True]

    global SigCritical8    
    Sig8Atributes =  Vissim.Net.SignalControllers.ItemByKey(8).SGs.GetMultipleAttributes(['No', 'CriticalPhase'])
    SigCritical8 = [x[0] for x in Sig8Atributes if x[1] == True]

    global SigCritical7    
    Sig7Atributes =  Vissim.Net.SignalControllers.ItemByKey(7).SGs.GetMultipleAttributes(['No', 'CriticalPhase'])
    SigCritical7 = [x[0] for x in Sig7Atributes if x[1] == True]


    global SigCritical6    
    Sig6Atributes =  Vissim.Net.SignalControllers.ItemByKey(6).SGs.GetMultipleAttributes(['No', 'CriticalPhase'])
    SigCritical6 = [x[0] for x in Sig6Atributes if x[1] == True]

    global SigCritical4    
    Sig4Atributes =  Vissim.Net.SignalControllers.ItemByKey(4).SGs.GetMultipleAttributes(['No', 'CriticalPhase'])
    SigCritical4 = [x[0] for x in Sig4Atributes if x[1] == True]

    global SigCritical3    
    Sig3Atributes =  Vissim.Net.SignalControllers.ItemByKey(3).SGs.GetMultipleAttributes(['No', 'CriticalPhase'])
    SigCritical3 = [x[0] for x in Sig3Atributes if x[1] == True]


    global SigCritical2    
    Sig2Atributes =  Vissim.Net.SignalControllers.ItemByKey(2).SGs.GetMultipleAttributes(['No', 'CriticalPhase'])
    SigCritical2 = [x[0] for x in Sig2Atributes if x[1] == True]


    global SigCritical12    
    Sig12Atributes =  Vissim.Net.SignalControllers.ItemByKey(12).SGs.GetMultipleAttributes(['No', 'CriticalPhase'])
    SigCritical12 = [x[0] for x in Sig12Atributes if x[1] == True]


    global SigCritical13    
    Sig13Atributes =  Vissim.Net.SignalControllers.ItemByKey(13).SGs.GetMultipleAttributes(['No', 'CriticalPhase'])
    SigCritical13 = [x[0] for x in Sig13Atributes if x[1] == True]

    global SigCritical5    
    Sig5Atributes =  Vissim.Net.SignalControllers.ItemByKey(5).SGs.GetMultipleAttributes(['No', 'CriticalPhase'])
    SigCritical5 = [x[0] for x in Sig5Atributes if x[1] == True]

    global SigCritical1    
    Sig1Atributes =  Vissim.Net.SignalControllers.ItemByKey(1).SGs.GetMultipleAttributes(['No', 'CriticalPhase'])
    SigCritical1 = [x[0] for x in Sig1Atributes if x[1] == True]







def GetVissimDataVehicles():
    global vehsAttributes
    global vehsAttNames
    vehsAttributesNames = ['No', 'VehType\No', 'Pos', 'VehType\No', 'Lane\Link', 'Speed', 'DistanceToSigHead','InQueue']
    vehsAttributes = toList(Vissim.Net.Vehicles.GetMultipleAttributes(vehsAttributesNames))
    vehsAttNames = {}
    cnt = 0
    for att in vehsAttributesNames:
        vehsAttNames.update({att: cnt})
        cnt += 1




def GetSignalsData1():
    global SignalAttributes1
    global SigAttNames1
    SignalAttributes1 = []
    SigAttNames1 = []
    SignalAttributesNames1 = ['No','GreenStart', 'GreenEnd', 'IGT', 'SigState', 'GreenTimeDuration']
    SignalAttributes1 = toList(Vissim.Net.SignalControllers.ItemByKey(1).SGs.GetMultipleAttributes(SignalAttributesNames1))
    SigAttNames1 = {}
    ctt = 0
    for ftt in SignalAttributesNames1:
        SigAttNames1.update({ftt: ctt})
        ctt+=1

def GetSignalsData5():
    global SignalAttributes5
    global SigAttNames5
    SignalAttributes5 = []
    SigAttNames5 = []
    SignalAttributesNames5 = ['No','GreenStart', 'GreenEnd', 'IGT', 'SigState', 'GreenTimeDuration']
    SignalAttributes5 = toList(Vissim.Net.SignalControllers.ItemByKey(5).SGs.GetMultipleAttributes(SignalAttributesNames5))
    SigAttNames5 = {}
    ctt = 0
    for ftt in SignalAttributesNames5:
        SigAttNames5.update({ftt: ctt})
        ctt+=5


def GetSignalsData12():
    global SignalAttributes12
    global SigAttNames12
    SignalAttributes12 = []
    SigAttNames12 = []
    SignalAttributesNames12 = ['No','GreenStart', 'GreenEnd', 'IGT', 'SigState', 'GreenTimeDuration']
    SignalAttributes12 = toList(Vissim.Net.SignalControllers.ItemByKey(12).SGs.GetMultipleAttributes(SignalAttributesNames12))
    SigAttNames12 = {}
    ctt = 0
    for ftt in SignalAttributesNames12:
        SigAttNames12.update({ftt: ctt})
        ctt+=12

def GetSignalsData13():
    global SignalAttributes13
    global SigAttNames13
    SignalAttributes13 = []
    SigAttNames13 = []
    SignalAttributesNames13 = ['No','GreenStart', 'GreenEnd', 'IGT', 'SigState', 'GreenTimeDuration']
    SignalAttributes13 = toList(Vissim.Net.SignalControllers.ItemByKey(13).SGs.GetMultipleAttributes(SignalAttributesNames13))
    SigAttNames13 = {}
    ctt = 0
    for ftt in SignalAttributesNames13:
        SigAttNames13.update({ftt: ctt})
        ctt+=13




def GetSignalsData2():
    global SignalAttributes2
    global SigAttNames2
    SignalAttributes2 = []
    SigAttNames2 = []
    SignalAttributesNames2 = ['No','GreenStart', 'GreenEnd', 'IGT', 'SigState', 'GreenTimeDuration']
    SignalAttributes2 = toList(Vissim.Net.SignalControllers.ItemByKey(2).SGs.GetMultipleAttributes(SignalAttributesNames2))
    SigAttNames2 = {}
    ctt = 0
    for ftt in SignalAttributesNames2:
        SigAttNames2.update({ftt: ctt})
        ctt+=1


def GetSignalsData3():
    global SignalAttributes3
    global SigAttNames3
    SignalAttributes3 = []
    SigAttNames3 = []
    SignalAttributesNames3 = ['No','GreenStart', 'GreenEnd', 'IGT', 'SigState', 'GreenTimeDuration']
    SignalAttributes3 = toList(Vissim.Net.SignalControllers.ItemByKey(3).SGs.GetMultipleAttributes(SignalAttributesNames3))
    SigAttNames3 = {}
    ctt = 0
    for ftt in SignalAttributesNames3:
        SigAttNames3.update({ftt: ctt})
        ctt+=1



def GetSignalsData4():
    global SignalAttributes4
    global SigAttNames4
    SignalAttributes4 = []
    SigAttNames4 = []
    SignalAttributesNames4 = ['No','GreenStart', 'GreenEnd', 'IGT', 'SigState', 'GreenTimeDuration']
    SignalAttributes4 = toList(Vissim.Net.SignalControllers.ItemByKey(4).SGs.GetMultipleAttributes(SignalAttributesNames4))
    SigAttNames4 = {}
    ctt = 0
    for ftt in SignalAttributesNames4:
        SigAttNames4.update({ftt: ctt})
        ctt+=1


def GetSignalsData6():
    global SignalAttributes6
    global SigAttNames6
    SignalAttributes6 = []
    SigAttNames6 = []
    SignalAttributesNames6 = ['No','GreenStart', 'GreenEnd', 'IGT', 'SigState', 'GreenTimeDuration']
    SignalAttributes6 = toList(Vissim.Net.SignalControllers.ItemByKey(6).SGs.GetMultipleAttributes(SignalAttributesNames6))
    SigAttNames6 = {}
    ctt = 0
    for ftt in SignalAttributesNames6:
        SigAttNames6.update({ftt: ctt})
        ctt+=1


def GetSignalsData7():
    global SignalAttributes7
    global SigAttNames7
    SignalAttributes7 = []
    SigAttNames7 = []
    SignalAttributesNames7 = ['No','GreenStart', 'GreenEnd', 'IGT', 'SigState', 'GreenTimeDuration']
    SignalAttributes7 = toList(Vissim.Net.SignalControllers.ItemByKey(7).SGs.GetMultipleAttributes(SignalAttributesNames7))
    SigAttNames7 = {}
    ctt = 0
    for ftt in SignalAttributesNames7:
        SigAttNames7.update({ftt: ctt})
        ctt+=1


def GetSignalsData8():
    global SignalAttributes8
    global SigAttNames8
    SignalAttributes8 = []
    SigAttNames8 = []
    SignalAttributesNames8 = ['No','GreenStart', 'GreenEnd', 'IGT', 'SigState', 'GreenTimeDuration']
    SignalAttributes8 = toList(Vissim.Net.SignalControllers.ItemByKey(8).SGs.GetMultipleAttributes(SignalAttributesNames8))
    SigAttNames8 = {}
    ctt = 0
    for ftt in SignalAttributesNames8:
        SigAttNames8.update({ftt: ctt})
        ctt+=1

def GetSignalsData9():
    global SignalAttributes9
    global SigAttNames9
    SignalAttributes9 = []
    SigAttNames9 = []
    SignalAttributesNames9 = ['No','GreenStart', 'GreenEnd', 'IGT', 'SigState', 'GreenTimeDuration']
    SignalAttributes9 = toList(Vissim.Net.SignalControllers.ItemByKey(9).SGs.GetMultipleAttributes(SignalAttributesNames9))
    SigAttNames9 = {}
    ctt = 0
    for ftt in SignalAttributesNames9:
        SigAttNames9.update({ftt: ctt})
        ctt+=1

def GetSignalsData10():
    global SignalAttributes10
    global SigAttNames10
    SignalAttributes10 = []
    SigAttNames10 = []
    SignalAttributesNames10 = ['No','GreenStart', 'GreenEnd', 'IGT', 'SigState', 'GreenTimeDuration']
    SignalAttributes10 = toList(Vissim.Net.SignalControllers.ItemByKey(10).SGs.GetMultipleAttributes(SignalAttributesNames10))
    SigAttNames10 = {}
    ctt = 0
    for ftt in SignalAttributesNames10:
        SigAttNames10.update({ftt: ctt})
        ctt+=1

def GetSignalsData11():
    global SignalAttributes11
    global SigAttNames11
    SignalAttributes11 = []
    SigAttNames11 = []
    SignalAttributesNames11 = ['No','GreenStart', 'GreenEnd', 'IGT', 'SigState', 'GreenTimeDuration', 'ContrByCOM']
    SignalAttributes11 = toList(Vissim.Net.SignalControllers.ItemByKey(11).SGs.GetMultipleAttributes(SignalAttributesNames11))
    SigAttNames11 = {}
    ctt = 0
    for ftt in SignalAttributesNames11:
        SigAttNames11.update({ftt: ctt})
        ctt+=1


def GetLinksData():
    global LinkAttributes
    global LinAttNames
    LinkAttributes = []
    LinAttNames = []
    LinkAttributesNames = ['No','Count:Vehs']
    LinkAttributes = toList(Vissim.Net.Links.GetMultipleAttributes(LinkAttributesNames))
    LinAttNames = {}
    ppc = 0
    for ftt in LinkAttributesNames:
        LinAttNames.update({ftt: ppc})
        ppc+=1


def Phase():
    Init()
    GetLinksData()
    GetVissimDataVehicles()
    GetSignalsData1()
    GetSignalsData5()
    GetSignalsData12()
    GetSignalsData13()
    GetVissimDataVehicles()
    GetSignalsData2()
    GetSignalsData3()
    GetSignalsData4()
    GetSignalsData6()
    GetSignalsData7()
    GetSignalsData8()
    GetSignalsData9()
    GetSignalsData10()
    GetSignalsData11()
    Kq=160
    GreenMinI2=15
    GreenMaxI2=65
    KalmanGain = 0.2
    proportion_of_CAVs=0.25
    LostTime = 0
    greenExtension=6
    GreenMin=10
    GreenMax=30
    Tt = 6
    St = 0.8
    TTTt = 10
    CLength=80
    InitialArrival = 10
    InitialArrival2 = 140
    Seconds = Vissim.Net.SignalControllers.ItemByKey(1).AttValue ('CycSec')
    Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).SetAttValue('Seconds',Vissim.Net.Simulation.SimulationSecond)
    if Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).AttValue('Seconds')<=3: 
        Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).SetAttValue('ArrivalRate',100)      
        Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(2).SetAttValue('ArrivalRate',0)
        Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(3).SetAttValue('ArrivalRate',0)
        Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(4).SetAttValue('ArrivalRate',0)
        Vissim.Net.SignalControllers.ItemByKey(5).SGs.ItemByKey(1).SetAttValue('ArrivalRate',100)      
        Vissim.Net.SignalControllers.ItemByKey(5).SGs.ItemByKey(2).SetAttValue('ArrivalRate',0)
        Vissim.Net.SignalControllers.ItemByKey(5).SGs.ItemByKey(3).SetAttValue('ArrivalRate',0)
        Vissim.Net.SignalControllers.ItemByKey(5).SGs.ItemByKey(4).SetAttValue('ArrivalRate',0)
        Vissim.Net.SignalControllers.ItemByKey(12).SGs.ItemByKey(1).SetAttValue('ArrivalRate',100)      
        Vissim.Net.SignalControllers.ItemByKey(12).SGs.ItemByKey(2).SetAttValue('ArrivalRate',0)
        Vissim.Net.SignalControllers.ItemByKey(12).SGs.ItemByKey(3).SetAttValue('ArrivalRate',0)
        Vissim.Net.SignalControllers.ItemByKey(12).SGs.ItemByKey(4).SetAttValue('ArrivalRate',0)
        Vissim.Net.SignalControllers.ItemByKey(13).SGs.ItemByKey(1).SetAttValue('ArrivalRate',100)      
        Vissim.Net.SignalControllers.ItemByKey(13).SGs.ItemByKey(2).SetAttValue('ArrivalRate',0)
        Vissim.Net.SignalControllers.ItemByKey(13).SGs.ItemByKey(3).SetAttValue('ArrivalRate',0)
        Vissim.Net.SignalControllers.ItemByKey(13).SGs.ItemByKey(4).SetAttValue('ArrivalRate',0)

        Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(1).SetAttValue('ArrivalRate',0)      
        Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(2).SetAttValue('ArrivalRate',0)
        Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(3).SetAttValue('ArrivalRate',0)
        Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(4).SetAttValue('ArrivalRate',0)

        Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(1).SetAttValue('ArrivalRate',0)      
        Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(2).SetAttValue('ArrivalRate',0)
        Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(3).SetAttValue('ArrivalRate',0)
        Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(4).SetAttValue('ArrivalRate',0)

        Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(1).SetAttValue('ArrivalRate',0)      
        Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(2).SetAttValue('ArrivalRate',0)
        Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(3).SetAttValue('ArrivalRate',0)
        Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(4).SetAttValue('ArrivalRate',0)

        Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(1).SetAttValue('ArrivalRate',0)      
        Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(2).SetAttValue('ArrivalRate',0)
        Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(3).SetAttValue('ArrivalRate',0)
        Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(4).SetAttValue('ArrivalRate',0)

        Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(1).SetAttValue('ArrivalRate',0)      
        Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(2).SetAttValue('ArrivalRate',0)
        Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(3).SetAttValue('ArrivalRate',0)
        Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(4).SetAttValue('ArrivalRate',0)

        Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(1).SetAttValue('ArrivalRate',0)      
        Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(2).SetAttValue('ArrivalRate',0)
        Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(3).SetAttValue('ArrivalRate',0)
        Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(4).SetAttValue('ArrivalRate',0)

        Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(1).SetAttValue('ArrivalRate',0)      
        Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(2).SetAttValue('ArrivalRate',0)
        Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(3).SetAttValue('ArrivalRate',0)
        Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(4).SetAttValue('ArrivalRate',0)

        Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(1).SetAttValue('ArrivalRate',0)      
        Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(2).SetAttValue('ArrivalRate',0)
        Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(3).SetAttValue('ArrivalRate',0)
        Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(4).SetAttValue('ArrivalRate',0)

        Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(1).SetAttValue('ArrivalRate',0)      
        Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(2).SetAttValue('ArrivalRate',0)
        Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(3).SetAttValue('ArrivalRate',0)
        Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(4).SetAttValue('ArrivalRate',0)


        Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).SetAttValue('Queuedup',0)      
        Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(2).SetAttValue('Queuedup',0)
        Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(3).SetAttValue('Queuedup',0)
        Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(4).SetAttValue('Queuedup',0)
        Vissim.Net.SignalControllers.ItemByKey(5).SGs.ItemByKey(1).SetAttValue('Queuedup',0)      
        Vissim.Net.SignalControllers.ItemByKey(5).SGs.ItemByKey(2).SetAttValue('Queuedup',0)
        Vissim.Net.SignalControllers.ItemByKey(5).SGs.ItemByKey(3).SetAttValue('Queuedup',0)
        Vissim.Net.SignalControllers.ItemByKey(5).SGs.ItemByKey(4).SetAttValue('Queuedup',0)
        Vissim.Net.SignalControllers.ItemByKey(12).SGs.ItemByKey(1).SetAttValue('Queuedup',0)      
        Vissim.Net.SignalControllers.ItemByKey(12).SGs.ItemByKey(2).SetAttValue('Queuedup',0)
        Vissim.Net.SignalControllers.ItemByKey(12).SGs.ItemByKey(3).SetAttValue('Queuedup',0)
        Vissim.Net.SignalControllers.ItemByKey(12).SGs.ItemByKey(4).SetAttValue('Queuedup',0)
        Vissim.Net.SignalControllers.ItemByKey(13).SGs.ItemByKey(1).SetAttValue('Queuedup',0)      
        Vissim.Net.SignalControllers.ItemByKey(13).SGs.ItemByKey(2).SetAttValue('Queuedup',0)
        Vissim.Net.SignalControllers.ItemByKey(13).SGs.ItemByKey(3).SetAttValue('Queuedup',0)
        Vissim.Net.SignalControllers.ItemByKey(13).SGs.ItemByKey(4).SetAttValue('Queuedup',0)

        Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(1).SetAttValue('Queuedup',0)      
        Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(2).SetAttValue('Queuedup',0)
        Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(3).SetAttValue('Queuedup',0)
        Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(4).SetAttValue('Queuedup',0)

        Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(1).SetAttValue('Queuedup',0)      
        Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(2).SetAttValue('Queuedup',0)
        Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(3).SetAttValue('Queuedup',0)
        Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(4).SetAttValue('Queuedup',0)

        Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(1).SetAttValue('Queuedup',0)      
        Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(2).SetAttValue('Queuedup',0)
        Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(3).SetAttValue('Queuedup',0)
        Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(4).SetAttValue('Queuedup',0)

        Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(1).SetAttValue('Queuedup',0)      
        Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(2).SetAttValue('Queuedup',0)
        Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(3).SetAttValue('Queuedup',0)
        Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(4).SetAttValue('Queuedup',0)

        Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(1).SetAttValue('Queuedup',0)      
        Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(2).SetAttValue('Queuedup',0)
        Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(3).SetAttValue('Queuedup',0)
        Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(4).SetAttValue('Queuedup',0)

        Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(1).SetAttValue('Queuedup',0)      
        Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(2).SetAttValue('Queuedup',0)
        Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(3).SetAttValue('Queuedup',0)
        Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(4).SetAttValue('Queuedup',0)

        Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(1).SetAttValue('Queuedup',0)      
        Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(2).SetAttValue('Queuedup',0)
        Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(3).SetAttValue('Queuedup',0)
        Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(4).SetAttValue('Queuedup',0)

        Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(1).SetAttValue('Queuedup',0)      
        Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(2).SetAttValue('Queuedup',0)
        Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(3).SetAttValue('Queuedup',0)
        Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(4).SetAttValue('Queuedup',0)

        Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(1).SetAttValue('Queuedup',0)      
        Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(2).SetAttValue('Queuedup',0)
        Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(3).SetAttValue('Queuedup',0)
        Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(4).SetAttValue('Queuedup',0)


        Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).SetAttValue('CriticalPhase',False)      
        Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(2).SetAttValue('CriticalPhase',False)
        Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(3).SetAttValue('CriticalPhase',False)
        Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(4).SetAttValue('CriticalPhase',False)
        Vissim.Net.SignalControllers.ItemByKey(5).SGs.ItemByKey(1).SetAttValue('CriticalPhase',False)      
        Vissim.Net.SignalControllers.ItemByKey(5).SGs.ItemByKey(2).SetAttValue('CriticalPhase',False)
        Vissim.Net.SignalControllers.ItemByKey(5).SGs.ItemByKey(3).SetAttValue('CriticalPhase',False)
        Vissim.Net.SignalControllers.ItemByKey(5).SGs.ItemByKey(4).SetAttValue('CriticalPhase',False)
        Vissim.Net.SignalControllers.ItemByKey(12).SGs.ItemByKey(1).SetAttValue('CriticalPhase',False)      
        Vissim.Net.SignalControllers.ItemByKey(12).SGs.ItemByKey(2).SetAttValue('CriticalPhase',False)
        Vissim.Net.SignalControllers.ItemByKey(12).SGs.ItemByKey(3).SetAttValue('CriticalPhase',False)
        Vissim.Net.SignalControllers.ItemByKey(12).SGs.ItemByKey(4).SetAttValue('CriticalPhase',False)
        Vissim.Net.SignalControllers.ItemByKey(13).SGs.ItemByKey(1).SetAttValue('CriticalPhase',False)      
        Vissim.Net.SignalControllers.ItemByKey(13).SGs.ItemByKey(2).SetAttValue('CriticalPhase',False)
        Vissim.Net.SignalControllers.ItemByKey(13).SGs.ItemByKey(3).SetAttValue('CriticalPhase',False)
        Vissim.Net.SignalControllers.ItemByKey(13).SGs.ItemByKey(4).SetAttValue('CriticalPhase',False)

        Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(1).SetAttValue('CriticalPhase',False)      
        Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(2).SetAttValue('CriticalPhase',False)
        Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(3).SetAttValue('CriticalPhase',False)
        Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(4).SetAttValue('CriticalPhase',False)

        Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(1).SetAttValue('CriticalPhase',False)      
        Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(2).SetAttValue('CriticalPhase',False)
        Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(3).SetAttValue('CriticalPhase',False)
        Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(4).SetAttValue('CriticalPhase',False)

        Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(1).SetAttValue('CriticalPhase',False)      
        Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(2).SetAttValue('CriticalPhase',False)
        Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(3).SetAttValue('CriticalPhase',False)
        Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(4).SetAttValue('CriticalPhase',False)

        Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(1).SetAttValue('CriticalPhase',False)      
        Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(2).SetAttValue('CriticalPhase',False)
        Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(3).SetAttValue('CriticalPhase',False)
        Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(4).SetAttValue('CriticalPhase',False)

        Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(1).SetAttValue('CriticalPhase',False)      
        Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(2).SetAttValue('CriticalPhase',False)
        Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(3).SetAttValue('CriticalPhase',False)
        Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(4).SetAttValue('CriticalPhase',False)

        Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(1).SetAttValue('CriticalPhase',False)      
        Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(2).SetAttValue('CriticalPhase',False)
        Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(3).SetAttValue('CriticalPhase',False)
        Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(4).SetAttValue('CriticalPhase',False)

        Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(1).SetAttValue('CriticalPhase',False)      
        Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(2).SetAttValue('CriticalPhase',False)
        Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(3).SetAttValue('CriticalPhase',False)
        Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(4).SetAttValue('CriticalPhase',False)

        Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(1).SetAttValue('CriticalPhase',False)      
        Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(2).SetAttValue('CriticalPhase',False)
        Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(3).SetAttValue('CriticalPhase',False)
        Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(4).SetAttValue('CriticalPhase',False)

        Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(1).SetAttValue('CriticalPhase',False)      
        Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(2).SetAttValue('CriticalPhase',False)
        Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(3).SetAttValue('CriticalPhase',False)
        Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(4).SetAttValue('CriticalPhase',False)


#Finding the critical phase according to the arrival rates
    if Seconds >=0:
        A1=0
        A2=0
        A3=0
        A4=0
        A5=0
        A6=0
        A7=0
        A8=0
        A9=0
        A10=0
        A11=0
        A12=0
        A13=0
        A14=0
        A15=0
        A16=0
        A17=0
        A18=0
        A19=0
        A20=0
        A21=0
        A22=0
        A23=0
        A24=0
        A25=0
        A26=0
        A27=0
        A28=0
        A29=0
        A30=0
        A31=0
        A32=0
        A33=0
        A34=0
        A35=0
        A36=0
        A37=0
        A38=0
        A39=0
        A40=0
        A41=0
        A42=0
        A43=0
        A44=0
        A45=0
        A46=0
        A47=0
        A48=0
        A49=0
        A50=0
        A51=0
        A52=0
        A53=0
        A54=0
        A55=0
        A56=0
        if Seconds <=1:
            A1=0
            A2=0
            A3=0
            A4=0
            A5=0
            A6=0
            A7=0
            A8=0
            A9=0
            A10=0
            A11=0
            A12=0
            A13=0
            A14=0
            A15=0
            A16=0
            A17=0
            A18=0
            A19=0
            A20=0
            A21=0
            A22=0
            A23=0
            A24=0
            A25=0
            A26=0
            A27=0
            A28=0
            A29=0
            A30=0
            A31=0
            A32=0
            A33=0
            A34=0
            A35=0
            A36=0
            A37=0
            A38=0
            A39=0
            A40=0
            A41=0
            A42=0
            A43=0
            A44=0
            A45=0
            A46=0
            A47=0
            A48=0
            A49=0
            A50=0
            A51=0
            A52=0
            A53=0
            A54=0
            A55=0
            A56=0
                    
            Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(1).SetAttValue ('len9',0)
       
            Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(3).SetAttValue ('len9',0)
       
            Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(2).SetAttValue ('len9',0)
         
            Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(4).SetAttValue ('len9',0)                                                                                     
       
            Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(1).SetAttValue ('len9',0)

            Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(4).SetAttValue ('len9',0)
         
            Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(2).SetAttValue ('len9',0)
         
            Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(3).SetAttValue ('len9',0)
       
            Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(1).SetAttValue ('len9',0)
         
            Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(4).SetAttValue ('len9',0)
            
            Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(3).SetAttValue ('len9',0)
         
            Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(2).SetAttValue ('len9',0)
          
            Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(2).SetAttValue ('len9',0)
          
            Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(3).SetAttValue ('len9',0)
     
            Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(4).SetAttValue ('len9',0)
         
            Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(1).SetAttValue ('len9',0)
       
            Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(3).SetAttValue ('len9',0)
     
            Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(4).SetAttValue ('len9',0)
        
            Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(1).SetAttValue ('len9',0)
         
            Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(2).SetAttValue ('len9',0)
      
            Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(3).SetAttValue ('len9',0)
        
            Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(4).SetAttValue ('len9',0)
       
            Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(1).SetAttValue ('len9',0)
        
            Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(2).SetAttValue ('len9',0)
         
            Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(2).SetAttValue ('len9',0)

            Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(1).SetAttValue ('len9',0)
             
            Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(3).SetAttValue ('len9',0)
            
            Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(4).SetAttValue ('len9',0)

            Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(1).SetAttValue ('len9',0)
        
            Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(2).SetAttValue ('len9',0)
        
            Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(3).SetAttValue ('len9',0)
      
            Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(4).SetAttValue ('len9',0)
            
            Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(1).SetAttValue ('len9',0)
                
            Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(2).SetAttValue ('len9',0)
              
            Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(3).SetAttValue ('len9',0)
          
            Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(4).SetAttValue ('len9',0)



        if Seconds >1:
            for vehAttributes in vehsAttributes:
                if vehAttributes[vehsAttNames['VehType\No']] in vehTypesEquipped:       
                    if vehAttributes[vehsAttNames['Pos']] != None:
                        if vehAttributes[vehsAttNames['Lane\Link']] != 107 and vehAttributes[vehsAttNames['Lane\Link']] != 108 and vehAttributes[vehsAttNames['Lane\Link']] != 109 and vehAttributes[vehsAttNames['Lane\Link']] != 110 and vehAttributes[vehsAttNames['Lane\Link']] != 112 and vehAttributes[vehsAttNames['Lane\Link']] != 113 and vehAttributes[vehsAttNames['Lane\Link']] != 114:
                            Dist = vehAttributes[vehsAttNames['DistanceToSigHead']]
                            Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).SetAttValue ('LinkNo3',Dist)
                            if Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).AttValue ('LinkNo3') <= 49 and Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).AttValue ('LinkNo3') >= 47:
                                Speed = vehAttributes[vehsAttNames['Speed']]
                                Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).SetAttValue ('LinkNo4',Speed)
                                if Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).AttValue ('LinkNo4') != 0:
                                    Link = vehAttributes[vehsAttNames['Lane\Link']]
                                    Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).SetAttValue ('LinkNo2',Link)
                                    if Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).AttValue ('LinkNo2') == 99:
                                        A6 = Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(1).AttValue ('len9')+1
                                        Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(1).SetAttValue ('len9', A6)

                                    if Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).AttValue ('LinkNo2') == 65:
                                        A7=Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(3).AttValue ('len9')+1
                                        Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(3).SetAttValue ('len9', A7)
                                        

                                    if Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).AttValue ('LinkNo2') == 75:
                                        A8 = Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(2).AttValue ('len9')+1
                                        Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(2).SetAttValue ('len9', A8)

                                    if Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).AttValue ('LinkNo2') == 102:
                                        A9 =  Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(4).AttValue ('len9')+1
                                        Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(4).SetAttValue ('len9', A9)


                                    if Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).AttValue ('LinkNo2') == 76:
                                        A15 =  Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(1).AttValue ('len9')+1
                                        Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(1).SetAttValue ('len9', A15)

                                    if Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).AttValue ('LinkNo2') == 86:
                                        A16 = Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(4).AttValue ('len9')+1
                                        Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(4).SetAttValue ('len9', A16)

                                    if Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).AttValue ('LinkNo2') == 77:
                                        A17 = Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(2).AttValue ('len9')+1
                                        Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(2).SetAttValue ('len9', A17)


                                    if Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).AttValue ('LinkNo2') == 67:
                                        A18 = Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(3).AttValue ('len9')+1
                                        Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(3).SetAttValue ('len9', A18)


                                    if Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).AttValue ('LinkNo2') == 78:
                                        A19 = Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(1).AttValue ('len9')+1
                                        Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(1).SetAttValue ('len9', A19)


                                    if Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).AttValue ('LinkNo2') == 96:
                                        A20 = Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(4).AttValue ('len9')+1
                                        Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(4).SetAttValue ('len9', A20)

                                    if Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).AttValue ('LinkNo2') == 69:
                                        A21 = Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(3).AttValue ('len9')+1
                                        Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(3).SetAttValue ('len9', A21)

                                    if Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).AttValue ('LinkNo2') == 97:
                                        A22 = Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(2).AttValue ('len9')+1
                                        Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(2).SetAttValue ('len9', A22)


                                    if Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).AttValue ('LinkNo2') == 70 :
                                        A28 = Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(2).AttValue ('len9')+1
                                        Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(2).SetAttValue ('len9', A28)

                                    if Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).AttValue ('LinkNo2') == 87:
                                        A29 = Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(3).AttValue ('len9')+1
                                        Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(3).SetAttValue ('len9', A29)

                                    if Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).AttValue ('LinkNo2') == 63 :
                                        A30 = Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(4).AttValue ('len9')+1
                                        Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(4).SetAttValue ('len9', A30)


                                    if Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).AttValue ('LinkNo2') == 82:
                                        A31 = Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(1).AttValue ('len9')+1
                                        Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(1).SetAttValue ('len9', A31)


                                    if Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).AttValue ('LinkNo2') == 81:
                                        A32 =  Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(3).AttValue ('len9')+1
                                        Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(3).SetAttValue ('len9', A32)


                                    if Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).AttValue ('LinkNo2') == 61:
                                        A33 =  Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(4).AttValue ('len9')+1
                                        Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(4).SetAttValue ('len9', A33)

                                    if Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).AttValue ('LinkNo2') == 80:
                                        A34 = Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(1).AttValue ('len9')+1
                                        Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(1).SetAttValue ('len9', A34)

                                    if Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).AttValue ('LinkNo2') == 68:
                                        A35 =  Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(2).AttValue ('len9')+1
                                        Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(2).SetAttValue ('len9', A35)


                                    if Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).AttValue ('LinkNo2') == 79:
                                        A36 =  Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(3).AttValue ('len9')+1
                                        Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(3).SetAttValue ('len9', A36)
                                       

                                    if Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).AttValue ('LinkNo2') == 59:
                                        A37 =  Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(4).AttValue ('len9')+1
                                        Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(4).SetAttValue ('len9', A37)

                                    if Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).AttValue ('LinkNo2') == 90:
                                        A38 =  Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(1).AttValue ('len9')+1
                                        Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(1).SetAttValue ('len9', A38)


                                    if Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).AttValue ('LinkNo2') == 66:
                                        A39 =  Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(2).AttValue ('len9')+1
                                        Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(2).SetAttValue ('len9', A39)


                                    if Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).AttValue ('LinkNo2') == 60:
                                        A40 = Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(2).AttValue ('len9')+1
                                        Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(2).SetAttValue ('len9', A40)

                                    if Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).AttValue ('LinkNo2') == 92:
                                        A41 =  Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(1).AttValue ('len9')+1
                                        Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(1).SetAttValue ('len9', A41)

                                    if Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).AttValue ('LinkNo2') == 71:
                                        A42 = Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(3).AttValue ('len9')+1
                                        Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(3).SetAttValue ('len9', A42)

                                    if Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).AttValue ('LinkNo2') == 93:
                                        A43 = Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(4).AttValue ('len9')+1
                                        Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(4).SetAttValue ('len9', A43)


                                    if Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).AttValue ('LinkNo2') == 72:
                                        A44 = Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(1).AttValue ('len9')+1
                                        Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(1).SetAttValue ('len9', A44)

                                    if Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).AttValue ('LinkNo2') == 62:
                                        A45 = Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(2).AttValue ('len9')+1
                                        Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(2).SetAttValue ('len9', A45)

                                    if Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).AttValue ('LinkNo2') == 73:
                                        A46 = Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(3).AttValue ('len9')+1
                                        Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(3).SetAttValue ('len9', A46)

                                    if Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).AttValue ('LinkNo2') == 83:
                                        A47 = Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(4).AttValue ('len9')+1
                                        Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(4).SetAttValue ('len9', A47)


                                    if Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).AttValue ('LinkNo2') == 74:
                                        A48 = Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(1).AttValue ('len9')+1
                                        Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(1).SetAttValue ('len9', A48)

                                    if Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).AttValue ('LinkNo2') == 64:
                                        A49 = Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(2).AttValue ('len9')+1
                                        Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(2).SetAttValue ('len9', A49)


                                    if Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).AttValue ('LinkNo2') == 104:
                                        A50 = Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(3).AttValue ('len9')+1
                                        Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(3).SetAttValue ('len9', A50)

                                    if Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).AttValue ('LinkNo2') == 105:
                                        A51 = Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(4).AttValue ('len9') +1
                                        Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(4).SetAttValue ('len9', A51)


                continue
                
        if Seconds>=72 and Seconds<=76:
            if Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(1).AttValue ('len9') == 0:
                arrival912= InitialArrival
            else:
                arrival912=(Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(1).AttValue ('len9')/(proportion_of_CAVs*CLength))*3600
            arrival911= Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(1).AttValue ('ArrivalRate')
            Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(1).SetAttValue ('Arrival1', arrival911)
            Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(1).SetAttValue ('Arrival2', arrival912)


            if Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(3).AttValue ('len9')==0:
                arrival932= InitialArrival
            else:
                arrival932=(Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(3).AttValue ('len9')/(proportion_of_CAVs*CLength))*3600
            arrival931= Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(3).AttValue ('ArrivalRate')

            Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(3).SetAttValue ('Arrival1', arrival931)
            Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(3).SetAttValue ('Arrival2', arrival932)



            if Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(2).AttValue ('len9')==0:
                arrival922= InitialArrival
            else:
                arrival922=(Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(2).AttValue ('len9')/(proportion_of_CAVs*CLength))*3600
            arrival921= Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(2).AttValue ('ArrivalRate')

            Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(2).SetAttValue ('Arrival1', arrival921)
            Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(2).SetAttValue ('Arrival2', arrival922)




            if Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(4).AttValue ('len9')==0:
                arrival942= InitialArrival
            else:
                arrival942=(Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(4).AttValue ('len9')/(proportion_of_CAVs*CLength))*3600
            arrival941= Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(4).AttValue ('ArrivalRate')

            Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(4).SetAttValue ('Arrival1', arrival941)
            Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(4).SetAttValue ('Arrival2', arrival942)

                                                                                           


            if Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(1).AttValue ('len9')==0:
                arrival1012= InitialArrival
            else:
                arrival1012=(Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(1).AttValue ('len9')/(proportion_of_CAVs*CLength))*3600
            arrival1011= Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(1).AttValue ('ArrivalRate')
            Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(1).SetAttValue ('Arrival1', arrival1011)
            Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(1).SetAttValue ('Arrival2', arrival1012)



            if Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(4).AttValue ('len9')==0:
                arrival1042= InitialArrival
            else:
                arrival1042=(Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(4).AttValue ('len9')/(proportion_of_CAVs*CLength))*3600
            arrival1041= Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(4).AttValue ('ArrivalRate')
            Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(4).SetAttValue ('Arrival1', arrival1041)
            Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(4).SetAttValue ('Arrival2', arrival1042)





            if Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(2).AttValue ('len9')==0:
                arrival1022= InitialArrival
            else:
                arrival1022=(Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(2).AttValue ('len9')/(proportion_of_CAVs*CLength))*3600
            arrival1021= Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(2).AttValue ('ArrivalRate')

            Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(2).SetAttValue ('Arrival1', arrival1021)
            Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(2).SetAttValue ('Arrival2', arrival1022)


            if Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(3).AttValue ('len9')==0:
                arrival1032= InitialArrival
            else:
                arrival1032=(Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(3).AttValue ('len9')/(proportion_of_CAVs*CLength))*3600
            arrival1031= Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(3).AttValue ('ArrivalRate')

            Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(3).SetAttValue ('Arrival1', arrival1031)
            Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(3).SetAttValue ('Arrival2', arrival1032)


            if  Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(1).AttValue ('len9')==0:
                arrival1112= InitialArrival
            else:
                arrival1112=( Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(1).AttValue ('len9')/(proportion_of_CAVs*CLength))*3600
            arrival1111= Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(1).AttValue ('ArrivalRate')

            Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(1).SetAttValue ('Arrival1', arrival1111)
            Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(1).SetAttValue ('Arrival2', arrival1112)



            if Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(4).AttValue ('len9')==0:
                arrival1142= InitialArrival
            else:
                arrival1142=(Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(4).AttValue ('len9')/(proportion_of_CAVs*CLength))*3600
            arrival1141= Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(4).AttValue ('ArrivalRate')

            Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(4).SetAttValue ('Arrival1', arrival1141)
            Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(4).SetAttValue ('Arrival2', arrival1142)




            if Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(3).AttValue ('len9')==0:
                arrival1132= InitialArrival
            else:
                arrival1132=(Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(3).AttValue ('len9')/(proportion_of_CAVs*CLength))*3600
            arrival1131= Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(3).AttValue ('ArrivalRate')


            Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(3).SetAttValue ('Arrival1', arrival1131)
            Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(3).SetAttValue ('Arrival2', arrival1132)

            
            if Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(2).AttValue ('len9')==0:
                arrival1122= InitialArrival
            else:
                arrival1122=(Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(2).AttValue ('len9')/(proportion_of_CAVs*CLength))*3600
            arrival1121= Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(2).AttValue ('ArrivalRate')


            Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(2).SetAttValue ('Arrival1', arrival1121)
            Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(2).SetAttValue ('Arrival2', arrival1122)



            if Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(2).AttValue ('len9')==0:
                arrival422= InitialArrival
            else:
                arrival422=(Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(2).AttValue ('len9')/(proportion_of_CAVs*CLength))*3600
            arrival421= Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(2).AttValue ('ArrivalRate')


            Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(2).SetAttValue ('Arrival1', arrival421)
            Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(2).SetAttValue ('Arrival2', arrival422)




            if Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(3).AttValue ('len9')==0:
                arrival432= InitialArrival
            else:
                arrival432=(Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(3).AttValue ('len9')/(proportion_of_CAVs*CLength))*3600
            arrival431= Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(3).AttValue ('ArrivalRate')
            Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(3).SetAttValue ('Arrival1', arrival431)
            Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(3).SetAttValue ('Arrival2', arrival432)






            if Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(4).AttValue ('len9')==0:
                arrival442= InitialArrival
            else:
                arrival442=(Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(4).AttValue ('len9')/(proportion_of_CAVs*CLength))*3600
            arrival441= Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(4).AttValue ('ArrivalRate')
            Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(4).SetAttValue ('Arrival1', arrival441)
            Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(4).SetAttValue ('Arrival2', arrival442)







            if Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(1).AttValue ('len9')==0:
                arrival412= InitialArrival
            else:
                arrival412=(Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(1).AttValue ('len9')/(proportion_of_CAVs*CLength))*3600
            arrival411= Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(1).AttValue ('ArrivalRate')

            Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(1).SetAttValue ('Arrival1', arrival411)
            Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(1).SetAttValue ('Arrival2', arrival412)







            if Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(3).AttValue ('len9') ==0:
                arrival332= InitialArrival
            else:
                arrival332=(Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(3).AttValue ('len9')/(proportion_of_CAVs*CLength))*3600
            arrival331= Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(3).AttValue ('ArrivalRate')


            Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(3).SetAttValue ('Arrival1', arrival331)
            Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(3).SetAttValue ('Arrival2', arrival332)





            if Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(4).AttValue ('len9')==0:
                arrival342= InitialArrival
            else:
                arrival342=(Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(4).AttValue ('len9')/(proportion_of_CAVs*CLength))*3600
            arrival341= Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(4).AttValue ('ArrivalRate')


            Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(4).SetAttValue ('Arrival1', arrival341)
            Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(4).SetAttValue ('Arrival2', arrival342)



            if Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(1).AttValue ('len9')==0:
                arrival312= InitialArrival
            else:
                arrival312=(Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(1).AttValue ('len9')/(proportion_of_CAVs*CLength))*3600
            arrival311= Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(1).AttValue ('ArrivalRate')


            Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(1).SetAttValue ('Arrival1', arrival311)
            Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(1).SetAttValue ('Arrival2', arrival312)




            if Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(2).AttValue ('len9')==0:
                arrival322= InitialArrival
            else:
                arrival322=(Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(2).AttValue ('len9')/(proportion_of_CAVs*CLength))*3600
            arrival321= Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(2).AttValue ('ArrivalRate')

            Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(2).SetAttValue ('Arrival1', arrival321)
            Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(2).SetAttValue ('Arrival2', arrival322)




            if Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(3).AttValue ('len9')==0:
                arrival232= InitialArrival
            else:
                arrival232=(Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(3).AttValue ('len9')/(proportion_of_CAVs*CLength))*3600
            arrival231= Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(3).AttValue ('ArrivalRate')


            Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(3).SetAttValue ('Arrival1', arrival231)
            Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(3).SetAttValue ('Arrival2', arrival232)



            if Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(4).AttValue ('len9')==0:
                arrival242= InitialArrival
            else:
                arrival242=(Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(4).AttValue ('len9')/(proportion_of_CAVs*CLength))*3600
            arrival241= Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(4).AttValue ('ArrivalRate')


            Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(4).SetAttValue ('Arrival1', arrival241)
            Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(4).SetAttValue ('Arrival2', arrival242)





            if Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(1).AttValue ('len9')==0:
                arrival212= InitialArrival
            else:
                arrival212=(Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(1).AttValue ('len9')/(proportion_of_CAVs*CLength))*3600
            arrival211= Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(1).AttValue ('ArrivalRate')
            Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(1).SetAttValue ('Arrival1', arrival211)
            Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(1).SetAttValue ('Arrival2', arrival212)




            if Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(2).AttValue ('len9')==0:
                arrival222= InitialArrival
            else:
                arrival222=(Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(2).AttValue ('len9')/(proportion_of_CAVs*CLength))*3600
            arrival221= Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(2).AttValue ('ArrivalRate')
            Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(2).SetAttValue ('Arrival1', arrival221)
            Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(2).SetAttValue ('Arrival2', arrival222)
            
                 



            if Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(2).AttValue ('len9')==0:
                arrival622= InitialArrival
            else:
                arrival622=(Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(2).AttValue ('len9')/(proportion_of_CAVs*CLength))*3600
            arrival621= Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(2).AttValue ('ArrivalRate')


            Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(2).SetAttValue ('Arrival1', arrival621)
            Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(2).SetAttValue ('Arrival2', arrival622)





            if Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(1).AttValue ('len9')==0:
                arrival612= InitialArrival
            else:
                arrival612=(Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(1).AttValue ('len9')/(proportion_of_CAVs*CLength))*3600
            arrival611= Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(1).AttValue ('ArrivalRate')

            Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(1).SetAttValue ('Arrival1', arrival611)
            Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(1).SetAttValue ('Arrival2', arrival612)        


            if  Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(3).AttValue ('len9')==0:
                arrival632= InitialArrival
            else:
                arrival632=( Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(3).AttValue ('len9')/(proportion_of_CAVs*CLength))*3600
            arrival631= Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(3).AttValue ('ArrivalRate')


            Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(3).SetAttValue ('Arrival1', arrival631)
            Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(3).SetAttValue ('Arrival2', arrival632)


            if Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(4).AttValue ('len9')==0:
                arrival642= InitialArrival
            else:
                arrival642=(Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(4).AttValue ('len9')/(proportion_of_CAVs*CLength))*3600
            arrival641= Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(4).AttValue ('ArrivalRate')

            Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(4).SetAttValue ('Arrival1', arrival641)
            Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(4).SetAttValue ('Arrival2', arrival642)


            if Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(1).AttValue ('len9')==0:
                arrival712= InitialArrival
            else:
                arrival712=(Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(1).AttValue ('len9')/(proportion_of_CAVs*CLength))*3600
            arrival711= Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(1).AttValue ('ArrivalRate')


            Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(1).SetAttValue ('Arrival1', arrival711)
            Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(1).SetAttValue ('Arrival2', arrival712)


            if Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(2).AttValue ('len9')==0:
                arrival722= InitialArrival
            else:
                arrival722=(Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(2).AttValue ('len9')/(proportion_of_CAVs*CLength))*3600
            arrival721= Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(2).AttValue ('ArrivalRate')

            Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(2).SetAttValue ('Arrival1', arrival721)
            Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(2).SetAttValue ('Arrival2', arrival722)



            if Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(3).AttValue ('len9')==0:
                arrival732= InitialArrival
            else:
                arrival732=(Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(3).AttValue ('len9')/(proportion_of_CAVs*CLength))*3600
                
            arrival731= Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(3).AttValue ('ArrivalRate')

            Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(3).SetAttValue ('Arrival1', arrival731)
            Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(3).SetAttValue ('Arrival2', arrival732)



            if Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(4).AttValue ('len9')==0:
                arrival742= InitialArrival
            else:
                arrival742=(Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(4).AttValue ('len9')/(proportion_of_CAVs*CLength))*3600
                
            arrival741= Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(4).AttValue ('ArrivalRate')

            Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(4).SetAttValue ('Arrival1', arrival741)
            Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(4).SetAttValue ('Arrival2', arrival742)



            if  Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(1).AttValue ('len9')==0:
                arrival812= InitialArrival
            else:
                arrival812=( Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(1).AttValue ('len9')/(proportion_of_CAVs*CLength))*3600
                
            arrival811= Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(1).AttValue ('ArrivalRate')

            Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(1).SetAttValue ('Arrival1', arrival811)
            Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(1).SetAttValue ('Arrival2', arrival812)        


            if Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(2).AttValue ('len9')==0:
                arrival822= InitialArrival
            else:
                arrival822=(Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(2).AttValue ('len9')/(proportion_of_CAVs*CLength))*3600
                
            arrival821= Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(2).AttValue ('ArrivalRate')
            Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(2).SetAttValue ('Arrival1', arrival821)
            Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(2).SetAttValue ('Arrival2', arrival822) 
            

            if Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(3).AttValue ('len9')==0:
                arrival832= InitialArrival
            else:
                arrival832=(Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(3).AttValue ('len9')/(proportion_of_CAVs*CLength))*3600
                
            arrival831= Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(3).AttValue ('ArrivalRate')

            Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(3).SetAttValue ('Arrival1', arrival831)
            Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(3).SetAttValue ('Arrival2', arrival832) 
            



            if Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(4).AttValue ('len9')==0:
                arrival842= InitialArrival
            else:
                arrival842=( Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(4).AttValue ('len9')/(proportion_of_CAVs*CLength))*3600
                
            arrival841= Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(4).AttValue ('ArrivalRate')

            Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(4).SetAttValue ('Arrival1', arrival821)
            Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(4).SetAttValue ('Arrival2', arrival822) 
            

        if Seconds >= 77:                     
            ArrivalUpdate91 = Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(1).AttValue ('Arrival1') + KalmanGain*(Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(1).AttValue ('Arrival2')-Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(1).AttValue ('Arrival1'))                       
            Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(1).SetAttValue ('ArrivalRate',ArrivalUpdate91)

            ArrivalUpdate92 = Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(2).AttValue ('Arrival1') + KalmanGain*(Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(2).AttValue ('Arrival2')-Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(2).AttValue ('Arrival1'))                       
            Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(2).SetAttValue ('ArrivalRate',ArrivalUpdate92)

            ArrivalUpdate93 = Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(3).AttValue ('Arrival1') + KalmanGain*(Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(3).AttValue ('Arrival2')-Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(3).AttValue ('Arrival1'))                       
            Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(3).SetAttValue ('ArrivalRate',ArrivalUpdate93)


            ArrivalUpdate94 = Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(4).AttValue ('Arrival1') + KalmanGain*(Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(4).AttValue ('Arrival2')-Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(4).AttValue ('Arrival1'))                       
            Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(4).SetAttValue ('ArrivalRate',ArrivalUpdate94)

            ArrivalUpdate101 = Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(1).AttValue ('Arrival1') + KalmanGain*(Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(1).AttValue ('Arrival2')-Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(1).AttValue ('Arrival1'))                       
            Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(1).SetAttValue ('ArrivalRate',ArrivalUpdate101)

            ArrivalUpdate102 = Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(2).AttValue ('Arrival1') + KalmanGain*(Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(2).AttValue ('Arrival2')-Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(2).AttValue ('Arrival1'))                       
            Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(2).SetAttValue ('ArrivalRate',ArrivalUpdate102)

            ArrivalUpdate103 = Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(3).AttValue ('Arrival1') + KalmanGain*(Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(3).AttValue ('Arrival2')-Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(3).AttValue ('Arrival1'))                       
            Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(3).SetAttValue ('ArrivalRate',ArrivalUpdate103)


            ArrivalUpdate104 = Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(4).AttValue ('Arrival1') + KalmanGain*(Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(4).AttValue ('Arrival2')-Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(4).AttValue ('Arrival1'))                       
            Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(4).SetAttValue ('ArrivalRate',ArrivalUpdate104)

            ArrivalUpdate111 = Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(1).AttValue ('Arrival1') + KalmanGain*(Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(1).AttValue ('Arrival2')-Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(1).AttValue ('Arrival1'))                       
            Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(1).SetAttValue ('ArrivalRate',ArrivalUpdate111)

            ArrivalUpdate112 = Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(2).AttValue ('Arrival1') + KalmanGain*(Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(2).AttValue ('Arrival2')-Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(2).AttValue ('Arrival1'))                       
            Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(2).SetAttValue ('ArrivalRate',ArrivalUpdate112)

            ArrivalUpdate113 = Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(3).AttValue ('Arrival1') + KalmanGain*(Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(3).AttValue ('Arrival2')-Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(3).AttValue ('Arrival1'))                       
            Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(3).SetAttValue ('ArrivalRate',ArrivalUpdate113)


            ArrivalUpdate114 = Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(4).AttValue ('Arrival1') + KalmanGain*(Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(4).AttValue ('Arrival2')-Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(4).AttValue ('Arrival1'))                       
            Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(4).SetAttValue ('ArrivalRate',ArrivalUpdate114)

            ArrivalUpdate61 = Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(1).AttValue ('Arrival1') + KalmanGain*(Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(1).AttValue ('Arrival2')-Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(1).AttValue ('Arrival1'))                       
            Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(1).SetAttValue ('ArrivalRate',ArrivalUpdate61)

            ArrivalUpdate62 = Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(2).AttValue ('Arrival1') + KalmanGain*(Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(2).AttValue ('Arrival2')-Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(2).AttValue ('Arrival1'))                       
            Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(2).SetAttValue ('ArrivalRate',ArrivalUpdate62)

            ArrivalUpdate63 = Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(3).AttValue ('Arrival1') + KalmanGain*(Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(3).AttValue ('Arrival2')-Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(3).AttValue ('Arrival1'))                       
            Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(3).SetAttValue ('ArrivalRate',ArrivalUpdate63)


            ArrivalUpdate64 = Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(4).AttValue ('Arrival1') + KalmanGain*(Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(4).AttValue ('Arrival2')-Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(4).AttValue ('Arrival1'))                       
            Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(4).SetAttValue ('ArrivalRate',ArrivalUpdate64)


            ArrivalUpdate71 = Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(1).AttValue ('Arrival1') + KalmanGain*(Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(1).AttValue ('Arrival2')-Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(1).AttValue ('Arrival1'))                       
            Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(1).SetAttValue ('ArrivalRate',ArrivalUpdate71)

            ArrivalUpdate72 = Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(2).AttValue ('Arrival1') + KalmanGain*(Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(2).AttValue ('Arrival2')-Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(2).AttValue ('Arrival1'))                       
            Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(2).SetAttValue ('ArrivalRate',ArrivalUpdate72)

            ArrivalUpdate73 = Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(3).AttValue ('Arrival1') + KalmanGain*(Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(3).AttValue ('Arrival2')-Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(3).AttValue ('Arrival1'))                       
            Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(3).SetAttValue ('ArrivalRate',ArrivalUpdate73)


            ArrivalUpdate74 = Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(4).AttValue ('Arrival1') + KalmanGain*(Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(4).AttValue ('Arrival2')-Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(4).AttValue ('Arrival1'))                       
            Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(4).SetAttValue ('ArrivalRate',ArrivalUpdate74)

            ArrivalUpdate81 = Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(1).AttValue ('Arrival1') + KalmanGain*(Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(1).AttValue ('Arrival2')-Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(1).AttValue ('Arrival1'))                       
            Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(1).SetAttValue ('ArrivalRate',ArrivalUpdate81)

            ArrivalUpdate82 = Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(2).AttValue ('Arrival1') + KalmanGain*(Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(2).AttValue ('Arrival2')-Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(2).AttValue ('Arrival1'))                       
            Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(2).SetAttValue ('ArrivalRate',ArrivalUpdate82)

            ArrivalUpdate83 = Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(3).AttValue ('Arrival1') + KalmanGain*(Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(3).AttValue ('Arrival2')-Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(3).AttValue ('Arrival1'))                       
            Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(3).SetAttValue ('ArrivalRate',ArrivalUpdate83)


            ArrivalUpdate84 = Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(4).AttValue ('Arrival1') + KalmanGain*(Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(4).AttValue ('Arrival2')-Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(4).AttValue ('Arrival1'))                       
            Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(4).SetAttValue ('ArrivalRate',ArrivalUpdate84)



            ArrivalUpdate21 = Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(1).AttValue ('Arrival1') + KalmanGain*(Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(1).AttValue ('Arrival2')-Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(1).AttValue ('Arrival1'))                       
            Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(1).SetAttValue ('ArrivalRate',ArrivalUpdate21)

            ArrivalUpdate22 = Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(2).AttValue ('Arrival1') + KalmanGain*(Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(2).AttValue ('Arrival2')-Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(2).AttValue ('Arrival1'))                       
            Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(2).SetAttValue ('ArrivalRate',ArrivalUpdate22)

            ArrivalUpdate23 = Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(3).AttValue ('Arrival1') + KalmanGain*(Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(3).AttValue ('Arrival2')-Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(3).AttValue ('Arrival1'))                       
            Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(3).SetAttValue ('ArrivalRate',ArrivalUpdate23)


            ArrivalUpdate24 = Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(4).AttValue ('Arrival1') + KalmanGain*(Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(4).AttValue ('Arrival2')-Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(4).AttValue ('Arrival1'))                       
            Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(4).SetAttValue ('ArrivalRate',ArrivalUpdate24)


            ArrivalUpdate31 = Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(1).AttValue ('Arrival1') + KalmanGain*(Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(1).AttValue ('Arrival2')-Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(1).AttValue ('Arrival1'))                       
            Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(1).SetAttValue ('ArrivalRate',ArrivalUpdate31)

            ArrivalUpdate32 = Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(2).AttValue ('Arrival1') + KalmanGain*(Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(2).AttValue ('Arrival2')-Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(2).AttValue ('Arrival1'))                       
            Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(2).SetAttValue ('ArrivalRate',ArrivalUpdate32)

            ArrivalUpdate33 = Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(3).AttValue ('Arrival1') + KalmanGain*(Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(3).AttValue ('Arrival2')-Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(3).AttValue ('Arrival1'))                       
            Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(3).SetAttValue ('ArrivalRate',ArrivalUpdate33)


            ArrivalUpdate34 = Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(4).AttValue ('Arrival1') + KalmanGain*(Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(4).AttValue ('Arrival2')-Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(4).AttValue ('Arrival1'))                       
            Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(4).SetAttValue ('ArrivalRate',ArrivalUpdate34)



            ArrivalUpdate41 = Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(1).AttValue ('Arrival1') + KalmanGain*(Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(1).AttValue ('Arrival2')-Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(1).AttValue ('Arrival1'))                       
            Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(1).SetAttValue ('ArrivalRate',ArrivalUpdate41)

            ArrivalUpdate42 = Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(2).AttValue ('Arrival1') + KalmanGain*(Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(2).AttValue ('Arrival2')-Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(2).AttValue ('Arrival1'))                       
            Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(2).SetAttValue ('ArrivalRate',ArrivalUpdate42)

            ArrivalUpdate43 = Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(3).AttValue ('Arrival1') + KalmanGain*(Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(3).AttValue ('Arrival2')-Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(3).AttValue ('Arrival1'))                       
            Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(3).SetAttValue ('ArrivalRate',ArrivalUpdate43)


            ArrivalUpdate44 = Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(4).AttValue ('Arrival1') + KalmanGain*(Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(4).AttValue ('Arrival2')-Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(4).AttValue ('Arrival1'))                       
            Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(4).SetAttValue ('ArrivalRate',ArrivalUpdate44)



            for sig in SignalAttributes8:
                if Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(1).AttValue ('ArrivalRate') == max(Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(1).AttValue ('ArrivalRate'), Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(2).AttValue ('ArrivalRate'), Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(3).AttValue ('ArrivalRate'), Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(4).AttValue ('ArrivalRate')):
                   Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(1).SetAttValue ('CriticalPhase', True) 
                   Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(2).SetAttValue ('CriticalPhase', False)
                   Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(3).SetAttValue ('CriticalPhase', False)
                   Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(4).SetAttValue ('CriticalPhase', False)
                   break
                elif Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(2).AttValue ('ArrivalRate') == max(Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(1).AttValue ('ArrivalRate'), Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(2).AttValue ('ArrivalRate'), Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(3).AttValue ('ArrivalRate'), Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(4).AttValue ('ArrivalRate')):
                   Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(2).SetAttValue ('CriticalPhase', True) 
                   Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(1).SetAttValue ('CriticalPhase', False)
                   Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(3).SetAttValue ('CriticalPhase', False)
                   Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(4).SetAttValue ('CriticalPhase', False)
                   break
                elif Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(3).AttValue ('ArrivalRate') == max(Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(1).AttValue ('ArrivalRate'), Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(2).AttValue ('ArrivalRate'), Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(3).AttValue ('ArrivalRate'), Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(4).AttValue ('ArrivalRate')):
                   Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(3).SetAttValue ('CriticalPhase', True) 
                   Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(2).SetAttValue ('CriticalPhase', False)
                   Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(1).SetAttValue ('CriticalPhase', False)
                   Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(4).SetAttValue ('CriticalPhase', False)
                   break
                elif Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(4).AttValue ('ArrivalRate') == max(Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(1).AttValue ('ArrivalRate'), Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(2).AttValue ('ArrivalRate'), Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(3).AttValue ('ArrivalRate'), Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(4).AttValue ('ArrivalRate')):
                   Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(4).SetAttValue ('CriticalPhase', True) 
                   Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(2).SetAttValue ('CriticalPhase', False)
                   Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(3).SetAttValue ('CriticalPhase', False)
                   Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(1).SetAttValue ('CriticalPhase', False)
                   break



            for sig in SignalAttributes11:
                if Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(1).AttValue ('ArrivalRate') == max(Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(1).AttValue ('ArrivalRate'), Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(2).AttValue ('ArrivalRate'), Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(3).AttValue ('ArrivalRate'), Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(4).AttValue ('ArrivalRate')):
                   Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(1).SetAttValue ('CriticalPhase', True) 
                   Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(2).SetAttValue ('CriticalPhase', False)
                   Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(3).SetAttValue ('CriticalPhase', False)
                   Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(4).SetAttValue ('CriticalPhase', False)
                   break
                elif Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(2).AttValue ('ArrivalRate') == max(Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(1).AttValue ('ArrivalRate'), Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(2).AttValue ('ArrivalRate'), Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(3).AttValue ('ArrivalRate'), Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(4).AttValue ('ArrivalRate')):
                   Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(2).SetAttValue ('CriticalPhase', True) 
                   Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(1).SetAttValue ('CriticalPhase', False)
                   Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(3).SetAttValue ('CriticalPhase', False)
                   Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(4).SetAttValue ('CriticalPhase', False)
                   break
                elif Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(3).AttValue ('ArrivalRate') == max(Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(1).AttValue ('ArrivalRate'), Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(2).AttValue ('ArrivalRate'), Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(3).AttValue ('ArrivalRate'), Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(4).AttValue ('ArrivalRate')):
                   Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(3).SetAttValue ('CriticalPhase', True) 
                   Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(2).SetAttValue ('CriticalPhase', False)
                   Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(1).SetAttValue ('CriticalPhase', False)
                   Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(4).SetAttValue ('CriticalPhase', False)
                   break
                elif Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(4).AttValue ('ArrivalRate') == max(Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(1).AttValue ('ArrivalRate'), Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(2).AttValue ('ArrivalRate'), Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(3).AttValue ('ArrivalRate'), Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(4).AttValue ('ArrivalRate')):
                   Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(4).SetAttValue ('CriticalPhase', True) 
                   Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(2).SetAttValue ('CriticalPhase', False)
                   Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(3).SetAttValue ('CriticalPhase', False)
                   Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(1).SetAttValue ('CriticalPhase', False)
                   break


            for sig in SignalAttributes10:
                if Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(1).AttValue ('ArrivalRate') == max(Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(1).AttValue ('ArrivalRate'), Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(2).AttValue ('ArrivalRate'), Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(3).AttValue ('ArrivalRate'), Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(4).AttValue ('ArrivalRate')):
                   Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(1).SetAttValue ('CriticalPhase', True) 
                   Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(2).SetAttValue ('CriticalPhase', False)
                   Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(3).SetAttValue ('CriticalPhase', False)
                   Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(4).SetAttValue ('CriticalPhase', False)
                   break
                elif Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(2).AttValue ('ArrivalRate') == max(Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(1).AttValue ('ArrivalRate'), Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(2).AttValue ('ArrivalRate'), Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(3).AttValue ('ArrivalRate'), Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(4).AttValue ('ArrivalRate')):
                   Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(2).SetAttValue ('CriticalPhase', True) 
                   Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(1).SetAttValue ('CriticalPhase', False)
                   Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(3).SetAttValue ('CriticalPhase', False)
                   Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(4).SetAttValue ('CriticalPhase', False)
                   break
                elif Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(3).AttValue ('ArrivalRate') == max(Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(1).AttValue ('ArrivalRate'), Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(2).AttValue ('ArrivalRate'), Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(3).AttValue ('ArrivalRate'), Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(4).AttValue ('ArrivalRate')):
                   Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(3).SetAttValue ('CriticalPhase', True) 
                   Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(2).SetAttValue ('CriticalPhase', False)
                   Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(1).SetAttValue ('CriticalPhase', False)
                   Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(4).SetAttValue ('CriticalPhase', False)
                   break
                elif Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(4).AttValue ('ArrivalRate') == max(Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(1).AttValue ('ArrivalRate'), Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(2).AttValue ('ArrivalRate'), Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(3).AttValue ('ArrivalRate'), Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(4).AttValue ('ArrivalRate')):
                   Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(4).SetAttValue ('CriticalPhase', True) 
                   Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(2).SetAttValue ('CriticalPhase', False)
                   Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(3).SetAttValue ('CriticalPhase', False)
                   Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(1).SetAttValue ('CriticalPhase', False)
                   break



            for sig in SignalAttributes9:
                if Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(1).AttValue ('ArrivalRate') == max(Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(1).AttValue ('ArrivalRate'), Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(2).AttValue ('ArrivalRate'), Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(3).AttValue ('ArrivalRate'), Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(4).AttValue ('ArrivalRate')):
                   Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(1).SetAttValue ('CriticalPhase', True) 
                   Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(2).SetAttValue ('CriticalPhase', False)
                   Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(3).SetAttValue ('CriticalPhase', False)
                   Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(4).SetAttValue ('CriticalPhase', False)
                   break
                elif Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(2).AttValue ('ArrivalRate') == max(Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(1).AttValue ('ArrivalRate'), Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(2).AttValue ('ArrivalRate'), Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(3).AttValue ('ArrivalRate'), Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(4).AttValue ('ArrivalRate')):
                   Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(2).SetAttValue ('CriticalPhase', True) 
                   Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(1).SetAttValue ('CriticalPhase', False)
                   Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(3).SetAttValue ('CriticalPhase', False)
                   Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(4).SetAttValue ('CriticalPhase', False)
                   break
                elif Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(3).AttValue ('ArrivalRate') == max(Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(1).AttValue ('ArrivalRate'), Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(2).AttValue ('ArrivalRate'), Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(3).AttValue ('ArrivalRate'), Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(4).AttValue ('ArrivalRate')):
                   Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(3).SetAttValue ('CriticalPhase', True) 
                   Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(2).SetAttValue ('CriticalPhase', False)
                   Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(1).SetAttValue ('CriticalPhase', False)
                   Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(4).SetAttValue ('CriticalPhase', False)
                   break
                elif Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(4).AttValue ('ArrivalRate') == max(Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(1).AttValue ('ArrivalRate'), Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(2).AttValue ('ArrivalRate'), Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(3).AttValue ('ArrivalRate'), Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(4).AttValue ('ArrivalRate')):
                   Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(4).SetAttValue ('CriticalPhase', True) 
                   Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(2).SetAttValue ('CriticalPhase', False)
                   Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(3).SetAttValue ('CriticalPhase', False)
                   Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(1).SetAttValue ('CriticalPhase', False)
                   break


            for sig in SignalAttributes7:
                if Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(1).AttValue ('ArrivalRate') == max(Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(1).AttValue ('ArrivalRate'), Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(2).AttValue ('ArrivalRate'), Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(3).AttValue ('ArrivalRate'), Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(4).AttValue ('ArrivalRate')):
                   Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(1).SetAttValue ('CriticalPhase', True) 
                   Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(2).SetAttValue ('CriticalPhase', False)
                   Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(3).SetAttValue ('CriticalPhase', False)
                   Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(4).SetAttValue ('CriticalPhase', False)
                   break
                elif Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(2).AttValue ('ArrivalRate') == max(Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(1).AttValue ('ArrivalRate'), Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(2).AttValue ('ArrivalRate'), Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(3).AttValue ('ArrivalRate'), Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(4).AttValue ('ArrivalRate')):
                   Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(2).SetAttValue ('CriticalPhase', True) 
                   Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(1).SetAttValue ('CriticalPhase', False)
                   Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(3).SetAttValue ('CriticalPhase', False)
                   Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(4).SetAttValue ('CriticalPhase', False)
                   break
                elif Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(3).AttValue ('ArrivalRate') == max(Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(1).AttValue ('ArrivalRate'), Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(2).AttValue ('ArrivalRate'), Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(3).AttValue ('ArrivalRate'), Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(4).AttValue ('ArrivalRate')):
                   Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(3).SetAttValue ('CriticalPhase', True) 
                   Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(2).SetAttValue ('CriticalPhase', False)
                   Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(1).SetAttValue ('CriticalPhase', False)
                   Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(4).SetAttValue ('CriticalPhase', False)
                   break
                elif Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(4).AttValue ('ArrivalRate') == max(Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(1).AttValue ('ArrivalRate'), Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(2).AttValue ('ArrivalRate'), Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(3).AttValue ('ArrivalRate'), Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(4).AttValue ('ArrivalRate')):
                   Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(4).SetAttValue ('CriticalPhase', True) 
                   Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(2).SetAttValue ('CriticalPhase', False)
                   Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(3).SetAttValue ('CriticalPhase', False)
                   Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(1).SetAttValue ('CriticalPhase', False)
                   break



            for sig in SignalAttributes6:
                if Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(1).AttValue ('ArrivalRate') == max(Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(1).AttValue ('ArrivalRate'), Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(2).AttValue ('ArrivalRate'), Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(3).AttValue ('ArrivalRate'), Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(4).AttValue ('ArrivalRate')):
                   Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(1).SetAttValue ('CriticalPhase', True) 
                   Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(2).SetAttValue ('CriticalPhase', False)
                   Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(3).SetAttValue ('CriticalPhase', False)
                   Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(4).SetAttValue ('CriticalPhase', False)
                   break
                elif Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(2).AttValue ('ArrivalRate') == max(Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(1).AttValue ('ArrivalRate'), Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(2).AttValue ('ArrivalRate'), Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(3).AttValue ('ArrivalRate'), Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(4).AttValue ('ArrivalRate')):
                   Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(2).SetAttValue ('CriticalPhase', True) 
                   Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(1).SetAttValue ('CriticalPhase', False)
                   Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(3).SetAttValue ('CriticalPhase', False)
                   Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(4).SetAttValue ('CriticalPhase', False)
                   break
                elif Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(3).AttValue ('ArrivalRate') == max(Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(1).AttValue ('ArrivalRate'), Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(2).AttValue ('ArrivalRate'), Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(3).AttValue ('ArrivalRate'), Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(4).AttValue ('ArrivalRate')):
                   Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(3).SetAttValue ('CriticalPhase', True) 
                   Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(2).SetAttValue ('CriticalPhase', False)
                   Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(1).SetAttValue ('CriticalPhase', False)
                   Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(4).SetAttValue ('CriticalPhase', False)
                   break
                elif Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(4).AttValue ('ArrivalRate') == max(Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(1).AttValue ('ArrivalRate'), Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(2).AttValue ('ArrivalRate'), Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(3).AttValue ('ArrivalRate'), Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(4).AttValue ('ArrivalRate')):
                   Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(4).SetAttValue ('CriticalPhase', True) 
                   Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(2).SetAttValue ('CriticalPhase', False)
                   Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(3).SetAttValue ('CriticalPhase', False)
                   Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(1).SetAttValue ('CriticalPhase', False)
                   break





            for sig in SignalAttributes4:
                if Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(1).AttValue ('ArrivalRate') == max(Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(1).AttValue ('ArrivalRate'), Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(2).AttValue ('ArrivalRate'), Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(3).AttValue ('ArrivalRate'), Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(4).AttValue ('ArrivalRate')):
                   Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(1).SetAttValue ('CriticalPhase', True) 
                   Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(2).SetAttValue ('CriticalPhase', False)
                   Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(3).SetAttValue ('CriticalPhase', False)
                   Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(4).SetAttValue ('CriticalPhase', False)
                   break
                elif Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(2).AttValue ('ArrivalRate') == max(Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(1).AttValue ('ArrivalRate'), Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(2).AttValue ('ArrivalRate'), Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(3).AttValue ('ArrivalRate'), Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(4).AttValue ('ArrivalRate')):
                   Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(2).SetAttValue ('CriticalPhase', True) 
                   Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(1).SetAttValue ('CriticalPhase', False)
                   Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(3).SetAttValue ('CriticalPhase', False)
                   Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(4).SetAttValue ('CriticalPhase', False)
                   break
                elif Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(3).AttValue ('ArrivalRate') == max(Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(1).AttValue ('ArrivalRate'), Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(2).AttValue ('ArrivalRate'), Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(3).AttValue ('ArrivalRate'), Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(4).AttValue ('ArrivalRate')):
                   Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(3).SetAttValue ('CriticalPhase', True) 
                   Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(2).SetAttValue ('CriticalPhase', False)
                   Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(1).SetAttValue ('CriticalPhase', False)
                   Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(4).SetAttValue ('CriticalPhase', False)
                   break
                elif Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(4).AttValue ('ArrivalRate') == max(Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(1).AttValue ('ArrivalRate'), Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(2).AttValue ('ArrivalRate'), Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(3).AttValue ('ArrivalRate'), Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(4).AttValue ('ArrivalRate')):
                   Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(4).SetAttValue ('CriticalPhase', True) 
                   Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(2).SetAttValue ('CriticalPhase', False)
                   Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(3).SetAttValue ('CriticalPhase', False)
                   Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(1).SetAttValue ('CriticalPhase', False)
                   break



            for sig in SignalAttributes3:
                if Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(1).AttValue ('ArrivalRate') == max(Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(1).AttValue ('ArrivalRate'), Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(2).AttValue ('ArrivalRate'), Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(3).AttValue ('ArrivalRate'), Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(4).AttValue ('ArrivalRate')):
                   Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(1).SetAttValue ('CriticalPhase', True) 
                   Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(2).SetAttValue ('CriticalPhase', False)
                   Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(3).SetAttValue ('CriticalPhase', False)
                   Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(4).SetAttValue ('CriticalPhase', False)
                   break
                elif Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(2).AttValue ('ArrivalRate') == max(Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(1).AttValue ('ArrivalRate'), Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(2).AttValue ('ArrivalRate'), Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(3).AttValue ('ArrivalRate'), Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(4).AttValue ('ArrivalRate')):
                   Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(2).SetAttValue ('CriticalPhase', True) 
                   Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(1).SetAttValue ('CriticalPhase', False)
                   Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(3).SetAttValue ('CriticalPhase', False)
                   Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(4).SetAttValue ('CriticalPhase', False)
                   break
                elif Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(3).AttValue ('ArrivalRate') == max(Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(1).AttValue ('ArrivalRate'), Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(2).AttValue ('ArrivalRate'), Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(3).AttValue ('ArrivalRate'), Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(4).AttValue ('ArrivalRate')):
                   Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(3).SetAttValue ('CriticalPhase', True) 
                   Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(2).SetAttValue ('CriticalPhase', False)
                   Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(1).SetAttValue ('CriticalPhase', False)
                   Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(4).SetAttValue ('CriticalPhase', False)
                   break
                elif Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(4).AttValue ('ArrivalRate') == max(Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(1).AttValue ('ArrivalRate'), Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(2).AttValue ('ArrivalRate'), Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(3).AttValue ('ArrivalRate'), Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(4).AttValue ('ArrivalRate')):
                   Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(4).SetAttValue ('CriticalPhase', True) 
                   Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(2).SetAttValue ('CriticalPhase', False)
                   Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(3).SetAttValue ('CriticalPhase', False)
                   Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(1).SetAttValue ('CriticalPhase', False)
                   break

            for sig in SignalAttributes1:
                Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).SetAttValue ('CriticalPhase', True) 
                Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(2).SetAttValue ('CriticalPhase', False)                 
                Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(3).SetAttValue ('CriticalPhase', False)
                Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(4).SetAttValue ('CriticalPhase', False)       

            for sig in SignalAttributes5:
                Vissim.Net.SignalControllers.ItemByKey(5).SGs.ItemByKey(1).SetAttValue ('CriticalPhase', True) 
                Vissim.Net.SignalControllers.ItemByKey(5).SGs.ItemByKey(2).SetAttValue ('CriticalPhase', False)                 
                Vissim.Net.SignalControllers.ItemByKey(5).SGs.ItemByKey(3).SetAttValue ('CriticalPhase', False)
                Vissim.Net.SignalControllers.ItemByKey(5).SGs.ItemByKey(4).SetAttValue ('CriticalPhase', False)       


            for sig in SignalAttributes12:
                Vissim.Net.SignalControllers.ItemByKey(12).SGs.ItemByKey(1).SetAttValue ('CriticalPhase', True) 
                Vissim.Net.SignalControllers.ItemByKey(12).SGs.ItemByKey(2).SetAttValue ('CriticalPhase', False)                 
                Vissim.Net.SignalControllers.ItemByKey(12).SGs.ItemByKey(3).SetAttValue ('CriticalPhase', False)
                Vissim.Net.SignalControllers.ItemByKey(12).SGs.ItemByKey(4).SetAttValue ('CriticalPhase', False)       

            for sig in SignalAttributes13:
                Vissim.Net.SignalControllers.ItemByKey(13).SGs.ItemByKey(1).SetAttValue ('CriticalPhase', True) 
                Vissim.Net.SignalControllers.ItemByKey(13).SGs.ItemByKey(2).SetAttValue ('CriticalPhase', False)                 
                Vissim.Net.SignalControllers.ItemByKey(13).SGs.ItemByKey(3).SetAttValue ('CriticalPhase', False)
                Vissim.Net.SignalControllers.ItemByKey(13).SGs.ItemByKey(4).SetAttValue ('CriticalPhase', False)       


            for sig in SignalAttributes2:
                if Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(1).AttValue ('ArrivalRate') == max(Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(1).AttValue ('ArrivalRate'), Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(2).AttValue ('ArrivalRate'), Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(3).AttValue ('ArrivalRate'), Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(4).AttValue ('ArrivalRate')):
                   Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(1).SetAttValue ('CriticalPhase', True) 
                   Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(2).SetAttValue ('CriticalPhase', False)
                   Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(3).SetAttValue ('CriticalPhase', False)
                   Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(4).SetAttValue ('CriticalPhase', False)
                   break
                elif Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(2).AttValue ('ArrivalRate') == max(Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(1).AttValue ('ArrivalRate'), Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(2).AttValue ('ArrivalRate'), Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(3).AttValue ('ArrivalRate'), Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(4).AttValue ('ArrivalRate')):
                   Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(2).SetAttValue ('CriticalPhase', True) 
                   Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(1).SetAttValue ('CriticalPhase', False)
                   Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(3).SetAttValue ('CriticalPhase', False)
                   Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(4).SetAttValue ('CriticalPhase', False)
                   break
                elif Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(3).AttValue ('ArrivalRate') == max(Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(1).AttValue ('ArrivalRate'), Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(2).AttValue ('ArrivalRate'), Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(3).AttValue ('ArrivalRate'), Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(4).AttValue ('ArrivalRate')):
                   Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(3).SetAttValue ('CriticalPhase', True) 
                   Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(2).SetAttValue ('CriticalPhase', False)
                   Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(1).SetAttValue ('CriticalPhase', False)
                   Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(4).SetAttValue ('CriticalPhase', False)
                   break
                elif Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(4).AttValue ('ArrivalRate') == max(Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(1).AttValue ('ArrivalRate'), Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(2).AttValue ('ArrivalRate'), Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(3).AttValue ('ArrivalRate'), Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(4).AttValue ('ArrivalRate')):
                   Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(4).SetAttValue ('CriticalPhase', True) 
                   Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(2).SetAttValue ('CriticalPhase', False)
                   Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(3).SetAttValue ('CriticalPhase', False)
                   Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(1).SetAttValue ('CriticalPhase', False)
                   break








#First time step

    if Seconds<2:
        L1=[]
        L2=[]
        L3=[]
        L4=[]
        L5=[]
        L6=[]
        L7=[]
        L8=[]
        L9=[]
        L10=[]
        L11=[]
        L12=[]
        L13=[]
        L14=[]
        L15=[]
        L16=[]
        L17=[]
        L18=[]
        L19=[]
        L20=[]
        L21=[]
        L22=[]
        L23=[]
        L24=[]
        L25=[]
        L26=[]
        L27=[]
        L28=[]
        L29=[]
        L30=[]
        L31=[]
        L32=[]
        L33=[]
        L34=[]
        L35=[]
        L36=[]
        L37=[]
        L38=[]
        L39=[]
        L40=[]
        L41=[]
        L42=[]
        L43=[]
        L44=[]
        L45=[]
        L46=[]
        L47=[]
        L48=[]
        L49=[]
        L50=[]
        L51=[]
        L52=[]
        L53=[]
        L54=[]
        L55=[]
        L56=[]
        S1=[]
        S2=[]
        S3=[]
        S4=[]
        S5=[]
        S6=[]
        S7=[]
        S8=[]
        S9=[]
        S10=[]
        S11=[]
        S12=[]
        S13=[]
        S14=[]
        S15=[]
        S16=[]
        S17=[]
        S18=[]
        S19=[]
        S20=[]
        S21=[]
        S22=[]
        S23=[]
        S24=[]
        S25=[]
        S26=[]
        S27=[]
        S28=[]
        S29=[]
        S30=[]
        S31=[]
        S32=[]
        S33=[]
        S34=[]
        S35=[]
        S36=[]
        S37=[]
        S38=[]
        S39=[]
        S40=[]
        S41=[]
        S42=[]
        S43=[]
        S44=[]
        S45=[]
        S46=[]
        S47=[]
        S48=[]
        S49=[]
        S50=[]
        S51=[]
        S52=[]
        S53=[]
        S54=[]
        S55=[]
        S56=[]



        for vehAttributes in vehsAttributes:
            if vehAttributes[vehsAttNames['VehType\No']] in vehTypesEquipped:       
                if vehAttributes[vehsAttNames['Pos']] != None:
                    InQueue = vehAttributes[vehsAttNames['InQueue']]               
                    if InQueue == True:
                        DistanceToSigHead = vehAttributes[vehsAttNames['DistanceToSigHead']]
                        Link = vehAttributes[vehsAttNames['Lane\Link']]
                        Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).SetAttValue ('LinkNo',Link)
                        if Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).AttValue ('LinkNo') == 99:
                            mm = round(pow(e, Tt * (Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(1).AttValue ('ArrivalRate'))/3600))+1
                            L6.append(DistanceToSigHead)
                            D6 = max (L6)
                            Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(1).SetAttValue ('len1',len(L6))

                            if len(L6) > 0:
                                k= max(min(round(D6/5),15),1)
                                
                                sum1 = 0
                                while k <= 15:
                                    f1=pow((1 - proportion_of_CAVs),k)* (0.067)
                                    sum1 = sum1 + f1
                                    k=k+1

                                n=max(min(round(D6/5),15),1)
                                sum2=0
                                while n <= 15:
                                    sum2 = sum2 + (n*(pow((1 - proportion_of_CAVs),n)*(0.067)))/sum1
                                    n = n+1
                                Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(1).SetAttValue ('Queuedup',round(sum2))
                                Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(1).SetAttValue ('WithoutInformation',0)
                                Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(1).SetAttValue ('Joining',mm)
                                

                                    
                            

                        if Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).AttValue ('LinkNo') == 65:
                            mm = round(pow(e, Tt * (Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(3).AttValue ('ArrivalRate'))/3600))+1
                            L7.append(DistanceToSigHead)
                            D7 = max (L7)
                            Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(3).SetAttValue ('len1',len(L7))

                            if len(L7) > 0:
                                k= max(min(round(D7/5),10),1)
                                
                                sum1 = 0
                                while k <= 10:
                                    f1=pow((1 - proportion_of_CAVs),k)* (0.1)
                                    sum1 = sum1 + f1
                                    k=k+1

                                n=max(min(round(D7/5),10),1)
                                sum2=0
                                while n <= 10:
                                    sum2 = sum2 + (n*(pow((1 - proportion_of_CAVs),n)*(0.1)))/sum1
                                    n = n+1
                                Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(3).SetAttValue ('Queuedup',round(sum2))
                                Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(3).SetAttValue ('WithoutInformation',0)
                                Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(3).SetAttValue ('Joining',mm)
                                


                        if Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).AttValue ('LinkNo') == 75:
                            
                            mm = round(pow(e, Tt * (Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(2).AttValue ('ArrivalRate'))/3600))+1
                            L8.append(DistanceToSigHead)
                            D8 = max(L8)
                            Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(2).SetAttValue ('len1',len(L8))

                            if len(L8) > 0:
                                k= max(min(round(D8/5),10),1)
                                
                                sum1 = 0
                                while k <= 10:
                                    f1=pow((1 - proportion_of_CAVs),k)* (0.1)
                                    sum1 = sum1 + f1
                                    k=k+1

                                n=max(min(round(D8/5),10),1)
                                sum2=0
                                while n <= 10:
                                    sum2 = sum2 + (n*(pow((1 - proportion_of_CAVs),n)*(0.1)))/sum1
                                    n = n+1
                                Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(2).SetAttValue ('Queuedup',round(sum2))
                                Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(2).SetAttValue ('WithoutInformation',0)
                                Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(2).SetAttValue ('Joining',mm)



                        if Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).AttValue ('LinkNo') == 102:
                            mm = round(pow(e, Tt * (Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(4).AttValue ('ArrivalRate'))/3600))+1
                            L9.append(DistanceToSigHead)
                            D9 = max (L9)
                            Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(4).SetAttValue ('len1',len(L9))


                            if len(L9) > 0:
                                k= max(min(round(D9/5),15),1)
                                
                                sum1 = 0
                                while k <= 15:
                                    f1=pow((1 - proportion_of_CAVs),k)* (0.067)
                                    sum1 = sum1 + f1
                                    k=k+1

                                n=max(min(round(D9/5),15),1)
                                sum2=0
                                while n <= 15:
                                    sum2 = sum2 + (n*(pow((1 - proportion_of_CAVs),n)*(0.067)))/sum1
                                    n = n+1
                                Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(4).SetAttValue ('Queuedup',round(sum2))
                                Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(4).SetAttValue ('WithoutInformation',0)
                                Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(4).SetAttValue ('Joining',mm)







                        if Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).AttValue ('LinkNo') == 76:
                            L15.append(DistanceToSigHead)
                            D15 = max (L15)
                            Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(1).SetAttValue ('len1',len(L15))
                            mm = round(pow(e, Tt * (Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(1).AttValue ('ArrivalRate'))/3600))+1


                            if len(L15) > 0:
                                k= max(min(round(D15/5),10),1)
                                
                                sum1 = 0
                                while k <= 10:
                                    f1=pow((1 - proportion_of_CAVs),k)* (0.1)
                                    sum1 = sum1 + f1
                                    k=k+1

                                n=max(min(round(D15/5),10),1)
                                sum2=0
                                while n <= 10:
                                    sum2 = sum2 + (n*(pow((1 - proportion_of_CAVs),n)*(0.1)))/sum1
                                    n = n+1
                                Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(1).SetAttValue ('Queuedup',round(sum2))
                                Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(1).SetAttValue ('WithoutInformation',0)
                                Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(1).SetAttValue ('Joining',mm)



                        if Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).AttValue ('LinkNo') == 86:
                            L16.append(DistanceToSigHead)
                            D16 = max (L16)
                            Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(4).SetAttValue ('len1',len(L16))
                            mm = round(pow(e, Tt * (Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(4).AttValue ('ArrivalRate'))/3600))+1
                            if len(L16) > 0:
                                k= max(min(round(D16/5),10),1)
                                
                                sum1 = 0
                                while k <= 10:
                                    f1=pow((1 - proportion_of_CAVs),k)* (0.1)
                                    sum1 = sum1 + f1
                                    k=k+1

                                n=max(min(round(D16/5),10),1)
                                sum2=0
                                while n <= 10:
                                    sum2 = sum2 + (n*(pow((1 - proportion_of_CAVs),n)*(0.1)))/sum1
                                    n = n+1
                                Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(4).SetAttValue ('Queuedup',round(sum2))
                                Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(4).SetAttValue ('WithoutInformation',0)
                                Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(4).SetAttValue ('Joining',mm)

                        if Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).AttValue ('LinkNo') == 77:
                            L17.append(DistanceToSigHead)
                            D17 = max (L17)
                            Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(2).SetAttValue ('len1',len(L17))
                            mm = round(pow(e, Tt * (Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(2).AttValue ('ArrivalRate'))/3600))+1
                            if len(L17) > 0:
                                k= max(min(round(D17/5),10),1)
                                
                                sum1 = 0
                                while k <= 10:
                                    f1=pow((1 - proportion_of_CAVs),k)* (0.1)
                                    sum1 = sum1 + f1
                                    k=k+1

                                n=max(min(round(D17/5),10),1)
                                sum2=0
                                while n <= 10:
                                    sum2 = sum2 + (n*(pow((1 - proportion_of_CAVs),n)*(0.1)))/sum1
                                    n = n+1
                                Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(2).SetAttValue ('Queuedup',round(sum2))
                                Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(2).SetAttValue ('WithoutInformation',0)
                                Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(2).SetAttValue ('Joining',mm)


                        if Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).AttValue ('LinkNo') == 67:
                            L18.append(DistanceToSigHead)
                            D18 = max (L18)
                            Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(3).SetAttValue ('len1',len(L18))
                            mm = round(pow(e, Tt * (Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(3).AttValue ('ArrivalRate'))/3600))+1
                            if len(L18) > 0:
                                k= max(min(round(D18/5),10),1)
                                
                                sum1 = 0
                                while k <= 10:
                                    f1=pow((1 - proportion_of_CAVs),k)* (0.1)
                                    sum1 = sum1 + f1
                                    k=k+1

                                n=max(min(round(D18/5),10),1)
                                sum2=0
                                while n <= 10:
                                    sum2 = sum2 + (n*(pow((1 - proportion_of_CAVs),n)*(0.1)))/sum1
                                    n = n+1
                                Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(3).SetAttValue ('Queuedup',round(sum2))
                                Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(3).SetAttValue ('WithoutInformation',0)
                                Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(3).SetAttValue ('Joining',mm)








                        if Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).AttValue ('LinkNo') == 78:
                            L19.append(DistanceToSigHead)
                            D19 = max (L19)
                            Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(1).SetAttValue ('len1',len(L19))
                            mm = round(pow(e, Tt * (Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(1).AttValue ('ArrivalRate'))/3600))+1
                            if len(L19) > 0:
                                k= max(min(round(D19/5),10),1)
                                
                                sum1 = 0
                                while k <= 10:
                                    f1=pow((1 - proportion_of_CAVs),k)* (0.1)
                                    sum1 = sum1 + f1
                                    k=k+1

                                n=max(min(round(D19/5),10),1)
                                sum2=0
                                while n <= 10:
                                    sum2 = sum2 + (n*(pow((1 - proportion_of_CAVs),n)*(0.1)))/sum1
                                    n = n+1
                                Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(1).SetAttValue ('Queuedup',round(sum2))
                                Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(1).SetAttValue ('WithoutInformation',0)
                                Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(1).SetAttValue ('Joining',mm)


                        if Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).AttValue ('LinkNo') == 96:
                            L20.append(DistanceToSigHead)
                            D20 = max (L20)
                            Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(4).SetAttValue ('len1',len(L20))
                            mm = round(pow(e, Tt * (Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(4).AttValue ('ArrivalRate'))/3600))+1

                            if len(L20) > 0:
                                k= max(min(round(D20/5),15),1)
                                
                                sum1 = 0
                                while k <= 15:
                                    f1=pow((1 - proportion_of_CAVs),k)* (0.067)
                                    sum1 = sum1 + f1
                                    k=k+1

                                n=max(min(round(D20/5),15),1)
                                sum2=0
                                while n <= 15:
                                    sum2 = sum2 + (n*(pow((1 - proportion_of_CAVs),n)*(0.067)))/sum1
                                    n = n+1
                                Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(4).SetAttValue ('Queuedup',round(sum2))
                                Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(4).SetAttValue ('WithoutInformation',0)
                                Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(4).SetAttValue ('Joining',mm)


                        if Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).AttValue ('LinkNo') == 69:
                            L21.append(DistanceToSigHead)
                            D21 = max (L21)
                            Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(3).SetAttValue ('len1',len(L21))
                            mm = round(pow(e, Tt * (Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(3).AttValue ('ArrivalRate'))/3600))+1
                            if len(L21) > 0:
                                k= max(min(round(D21/5),10),1)                               
                                sum1 = 0
                                while k <= 10:
                                    f1=pow((1 - proportion_of_CAVs),k)* (0.1)
                                    sum1 = sum1 + f1
                                    k=k+1

                                n=max(min(round(D21/5),10),1)
                                sum2=0
                                while n <= 10:
                                    sum2 = sum2 + (n*(pow((1 - proportion_of_CAVs),n)*(0.1)))/sum1
                                    n = n+1
                                Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(3).SetAttValue ('Queuedup',round(sum2))
                                Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(3).SetAttValue ('WithoutInformation',0)
                                Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(3).SetAttValue ('Joining',mm)

                        if Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).AttValue ('LinkNo') == 97:
                            L22.append(DistanceToSigHead)
                            D22 = max (L22)
                            Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(2).SetAttValue ('len1',len(L22))
                            mm = round(pow(e, Tt * (Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(2).AttValue ('ArrivalRate'))/3600))+1

                            if len(L22) > 0:
                                k= max(min(round(D22/5),15),1)
                                
                                sum1 = 0
                                while k <= 15:
                                    f1=pow((1 - proportion_of_CAVs),k)* (0.067)
                                    sum1 = sum1 + f1
                                    k=k+1

                                n=max(min(round(D22/5),15),1)
                                sum2=0
                                while n <= 15:
                                    sum2 = sum2 + (n*(pow((1 - proportion_of_CAVs),n)*(0.067)))/sum1
                                    n = n+1
                                Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(2).SetAttValue ('Queuedup',round(sum2))
                                Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(2).SetAttValue ('WithoutInformation',0)
                                Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(2).SetAttValue ('Joining',mm)








                        if Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).AttValue ('LinkNo') == 70:
                            L28.append(DistanceToSigHead)
                            D28 = max (L28)
                            Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(2).SetAttValue ('len1',len(L28))
                            mm = round(pow(e, Tt * (Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(2).AttValue ('ArrivalRate'))/3600))+1
                            if len(L28) > 0:
                                k= max(min(round(D28/5),10),1)                               
                                sum1 = 0
                                while k <= 10:
                                    f1=pow((1 - proportion_of_CAVs),k)* (0.1)
                                    sum1 = sum1 + f1
                                    k=k+1

                                n=max(min(round(D28/5),10),1)
                                sum2=0
                                while n <= 10:
                                    sum2 = sum2 + (n*(pow((1 - proportion_of_CAVs),n)*(0.1)))/sum1
                                    n = n+1
                                Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(2).SetAttValue ('Queuedup',round(sum2))
                                Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(2).SetAttValue ('WithoutInformation',0)
                                Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(2).SetAttValue ('Joining',mm)


                        if Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).AttValue ('LinkNo') == 87:
                            L29.append(DistanceToSigHead)
                            D29 = max (L29)
                            Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(3).SetAttValue ('len1',len(L29))
                            mm = round(pow(e, Tt * (Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(3).AttValue ('ArrivalRate'))/3600))+1
                            if len(L29) > 0:
                                k= max(min(round(D29/5),10),1)                               
                                sum1 = 0
                                while k <= 10:
                                    f1=pow((1 - proportion_of_CAVs),k)* (0.1)
                                    sum1 = sum1 + f1
                                    k=k+1

                                n=max(min(round(D29/5),10),1)
                                sum2=0
                                while n <= 10:
                                    sum2 = sum2 + (n*(pow((1 - proportion_of_CAVs),n)*(0.1)))/sum1
                                    n = n+1
                                Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(3).SetAttValue ('Queuedup',round(sum2))
                                Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(3).SetAttValue ('WithoutInformation',0)
                                Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(3).SetAttValue ('Joining',mm)


                        if Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).AttValue ('LinkNo') == 63:
                            L30.append(DistanceToSigHead)
                            D30 = max (L30)
                            Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(4).SetAttValue ('len1',len(L30))
                            mm = round(pow(e, Tt * (Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(4).AttValue ('ArrivalRate'))/3600))+1
                            if len(L30) > 0:
                                k= max(min(round(D30/5),10),1)                               
                                sum1 = 0
                                while k <= 10:
                                    f1=pow((1 - proportion_of_CAVs),k)* (0.1)
                                    sum1 = sum1 + f1
                                    k=k+1

                                n=max(min(round(D30/5),10),1)
                                sum2=0
                                while n <= 10:
                                    sum2 = sum2 + (n*(pow((1 - proportion_of_CAVs),n)*(0.1)))/sum1
                                    n = n+1
                                Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(4).SetAttValue ('Queuedup',round(sum2))
                                Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(4).SetAttValue ('WithoutInformation',0)
                                Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(4).SetAttValue ('Joining',mm)



                        if Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).AttValue ('LinkNo') == 82:
                            L31.append(DistanceToSigHead)
                            D31 = max (L31)
                            Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(1).SetAttValue ('len1',len(L31))
                            mm = round(pow(e, Tt * (Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(1).AttValue ('ArrivalRate'))/3600))+1
                            if len(L31) > 0:
                                k= max(min(round(D31/5),10),1)                               
                                sum1 = 0
                                while k <= 10:
                                    f1=pow((1 - proportion_of_CAVs),k)* (0.1)
                                    sum1 = sum1 + f1
                                    k=k+1

                                n=max(min(round(D31/5),10),1)
                                sum2=0
                                while n <= 10:
                                    sum2 = sum2 + (n*(pow((1 - proportion_of_CAVs),n)*(0.1)))/sum1
                                    n = n+1
                                Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(1).SetAttValue ('Queuedup',round(sum2))
                                Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(1).SetAttValue ('WithoutInformation',0)
                                Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(1).SetAttValue ('Joining',mm)





                        if Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).AttValue ('LinkNo') == 81:
                            L32.append(DistanceToSigHead)
                            D32 = max (L32)
                            Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(3).SetAttValue ('len1',len(L32))
                            mm = round(pow(e, Tt * (Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(3).AttValue ('ArrivalRate'))/3600))+1

                            if len(L32) > 0:
                                k= max(min(round(D32/5),10),1)                               
                                sum1 = 0
                                while k <= 10:
                                    f1=pow((1 - proportion_of_CAVs),k)* (0.1)
                                    sum1 = sum1 + f1
                                    k=k+1

                                n=max(min(round(D32/5),10),1)
                                sum2=0
                                while n <= 10:
                                    sum2 = sum2 + (n*(pow((1 - proportion_of_CAVs),n)*(0.1)))/sum1
                                    n = n+1
                                Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(3).SetAttValue ('Queuedup',round(sum2))
                                Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(3).SetAttValue ('WithoutInformation',0)
                                Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(3).SetAttValue ('Joining',mm)

                        if Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).AttValue ('LinkNo') == 61:
                            L33.append(DistanceToSigHead)
                            D33 = max (L33)
                            Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(4).SetAttValue ('len1',len(L33))
                            mm = round(pow(e, Tt * (Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(4).AttValue ('ArrivalRate'))/3600))+1

                            if len(L33) > 0:
                                k= max(min(round(D33/5),10),1)                               
                                sum1 = 0
                                while k <= 10:
                                    f1=pow((1 - proportion_of_CAVs),k)* (0.1)
                                    sum1 = sum1 + f1
                                    k=k+1

                                n=max(min(round(D33/5),10),1)
                                sum2=0
                                while n <= 10:
                                    sum2 = sum2 + (n*(pow((1 - proportion_of_CAVs),n)*(0.1)))/sum1
                                    n = n+1
                                Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(4).SetAttValue ('Queuedup',round(sum2))
                                Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(4).SetAttValue ('WithoutInformation',0)
                                Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(4).SetAttValue ('Joining',mm)

                        if Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).AttValue ('LinkNo') == 80:
                            L34.append(DistanceToSigHead)
                            D34 = max (L34)
                            Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(1).SetAttValue ('len1',len(L34))
                            mm = round(pow(e, Tt * (Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(1).AttValue ('ArrivalRate'))/3600))+1

                            if len(L34) > 0:
                                k= max(min(round(D34/5),10),1)                               
                                sum1 = 0
                                while k <= 10:
                                    f1=pow((1 - proportion_of_CAVs),k)* (0.1)
                                    sum1 = sum1 + f1
                                    k=k+1

                                n=max(min(round(D34/5),10),1)
                                sum2=0
                                while n <= 10:
                                    sum2 = sum2 + (n*(pow((1 - proportion_of_CAVs),n)*(0.1)))/sum1
                                    n = n+1
                                Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(1).SetAttValue ('Queuedup',round(sum2))
                                Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(1).SetAttValue ('WithoutInformation',0)
                                Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(1).SetAttValue ('Joining',mm)

                        if Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).AttValue ('LinkNo') == 68:
                            L35.append(DistanceToSigHead)
                            D35 = max (L35)
                            Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(2).SetAttValue ('len1',len(L35))
                            mm = round(pow(e, Tt * (Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(2).AttValue ('ArrivalRate'))/3600))+1

                            if len(L35) > 0:
                                k= max(min(round(D35/5),10),1)                               
                                sum1 = 0
                                while k <= 10:
                                    f1=pow((1 - proportion_of_CAVs),k)* (0.1)
                                    sum1 = sum1 + f1
                                    k=k+1

                                n=max(min(round(D35/5),10),1)
                                sum2=0
                                while n <= 10:
                                    sum2 = sum2 + (n*(pow((1 - proportion_of_CAVs),n)*(0.1)))/sum1
                                    n = n+1
                                Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(2).SetAttValue ('Queuedup',round(sum2))
                                Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(2).SetAttValue ('WithoutInformation',0)
                                Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(2).SetAttValue ('Joining',mm)







                        if Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).AttValue ('LinkNo') == 79:
                            L36.append(DistanceToSigHead)
                            D36 = max (L36)
                            Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(3).SetAttValue ('len1',len(L36))
                            mm = round(pow(e, Tt * (Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(3).AttValue ('ArrivalRate'))/3600))+1

                            if len(L36) > 0:
                                k= max(min(round(D36/5),10),1)                               
                                sum1 = 0
                                while k <= 10:
                                    f1=pow((1 - proportion_of_CAVs),k)* (0.1)
                                    sum1 = sum1 + f1
                                    k=k+1

                                n=max(min(round(D36/5),10),1)
                                sum2=0
                                while n <= 10:
                                    sum2 = sum2 + (n*(pow((1 - proportion_of_CAVs),n)*(0.1)))/sum1
                                    n = n+1
                                Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(3).SetAttValue ('Queuedup',round(sum2))
                                Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(3).SetAttValue ('WithoutInformation',0)
                                Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(3).SetAttValue ('Joining',mm)
                            

                        if Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).AttValue ('LinkNo') == 59:
                            L37.append(DistanceToSigHead)
                            D37 = max (L37)
                            Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(4).SetAttValue ('len1',len(L37))
                            mm = round(pow(e, Tt * (Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(4).AttValue ('ArrivalRate'))/3600))+1

                            if len(L37) > 0:
                                k= max(min(round(D37/5),10),1)                               
                                sum1 = 0
                                while k <= 10:
                                    f1=pow((1 - proportion_of_CAVs),k)* (0.1)
                                    sum1 = sum1 + f1
                                    k=k+1

                                n=max(min(round(D37/5),10),1)
                                sum2=0
                                while n <= 10:
                                    sum2 = sum2 + (n*(pow((1 - proportion_of_CAVs),n)*(0.1)))/sum1
                                    n = n+1
                                Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(4).SetAttValue ('Queuedup',round(sum2))
                                Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(4).SetAttValue ('WithoutInformation',0)
                                Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(4).SetAttValue ('Joining',mm)

                        if Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).AttValue ('LinkNo') == 90:
                            L38.append(DistanceToSigHead)
                            D38 = max (L38)
                            Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(1).SetAttValue ('len1',len(L38))
                            mm = round(pow(e, Tt * (Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(1).AttValue ('ArrivalRate'))/3600))+1
                            

                            if len(L38) > 0:
                                k= max(min(round(D38/5),10),1)                               
                                sum1 = 0
                                while k <= 10:
                                    f1=pow((1 - proportion_of_CAVs),k)* (0.1)
                                    sum1 = sum1 + f1
                                    k=k+1

                                n=max(min(round(D38/5),10),1)
                                sum2=0
                                while n <= 10:
                                    sum2 = sum2 + (n*(pow((1 - proportion_of_CAVs),n)*(0.1)))/sum1
                                    n = n+1
                                Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(1).SetAttValue ('Queuedup',round(sum2))
                                Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(1).SetAttValue ('WithoutInformation',0)
                                Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(1).SetAttValue ('Joining',mm)



                        if Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).AttValue ('LinkNo') == 66:
                            L39.append(DistanceToSigHead)
                            D39 = max (L39)
                            Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(2).SetAttValue ('len1',len(L39))
                            mm = round(pow(e, Tt * (Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(2).AttValue ('ArrivalRate'))/3600))+1

                            if len(L39) > 0:
                                k= max(min(round(D39/5),10),1)                               
                                sum1 = 0
                                while k <= 10:
                                    f1=pow((1 - proportion_of_CAVs),k)* (0.1)
                                    sum1 = sum1 + f1
                                    k=k+1

                                n=max(min(round(D39/5),10),1)
                                sum2=0
                                while n <= 10:
                                    sum2 = sum2 + (n*(pow((1 - proportion_of_CAVs),n)*(0.1)))/sum1
                                    n = n+1
                                Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(2).SetAttValue ('Queuedup',round(sum2))
                                Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(2).SetAttValue ('WithoutInformation',0)
                                Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(2).SetAttValue ('Joining',mm)









                        if Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).AttValue ('LinkNo') == 60:
                            L40.append(DistanceToSigHead)
                            D40 = max (L40)
                            Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(2).SetAttValue ('len1',len(L40))
                            mm = round(pow(e, Tt * (Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(2).AttValue ('ArrivalRate'))/3600))+1

                            if len(L40) > 0:
                                k= max(min(round(D40/5),10),1)                               
                                sum1 = 0
                                while k <= 10:
                                    f1=pow((1 - proportion_of_CAVs),k)* (0.1)
                                    sum1 = sum1 + f1
                                    k=k+1

                                n=max(min(round(D40/5),10),1)
                                sum2=0
                                while n <= 10:
                                    sum2 = sum2 + (n*(pow((1 - proportion_of_CAVs),n)*(0.1)))/sum1
                                    n = n+1
                                Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(2).SetAttValue ('Queuedup',round(sum2))
                                Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(2).SetAttValue ('WithoutInformation',0)
                                Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(2).SetAttValue ('Joining',mm)

                        if Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).AttValue ('LinkNo') == 92:
                            L41.append(DistanceToSigHead)
                            D41 = max (L41)
                            Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(1).SetAttValue ('len1',len(L41))
                            mm = round(pow(e, Tt * (Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(1).AttValue ('ArrivalRate'))/3600))+1

                            if len(L41) > 0:
                                k= max(min(round(D41/5),15),1)
                                
                                sum1 = 0
                                while k <= 15:
                                    f1=pow((1 - proportion_of_CAVs),k)* (0.067)
                                    sum1 = sum1 + f1
                                    k=k+1

                                n=max(min(round(D41/5),15),1)
                                sum2=0
                                while n <= 15:
                                    sum2 = sum2 + (n*(pow((1 - proportion_of_CAVs),n)*(0.067)))/sum1
                                    n = n+1
                                Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(1).SetAttValue ('Queuedup',round(sum2))
                                Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(1).SetAttValue ('WithoutInformation',0)
                                Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(1).SetAttValue ('Joining',mm)

                        if Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).AttValue ('LinkNo') == 71:
                            L42.append(DistanceToSigHead)
                            D42 = max (L42)
                            Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(3).SetAttValue ('len1',len(L42))
                            mm = round(pow(e, Tt * (Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(3).AttValue ('ArrivalRate'))/3600))+1

                            if len(L42) > 0:
                                k= max(min(round(D42/5),10),1)                               
                                sum1 = 0
                                while k <= 10:
                                    f1=pow((1 - proportion_of_CAVs),k)* (0.1)
                                    sum1 = sum1 + f1
                                    k=k+1

                                n=max(min(round(D42/5),10),1)
                                sum2=0
                                while n <= 10:
                                    sum2 = sum2 + (n*(pow((1 - proportion_of_CAVs),n)*(0.1)))/sum1
                                    n = n+1
                                Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(3).SetAttValue ('Queuedup',round(sum2))
                                Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(3).SetAttValue ('WithoutInformation',0)
                                Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(3).SetAttValue ('Joining',mm)

                        if Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).AttValue ('LinkNo') == 93:
                            L43.append(DistanceToSigHead)
                            D43 = max (L43)
                            Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(4).SetAttValue ('len1',len(L43))
                            mm = round(pow(e, Tt * (Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(4).AttValue ('ArrivalRate'))/3600))+1

                            if len(L43) > 0:
                                k= max(min(round(D43/5),15),1)
                                
                                sum1 = 0
                                while k <= 15:
                                    f1=pow((1 - proportion_of_CAVs),k)* (0.067)
                                    sum1 = sum1 + f1
                                    k=k+1

                                n=max(min(round(D43/5),15),1)
                                sum2=0
                                while n <= 15:
                                    sum2 = sum2 + (n*(pow((1 - proportion_of_CAVs),n)*(0.067)))/sum1
                                    n = n+1
                                Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(4).SetAttValue ('Queuedup',round(sum2))
                                Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(4).SetAttValue ('WithoutInformation',0)
                                Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(4).SetAttValue ('Joining',mm)







                        if Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).AttValue ('LinkNo') == 72:
                            L44.append(DistanceToSigHead)
                            D44 = max (L44)
                            Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(1).SetAttValue ('len1',len(L44))
                            mm = round(pow(e, Tt * (Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(1).AttValue ('ArrivalRate'))/3600))+1

                            if len(L44) > 0:
                                k= max(min(round(D44/5),10),1)                               
                                sum1 = 0
                                while k <= 10:
                                    f1=pow((1 - proportion_of_CAVs),k)* (0.1)
                                    sum1 = sum1 + f1
                                    k=k+1

                                n=max(min(round(D44/5),10),1)
                                sum2=0
                                while n <= 10:
                                    sum2 = sum2 + (n*(pow((1 - proportion_of_CAVs),n)*(0.1)))/sum1
                                    n = n+1
                                Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(1).SetAttValue ('Queuedup',round(sum2))
                                Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(1).SetAttValue ('WithoutInformation',0)
                                Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(1).SetAttValue ('Joining',mm)

                        if Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).AttValue ('LinkNo') == 62:
                            L45.append(DistanceToSigHead)
                            D45 = max (L45)
                            Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(2).SetAttValue ('len1',len(L45))
                            mm = round(pow(e, Tt * (Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(2).AttValue ('ArrivalRate'))/3600))+1

                            if len(L45) > 0:
                                k= max(min(round(D45/5),10),1)                               
                                sum1 = 0
                                while k <= 10:
                                    f1=pow((1 - proportion_of_CAVs),k)* (0.1)
                                    sum1 = sum1 + f1
                                    k=k+1

                                n=max(min(round(D45/5),10),1)
                                sum2=0
                                while n <= 10:
                                    sum2 = sum2 + (n*(pow((1 - proportion_of_CAVs),n)*(0.1)))/sum1
                                    n = n+1
                                Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(2).SetAttValue ('Queuedup',round(sum2))
                                Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(2).SetAttValue ('WithoutInformation',0)
                                Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(2).SetAttValue ('Joining',mm)

                        if Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).AttValue ('LinkNo') == 73:
                            L46.append(DistanceToSigHead)
                            D46 = max (L46)
                            Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(3).SetAttValue ('len1',len(L46))
                            mm = round(pow(e, Tt * (Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(3).AttValue ('ArrivalRate'))/3600))+1

                            if len(L46) > 0:
                                k= max(min(round(D46/5),10),1)                               
                                sum1 = 0
                                while k <= 10:
                                    f1=pow((1 - proportion_of_CAVs),k)* (0.1)
                                    sum1 = sum1 + f1
                                    k=k+1

                                n=max(min(round(D46/5),10),1)
                                sum2=0
                                while n <= 10:
                                    sum2 = sum2 + (n*(pow((1 - proportion_of_CAVs),n)*(0.1)))/sum1
                                    n = n+1
                                Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(3).SetAttValue ('Queuedup',round(sum2))
                                Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(3).SetAttValue ('WithoutInformation',0)
                                Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(3).SetAttValue ('Joining',mm)

                        if Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).AttValue ('LinkNo') == 83:
                            L47.append(DistanceToSigHead)
                            D47 = max (L47)
                            Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(4).SetAttValue ('len1',len(L47))
                            mm = round(pow(e, Tt * (Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(4).AttValue ('ArrivalRate'))/3600))+1

                            if len(L47) > 0:
                                k= max(min(round(D47/5),10),1)                               
                                sum1 = 0
                                while k <= 10:
                                    f1=pow((1 - proportion_of_CAVs),k)* (0.1)
                                    sum1 = sum1 + f1
                                    k=k+1

                                n=max(min(round(D47/5),10),1)
                                sum2=0
                                while n <= 10:
                                    sum2 = sum2 + (n*(pow((1 - proportion_of_CAVs),n)*(0.1)))/sum1
                                    n = n+1
                                Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(4).SetAttValue ('Queuedup',round(sum2))
                                Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(4).SetAttValue ('WithoutInformation',0)
                                Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(4).SetAttValue ('Joining',mm)






                        if Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).AttValue ('LinkNo') == 74:
                            L48.append(DistanceToSigHead)
                            D48 = max (L48)
                            Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(1).SetAttValue ('len1',len(L48))
                            mm = round(pow(e, Tt * (Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(1).AttValue ('ArrivalRate'))/3600))+1

                            if len(L48) > 0:
                                k= max(min(round(D48/5),10),1)                               
                                sum1 = 0
                                while k <= 10:
                                    f1=pow((1 - proportion_of_CAVs),k)* (0.1)
                                    sum1 = sum1 + f1
                                    k=k+1

                                n=max(min(round(D48/5),10),1)
                                sum2=0
                                while n <= 10:
                                    sum2 = sum2 + (n*(pow((1 - proportion_of_CAVs),n)*(0.1)))/sum1
                                    n = n+1
                                Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(1).SetAttValue ('Queuedup',round(sum2))
                                Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(1).SetAttValue ('WithoutInformation',0)
                                Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(1).SetAttValue ('Joining',mm)

                        if Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).AttValue ('LinkNo') == 64:
                            L49.append(DistanceToSigHead)
                            D49 = max (L49)
                            Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(2).SetAttValue ('len1',len(L49))
                            mm = round(pow(e, Tt * (Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(2).AttValue ('ArrivalRate'))/3600))+1
                            if len(L49) > 0:
                                k= max(min(round(D49/5),10),1)                               
                                sum1 = 0
                                while k <= 10:
                                    f1=pow((1 - proportion_of_CAVs),k)* (0.1)
                                    sum1 = sum1 + f1
                                    k=k+1

                                n=max(min(round(D49/5),10),1)
                                sum2=0
                                while n <= 10:
                                    sum2 = sum2 + (n*(pow((1 - proportion_of_CAVs),n)*(0.1)))/sum1
                                    n = n+1
                                Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(2).SetAttValue ('Queuedup',round(sum2))
                                Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(2).SetAttValue ('WithoutInformation',0)
                                Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(2).SetAttValue ('Joining',mm)


                        if Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).AttValue ('LinkNo') == 104:
                            L50.append(DistanceToSigHead)
                            D50 = max (L50)
                            Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(3).SetAttValue ('len1',len(L50))
                            mm = round(pow(e, Tt * (Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(3).AttValue ('ArrivalRate'))/3600))+1

                            if len(L50) > 0:
                                k= max(min(round(D50/5),15),1)
                                
                                sum1 = 0
                                while k <= 15:
                                    f1=pow((1 - proportion_of_CAVs),k)* (0.067)
                                    sum1 = sum1 + f1
                                    k=k+1

                                n=max(min(round(D50/5),15),1)
                                sum2=0
                                while n <= 15:
                                    sum2 = sum2 + (n*(pow((1 - proportion_of_CAVs),n)*(0.067)))/sum1
                                    n = n+1
                                Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(3).SetAttValue ('Queuedup',round(sum2))
                                Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(3).SetAttValue ('WithoutInformation',0)
                                Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(3).SetAttValue ('Joining',mm)

                        if Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).AttValue ('LinkNo') == 105:
                            L51.append(DistanceToSigHead)
                            D51 = max (L51)
                            Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(4).SetAttValue ('len1',len(L51))
                            mm = round(pow(e, Tt * (Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(4).AttValue ('ArrivalRate'))/3600))+1


                            if len(L51) > 0:
                                k= max(min(round(D51/5),15),1)
                                
                                sum1 = 0
                                while k <= 15:
                                    f1=pow((1 - proportion_of_CAVs),k)* (0.067)
                                    sum1 = sum1 + f1
                                    k=k+1

                                n=max(min(round(D51/5),15),1)
                                sum2=0
                                while n <= 15:
                                    sum2 = sum2 + (n*(pow((1 - proportion_of_CAVs),n)*(0.067)))/sum1
                                    n = n+1
                                Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(4).SetAttValue ('Queuedup',round(sum2))
                                Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(4).SetAttValue ('WithoutInformation',0)
                                Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(4).SetAttValue ('Joining',mm)


                    else:
                        continue




                    if vehAttributes[vehsAttNames['VehType\No']] in vehTypesSpecial:
                        Link = vehAttributes[vehsAttNames['Lane\Link']]
                        Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).SetAttValue ('LinkNo1',Link)
                        if Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).AttValue ('LinkNo1') == 99:
                            S6.append(1)
                            if len(S6)>0:
                                Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(1).SetAttValue ('SpecialExtension',greenExtension)

                        if Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).AttValue ('LinkNo1') == 65:
                            S7.append(1)
                            if len(S7) >0:
                                Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(3).SetAttValue ('SpecialExtension',greenExtension)
                     

                        if Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).AttValue ('LinkNo1') == 75:
                            S8.append(1)
                            if len(S8) >0:
                                Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(2).SetAttValue ('SpecialExtension',greenExtension)
                            

                        if Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).AttValue ('LinkNo1') == 102:
                            S9.append(1)
                            if len(S9) >0:
                                Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(4).SetAttValue ('SpecialExtension',greenExtension)


                        if Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).AttValue ('LinkNo1') == 76:
                            S15.append(1)
                            if len(S15) >0:
                                Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(1).SetAttValue ('SpecialExtension',greenExtension)



                        if Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).AttValue ('LinkNo1') == 86:
                            S16.append(1)
                            if len(S16) >0:
                                Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(4).SetAttValue ('SpecialExtension',greenExtension)


                        if Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).AttValue ('LinkNo1') == 77:
                            S17.append(1)
                            if len(S17) >0:
                                Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(2).SetAttValue ('SpecialExtension',greenExtension)

                        if Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).AttValue ('LinkNo1') == 67:
                            S18.append(1)
                            if len(S18) >0:
                                Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(3).SetAttValue ('SpecialExtension',greenExtension)

                        if Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).AttValue ('LinkNo1') == 78:
                            S19.append(1)
                            if len(S19) >0:
                                Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(1).SetAttValue ('SpecialExtension',greenExtension)


                        if Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).AttValue ('LinkNo1') == 96:
                            S20.append(1)
                            if len(S20) >0:
                                Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(4).SetAttValue ('SpecialExtension',greenExtension)


                        if Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).AttValue ('LinkNo1') == 69:
                            S21.append(1)
                            if len(S21) >0:
                                Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(3).SetAttValue ('SpecialExtension',greenExtension)


                        if Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).AttValue ('LinkNo1') == 97:
                            S22.append(1)
                            if len(S22) >0:
                                Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(2).SetAttValue ('SpecialExtension',greenExtension)


                        if Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).AttValue ('LinkNo1') == 70:
                            S28.append(1)
                            if len(S28) >0:
                                Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(2).SetAttValue ('SpecialExtension',greenExtension)

                        if Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).AttValue ('LinkNo1') == 87:
                            S29.append(1)
                            if len(S29) >0:
                                Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(3).SetAttValue ('SpecialExtension',greenExtension)

                        if Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).AttValue ('LinkNo1') == 63:
                            S30.append(1)
                            if len(S30) >0:
                                Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(4).SetAttValue ('SpecialExtension',greenExtension)

                        if Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).AttValue ('LinkNo1') == 82:
                            S31.append(1)
                            if len(S31) >0:
                                Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(1).SetAttValue ('SpecialExtension',greenExtension)

                        if Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).AttValue ('LinkNo1') == 81:
                            S32.append(1)
                            if len(S32) >0:
                                Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(3).SetAttValue ('SpecialExtension',greenExtension)

                        if Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).AttValue ('LinkNo1') == 61:
                            S33.append(1)
                            if len(S33) >0:
                                Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(4).SetAttValue ('SpecialExtension',greenExtension)

                        if Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).AttValue ('LinkNo1') == 80:
                            S34.append(1)
                            if len(S34) >0:
                                Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(1).SetAttValue ('SpecialExtension',greenExtension)


                        if Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).AttValue ('LinkNo1') == 68:
                            S35.append(1)
                            if len(S35) >0:
                                Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(2).SetAttValue ('SpecialExtension',greenExtension)

                        if Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).AttValue ('LinkNo1') == 79:
                            S36.append(1)
                            if len(S36) >0:
                                Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(3).SetAttValue ('SpecialExtension',greenExtension)


                        if Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).AttValue ('LinkNo1') == 59:
                            S37.append(1)
                            if len(S37) >0:
                                Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(4).SetAttValue ('SpecialExtension',greenExtension)



                        if Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).AttValue ('LinkNo1') == 90:
                            S38.append(1)
                            if len(S38) >0:
                                Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(1).SetAttValue ('SpecialExtension',greenExtension)



                        if Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).AttValue ('LinkNo1') == 66:
                            S39.append(1)
                            if len(S39) >0:
                                Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(2).SetAttValue ('SpecialExtension',greenExtension)

                        if Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).AttValue ('LinkNo1') == 60:
                            S40.append(1)
                            if len(S40) >0:
                                Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(2).SetAttValue ('SpecialExtension',greenExtension)
 
                        if Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).AttValue ('LinkNo1') == 92:
                            S41.append(1)
                            if len(S41) >0:
                                Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(1).SetAttValue ('SpecialExtension',greenExtension)

                        if Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).AttValue ('LinkNo1') == 71:
                            S42.append(1)
                            if len(S42) >0:
                                Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(3).SetAttValue ('SpecialExtension',greenExtension)


                        if Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).AttValue ('LinkNo1') == 93:
                            S43.append(1)
                            if len(S43) >0:
                                Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(4).SetAttValue ('SpecialExtension',greenExtension)

                        if Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).AttValue ('LinkNo1') == 72:
                            S44.append(1)
                            if len(S44) >0:
                                Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(1).SetAttValue ('SpecialExtension',greenExtension)

                        if Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).AttValue ('LinkNo1') == 62:
                            S45.append(1)
                            if len(S45) >0:
                                Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(2).SetAttValue ('SpecialExtension',greenExtension)


                        if Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).AttValue ('LinkNo1') == 73:
                            S46.append(1)
                            if len(S46) >0:
                                Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(3).SetAttValue ('SpecialExtension',greenExtension)

                        if Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).AttValue ('LinkNo1') == 83:
                            S47.append(1)
                            if len(S47) >0:
                                Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(4).SetAttValue ('SpecialExtension',greenExtension)


                        if Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).AttValue ('LinkNo1') == 74:
                            S48.append(1)
                            if len(S48) >0:
                                Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(1).SetAttValue ('SpecialExtension',greenExtension)

                        if Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).AttValue ('LinkNo1') == 64:
                            S49.append(1)
                            if len(S49) >0:
                                Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(2).SetAttValue ('SpecialExtension',greenExtension)

                        if Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).AttValue ('LinkNo1') == 104:
                            S50.append(1)
                            if len(S50) >0:
                                Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(3).SetAttValue ('SpecialExtension',greenExtension)


                        if Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).AttValue ('LinkNo1') == 105:
                            S51.append(1)
                            if len(S51) >0:
                                Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(4).SetAttValue ('SpecialExtension',greenExtension)

        if len(L6)==0:
            Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(1).SetAttValue ('Queuedup',0)
            Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(1).SetAttValue ('WithoutInformation',3)
            Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(1).SetAttValue ('len1',0)
            Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(1).SetAttValue ('Joining',0)



        if len(L7)==0:
            Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(3).SetAttValue ('Queuedup',0)
            Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(3).SetAttValue ('WithoutInformation',3)
            Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(3).SetAttValue ('len1',0)
            Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(3).SetAttValue ('Joining',0)



        if len(L8)==0:
            Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(2).SetAttValue ('Queuedup',0)
            Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(2).SetAttValue ('WithoutInformation',3)
            Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(2).SetAttValue ('len1',0)
            Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(2).SetAttValue ('Joining',0)

        if len(L9)==0:
            Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(4).SetAttValue ('Queuedup',0)
            Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(4).SetAttValue ('WithoutInformation',3)
            Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(4).SetAttValue ('len1',0)
            Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(4).SetAttValue ('Joining',0)


        if len(L15)==0:
            Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(1).SetAttValue ('Queuedup',0)
            Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(1).SetAttValue ('WithoutInformation',3)
            Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(1).SetAttValue ('len1',0)
            Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(1).SetAttValue ('Joining',0)


        if len(L16)==0:
            Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(4).SetAttValue ('Queuedup',0)
            Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(4).SetAttValue ('WithoutInformation',3)
            Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(4).SetAttValue ('len1',0)
            Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(4).SetAttValue ('Joining',0)


        if len(L17)==0:
            Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(2).SetAttValue ('Queuedup',0)
            Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(2).SetAttValue ('WithoutInformation',3)
            Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(2).SetAttValue ('len1',0)
            Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(2).SetAttValue ('Joining',0)


        if len(L18)==0:
            Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(3).SetAttValue ('Queuedup',0)
            Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(3).SetAttValue ('WithoutInformation',3)
            Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(3).SetAttValue ('len1',0)
            Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(3).SetAttValue ('Joining',0)





        if len(L19)==0:
            Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(1).SetAttValue ('Queuedup',0)
            Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(1).SetAttValue ('WithoutInformation',3)
            Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(1).SetAttValue ('len1',0)
            Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(1).SetAttValue ('Joining',0)



        if len(L20)==0:
            Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(4).SetAttValue ('Queuedup',0)
            Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(4).SetAttValue ('WithoutInformation',3)
            Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(4).SetAttValue ('len1',0)
            Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(4).SetAttValue ('Joining',0)

        if len(L21)==0:
            Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(3).SetAttValue ('Queuedup',0)
            Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(3).SetAttValue ('WithoutInformation',3)
            Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(3).SetAttValue ('len1',0)
            Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(3).SetAttValue ('Joining',0)


        if len(L22)==0:
            Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(2).SetAttValue ('Queuedup',0)
            Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(2).SetAttValue ('WithoutInformation',3)
            Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(2).SetAttValue ('len1',0)
            Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(2).SetAttValue ('Joining',0)


        if len(L28)==0:
            Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(2).SetAttValue ('Queuedup',0)
            Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(2).SetAttValue ('WithoutInformation',3)
            Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(2).SetAttValue ('len1',0)
            Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(2).SetAttValue ('Joining',0)




        if len(L29)==0:
            Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(3).SetAttValue ('Queuedup',0)
            Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(3).SetAttValue ('WithoutInformation',3)
            Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(3).SetAttValue ('len1',0)
            Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(3).SetAttValue ('Joining',0)



        if len(L30)==0:
            Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(4).SetAttValue ('Queuedup',0)
            Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(4).SetAttValue ('WithoutInformation',3)
            Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(4).SetAttValue ('len1',0)
            Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(4).SetAttValue ('Joining',0)



        if len(L31)==0:
            Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(1).SetAttValue ('Queuedup',0)
            Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(1).SetAttValue ('WithoutInformation',3)
            Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(1).SetAttValue ('len1',0)
            Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(1).SetAttValue ('Joining',0)




        if len(L32)==0:
            Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(3).SetAttValue ('Queuedup',0)
            Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(3).SetAttValue ('WithoutInformation',3)
            Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(3).SetAttValue ('len1',0)
            Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(3).SetAttValue ('Joining',0)


        if len(L33)==0:
            Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(4).SetAttValue ('Queuedup',0)
            Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(4).SetAttValue ('WithoutInformation',3)
            Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(4).SetAttValue ('len1',0)
            Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(4).SetAttValue ('Joining',0)



        if len(L34)==0:
            Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(1).SetAttValue ('Queuedup',0)
            Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(1).SetAttValue ('WithoutInformation',3)
            Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(1).SetAttValue ('len1',0)
            Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(1).SetAttValue ('Joining',0)


        if len(L35)==0:
            Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(2).SetAttValue ('Queuedup',0)
            Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(2).SetAttValue ('WithoutInformation',3)
            Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(2).SetAttValue ('len1',0)
            Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(2).SetAttValue ('Joining',0)



        if len(L36)==0:
            Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(3).SetAttValue ('Queuedup',0)
            Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(3).SetAttValue ('WithoutInformation',3)
            Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(3).SetAttValue ('len1',0)
            Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(3).SetAttValue ('Joining',0)


        if len(L37)==0:
            Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(4).SetAttValue ('Queuedup',0)
            Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(4).SetAttValue ('WithoutInformation',3)
            Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(4).SetAttValue ('len1',0)
            Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(4).SetAttValue ('Joining',0)



        if len(L38)==0:
            Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(1).SetAttValue ('Queuedup',0)
            Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(1).SetAttValue ('WithoutInformation',3)
            Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(1).SetAttValue ('len1',0)
            Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(1).SetAttValue ('Joining',0)



        if len(L39)==0:
            Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(2).SetAttValue ('Queuedup',0)
            Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(2).SetAttValue ('WithoutInformation',3)
            Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(2).SetAttValue ('len1',0)
            Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(2).SetAttValue ('Joining',0)


        if len(L40)==0:
            Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(2).SetAttValue ('Queuedup',0)
            Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(2).SetAttValue ('WithoutInformation',3)
            Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(2).SetAttValue ('len1',0)
            Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(2).SetAttValue ('Joining',0)



        if len(L41)==0:
            Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(1).SetAttValue ('Queuedup',0)
            Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(1).SetAttValue ('WithoutInformation',3)
            Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(1).SetAttValue ('len1',0)
            Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(1).SetAttValue ('Joining',0)



        if len(L42)==0:
            Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(3).SetAttValue ('Queuedup',0)
            Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(3).SetAttValue ('WithoutInformation',3)
            Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(3).SetAttValue ('len1',0)
            Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(3).SetAttValue ('Joining',0)



        if len(L43)==0:
            Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(4).SetAttValue ('Queuedup',0)
            Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(4).SetAttValue ('WithoutInformation',3)
            Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(4).SetAttValue ('len1',0)
            Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(4).SetAttValue ('Joining',0)


        if len(L44)==0:
            Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(1).SetAttValue ('Queuedup',0)
            Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(1).SetAttValue ('WithoutInformation',3)
            Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(1).SetAttValue ('len1',0)
            Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(1).SetAttValue ('Joining',0)



        if len(L45)==0:
            Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(2).SetAttValue ('Queuedup',0)
            Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(2).SetAttValue ('WithoutInformation',3)
            Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(2).SetAttValue ('len1',0)
            Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(2).SetAttValue ('Joining',0)





        if len(L46)==0:
            Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(3).SetAttValue ('Queuedup',0)
            Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(3).SetAttValue ('WithoutInformation',3)
            Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(3).SetAttValue ('len1',0)
            Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(3).SetAttValue ('Joining',0)


        if len(L47)==0:
            Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(4).SetAttValue ('Queuedup',0)
            Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(4).SetAttValue ('WithoutInformation',3)
            Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(4).SetAttValue ('len1',0)
            Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(4).SetAttValue ('Joining',0)



        if len(L48)==0:
            Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(1).SetAttValue ('Queuedup',0)
            Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(1).SetAttValue ('WithoutInformation',3)
            Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(1).SetAttValue ('len1',0)
            Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(1).SetAttValue ('Joining',0)



        if len(L49)==0:
            Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(2).SetAttValue ('Queuedup',0)
            Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(2).SetAttValue ('WithoutInformation',3)
            Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(2).SetAttValue ('len1',0)
            Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(2).SetAttValue ('Joining',0)



        if len(L50)==0:
            Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(3).SetAttValue ('Queuedup',0)
            Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(3).SetAttValue ('WithoutInformation',3)
            Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(3).SetAttValue ('len1',0)
            Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(3).SetAttValue ('Joining',0)


        if len(L51)==0:
            Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(4).SetAttValue ('Queuedup',0)
            Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(4).SetAttValue ('WithoutInformation',3)
            Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(4).SetAttValue ('len1',0)
            Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(4).SetAttValue ('Joining',0)





        if len(S6)==0:
            Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(1).SetAttValue ('SpecialExtension',0)




        if len(S7)==0:
            Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(3).SetAttValue ('SpecialExtension',0)




        if len(S8)==0:
            Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(2).SetAttValue ('SpecialExtension',0)


        if len(S9)==0:
            Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(4).SetAttValue ('SpecialExtension',0)



        if len(S15)==0:
            Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(1).SetAttValue ('SpecialExtension',0)



        if len(S16)==0:
            Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(4).SetAttValue ('SpecialExtension',0)



        if len(S17)==0:
            Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(2).SetAttValue ('SpecialExtension',0)



        if len(S18)==0:
            Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(3).SetAttValue ('SpecialExtension',0)






        if len(S19)==0:
            Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(1).SetAttValue ('SpecialExtension',0)




        if len(S20)==0:
            Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(4).SetAttValue ('SpecialExtension',0)


        if len(S21)==0:
            Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(3).SetAttValue ('SpecialExtension',0)



        if len(S22)==0:
            Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(2).SetAttValue ('SpecialExtension',0)



        if len(S28)==0:
            Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(2).SetAttValue ('SpecialExtension',0)





        if len(S29)==0:
            Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(3).SetAttValue ('SpecialExtension',0)




        if len(S30)==0:
            Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(4).SetAttValue ('SpecialExtension',0)




        if len(S31)==0:
            Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(1).SetAttValue ('SpecialExtension',0)





        if len(S32)==0:
            Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(3).SetAttValue ('SpecialExtension',0)



        if len(S33)==0:
            Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(4).SetAttValue ('SpecialExtension',0)




        if len(S34)==0:
            Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(1).SetAttValue ('SpecialExtension',0)



        if len(S35)==0:
            Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(2).SetAttValue ('SpecialExtension',0)




        if len(S36)==0:
            Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(3).SetAttValue ('SpecialExtension',0)



        if len(S37)==0:
            Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(4).SetAttValue ('SpecialExtension',0)




        if len(S38)==0:
            Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(1).SetAttValue ('SpecialExtension',0)




        if len(S39)==0:
            Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(2).SetAttValue ('SpecialExtension',0)



        if len(S40)==0:
            Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(2).SetAttValue ('SpecialExtension',0)




        if len(S41)==0:
            Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(1).SetAttValue ('SpecialExtension',0)




        if len(S42)==0:
            Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(3).SetAttValue ('SpecialExtension',0)




        if len(S43)==0:
            Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(4).SetAttValue ('SpecialExtension',0)



        if len(S44)==0:
            Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(1).SetAttValue ('SpecialExtension',0)




        if len(S45)==0:
            Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(2).SetAttValue ('SpecialExtension',0)






        if len(S46)==0:
            Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(3).SetAttValue ('SpecialExtension',0)



        if len(S47)==0:
            Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(4).SetAttValue ('SpecialExtension',0)




        if len(S48)==0:
            Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(1).SetAttValue ('SpecialExtension',0)



        if len(S49)==0:
            Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(2).SetAttValue ('SpecialExtension',0)



        if len(S49)==0:
            Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(2).SetAttValue ('SpecialExtension',0)




        if len(S50)==0:
            Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(3).SetAttValue ('SpecialExtension',0)



        if len(S51)==0:
            Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(4).SetAttValue ('SpecialExtension',0)


        data = [1,2,3,4]
        kios = permutation(data)
        strategies=[]
        for i in range(len(kios)):
            strategies.append(i)        





        GreenStarts=[]
        Queuedups=[]


        pre167=[]
        pre1=[]
        for i in kios:
            pre167.append([2])
            pre1.append([0])

        GreenStarts.append(pre167)
        Queuedups.append(pre1)

        pre2=[]
        pre21=[]
        pre22=[]


        for i in kios:
            kg1 = Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(i[0]).AttValue ('Queuedup')+Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(i[0]).AttValue ('WithoutInformation')+Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(i[0]).AttValue ('Joining')
            kg2 = Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(i[1]).AttValue ('Queuedup')+Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(i[1]).AttValue ('WithoutInformation')+Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(i[1]).AttValue ('Joining')
            kg3 = Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(i[2]).AttValue ('Queuedup')+Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(i[2]).AttValue ('WithoutInformation')+Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(i[2]).AttValue ('Joining')
            kg4 = Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(i[3]).AttValue ('Queuedup')+Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(i[3]).AttValue ('WithoutInformation')+Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(i[3]).AttValue ('Joining')
            fot = ((kg1+kg2+kg3+kg4)/St)/(CLength-12)            
            pre2.append([kg1,kg2+ round(((kg1/ St)/fot)*Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(i[1]).AttValue ('ArrivalRate')/3600)+1,kg3 +round(((kg1+kg2/ St)/fot)*Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(i[2]).AttValue ('ArrivalRate')/3600)+1, kg4+round(((kg1+kg2+kg3/ St)/fot)*Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(i[3]).AttValue ('ArrivalRate')/3600)+1])
        for k in pre2:
            pre21.append([round((k[0]/(k[1]+k[2]+k[3]+k[0]))*(CLength-12)), round((k[1]/(k[1]+k[2]+k[3]+k[0]))*(CLength-12)), round((k[2]/(k[1]+k[2]+k[3]+k[0]))*(CLength-12)), round((k[3]/(k[1]+k[2]+k[3]+k[0]))*(CLength-12))])
        for m in pre21:
            pre22.append([2, m[0]+5, m[0] + m[1]+8, m[0] + m[1]+ m[2]+11])


        GreenStarts.append(pre22)
        Queuedups.append(pre2)




        pre3=[]
        pre31=[]
        pre32=[]


        for i in kios:
            kg1 = Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(i[0]).AttValue ('Queuedup')+Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(i[0]).AttValue ('WithoutInformation')+Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(i[0]).AttValue ('Joining')
            kg2 = Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(i[1]).AttValue ('Queuedup')+Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(i[1]).AttValue ('WithoutInformation')+Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(i[1]).AttValue ('Joining')
            kg3 = Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(i[2]).AttValue ('Queuedup')+Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(i[2]).AttValue ('WithoutInformation')+Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(i[2]).AttValue ('Joining')
            kg4 = Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(i[3]).AttValue ('Queuedup')+Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(i[3]).AttValue ('WithoutInformation')+Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(i[3]).AttValue ('Joining')
            fot = ((kg1+kg2+kg3+kg4)/St)/(CLength-12)            
            pre3.append([kg1,kg2+ round(((kg1/ St)/fot)*Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(i[1]).AttValue ('ArrivalRate')/3600)+1,kg3 +round(((kg1+kg2/ St)/fot)*Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(i[2]).AttValue ('ArrivalRate')/3600)+1, kg4+round(((kg1+kg2+kg3/ St)/fot)*Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(i[3]).AttValue ('ArrivalRate')/3600)+1])

        for k in pre3:
            pre31.append([round((k[0]/(k[1]+k[2]+k[3]+k[0]))*(CLength-12)), round((k[1]/(k[1]+k[2]+k[3]+k[0]))*(CLength-12)), round((k[2]/(k[1]+k[2]+k[3]+k[0]))*(CLength-12)), round((k[3]/(k[1]+k[2]+k[3]+k[0]))*(CLength-12))])
        for m in pre31:
                pre32.append([2, m[0]+5, m[0] + m[1]+8, m[0] + m[1]+ m[2]+11])


        GreenStarts.append(pre32)
        Queuedups.append(pre3)

        pre4=[]
        pre41=[]
        pre42=[]


        for i in kios:
            kg1 = Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(i[0]).AttValue ('Queuedup')+Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(i[0]).AttValue ('WithoutInformation')+Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(i[0]).AttValue ('Joining')
            kg2 = Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(i[1]).AttValue ('Queuedup')+Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(i[1]).AttValue ('WithoutInformation')+Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(i[1]).AttValue ('Joining')
            kg3 = Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(i[2]).AttValue ('Queuedup')+Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(i[2]).AttValue ('WithoutInformation')+Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(i[2]).AttValue ('Joining')
            kg4 = Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(i[3]).AttValue ('Queuedup')+Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(i[3]).AttValue ('WithoutInformation')+Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(i[3]).AttValue ('Joining')
            fot = ((kg1+kg2+kg3+kg4)/St)/(CLength-12)            
            pre4.append([kg1,kg2+ round(((kg1/ St)/fot)*Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(i[1]).AttValue ('ArrivalRate')/3600)+1,kg3 +round(((kg1+kg2/ St)/fot)*Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(i[2]).AttValue ('ArrivalRate')/3600)+1, kg4+round(((kg1+kg2+kg3/ St)/fot)*Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(i[3]).AttValue ('ArrivalRate')/3600)+1])
        for k in pre4:
            pre41.append([round((k[0]/(k[1]+k[2]+k[3]+k[0]))*(CLength-12)), round((k[1]/(k[1]+k[2]+k[3]+k[0]))*(CLength-12)), round((k[2]/(k[1]+k[2]+k[3]+k[0]))*(CLength-12)), round((k[3]/(k[1]+k[2]+k[3]+k[0]))*(CLength-12))])
        for m in pre41:
                pre42.append([2, m[0]+5, m[0] + m[1]+8, m[0] + m[1]+ m[2]+11])


        GreenStarts.append(pre42)
        Queuedups.append(pre4)


        pre52=[]
        pre5=[]
        for i in kios:
            pre52.append([2])
            pre5.append([0])

        GreenStarts.append(pre52)
        Queuedups.append(pre5)





        pre6=[]
        pre61=[]
        pre62=[]


        for i in kios:
            kg1 = Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(i[0]).AttValue ('Queuedup')+Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(i[0]).AttValue ('WithoutInformation')+Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(i[0]).AttValue ('Joining')
            kg2 = Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(i[1]).AttValue ('Queuedup')+Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(i[1]).AttValue ('WithoutInformation')+Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(i[1]).AttValue ('Joining')
            kg3 = Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(i[2]).AttValue ('Queuedup')+Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(i[2]).AttValue ('WithoutInformation')+Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(i[2]).AttValue ('Joining')
            kg4 = Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(i[3]).AttValue ('Queuedup')+Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(i[3]).AttValue ('WithoutInformation')+Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(i[3]).AttValue ('Joining')
            fot = ((kg1+kg2+kg3+kg4)/St)/(CLength-12)            
            pre6.append([kg1,kg2+ round(((kg1/ St)/fot)*Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(i[1]).AttValue ('ArrivalRate')/3600)+1,kg3 +round(((kg1+kg2/ St)/fot)*Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(i[2]).AttValue ('ArrivalRate')/3600)+1, kg4+round(((kg1+kg2+kg3/ St)/fot)*Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(i[3]).AttValue ('ArrivalRate')/3600)+1])
        for k in pre6:
            pre61.append([round((k[0]/(k[1]+k[2]+k[3]+k[0]))*(CLength-12)), round((k[1]/(k[1]+k[2]+k[3]+k[0]))*(CLength-12)), round((k[2]/(k[1]+k[2]+k[3]+k[0]))*(CLength-12)), round((k[3]/(k[1]+k[2]+k[3]+k[0]))*(CLength-12))])
        for m in pre61:
                pre62.append([2, m[0]+5, m[0] + m[1]+8, m[0] + m[1]+ m[2]+11])


        GreenStarts.append(pre62)
        Queuedups.append(pre6)

        pre7=[]
        pre71=[]
        pre72=[]


        for i in kios:
            kg1 = Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(i[0]).AttValue ('Queuedup')+Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(i[0]).AttValue ('WithoutInformation')+Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(i[0]).AttValue ('Joining')
            kg2 = Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(i[1]).AttValue ('Queuedup')+Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(i[1]).AttValue ('WithoutInformation')+Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(i[1]).AttValue ('Joining')
            kg3 = Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(i[2]).AttValue ('Queuedup')+Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(i[2]).AttValue ('WithoutInformation')+Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(i[2]).AttValue ('Joining')
            kg4 = Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(i[3]).AttValue ('Queuedup')+Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(i[3]).AttValue ('WithoutInformation')+Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(i[3]).AttValue ('Joining')
            fot = ((kg1+kg2+kg3+kg4)/St)/(CLength-12)            
            pre7.append([kg1,kg2+ round(((kg1/ St)/fot)*Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(i[1]).AttValue ('ArrivalRate')/3600)+1,kg3 +round(((kg1+kg2/ St)/fot)*Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(i[2]).AttValue ('ArrivalRate')/3600)+1, kg4+round(((kg1+kg2+kg3/ St)/fot)*Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(i[3]).AttValue ('ArrivalRate')/3600)+1])
        for k in pre7:
            pre71.append([round((k[0]/(k[1]+k[2]+k[3]+k[0]))*(CLength-12)), round((k[1]/(k[1]+k[2]+k[3]+k[0]))*(CLength-12)), round((k[2]/(k[1]+k[2]+k[3]+k[0]))*(CLength-12)), round((k[3]/(k[1]+k[2]+k[3]+k[0]))*(CLength-12))])
        for m in pre71:
            pre72.append([2, m[0]+5, m[0] + m[1]+8, m[0] + m[1]+ m[2]+11])


        GreenStarts.append(pre72)
        Queuedups.append(pre7)

        pre8=[]
        pre81=[]
        pre82=[]


        for i in kios:
            kg1 = Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(i[0]).AttValue ('Queuedup')+Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(i[0]).AttValue ('WithoutInformation')+Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(i[0]).AttValue ('Joining')
            kg2 = Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(i[1]).AttValue ('Queuedup')+Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(i[1]).AttValue ('WithoutInformation')+Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(i[1]).AttValue ('Joining')
            kg3 = Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(i[2]).AttValue ('Queuedup')+Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(i[2]).AttValue ('WithoutInformation')+Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(i[2]).AttValue ('Joining')
            kg4 = Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(i[3]).AttValue ('Queuedup')+Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(i[3]).AttValue ('WithoutInformation')+Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(i[3]).AttValue ('Joining')
            fot = ((kg1+kg2+kg3+kg4)/St)/(CLength-12)            
            pre8.append([kg1,kg2+ round(((kg1/ St)/fot)*Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(i[1]).AttValue ('ArrivalRate')/3600)+1,kg3 +round(((kg1+kg2/ St)/fot)*Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(i[2]).AttValue ('ArrivalRate')/3600)+1, kg4+round(((kg1+kg2+kg3/ St)/fot)*Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(i[3]).AttValue ('ArrivalRate')/3600)+1])
        for k in pre8:
            pre81.append([round((k[0]/(k[1]+k[2]+k[3]+k[0]))*(CLength-12)), round((k[1]/(k[1]+k[2]+k[3]+k[0]))*(CLength-12)), round((k[2]/(k[1]+k[2]+k[3]+k[0]))*(CLength-12)), round((k[3]/(k[1]+k[2]+k[3]+k[0]))*(CLength-12))])
        for m in pre81:
            pre82.append([2, m[0]+5, m[0] + m[1]+8, m[0] + m[1]+ m[2]+11])


        GreenStarts.append(pre82)
        Queuedups.append(pre8)


        pre9=[]
        pre91=[]
        pre92=[]


        for i in kios:
            kg1 = Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(i[0]).AttValue ('Queuedup')+Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(i[0]).AttValue ('WithoutInformation')+Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(i[0]).AttValue ('Joining')
            kg2 = Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(i[1]).AttValue ('Queuedup')+Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(i[1]).AttValue ('WithoutInformation')+Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(i[1]).AttValue ('Joining')
            kg3 = Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(i[2]).AttValue ('Queuedup')+Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(i[2]).AttValue ('WithoutInformation')+Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(i[2]).AttValue ('Joining')
            kg4 = Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(i[3]).AttValue ('Queuedup')+Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(i[3]).AttValue ('WithoutInformation')+Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(i[3]).AttValue ('Joining')
            fot = ((kg1+kg2+kg3+kg4)/St)/(CLength-12)            
            pre9.append([kg1,kg2+ round(((kg1/ St)/fot)*Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(i[1]).AttValue ('ArrivalRate')/3600)+1,kg3 +round(((kg1+kg2/ St)/fot)*Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(i[2]).AttValue ('ArrivalRate')/3600)+1, kg4+round(((kg1+kg2+kg3/ St)/fot)*Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(i[3]).AttValue ('ArrivalRate')/3600)+1])
        for k in pre9:
            pre91.append([round((k[0]/(k[1]+k[2]+k[3]+k[0]))*(CLength-12)), round((k[1]/(k[1]+k[2]+k[3]+k[0]))*(CLength-12)), round((k[2]/(k[1]+k[2]+k[3]+k[0]))*(CLength-12)), round((k[3]/(k[1]+k[2]+k[3]+k[0]))*(CLength-12))])

        for m in pre91:
            pre92.append([2, m[0]+5, m[0] + m[1]+8, m[0] + m[1]+ m[2]+11])



        GreenStarts.append(pre92)

        Queuedups.append(pre9)
        pre10=[]
        pre101=[]
        pre102=[]


        for i in kios:
            kg1 = Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(i[0]).AttValue ('Queuedup')+Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(i[0]).AttValue ('WithoutInformation')+Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(i[0]).AttValue ('Joining')
            kg2 = Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(i[1]).AttValue ('Queuedup')+Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(i[1]).AttValue ('WithoutInformation')+Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(i[1]).AttValue ('Joining')
            kg3 = Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(i[2]).AttValue ('Queuedup')+Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(i[2]).AttValue ('WithoutInformation')+Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(i[2]).AttValue ('Joining')
            kg4 = Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(i[3]).AttValue ('Queuedup')+Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(i[3]).AttValue ('WithoutInformation')+Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(i[3]).AttValue ('Joining')
            fot = ((kg1+kg2+kg3+kg4)/St)/(CLength-12)            
            pre10.append([kg1,kg2+ round(((kg1/ St)/fot)*Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(i[1]).AttValue ('ArrivalRate')/3600)+1,kg3 +round(((kg1+kg2/ St)/fot)*Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(i[2]).AttValue ('ArrivalRate')/3600)+1, kg4+round(((kg1+kg2+kg3/ St)/fot)*Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(i[3]).AttValue ('ArrivalRate')/3600)+1])
        for k in pre10:
            pre101.append([round((k[0]/(k[1]+k[2]+k[3]+k[0]))*(CLength-12)), round((k[1]/(k[1]+k[2]+k[3]+k[0]))*(CLength-12)), round((k[2]/(k[1]+k[2]+k[3]+k[0]))*(CLength-12)), round((k[3]/(k[1]+k[2]+k[3]+k[0]))*(CLength-12))])
        for m in pre101:
            pre102.append([2, m[0]+5, m[0] + m[1]+8, m[0] + m[1]+ m[2]+11])


        GreenStarts.append(pre102)
        Queuedups.append(pre10)


        pre11=[]
        pre111=[]
        pre112=[]


        for i in kios:
            kg1 = Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(i[0]).AttValue ('Queuedup')+Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(i[0]).AttValue ('WithoutInformation')+Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(i[0]).AttValue ('Joining')
            kg2 = Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(i[1]).AttValue ('Queuedup')+Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(i[1]).AttValue ('WithoutInformation')+Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(i[1]).AttValue ('Joining')
            kg3 = Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(i[2]).AttValue ('Queuedup')+Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(i[2]).AttValue ('WithoutInformation')+Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(i[2]).AttValue ('Joining')
            kg4 = Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(i[3]).AttValue ('Queuedup')+Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(i[3]).AttValue ('WithoutInformation')+Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(i[3]).AttValue ('Joining')
            fot = ((kg1+kg2+kg3+kg4)/St)/(CLength-12)            
            pre11.append([kg1,kg2+ round(((kg1/ St)/fot)*Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(i[1]).AttValue ('ArrivalRate')/3600)+1,kg3 +round(((kg1+kg2/ St)/fot)*Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(i[2]).AttValue ('ArrivalRate')/3600)+1, kg4+round(((kg1+kg2+kg3/ St)/fot)*Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(i[3]).AttValue ('ArrivalRate')/3600)+1])
        for k in pre11:
            pre111.append([round((k[0]/(k[1]+k[2]+k[3]+k[0]))*(CLength-12)), round((k[1]/(k[1]+k[2]+k[3]+k[0]))*(CLength-12)), round((k[2]/(k[1]+k[2]+k[3]+k[0]))*(CLength-12)), round((k[3]/(k[1]+k[2]+k[3]+k[0]))*(CLength-12))])
        for m in pre111:
            pre112.append([2, m[0]+5, m[0] + m[1]+8, m[0] + m[1]+ m[2]+11])


        GreenStarts.append(pre112)
        Queuedups.append(pre11)

        pre122=[]
        pre12=[]
        for i in kios:
            pre122.append([2])
            pre12.append([0])

        GreenStarts.append(pre122)
        Queuedups.append(pre12)

        pre132=[]
        pre13=[]
        for i in kios:
            pre132.append([2])
            pre13.append([0])

        GreenStarts.append(pre132)
        Queuedups.append(pre13)

        CriticalPaths=[]


        for x in SignalAttributes1:
            if x[SigAttNames1['No']] in SigCritical1:
                CriticalPaths.append([1,x[SigAttNames1['No']]])

        for x in SignalAttributes2:
            if x[SigAttNames2['No']] in SigCritical2:
                CriticalPaths.append([2,x[SigAttNames2['No']]])

        for x in SignalAttributes3:
            if x[SigAttNames3['No']] in SigCritical3:
                CriticalPaths.append([3,x[SigAttNames3['No']]])

        for x in SignalAttributes4:
            if x[SigAttNames4['No']] in SigCritical4:
                CriticalPaths.append([4,x[SigAttNames4['No']]])

        for x in SignalAttributes5:
            if x[SigAttNames5['No']] in SigCritical5:
                CriticalPaths.append([5,x[SigAttNames5['No']]])

        for x in SignalAttributes6:
            if x[SigAttNames6['No']] in SigCritical6:
                CriticalPaths.append([6,x[SigAttNames6['No']]])

        for x in SignalAttributes7:
            if x[SigAttNames7['No']] in SigCritical7:
                CriticalPaths.append([7,x[SigAttNames7['No']]])

        for x in SignalAttributes8:
            if x[SigAttNames8['No']] in SigCritical8:
                CriticalPaths.append([8,x[SigAttNames8['No']]])

        for x in SignalAttributes9:
            if x[SigAttNames9['No']] in SigCritical9:
                CriticalPaths.append([9,x[SigAttNames9['No']]])

        for x in SignalAttributes10:
            if x[SigAttNames10['No']] in SigCritical10:
                CriticalPaths.append([10,x[SigAttNames10['No']]])

        for x in SignalAttributes11:
            if x[SigAttNames11['No']] in SigCritical11:
                CriticalPaths.append([11,x[SigAttNames11['No']]])

        for x in SignalAttributes12:
            if x[SigAttNames12['No']] in SigCritical12:
                CriticalPaths.append([12,x[SigAttNames12['No']]])

        for x in SignalAttributes13:
            if x[SigAttNames13['No']] in SigCritical13:
                CriticalPaths.append([13,x[SigAttNames13['No']]])




        upstream21=[[1,1], [2,1]]
        upstream22=[[9,4], [2,2]]
        upstream23=[[3,3], [2,3]]
        upstream24=[[6,4], [2,4]]

        Criticals=[]


        if Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(1).AttValue ('ArrivalRate')> Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(1).AttValue ('ArrivalRate'):
            if Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(1).AttValue ('ArrivalRate')> Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(1).AttValue ('ArrivalRate'):
                if upstream21[0] in CriticalPaths and upstream21[1] in CriticalPaths:
                    Criticals.append(upstream21)

        if upstream22[0] in CriticalPaths and upstream22[1] in CriticalPaths:
            Criticals.append(upstream22)

        if upstream23[0] in CriticalPaths and upstream23[1] in CriticalPaths:
            Criticals.append(upstream23)


        if upstream24[0] in CriticalPaths and upstream24[1] in CriticalPaths:
            Criticals.append(upstream24)

        upstream31=[[2,1], [3,1]]
        upstream32=[[10,4], [3,2]]
        upstream33=[[4,3], [3,3]]
        upstream34=[[7,4], [3,4]]

        if upstream31[0] in CriticalPaths and upstream31[1] in CriticalPaths:
            Criticals.append(upstream31)

        if upstream32[0] in CriticalPaths and upstream32[1] in CriticalPaths:
            Criticals.append(upstream32)

        if upstream33[0] in CriticalPaths and upstream33[1] in CriticalPaths:
            Criticals.append(upstream33)


        if upstream34[0] in CriticalPaths and upstream34[1] in CriticalPaths:
            Criticals.append(upstream34)


        upstream41=[[3,1], [4,1]]
        upstream42=[[11,4], [4,2]]
        upstream43=[[5,1], [4,3]]
        upstream44=[[8,4], [4,4]]


        if upstream41[0] in CriticalPaths and upstream41[1] in CriticalPaths:
            Criticals.append(upstream41)

        if upstream42[0] in CriticalPaths and upstream42[1] in CriticalPaths:
            Criticals.append(upstream42)

        if Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(3).AttValue ('ArrivalRate')> Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(3).AttValue ('ArrivalRate'):
            if Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(3).AttValue ('ArrivalRate')> Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(2).AttValue ('ArrivalRate'):
                if upstream43[0] in CriticalPaths and upstream43[1] in CriticalPaths:
                    Criticals.append(upstream43)


        if upstream44[0] in CriticalPaths and upstream44[1] in CriticalPaths:
            Criticals.append(upstream44)



        upstream61=[[1,1], [6,1]]
        upstream62=[[2,2],[6,2]]
        upstream63=[[7,3], [6,3]]
        upstream64=[[13,1], [6,4]]


        if Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(1).AttValue ('ArrivalRate')> Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(1).AttValue ('ArrivalRate'):
            if Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(1).AttValue ('ArrivalRate')> Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(1).AttValue ('ArrivalRate'):
                if upstream61[0] in CriticalPaths and upstream61[1] in CriticalPaths:
                    Criticals.append(upstream61)

        if upstream62[0] in CriticalPaths and upstream62[1] in CriticalPaths:
            Criticals.append(upstream62)

        if upstream63[0] in CriticalPaths and upstream63[1] in CriticalPaths:
            Criticals.append(upstream63)

        if Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(4).AttValue ('ArrivalRate')> Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(4).AttValue ('ArrivalRate'):
            if Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(4).AttValue ('ArrivalRate')> Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(4).AttValue ('ArrivalRate'):
                if upstream64[0] in CriticalPaths and upstream64[1] in CriticalPaths:
                    Criticals.append(upstream64)


        upstream71=[[6,1], [7,1]]
        upstream72=[[3,2],[7,2]]
        upstream73=[[8,3], [7,3]]
        upstream74=[[13,1], [7,4]]



        if upstream71[0] in CriticalPaths and upstream71[1] in CriticalPaths:
            Criticals.append(upstream71)

        if upstream72[0] in CriticalPaths and upstream72[1] in CriticalPaths:
            Criticals.append(upstream72)

        if upstream73[0] in CriticalPaths and upstream73[1] in CriticalPaths:
            Criticals.append(upstream73)

        if Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(4).AttValue ('ArrivalRate')> Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(4).AttValue ('ArrivalRate'):
            if Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(4).AttValue ('ArrivalRate')> Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(4).AttValue ('ArrivalRate'):
                if upstream74[0] in CriticalPaths and upstream74[1] in CriticalPaths:
                    Criticals.append(upstream74)




        upstream81=[[7,1], [8,1]]
        upstream82=[[4,2],[8,2]]
        upstream83=[[5,1], [8,3]]
        upstream84=[[13,1], [8,4]]


        if upstream81[0] in CriticalPaths and upstream81[1] in CriticalPaths:
            Criticals.append(upstream81)

        if upstream82[0] in CriticalPaths and upstream82[1] in CriticalPaths:
            Criticals.append(upstream82)

        if Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(3).AttValue ('ArrivalRate')> Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(3).AttValue ('ArrivalRate'):
            if Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(3).AttValue ('ArrivalRate')> Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(2).AttValue ('ArrivalRate'):
                if upstream83[0] in CriticalPaths and upstream83[1] in CriticalPaths:
                    Criticals.append(upstream83)

        if Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(4).AttValue ('ArrivalRate')> Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(4).AttValue ('ArrivalRate'):
            if Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(4).AttValue ('ArrivalRate')> Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(4).AttValue ('ArrivalRate'):
                if upstream84[0] in CriticalPaths and upstream84[1] in CriticalPaths:
                    Criticals.append(upstream84)


        upstream91=[[1,1], [9,1]]
        upstream92=[[10,2],[9,2]]
        upstream93=[[2,4], [9,3]]
        upstream94=[[12,1], [9,4]]


        if Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(1).AttValue ('ArrivalRate')> Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(1).AttValue ('ArrivalRate'):
            if Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(1).AttValue ('ArrivalRate')> Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(1).AttValue ('ArrivalRate'):
                if upstream91[0] in CriticalPaths and upstream91[1] in CriticalPaths:
                    Criticals.append(upstream91)

        if upstream92[0] in CriticalPaths and upstream92[1] in CriticalPaths:
            Criticals.append(upstream92)

        if upstream93[0] in CriticalPaths and upstream93[1] in CriticalPaths:
            Criticals.append(upstream93)

        if Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(4).AttValue ('ArrivalRate')> Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(4).AttValue ('ArrivalRate'):
            if Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(4).AttValue ('ArrivalRate')> Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(4).AttValue ('ArrivalRate'):
                if upstream94[0] in CriticalPaths and upstream94[1] in CriticalPaths:
                    Criticals.append(upstream94)



        upstream101=[[9,1], [10,1]]
        upstream102=[[10,2],[10,2]]
        upstream103=[[3,4], [10,3]]
        upstream104=[[12,1],[10,4]]


        if upstream101[0] in CriticalPaths and upstream101[1] in CriticalPaths:
            Criticals.append(upstream101)

        if upstream102[0] in CriticalPaths and upstream102[1] in CriticalPaths:
            Criticals.append(upstream102)

        if upstream103[0] in CriticalPaths and upstream103[1] in CriticalPaths:
            Criticals.append(upstream103)


        if Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(4).AttValue ('ArrivalRate')> Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(4).AttValue ('ArrivalRate'):
            if Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(4).AttValue ('ArrivalRate')> Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(4).AttValue ('ArrivalRate'):
                if upstream104[0] in CriticalPaths and upstream104[1] in CriticalPaths:
                    Criticals.append(upstream104)




        upstream111=[[10,1], [11,1]]
        upstream112=[[5,1],[11,2]]
        upstream113=[[4,4], [11,3]]
        upstream114=[[12,1],[11,4]]



        if upstream111[0] in CriticalPaths and upstream111[1] in CriticalPaths:
            Criticals.append(upstream111)

        if Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(2).AttValue ('ArrivalRate')> Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(3).AttValue ('ArrivalRate'):
            if Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(2).AttValue ('ArrivalRate')> Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(3).AttValue ('ArrivalRate'):
                if upstream112[0] in CriticalPaths and upstream112[1] in CriticalPaths:
                    Criticals.append(upstream112)

        if upstream113[0] in CriticalPaths and upstream113[1] in CriticalPaths:
            Criticals.append(upstream113)

        if Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(4).AttValue ('ArrivalRate')> Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(4).AttValue ('ArrivalRate'):
            if Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(4).AttValue ('ArrivalRate')> Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(4).AttValue ('ArrivalRate'):
                if upstream114[0] in CriticalPaths and upstream114[1] in CriticalPaths:
                    Criticals.append(upstream114)

        
  
        


        if len(Criticals)>0:
            for kos in range(len(Criticals)):
                for i in Criticals:
                    for j in Criticals:
                        B= i[-2]
                        C= j[-1]
                        if B==C:
                            j.append(i[-1])
                            Criticals.remove(i)




        CriticalIntersections=[]
        for i in Criticals:
            mm=[]
            for j in i:
                mm.append(j[0])
            CriticalIntersections.append(mm)



        kios2=[]
        for ik in range(len(kios)):
            kios2.append([1,2])


        f2= open("12.txt","w")
        f2.write(str(Criticals))
        f2.write("\n")
        f2.close()

        f2= open("13.txt","w")
        f2.write(str(CriticalIntersections))
        f2.write("\n")
        f2.close()

        totalop=[]
        for i in Criticals:
            kk2 = []
            kk22=[]
            op =-1
            # this derives possible positions of each critical phase 
            while op >= -len(i):
                kk=[]
                kk11=[]
                if i[op][0] != 1 and i[op][0] != 5 and i[op][0] != 12 and i[op][0] != 13:
                    for mm in kios:
                        for mmm in mm:
                            if mmm == i[op][1]:
                                kk.append(mm.index(mmm))
                                kk11.append([i[op][0],i[op][1], mm.index(mmm),mm])
                    kk2.append(kk)
                    kk22.append(kk11)


                else:
                    for mm in kios2:
                        for mmm in mm:
                            if mmm == i[op][1]:
                                kk.append(mm.index(mmm))
                                kk11.append([i[op][0],i[op][1], mm.index(mmm),mm])
                    kk2.append(kk)
                    kk22.append(kk11)
                op = op-1


            mth2=[]
            qth2 = []
            mth22=[]
            qth22 = []
            op = -1
            fos=0

            # it derives the possible green starts and queued up vehicles og critical phases with respect to the above positions
            while op >= -len(i):
                mth = []
                qth = []
                mth11 = []
                qth11 = []
                if i[op][0] != 1 and i[op][0] != 5 and i[op][0] != 12 and i[op][0] != 13:
                    for k in range(len(GreenStarts[i[op][0] - 1])):
                        mth.append(GreenStarts[i[op][0] - 1][k][kk2[fos][k]])
                        qth.append(Queuedups[i[op][0] - 1][k][kk2[fos][k]])
                        qth11.append([i[op][0],i[op][1],kk2[fos][k], Queuedups[i[op][0] - 1][k][kk2[fos][k]],kios[k]])
                        mth11.append([i[op][0],i[op][1],kk2[fos][k], GreenStarts[i[op][0] - 1][k][kk2[fos][k]],kios[k]])
                else:
                    for k in range(len(GreenStarts[i[op][0] - 1])):
                        mth.append(GreenStarts[i[op][0] - 1][k][kk2[fos][k]])
                        qth.append(Queuedups[i[op][0] - 1][k][kk2[fos][k]])
                        qth11.append([i[op][0],i[op][1],kk2[fos][k], Queuedups[i[op][0] - 1][k][kk2[fos][k]],kios2[k]])
                        mth11.append([i[op][0],i[op][1],kk2[fos][k], GreenStarts[i[op][0] - 1][k][kk2[fos][k]],kios2[k]])


                mth2.append(mth)
                mth22.append(mth11)
                qth22.append(qth11)
                qth2.append(qth)
                op = op - 1
                fos+=1

            optimization2=[]
            indexoptimization2 = []
            indexoptimization22 = []
            bo=0
            #finding optimal sequence
            while bo < len(mth2)-1:
                optimization = []
                indexoptimization1=[]
                indexoptimization11 = []
                for kkk in range(len(mth2[bo])):
                    for jjj in range(len(mth2[bo+1])):
                        klj = abs(mth2[bo][kkk] - qth2[bo][kkk] / St - mth2[bo+1][jjj] + TTTt)
                        optimization.append(klj)
                        indexoptimization1.append([mth22[bo][kkk][0],mth22[bo][kkk][1],mth22[bo][kkk][2],mth22[bo][kkk][-1]])
                        indexoptimization11.append([mth22[bo + 1][jjj][0], mth22[bo + 1][jjj][1], mth22[bo + 1][jjj][2],mth22[bo+1][jjj][-1]])

                optimization2.append(optimization)
                indexoptimization2.append(indexoptimization1)
                indexoptimization22.append(indexoptimization11)
                bo+=1




            optimization3=[]
            indexes4=[]
            for book in optimization2[0]:
                optimization3.append(0)



            for bid in range(len(optimization2)):
                for zzz in range(len(optimization2[bid])):
                    optimization3[zzz]= optimization3[zzz] + optimization2[bid][zzz]

            opti = min(optimization3)
            kkkp = optimization3.index(opti)




            finaloptimization=[]
            for sss in range(len(i)):
                if sss == 0:
                    finaloptimization.append(indexoptimization2[sss][kkkp])
                    finaloptimization.append(indexoptimization22[sss][kkkp])
                elif sss <= len(i)-2:
                    finaloptimization.append(indexoptimization22[sss][kkkp])

            totalop.append(finaloptimization)

        innn=[]
        seqc=[]
        for i in totalop:
            for j in i:
                innn.append(j[0])
                seqc.append(j[-1])




        kkp=1
        Aseq=[]
        while kkp<=13:
            if kkp == 1 or kkp == 5 or kkp == 12 or kkp == 13:
                Aseq.append([1, 2,3,4])

            elif kkp in innn:
                bno=innn.index(kkp)
                Aseq.append(seqc[bno])
            else:
                Aseq.append([1, 2, 3, 4])
            kkp+=1

        f2= open("3.txt","w")
        f2.write(str(Aseq))
        f2.write("\n")
        f2.close()



# circling signals

    if Seconds >=1:
        f2 = open("3.txt","r")  
        ggg = f2.readline()
        f2.close()
        Aseq= ast.literal_eval(ggg)       

   




    CLength=80
    if Seconds >= 1 and Seconds < 5:
        Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(Aseq[0][0]).SetAttValue ('GreenTimeDuration',37)
        Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(Aseq[0][1]).SetAttValue ('GreenTimeDuration',37)
        Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(Aseq[0][2]).SetAttValue ('GreenTimeDuration',37)
        Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(Aseq[0][3]).SetAttValue ('GreenTimeDuration',37)

        Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(Aseq[1][0]).SetAttValue ('GreenTimeDuration',17)
        Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(Aseq[1][1]).SetAttValue ('GreenTimeDuration',17)
        Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(Aseq[1][2]).SetAttValue ('GreenTimeDuration',17)
        Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(Aseq[1][3]).SetAttValue ('GreenTimeDuration',17)
                    

        Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(Aseq[2][0]).SetAttValue ('GreenTimeDuration',17)
        Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(Aseq[2][1]).SetAttValue ('GreenTimeDuration',17)
        Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(Aseq[2][2]).SetAttValue ('GreenTimeDuration',17)
        Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(Aseq[2][3]).SetAttValue ('GreenTimeDuration',17)
        

        Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(Aseq[3][0]).SetAttValue ('GreenTimeDuration',17)
        Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(Aseq[3][1]).SetAttValue ('GreenTimeDuration',17)
        Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(Aseq[3][2]).SetAttValue ('GreenTimeDuration',17)
        Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(Aseq[3][3]).SetAttValue ('GreenTimeDuration',17)

        Vissim.Net.SignalControllers.ItemByKey(5).SGs.ItemByKey(Aseq[4][0]).SetAttValue ('GreenTimeDuration',37)
        Vissim.Net.SignalControllers.ItemByKey(5).SGs.ItemByKey(Aseq[4][1]).SetAttValue ('GreenTimeDuration',37)
        Vissim.Net.SignalControllers.ItemByKey(5).SGs.ItemByKey(Aseq[4][2]).SetAttValue ('GreenTimeDuration',37)
        Vissim.Net.SignalControllers.ItemByKey(5).SGs.ItemByKey(Aseq[4][3]).SetAttValue ('GreenTimeDuration',37)



        Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(Aseq[5][0]).SetAttValue ('GreenTimeDuration',17)
        Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(Aseq[5][1]).SetAttValue ('GreenTimeDuration',17)
        Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(Aseq[5][2]).SetAttValue ('GreenTimeDuration',17)
        Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(Aseq[5][3]).SetAttValue ('GreenTimeDuration',17)

        Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(Aseq[6][0]).SetAttValue ('GreenTimeDuration',17)
        Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(Aseq[6][1]).SetAttValue ('GreenTimeDuration',17)
        Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(Aseq[6][2]).SetAttValue ('GreenTimeDuration',17)
        Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(Aseq[6][3]).SetAttValue ('GreenTimeDuration',17)

        Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(Aseq[7][0]).SetAttValue ('GreenTimeDuration',17)
        Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(Aseq[7][1]).SetAttValue ('GreenTimeDuration',17)
        Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(Aseq[7][2]).SetAttValue ('GreenTimeDuration',17)
        Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(Aseq[7][3]).SetAttValue ('GreenTimeDuration',17)


        Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(Aseq[8][0]).SetAttValue ('GreenTimeDuration',17)
        Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(Aseq[8][1]).SetAttValue ('GreenTimeDuration',17)
        Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(Aseq[8][2]).SetAttValue ('GreenTimeDuration',17)
        Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(Aseq[8][3]).SetAttValue ('GreenTimeDuration',17)

        Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(Aseq[9][0]).SetAttValue ('GreenTimeDuration',17)
        Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(Aseq[9][1]).SetAttValue ('GreenTimeDuration',17)
        Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(Aseq[9][2]).SetAttValue ('GreenTimeDuration',17)
        Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(Aseq[9][3]).SetAttValue ('GreenTimeDuration',17)

        Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(Aseq[10][0]).SetAttValue ('GreenTimeDuration',17)
        Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(Aseq[10][1]).SetAttValue ('GreenTimeDuration',17)
        Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(Aseq[10][2]).SetAttValue ('GreenTimeDuration',17)
        Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(Aseq[10][3]).SetAttValue ('GreenTimeDuration',17)

        Vissim.Net.SignalControllers.ItemByKey(12).SGs.ItemByKey(Aseq[11][0]).SetAttValue ('GreenTimeDuration',37)
        Vissim.Net.SignalControllers.ItemByKey(12).SGs.ItemByKey(Aseq[11][1]).SetAttValue ('GreenTimeDuration',37)
        Vissim.Net.SignalControllers.ItemByKey(12).SGs.ItemByKey(Aseq[11][2]).SetAttValue ('GreenTimeDuration',37)
        Vissim.Net.SignalControllers.ItemByKey(12).SGs.ItemByKey(Aseq[11][3]).SetAttValue ('GreenTimeDuration',37)


        Vissim.Net.SignalControllers.ItemByKey(13).SGs.ItemByKey(Aseq[12][0]).SetAttValue ('GreenTimeDuration',37)
        Vissim.Net.SignalControllers.ItemByKey(13).SGs.ItemByKey(Aseq[12][1]).SetAttValue ('GreenTimeDuration',37)
        Vissim.Net.SignalControllers.ItemByKey(13).SGs.ItemByKey(Aseq[12][2]).SetAttValue ('GreenTimeDuration',37)
        Vissim.Net.SignalControllers.ItemByKey(13).SGs.ItemByKey(Aseq[12][3]).SetAttValue ('GreenTimeDuration',37)




        Vissim.Net.SignalControllers.ItemByKey(13).SGs.ItemByKey(1).SetAttValue ('ContrByCOM',True)
        Vissim.Net.SignalControllers.ItemByKey(13).SGs.ItemByKey(2).SetAttValue ('ContrByCOM',True)
        Vissim.Net.SignalControllers.ItemByKey(13).SGs.ItemByKey(3).SetAttValue ('ContrByCOM',True)
        Vissim.Net.SignalControllers.ItemByKey(13).SGs.ItemByKey(4).SetAttValue ('ContrByCOM',True)
        Vissim.Net.SignalControllers.ItemByKey(13).SGs.ItemByKey(Aseq[12][0]).SetAttValue ('SigState','GREEN')


        Vissim.Net.SignalControllers.ItemByKey(12).SGs.ItemByKey(1).SetAttValue ('ContrByCOM',True)
        Vissim.Net.SignalControllers.ItemByKey(12).SGs.ItemByKey(2).SetAttValue ('ContrByCOM',True)
        Vissim.Net.SignalControllers.ItemByKey(12).SGs.ItemByKey(3).SetAttValue ('ContrByCOM',True)
        Vissim.Net.SignalControllers.ItemByKey(12).SGs.ItemByKey(4).SetAttValue ('ContrByCOM',True)
        Vissim.Net.SignalControllers.ItemByKey(12).SGs.ItemByKey(Aseq[11][0]).SetAttValue ('SigState','GREEN')



        Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(1).SetAttValue ('ContrByCOM',True)
        Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(2).SetAttValue ('ContrByCOM',True)
        Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(3).SetAttValue ('ContrByCOM',True)
        Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(4).SetAttValue ('ContrByCOM',True)
        Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(Aseq[10][0]).SetAttValue ('SigState','GREEN')


        Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(1).SetAttValue ('ContrByCOM',True)
        Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(2).SetAttValue ('ContrByCOM',True)
        Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(3).SetAttValue ('ContrByCOM',True)
        Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(4).SetAttValue ('ContrByCOM',True)
        Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(Aseq[9][0]).SetAttValue ('SigState','GREEN')


        Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(1).SetAttValue ('ContrByCOM',True)
        Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(2).SetAttValue ('ContrByCOM',True)
        Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(3).SetAttValue ('ContrByCOM',True)
        Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(4).SetAttValue ('ContrByCOM',True)
        Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(Aseq[8][0]).SetAttValue ('SigState','GREEN')

        Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(1).SetAttValue ('ContrByCOM',True)
        Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(2).SetAttValue ('ContrByCOM',True)
        Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(3).SetAttValue ('ContrByCOM',True)
        Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(4).SetAttValue ('ContrByCOM',True)
        Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(Aseq[7][0]).SetAttValue ('SigState','GREEN')

        Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(1).SetAttValue ('ContrByCOM',True)
        Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(2).SetAttValue ('ContrByCOM',True)
        Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(3).SetAttValue ('ContrByCOM',True)
        Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(4).SetAttValue ('ContrByCOM',True)
        Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(Aseq[6][0]).SetAttValue ('SigState','GREEN')

        Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(1).SetAttValue ('ContrByCOM',True)
        Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(2).SetAttValue ('ContrByCOM',True)
        Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(3).SetAttValue ('ContrByCOM',True)
        Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(4).SetAttValue ('ContrByCOM',True)
        Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(Aseq[5][0]).SetAttValue ('SigState','GREEN')


        Vissim.Net.SignalControllers.ItemByKey(5).SGs.ItemByKey(1).SetAttValue ('ContrByCOM',True)
        Vissim.Net.SignalControllers.ItemByKey(5).SGs.ItemByKey(2).SetAttValue ('ContrByCOM',True)
        Vissim.Net.SignalControllers.ItemByKey(5).SGs.ItemByKey(3).SetAttValue ('ContrByCOM',True)
        Vissim.Net.SignalControllers.ItemByKey(5).SGs.ItemByKey(4).SetAttValue ('ContrByCOM',True)
        Vissim.Net.SignalControllers.ItemByKey(5).SGs.ItemByKey(Aseq[4][0]).SetAttValue ('SigState','GREEN')


        Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(1).SetAttValue ('ContrByCOM',True)
        Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(2).SetAttValue ('ContrByCOM',True)
        Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(3).SetAttValue ('ContrByCOM',True)
        Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(4).SetAttValue ('ContrByCOM',True)
        Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(Aseq[3][0]).SetAttValue ('SigState','GREEN')

        Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(1).SetAttValue ('ContrByCOM',True)
        Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(2).SetAttValue ('ContrByCOM',True)
        Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(3).SetAttValue ('ContrByCOM',True)
        Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(4).SetAttValue ('ContrByCOM',True)
        Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(Aseq[2][0]).SetAttValue ('SigState','GREEN')


        Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(1).SetAttValue ('ContrByCOM',True)
        Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(2).SetAttValue ('ContrByCOM',True)
        Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(3).SetAttValue ('ContrByCOM',True)
        Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(4).SetAttValue ('ContrByCOM',True)
        Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(Aseq[1][0]).SetAttValue ('SigState','GREEN')


        Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).SetAttValue ('ContrByCOM',True)
        Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(2).SetAttValue ('ContrByCOM',True)
        Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(3).SetAttValue ('ContrByCOM',True)
        Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(4).SetAttValue ('ContrByCOM',True)
        Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(Aseq[0][0]).SetAttValue ('SigState','GREEN')




        Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(Aseq[0][0]).SetAttValue ('GreenStart',2)
        Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(Aseq[0][0]).SetAttValue ('GreenEnd',Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(Aseq[0][0]).AttValue ('GreenStart')+Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(Aseq[0][0]).AttValue ('GreenTimeDuration'))
        Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(Aseq[0][1]).SetAttValue ('GreenStart',Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(Aseq[0][0]).AttValue ('GreenEnd')+3)
        Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(Aseq[0][2]).SetAttValue ('GreenStart',Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(Aseq[0][0]).AttValue ('GreenEnd')+3)
        Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(Aseq[0][3]).SetAttValue ('GreenStart',Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(Aseq[0][0]).AttValue ('GreenEnd')+3)
        Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(Aseq[0][1]).SetAttValue ('GreenEnd', CLength-1)
        Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(Aseq[0][2]).SetAttValue ('GreenEnd', CLength-1)
        Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(Aseq[0][3]).SetAttValue ('GreenEnd', CLength-1)



        Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(Aseq[1][0]).SetAttValue ('GreenStart',2)
        Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(Aseq[1][0]).SetAttValue ('GreenEnd',Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(Aseq[1][0]).AttValue ('GreenStart')+Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(Aseq[1][0]).AttValue ('GreenTimeDuration'))
        Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(Aseq[1][1]).SetAttValue ('GreenStart',Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(Aseq[1][0]).AttValue ('GreenEnd')+3)
        Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(Aseq[1][1]).SetAttValue ('GreenEnd', Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(Aseq[1][1]).AttValue ('GreenStart')+Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(Aseq[1][1]).AttValue ('GreenTimeDuration'))
        Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(Aseq[1][2]).SetAttValue ('GreenStart',Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(Aseq[1][1]).AttValue ('GreenEnd')+3)
        Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(Aseq[1][2]).SetAttValue ('GreenEnd', Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(Aseq[1][2]).AttValue ('GreenStart')+Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(Aseq[1][2]).AttValue ('GreenTimeDuration'))
        Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(Aseq[1][3]).SetAttValue ('GreenStart',Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(Aseq[1][2]).AttValue ('GreenEnd')+3)
        Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(Aseq[1][3]).SetAttValue ('GreenEnd', CLength-1)


        Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(Aseq[2][0]).SetAttValue ('GreenStart',2)
        Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(Aseq[2][0]).SetAttValue ('GreenEnd',Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(Aseq[2][0]).AttValue ('GreenStart')+Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(Aseq[2][0]).AttValue ('GreenTimeDuration'))
        Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(Aseq[2][1]).SetAttValue ('GreenStart',Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(Aseq[2][0]).AttValue ('GreenEnd')+3)
        Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(Aseq[2][1]).SetAttValue ('GreenEnd', Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(Aseq[2][1]).AttValue ('GreenStart')+Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(Aseq[2][1]).AttValue ('GreenTimeDuration'))
        Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(Aseq[2][2]).SetAttValue ('GreenStart',Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(Aseq[2][1]).AttValue ('GreenEnd')+3)
        Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(Aseq[2][2]).SetAttValue ('GreenEnd', Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(Aseq[2][2]).AttValue ('GreenStart')+Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(Aseq[2][2]).AttValue ('GreenTimeDuration'))
        Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(Aseq[2][3]).SetAttValue ('GreenStart',Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(Aseq[2][2]).AttValue ('GreenEnd')+3)
        Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(Aseq[2][3]).SetAttValue ('GreenEnd', CLength-1)


        Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(Aseq[3][0]).SetAttValue ('GreenStart',2)
        Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(Aseq[3][0]).SetAttValue ('GreenEnd',Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(Aseq[3][0]).AttValue ('GreenStart')+Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(Aseq[3][0]).AttValue ('GreenTimeDuration'))
        Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(Aseq[3][1]).SetAttValue ('GreenStart',Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(Aseq[3][0]).AttValue ('GreenEnd')+3)
        Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(Aseq[3][1]).SetAttValue ('GreenEnd', Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(Aseq[3][1]).AttValue ('GreenStart')+Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(Aseq[3][1]).AttValue ('GreenTimeDuration'))
        Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(Aseq[3][2]).SetAttValue ('GreenStart',Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(Aseq[3][1]).AttValue ('GreenEnd')+3)
        Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(Aseq[3][2]).SetAttValue ('GreenEnd', Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(Aseq[3][2]).AttValue ('GreenStart')+Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(Aseq[3][2]).AttValue ('GreenTimeDuration'))
        Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(Aseq[3][3]).SetAttValue ('GreenStart',Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(Aseq[3][2]).AttValue ('GreenEnd')+3)
        Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(Aseq[3][3]).SetAttValue ('GreenEnd', CLength-1)





        Vissim.Net.SignalControllers.ItemByKey(5).SGs.ItemByKey(Aseq[4][0]).SetAttValue ('GreenStart',2)
        Vissim.Net.SignalControllers.ItemByKey(5).SGs.ItemByKey(Aseq[4][0]).SetAttValue ('GreenEnd',Vissim.Net.SignalControllers.ItemByKey(5).SGs.ItemByKey(Aseq[4][0]).AttValue ('GreenStart')+Vissim.Net.SignalControllers.ItemByKey(5).SGs.ItemByKey(Aseq[4][0]).AttValue ('GreenTimeDuration'))
        Vissim.Net.SignalControllers.ItemByKey(5).SGs.ItemByKey(Aseq[4][1]).SetAttValue ('GreenStart',Vissim.Net.SignalControllers.ItemByKey(5).SGs.ItemByKey(Aseq[4][0]).AttValue ('GreenEnd')+3)
        Vissim.Net.SignalControllers.ItemByKey(5).SGs.ItemByKey(Aseq[4][2]).SetAttValue ('GreenStart',Vissim.Net.SignalControllers.ItemByKey(5).SGs.ItemByKey(Aseq[4][0]).AttValue ('GreenEnd')+3)
        Vissim.Net.SignalControllers.ItemByKey(5).SGs.ItemByKey(Aseq[4][3]).SetAttValue ('GreenStart',Vissim.Net.SignalControllers.ItemByKey(5).SGs.ItemByKey(Aseq[4][0]).AttValue ('GreenEnd')+3)
        Vissim.Net.SignalControllers.ItemByKey(5).SGs.ItemByKey(Aseq[4][1]).SetAttValue ('GreenEnd', CLength-1)
        Vissim.Net.SignalControllers.ItemByKey(5).SGs.ItemByKey(Aseq[4][2]).SetAttValue ('GreenEnd', CLength-1)
        Vissim.Net.SignalControllers.ItemByKey(5).SGs.ItemByKey(Aseq[4][3]).SetAttValue ('GreenEnd', CLength-1)




        Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(Aseq[5][0]).SetAttValue ('GreenStart',2)
        Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(Aseq[5][0]).SetAttValue ('GreenEnd',Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(Aseq[5][0]).AttValue ('GreenStart')+Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(Aseq[5][0]).AttValue ('GreenTimeDuration'))
        Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(Aseq[5][1]).SetAttValue ('GreenStart',Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(Aseq[5][0]).AttValue ('GreenEnd')+3)
        Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(Aseq[5][1]).SetAttValue ('GreenEnd', Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(Aseq[5][1]).AttValue ('GreenStart')+Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(Aseq[5][1]).AttValue ('GreenTimeDuration'))
        Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(Aseq[5][2]).SetAttValue ('GreenStart',Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(Aseq[5][1]).AttValue ('GreenEnd')+3)
        Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(Aseq[5][2]).SetAttValue ('GreenEnd', Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(Aseq[5][2]).AttValue ('GreenStart')+Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(Aseq[5][2]).AttValue ('GreenTimeDuration'))
        Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(Aseq[5][3]).SetAttValue ('GreenStart',Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(Aseq[5][2]).AttValue ('GreenEnd')+3)
        Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(Aseq[5][3]).SetAttValue ('GreenEnd', CLength-1)




        Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(Aseq[6][0]).SetAttValue ('GreenStart',2)
        Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(Aseq[6][0]).SetAttValue ('GreenEnd',Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(Aseq[6][0]).AttValue ('GreenStart')+Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(Aseq[6][0]).AttValue ('GreenTimeDuration'))
        Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(Aseq[6][1]).SetAttValue ('GreenStart',Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(Aseq[6][0]).AttValue ('GreenEnd')+3)
        Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(Aseq[6][1]).SetAttValue ('GreenEnd', Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(Aseq[6][1]).AttValue ('GreenStart')+Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(Aseq[6][1]).AttValue ('GreenTimeDuration'))
        Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(Aseq[6][2]).SetAttValue ('GreenStart',Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(Aseq[6][1]).AttValue ('GreenEnd')+3)
        Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(Aseq[6][2]).SetAttValue ('GreenEnd', Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(Aseq[6][2]).AttValue ('GreenStart')+Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(Aseq[6][2]).AttValue ('GreenTimeDuration'))
        Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(Aseq[6][3]).SetAttValue ('GreenStart',Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(Aseq[6][2]).AttValue ('GreenEnd')+3)
        Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(Aseq[6][3]).SetAttValue ('GreenEnd', CLength-1)



        Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(Aseq[7][0]).SetAttValue ('GreenStart',2)
        Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(Aseq[7][0]).SetAttValue ('GreenEnd',Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(Aseq[7][0]).AttValue ('GreenStart')+Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(Aseq[7][0]).AttValue ('GreenTimeDuration'))
        Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(Aseq[7][1]).SetAttValue ('GreenStart',Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(Aseq[7][0]).AttValue ('GreenEnd')+3)
        Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(Aseq[7][1]).SetAttValue ('GreenEnd', Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(Aseq[7][1]).AttValue ('GreenStart')+Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(Aseq[7][1]).AttValue ('GreenTimeDuration'))
        Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(Aseq[7][2]).SetAttValue ('GreenStart',Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(Aseq[7][1]).AttValue ('GreenEnd')+3)
        Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(Aseq[7][2]).SetAttValue ('GreenEnd', Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(Aseq[7][2]).AttValue ('GreenStart')+Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(Aseq[7][2]).AttValue ('GreenTimeDuration'))
        Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(Aseq[7][3]).SetAttValue ('GreenStart',Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(Aseq[7][2]).AttValue ('GreenEnd')+3)
        Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(Aseq[7][3]).SetAttValue ('GreenEnd', CLength-1)




        Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(Aseq[8][0]).SetAttValue ('GreenStart',2)
        Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(Aseq[8][0]).SetAttValue ('GreenEnd',Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(Aseq[8][0]).AttValue ('GreenStart')+Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(Aseq[8][0]).AttValue ('GreenTimeDuration'))
        Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(Aseq[8][1]).SetAttValue ('GreenStart',Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(Aseq[8][0]).AttValue ('GreenEnd')+3)
        Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(Aseq[8][1]).SetAttValue ('GreenEnd', Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(Aseq[8][1]).AttValue ('GreenStart')+Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(Aseq[8][1]).AttValue ('GreenTimeDuration'))
        Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(Aseq[8][2]).SetAttValue ('GreenStart',Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(Aseq[8][1]).AttValue ('GreenEnd')+3)
        Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(Aseq[8][2]).SetAttValue ('GreenEnd', Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(Aseq[8][2]).AttValue ('GreenStart')+Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(Aseq[8][2]).AttValue ('GreenTimeDuration'))
        Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(Aseq[8][3]).SetAttValue ('GreenStart',Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(Aseq[8][2]).AttValue ('GreenEnd')+3)
        Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(Aseq[8][3]).SetAttValue ('GreenEnd', CLength-1)



        Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(Aseq[9][0]).SetAttValue ('GreenStart',2)
        Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(Aseq[9][0]).SetAttValue ('GreenEnd',Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(Aseq[9][0]).AttValue ('GreenStart')+Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(Aseq[9][0]).AttValue ('GreenTimeDuration'))
        Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(Aseq[9][1]).SetAttValue ('GreenStart',Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(Aseq[9][0]).AttValue ('GreenEnd')+3)
        Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(Aseq[9][1]).SetAttValue ('GreenEnd', Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(Aseq[9][1]).AttValue ('GreenStart')+Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(Aseq[9][1]).AttValue ('GreenTimeDuration'))
        Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(Aseq[9][2]).SetAttValue ('GreenStart',Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(Aseq[9][1]).AttValue ('GreenEnd')+3)
        Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(Aseq[9][2]).SetAttValue ('GreenEnd', Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(Aseq[9][2]).AttValue ('GreenStart')+Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(Aseq[9][2]).AttValue ('GreenTimeDuration'))
        Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(Aseq[9][3]).SetAttValue ('GreenStart',Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(Aseq[9][2]).AttValue ('GreenEnd')+3)
        Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(Aseq[9][3]).SetAttValue ('GreenEnd', CLength-1)





        Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(Aseq[10][0]).SetAttValue ('GreenStart',2)
        Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(Aseq[10][0]).SetAttValue ('GreenEnd',Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(Aseq[10][0]).AttValue ('GreenStart')+Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(Aseq[10][0]).AttValue ('GreenTimeDuration'))
        Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(Aseq[10][1]).SetAttValue ('GreenStart',Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(Aseq[10][0]).AttValue ('GreenEnd')+3)
        Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(Aseq[10][1]).SetAttValue ('GreenEnd', Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(Aseq[10][1]).AttValue ('GreenStart')+Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(Aseq[10][1]).AttValue ('GreenTimeDuration'))
        Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(Aseq[10][2]).SetAttValue ('GreenStart',Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(Aseq[10][1]).AttValue ('GreenEnd')+3)
        Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(Aseq[10][2]).SetAttValue ('GreenEnd', Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(Aseq[10][2]).AttValue ('GreenStart')+Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(Aseq[10][2]).AttValue ('GreenTimeDuration'))
        Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(Aseq[10][3]).SetAttValue ('GreenStart',Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(Aseq[10][2]).AttValue ('GreenEnd')+3)
        Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(Aseq[10][3]).SetAttValue ('GreenEnd', CLength-1)




        Vissim.Net.SignalControllers.ItemByKey(12).SGs.ItemByKey(Aseq[11][0]).SetAttValue ('GreenStart',2)
        Vissim.Net.SignalControllers.ItemByKey(12).SGs.ItemByKey(Aseq[11][0]).SetAttValue ('GreenEnd',Vissim.Net.SignalControllers.ItemByKey(12).SGs.ItemByKey(Aseq[11][0]).AttValue ('GreenStart')+Vissim.Net.SignalControllers.ItemByKey(12).SGs.ItemByKey(Aseq[11][0]).AttValue ('GreenTimeDuration'))
        Vissim.Net.SignalControllers.ItemByKey(12).SGs.ItemByKey(Aseq[11][1]).SetAttValue ('GreenStart',Vissim.Net.SignalControllers.ItemByKey(12).SGs.ItemByKey(Aseq[11][0]).AttValue ('GreenEnd')+3)
        Vissim.Net.SignalControllers.ItemByKey(12).SGs.ItemByKey(Aseq[11][2]).SetAttValue ('GreenStart',Vissim.Net.SignalControllers.ItemByKey(12).SGs.ItemByKey(Aseq[11][0]).AttValue ('GreenEnd')+3)
        Vissim.Net.SignalControllers.ItemByKey(12).SGs.ItemByKey(Aseq[11][3]).SetAttValue ('GreenStart',Vissim.Net.SignalControllers.ItemByKey(12).SGs.ItemByKey(Aseq[11][0]).AttValue ('GreenEnd')+3)
        Vissim.Net.SignalControllers.ItemByKey(12).SGs.ItemByKey(Aseq[11][1]).SetAttValue ('GreenEnd', CLength-1)
        Vissim.Net.SignalControllers.ItemByKey(12).SGs.ItemByKey(Aseq[11][2]).SetAttValue ('GreenEnd', CLength-1)
        Vissim.Net.SignalControllers.ItemByKey(12).SGs.ItemByKey(Aseq[11][3]).SetAttValue ('GreenEnd', CLength-1)


        Vissim.Net.SignalControllers.ItemByKey(13).SGs.ItemByKey(Aseq[12][0]).SetAttValue ('GreenStart',2)
        Vissim.Net.SignalControllers.ItemByKey(13).SGs.ItemByKey(Aseq[12][0]).SetAttValue ('GreenEnd',Vissim.Net.SignalControllers.ItemByKey(13).SGs.ItemByKey(Aseq[12][0]).AttValue ('GreenStart')+Vissim.Net.SignalControllers.ItemByKey(13).SGs.ItemByKey(Aseq[12][0]).AttValue ('GreenTimeDuration'))
        Vissim.Net.SignalControllers.ItemByKey(13).SGs.ItemByKey(Aseq[12][1]).SetAttValue ('GreenStart',Vissim.Net.SignalControllers.ItemByKey(13).SGs.ItemByKey(Aseq[12][0]).AttValue ('GreenEnd')+3)
        Vissim.Net.SignalControllers.ItemByKey(13).SGs.ItemByKey(Aseq[12][2]).SetAttValue ('GreenStart',Vissim.Net.SignalControllers.ItemByKey(13).SGs.ItemByKey(Aseq[12][0]).AttValue ('GreenEnd')+3)
        Vissim.Net.SignalControllers.ItemByKey(13).SGs.ItemByKey(Aseq[12][3]).SetAttValue ('GreenStart',Vissim.Net.SignalControllers.ItemByKey(13).SGs.ItemByKey(Aseq[12][0]).AttValue ('GreenEnd')+3)
        Vissim.Net.SignalControllers.ItemByKey(13).SGs.ItemByKey(Aseq[12][1]).SetAttValue ('GreenEnd', CLength-1)
        Vissim.Net.SignalControllers.ItemByKey(13).SGs.ItemByKey(Aseq[12][2]).SetAttValue ('GreenEnd', CLength-1)
        Vissim.Net.SignalControllers.ItemByKey(13).SGs.ItemByKey(Aseq[12][3]).SetAttValue ('GreenEnd', CLength-1)






    if Seconds>=1:
               
                if  Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(Aseq[10][0]).AttValue ('SigState') == 'GREEN':
                    Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(Aseq[10][1]).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(Aseq[10][2]).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(Aseq[10][3]).SetAttValue ('SigState','RED')
                    if Seconds >= Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(Aseq[10][0]).AttValue ('GreenEnd')-1:
                        if Seconds < Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(Aseq[10][0]).AttValue ('GreenEnd')+2:
                            Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(Aseq[10][1]).SetAttValue ('SigState','RED')
                            Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(Aseq[10][0]).SetAttValue ('SigState','RED')
                            Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(Aseq[10][2]).SetAttValue ('SigState','RED')
                            Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(Aseq[10][3]).SetAttValue ('SigState','RED')


                if Seconds >= Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(Aseq[10][1]).AttValue ('GreenStart')-1:
                    if Seconds <= Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(Aseq[10][1]).AttValue ('GreenEnd')-1:
                            Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(Aseq[10][1]).SetAttValue ('SigState','GREEN')
                            Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(Aseq[10][0]).SetAttValue ('SigState','RED')
                            Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(Aseq[10][2]).SetAttValue ('SigState','RED')
                            Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(Aseq[10][3]).SetAttValue ('SigState','RED')


                if  Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(Aseq[10][1]).AttValue ('SigState') == 'GREEN':
                    Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(Aseq[10][0]).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(Aseq[10][2]).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(Aseq[10][3]).SetAttValue ('SigState','RED')             
                    if Seconds >= Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(Aseq[10][1]).AttValue ('GreenEnd')-1:
                        if Seconds < Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(Aseq[10][1]).AttValue ('GreenEnd')+2:                 
                            Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(Aseq[10][2]).SetAttValue ('SigState','RED')
                            Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(Aseq[10][0]).SetAttValue ('SigState','RED')
                            Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(Aseq[10][1]).SetAttValue ('SigState','RED')
                            Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(Aseq[10][3]).SetAttValue ('SigState','RED')


                if Seconds >= Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(Aseq[10][2]).AttValue ('GreenStart')-1:
                    if Seconds <= Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(Aseq[10][2]).AttValue ('GreenEnd')-1:
                            Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(Aseq[10][2]).SetAttValue ('SigState','GREEN')
                            Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(Aseq[10][0]).SetAttValue ('SigState','RED')
                            Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(Aseq[10][1]).SetAttValue ('SigState','RED')
                            Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(Aseq[10][3]).SetAttValue ('SigState','RED')


                if  Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(Aseq[10][2]).AttValue ('SigState') == 'GREEN':
                    Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(Aseq[10][0]).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(Aseq[10][1]).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(Aseq[10][3]).SetAttValue ('SigState','RED') 
                    if Seconds >= Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(Aseq[10][2]).AttValue ('GreenEnd')-1:
                        if Seconds < Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(Aseq[10][2]).AttValue ('GreenEnd')+2:             
                            Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(Aseq[10][3]).SetAttValue ('SigState','RED')
                            Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(Aseq[10][0]).SetAttValue ('SigState','RED')
                            Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(Aseq[10][1]).SetAttValue ('SigState','RED')
                            Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(Aseq[10][2]).SetAttValue ('SigState','RED')


                if Seconds >= Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(Aseq[10][3]).AttValue ('GreenStart')-1:
                    if Seconds <= Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(Aseq[10][3]).AttValue ('GreenEnd')-1:
                            Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(Aseq[10][3]).SetAttValue ('SigState','GREEN')
                            Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(Aseq[10][0]).SetAttValue ('SigState','RED')
                            Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(Aseq[10][1]).SetAttValue ('SigState','RED')
                            Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(Aseq[10][2]).SetAttValue ('SigState','RED')


                if  Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(Aseq[10][3]).AttValue ('SigState') == 'GREEN':
                    Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(Aseq[10][0]).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(Aseq[10][1]).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(Aseq[10][2]).SetAttValue ('SigState','RED')
                    if Seconds >= Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(Aseq[10][3]).AttValue ('GreenEnd')-1:             
                            Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(Aseq[10][0]).SetAttValue ('SigState','RED')
                            Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(Aseq[10][1]).SetAttValue ('SigState','RED')
                            Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(Aseq[10][2]).SetAttValue ('SigState','RED')
                            Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(Aseq[10][3]).SetAttValue ('SigState','RED')


                if  Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(Aseq[9][0]).AttValue ('SigState') == 'GREEN':
                    Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(Aseq[9][1]).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(Aseq[9][2]).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(Aseq[9][3]).SetAttValue ('SigState','RED')
                    if Seconds >= Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(Aseq[9][0]).AttValue ('GreenEnd')-1:
                        if Seconds < Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(Aseq[9][0]).AttValue ('GreenEnd')+2:
                            Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(Aseq[9][1]).SetAttValue ('SigState','RED')
                            Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(Aseq[9][0]).SetAttValue ('SigState','RED')
                            Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(Aseq[9][2]).SetAttValue ('SigState','RED')
                            Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(Aseq[9][3]).SetAttValue ('SigState','RED')


                if Seconds >= Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(Aseq[9][1]).AttValue ('GreenStart')-1:
                    if Seconds <= Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(Aseq[9][1]).AttValue ('GreenEnd')-1:
                            Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(Aseq[9][1]).SetAttValue ('SigState','GREEN')
                            Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(Aseq[9][0]).SetAttValue ('SigState','RED')
                            Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(Aseq[9][2]).SetAttValue ('SigState','RED')
                            Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(Aseq[9][3]).SetAttValue ('SigState','RED')


                if  Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(Aseq[9][1]).AttValue ('SigState') == 'GREEN':
                    Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(Aseq[9][0]).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(Aseq[9][2]).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(Aseq[9][3]).SetAttValue ('SigState','RED')             
                    if Seconds >= Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(Aseq[9][1]).AttValue ('GreenEnd')-1:
                        if Seconds < Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(Aseq[9][1]).AttValue ('GreenEnd')+2:                 
                            Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(Aseq[9][2]).SetAttValue ('SigState','RED')
                            Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(Aseq[9][0]).SetAttValue ('SigState','RED')
                            Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(Aseq[9][1]).SetAttValue ('SigState','RED')
                            Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(Aseq[9][3]).SetAttValue ('SigState','RED')


                if Seconds >= Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(Aseq[9][2]).AttValue ('GreenStart')-1:
                    if Seconds <= Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(Aseq[9][2]).AttValue ('GreenEnd')-1:
                            Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(Aseq[9][2]).SetAttValue ('SigState','GREEN')
                            Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(Aseq[9][0]).SetAttValue ('SigState','RED')
                            Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(Aseq[9][1]).SetAttValue ('SigState','RED')
                            Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(Aseq[9][3]).SetAttValue ('SigState','RED')


                if  Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(Aseq[9][2]).AttValue ('SigState') == 'GREEN':
                    Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(Aseq[9][0]).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(Aseq[9][1]).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(Aseq[9][3]).SetAttValue ('SigState','RED') 
                    if Seconds >= Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(Aseq[9][2]).AttValue ('GreenEnd')-1:
                        if Seconds < Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(Aseq[9][2]).AttValue ('GreenEnd')+2:             
                            Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(Aseq[9][3]).SetAttValue ('SigState','RED')
                            Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(Aseq[9][0]).SetAttValue ('SigState','RED')
                            Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(Aseq[9][1]).SetAttValue ('SigState','RED')
                            Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(Aseq[9][2]).SetAttValue ('SigState','RED')


                if Seconds >= Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(Aseq[9][3]).AttValue ('GreenStart')-1:
                    if Seconds <= Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(Aseq[9][3]).AttValue ('GreenEnd')-1:
                            Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(Aseq[9][3]).SetAttValue ('SigState','GREEN')
                            Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(Aseq[9][0]).SetAttValue ('SigState','RED')
                            Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(Aseq[9][1]).SetAttValue ('SigState','RED')
                            Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(Aseq[9][2]).SetAttValue ('SigState','RED')


                if  Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(Aseq[9][3]).AttValue ('SigState') == 'GREEN':
                    Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(Aseq[9][0]).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(Aseq[9][1]).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(Aseq[9][2]).SetAttValue ('SigState','RED')
                    if Seconds >= Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(Aseq[9][3]).AttValue ('GreenEnd')-1:             
                            Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(Aseq[9][0]).SetAttValue ('SigState','RED')
                            Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(Aseq[9][1]).SetAttValue ('SigState','RED')
                            Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(Aseq[9][2]).SetAttValue ('SigState','RED')
                            Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(Aseq[9][3]).SetAttValue ('SigState','RED')






                if  Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(Aseq[8][0]).AttValue ('SigState') == 'GREEN':
                    Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(Aseq[8][1]).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(Aseq[8][2]).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(Aseq[8][3]).SetAttValue ('SigState','RED')
                    if Seconds >= Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(Aseq[8][0]).AttValue ('GreenEnd')-1:
                        if Seconds < Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(Aseq[8][0]).AttValue ('GreenEnd')+2:
                            Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(Aseq[8][1]).SetAttValue ('SigState','RED')
                            Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(Aseq[8][0]).SetAttValue ('SigState','RED')
                            Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(Aseq[8][2]).SetAttValue ('SigState','RED')
                            Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(Aseq[8][3]).SetAttValue ('SigState','RED')


                if Seconds >= Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(Aseq[8][1]).AttValue ('GreenStart')-1:
                    if Seconds <= Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(Aseq[8][1]).AttValue ('GreenEnd')-1:
                            Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(Aseq[8][1]).SetAttValue ('SigState','GREEN')
                            Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(Aseq[8][0]).SetAttValue ('SigState','RED')
                            Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(Aseq[8][2]).SetAttValue ('SigState','RED')
                            Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(Aseq[8][3]).SetAttValue ('SigState','RED')


                if  Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(Aseq[8][1]).AttValue ('SigState') == 'GREEN':
                    Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(Aseq[8][0]).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(Aseq[8][2]).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(Aseq[8][3]).SetAttValue ('SigState','RED')             
                    if Seconds >= Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(Aseq[8][1]).AttValue ('GreenEnd')-1:
                        if Seconds < Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(Aseq[8][1]).AttValue ('GreenEnd')+2:                 
                            Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(Aseq[8][2]).SetAttValue ('SigState','RED')
                            Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(Aseq[8][0]).SetAttValue ('SigState','RED')
                            Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(Aseq[8][1]).SetAttValue ('SigState','RED')
                            Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(Aseq[8][3]).SetAttValue ('SigState','RED')


                if Seconds >= Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(Aseq[8][2]).AttValue ('GreenStart')-1:
                    if Seconds <= Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(Aseq[8][2]).AttValue ('GreenEnd')-1:
                            Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(Aseq[8][2]).SetAttValue ('SigState','GREEN')
                            Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(Aseq[8][0]).SetAttValue ('SigState','RED')
                            Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(Aseq[8][1]).SetAttValue ('SigState','RED')
                            Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(Aseq[8][3]).SetAttValue ('SigState','RED')


                if  Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(Aseq[8][2]).AttValue ('SigState') == 'GREEN':
                    Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(Aseq[8][0]).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(Aseq[8][1]).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(Aseq[8][3]).SetAttValue ('SigState','RED') 
                    if Seconds >= Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(Aseq[8][2]).AttValue ('GreenEnd')-1:
                        if Seconds < Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(Aseq[8][2]).AttValue ('GreenEnd')+2:             
                            Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(Aseq[8][3]).SetAttValue ('SigState','RED')
                            Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(Aseq[8][0]).SetAttValue ('SigState','RED')
                            Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(Aseq[8][1]).SetAttValue ('SigState','RED')
                            Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(Aseq[8][2]).SetAttValue ('SigState','RED')


                if Seconds >= Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(Aseq[8][3]).AttValue ('GreenStart')-1:
                    if Seconds <= Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(Aseq[8][3]).AttValue ('GreenEnd')-1:
                            Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(Aseq[8][3]).SetAttValue ('SigState','GREEN')
                            Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(Aseq[8][0]).SetAttValue ('SigState','RED')
                            Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(Aseq[8][1]).SetAttValue ('SigState','RED')
                            Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(Aseq[8][2]).SetAttValue ('SigState','RED')


                if  Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(Aseq[8][3]).AttValue ('SigState') == 'GREEN':
                    Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(Aseq[8][0]).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(Aseq[8][1]).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(Aseq[8][2]).SetAttValue ('SigState','RED')
                    if Seconds >= Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(Aseq[8][3]).AttValue ('GreenEnd')-1:             
                            Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(Aseq[8][0]).SetAttValue ('SigState','RED')
                            Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(Aseq[8][1]).SetAttValue ('SigState','RED')
                            Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(Aseq[8][2]).SetAttValue ('SigState','RED')
                            Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(Aseq[8][3]).SetAttValue ('SigState','RED')







                if  Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(Aseq[7][0]).AttValue ('SigState') == 'GREEN':
                    Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(Aseq[7][1]).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(Aseq[7][2]).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(Aseq[7][3]).SetAttValue ('SigState','RED')
                    if Seconds >= Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(Aseq[7][0]).AttValue ('GreenEnd')-1:
                        if Seconds < Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(Aseq[7][0]).AttValue ('GreenEnd')+2:
                            Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(Aseq[7][1]).SetAttValue ('SigState','RED')
                            Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(Aseq[7][0]).SetAttValue ('SigState','RED')
                            Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(Aseq[7][2]).SetAttValue ('SigState','RED')
                            Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(Aseq[7][3]).SetAttValue ('SigState','RED')


                if Seconds >= Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(Aseq[7][1]).AttValue ('GreenStart')-1:
                    if Seconds <= Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(Aseq[7][1]).AttValue ('GreenEnd')-1:
                            Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(Aseq[7][1]).SetAttValue ('SigState','GREEN')
                            Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(Aseq[7][0]).SetAttValue ('SigState','RED')
                            Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(Aseq[7][2]).SetAttValue ('SigState','RED')
                            Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(Aseq[7][3]).SetAttValue ('SigState','RED')


                if  Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(Aseq[7][1]).AttValue ('SigState') == 'GREEN':
                    Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(Aseq[7][0]).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(Aseq[7][2]).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(Aseq[7][3]).SetAttValue ('SigState','RED')             
                    if Seconds >= Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(Aseq[7][1]).AttValue ('GreenEnd')-1:
                        if Seconds < Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(Aseq[7][1]).AttValue ('GreenEnd')+2:                 
                            Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(Aseq[7][2]).SetAttValue ('SigState','RED')
                            Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(Aseq[7][0]).SetAttValue ('SigState','RED')
                            Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(Aseq[7][1]).SetAttValue ('SigState','RED')
                            Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(Aseq[7][3]).SetAttValue ('SigState','RED')


                if Seconds >= Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(Aseq[7][2]).AttValue ('GreenStart')-1:
                    if Seconds <= Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(Aseq[7][2]).AttValue ('GreenEnd')-1:
                            Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(Aseq[7][2]).SetAttValue ('SigState','GREEN')
                            Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(Aseq[7][0]).SetAttValue ('SigState','RED')
                            Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(Aseq[7][1]).SetAttValue ('SigState','RED')
                            Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(Aseq[7][3]).SetAttValue ('SigState','RED')


                if  Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(Aseq[7][2]).AttValue ('SigState') == 'GREEN':
                    Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(Aseq[7][0]).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(Aseq[7][1]).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(Aseq[7][3]).SetAttValue ('SigState','RED') 
                    if Seconds >= Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(Aseq[7][2]).AttValue ('GreenEnd')-1:
                        if Seconds < Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(Aseq[7][2]).AttValue ('GreenEnd')+2:             
                            Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(Aseq[7][3]).SetAttValue ('SigState','RED')
                            Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(Aseq[7][0]).SetAttValue ('SigState','RED')
                            Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(Aseq[7][1]).SetAttValue ('SigState','RED')
                            Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(Aseq[7][2]).SetAttValue ('SigState','RED')


                if Seconds >= Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(Aseq[7][3]).AttValue ('GreenStart')-1:
                    if Seconds <= Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(Aseq[7][3]).AttValue ('GreenEnd')-1:
                            Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(Aseq[7][3]).SetAttValue ('SigState','GREEN')
                            Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(Aseq[7][0]).SetAttValue ('SigState','RED')
                            Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(Aseq[7][1]).SetAttValue ('SigState','RED')
                            Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(Aseq[7][2]).SetAttValue ('SigState','RED')


                if  Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(Aseq[7][3]).AttValue ('SigState') == 'GREEN':
                    Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(Aseq[7][0]).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(Aseq[7][1]).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(Aseq[7][2]).SetAttValue ('SigState','RED')
                    if Seconds >= Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(Aseq[7][3]).AttValue ('GreenEnd')-1:             
                            Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(Aseq[7][0]).SetAttValue ('SigState','RED')
                            Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(Aseq[7][1]).SetAttValue ('SigState','RED')
                            Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(Aseq[7][2]).SetAttValue ('SigState','RED')
                            Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(Aseq[7][3]).SetAttValue ('SigState','RED')



                if  Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(Aseq[6][0]).AttValue ('SigState') == 'GREEN':
                    Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(Aseq[6][1]).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(Aseq[6][2]).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(Aseq[6][3]).SetAttValue ('SigState','RED')
                    if Seconds >= Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(Aseq[6][0]).AttValue ('GreenEnd')-1:
                        if Seconds < Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(Aseq[6][0]).AttValue ('GreenEnd')+2:
                            Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(Aseq[6][1]).SetAttValue ('SigState','RED')
                            Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(Aseq[6][0]).SetAttValue ('SigState','RED')
                            Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(Aseq[6][2]).SetAttValue ('SigState','RED')
                            Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(Aseq[6][3]).SetAttValue ('SigState','RED')


                if Seconds >= Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(Aseq[6][1]).AttValue ('GreenStart')-1:
                    if Seconds <= Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(Aseq[6][1]).AttValue ('GreenEnd')-1:
                            Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(Aseq[6][1]).SetAttValue ('SigState','GREEN')
                            Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(Aseq[6][0]).SetAttValue ('SigState','RED')
                            Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(Aseq[6][2]).SetAttValue ('SigState','RED')
                            Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(Aseq[6][3]).SetAttValue ('SigState','RED')


                if  Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(Aseq[6][1]).AttValue ('SigState') == 'GREEN':
                    Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(Aseq[6][0]).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(Aseq[6][2]).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(Aseq[6][3]).SetAttValue ('SigState','RED')             
                    if Seconds >= Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(Aseq[6][1]).AttValue ('GreenEnd')-1:
                        if Seconds < Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(Aseq[6][1]).AttValue ('GreenEnd')+2:                 
                            Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(Aseq[6][2]).SetAttValue ('SigState','RED')
                            Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(Aseq[6][0]).SetAttValue ('SigState','RED')
                            Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(Aseq[6][1]).SetAttValue ('SigState','RED')
                            Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(Aseq[6][3]).SetAttValue ('SigState','RED')


                if Seconds >= Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(Aseq[6][2]).AttValue ('GreenStart')-1:
                    if Seconds <= Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(Aseq[6][2]).AttValue ('GreenEnd')-1:
                            Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(Aseq[6][2]).SetAttValue ('SigState','GREEN')
                            Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(Aseq[6][0]).SetAttValue ('SigState','RED')
                            Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(Aseq[6][1]).SetAttValue ('SigState','RED')
                            Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(Aseq[6][3]).SetAttValue ('SigState','RED')


                if  Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(Aseq[6][2]).AttValue ('SigState') == 'GREEN':
                    Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(Aseq[6][0]).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(Aseq[6][1]).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(Aseq[6][3]).SetAttValue ('SigState','RED') 
                    if Seconds >= Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(Aseq[6][2]).AttValue ('GreenEnd')-1:
                        if Seconds < Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(Aseq[6][2]).AttValue ('GreenEnd')+2:             
                            Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(Aseq[6][3]).SetAttValue ('SigState','RED')
                            Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(Aseq[6][0]).SetAttValue ('SigState','RED')
                            Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(Aseq[6][1]).SetAttValue ('SigState','RED')
                            Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(Aseq[6][2]).SetAttValue ('SigState','RED')


                if Seconds >= Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(Aseq[6][3]).AttValue ('GreenStart')-1:
                    if Seconds <= Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(Aseq[6][3]).AttValue ('GreenEnd')-1:
                            Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(Aseq[6][3]).SetAttValue ('SigState','GREEN')
                            Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(Aseq[6][0]).SetAttValue ('SigState','RED')
                            Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(Aseq[6][1]).SetAttValue ('SigState','RED')
                            Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(Aseq[6][2]).SetAttValue ('SigState','RED')


                if  Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(Aseq[6][3]).AttValue ('SigState') == 'GREEN':
                    Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(Aseq[6][0]).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(Aseq[6][1]).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(Aseq[6][2]).SetAttValue ('SigState','RED')
                    if Seconds >= Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(Aseq[6][3]).AttValue ('GreenEnd')-1:             
                            Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(Aseq[6][0]).SetAttValue ('SigState','RED')
                            Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(Aseq[6][1]).SetAttValue ('SigState','RED')
                            Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(Aseq[6][2]).SetAttValue ('SigState','RED')
                            Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(Aseq[6][3]).SetAttValue ('SigState','RED')


                if  Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(Aseq[5][0]).AttValue ('SigState') == 'GREEN':
                    Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(Aseq[5][1]).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(Aseq[5][2]).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(Aseq[5][3]).SetAttValue ('SigState','RED')
                    if Seconds >= Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(Aseq[5][0]).AttValue ('GreenEnd')-1:
                        if Seconds < Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(Aseq[5][0]).AttValue ('GreenEnd')+2:
                            Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(Aseq[5][1]).SetAttValue ('SigState','RED')
                            Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(Aseq[5][0]).SetAttValue ('SigState','RED')
                            Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(Aseq[5][2]).SetAttValue ('SigState','RED')
                            Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(Aseq[5][3]).SetAttValue ('SigState','RED')


                if Seconds >= Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(Aseq[5][1]).AttValue ('GreenStart')-1:
                    if Seconds <= Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(Aseq[5][1]).AttValue ('GreenEnd')-1:
                            Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(Aseq[5][1]).SetAttValue ('SigState','GREEN')
                            Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(Aseq[5][0]).SetAttValue ('SigState','RED')
                            Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(Aseq[5][2]).SetAttValue ('SigState','RED')
                            Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(Aseq[5][3]).SetAttValue ('SigState','RED')


                if  Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(Aseq[5][1]).AttValue ('SigState') == 'GREEN':
                    Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(Aseq[5][0]).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(Aseq[5][2]).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(Aseq[5][3]).SetAttValue ('SigState','RED')             
                    if Seconds >= Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(Aseq[5][1]).AttValue ('GreenEnd')-1:
                        if Seconds < Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(Aseq[5][1]).AttValue ('GreenEnd')+2:                 
                            Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(Aseq[5][2]).SetAttValue ('SigState','RED')
                            Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(Aseq[5][0]).SetAttValue ('SigState','RED')
                            Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(Aseq[5][1]).SetAttValue ('SigState','RED')
                            Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(Aseq[5][3]).SetAttValue ('SigState','RED')


                if Seconds >= Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(Aseq[5][2]).AttValue ('GreenStart')-1:
                    if Seconds <= Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(Aseq[5][2]).AttValue ('GreenEnd')-1:
                            Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(Aseq[5][2]).SetAttValue ('SigState','GREEN')
                            Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(Aseq[5][0]).SetAttValue ('SigState','RED')
                            Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(Aseq[5][1]).SetAttValue ('SigState','RED')
                            Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(Aseq[5][3]).SetAttValue ('SigState','RED')


                if  Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(Aseq[5][2]).AttValue ('SigState') == 'GREEN':
                    Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(Aseq[5][0]).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(Aseq[5][1]).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(Aseq[5][3]).SetAttValue ('SigState','RED') 
                    if Seconds >= Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(Aseq[5][2]).AttValue ('GreenEnd')-1:
                        if Seconds < Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(Aseq[5][2]).AttValue ('GreenEnd')+2:             
                            Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(Aseq[5][3]).SetAttValue ('SigState','RED')
                            Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(Aseq[5][0]).SetAttValue ('SigState','RED')
                            Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(Aseq[5][1]).SetAttValue ('SigState','RED')
                            Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(Aseq[5][2]).SetAttValue ('SigState','RED')


                if Seconds >= Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(Aseq[5][3]).AttValue ('GreenStart')-1:
                    if Seconds <= Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(Aseq[5][3]).AttValue ('GreenEnd')-1:
                            Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(Aseq[5][3]).SetAttValue ('SigState','GREEN')
                            Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(Aseq[5][0]).SetAttValue ('SigState','RED')
                            Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(Aseq[5][1]).SetAttValue ('SigState','RED')
                            Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(Aseq[5][2]).SetAttValue ('SigState','RED')


                if  Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(Aseq[5][3]).AttValue ('SigState') == 'GREEN':
                    Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(Aseq[5][0]).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(Aseq[5][1]).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(Aseq[5][2]).SetAttValue ('SigState','RED')
                    if Seconds >= Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(Aseq[5][3]).AttValue ('GreenEnd')-1:             
                            Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(Aseq[5][0]).SetAttValue ('SigState','RED')
                            Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(Aseq[5][1]).SetAttValue ('SigState','RED')
                            Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(Aseq[5][2]).SetAttValue ('SigState','RED')
                            Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(Aseq[5][3]).SetAttValue ('SigState','RED')






                if  Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(Aseq[3][0]).AttValue ('SigState') == 'GREEN':
                    Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(Aseq[3][1]).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(Aseq[3][2]).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(Aseq[3][3]).SetAttValue ('SigState','RED')
                    if Seconds >= Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(Aseq[3][0]).AttValue ('GreenEnd')-1:
                        if Seconds < Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(Aseq[3][0]).AttValue ('GreenEnd')+2:
                            Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(Aseq[3][1]).SetAttValue ('SigState','RED')
                            Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(Aseq[3][0]).SetAttValue ('SigState','RED')
                            Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(Aseq[3][2]).SetAttValue ('SigState','RED')
                            Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(Aseq[3][3]).SetAttValue ('SigState','RED')


                if Seconds >= Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(Aseq[3][1]).AttValue ('GreenStart')-1:
                    if Seconds <= Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(Aseq[3][1]).AttValue ('GreenEnd')-1:
                            Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(Aseq[3][1]).SetAttValue ('SigState','GREEN')
                            Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(Aseq[3][0]).SetAttValue ('SigState','RED')
                            Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(Aseq[3][2]).SetAttValue ('SigState','RED')
                            Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(Aseq[3][3]).SetAttValue ('SigState','RED')


                if  Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(Aseq[3][1]).AttValue ('SigState') == 'GREEN':
                    Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(Aseq[3][0]).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(Aseq[3][2]).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(Aseq[3][3]).SetAttValue ('SigState','RED')             
                    if Seconds >= Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(Aseq[3][1]).AttValue ('GreenEnd')-1:
                        if Seconds < Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(Aseq[3][1]).AttValue ('GreenEnd')+2:                 
                            Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(Aseq[3][2]).SetAttValue ('SigState','RED')
                            Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(Aseq[3][0]).SetAttValue ('SigState','RED')
                            Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(Aseq[3][1]).SetAttValue ('SigState','RED')
                            Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(Aseq[3][3]).SetAttValue ('SigState','RED')


                if Seconds >= Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(Aseq[3][2]).AttValue ('GreenStart')-1:
                    if Seconds <= Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(Aseq[3][2]).AttValue ('GreenEnd')-1:
                            Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(Aseq[3][2]).SetAttValue ('SigState','GREEN')
                            Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(Aseq[3][0]).SetAttValue ('SigState','RED')
                            Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(Aseq[3][1]).SetAttValue ('SigState','RED')
                            Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(Aseq[3][3]).SetAttValue ('SigState','RED')


                if  Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(Aseq[3][2]).AttValue ('SigState') == 'GREEN':
                    Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(Aseq[3][0]).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(Aseq[3][1]).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(Aseq[3][3]).SetAttValue ('SigState','RED') 
                    if Seconds >= Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(Aseq[3][2]).AttValue ('GreenEnd')-1:
                        if Seconds < Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(Aseq[3][2]).AttValue ('GreenEnd')+2:             
                            Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(Aseq[3][3]).SetAttValue ('SigState','RED')
                            Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(Aseq[3][0]).SetAttValue ('SigState','RED')
                            Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(Aseq[3][1]).SetAttValue ('SigState','RED')
                            Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(Aseq[3][2]).SetAttValue ('SigState','RED')


                if Seconds >= Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(Aseq[3][3]).AttValue ('GreenStart')-1:
                    if Seconds <= Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(Aseq[3][3]).AttValue ('GreenEnd')-1:
                            Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(Aseq[3][3]).SetAttValue ('SigState','GREEN')
                            Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(Aseq[3][0]).SetAttValue ('SigState','RED')
                            Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(Aseq[3][1]).SetAttValue ('SigState','RED')
                            Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(Aseq[3][2]).SetAttValue ('SigState','RED')


                if  Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(Aseq[3][3]).AttValue ('SigState') == 'GREEN':
                    Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(Aseq[3][0]).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(Aseq[3][1]).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(Aseq[3][2]).SetAttValue ('SigState','RED')
                    if Seconds >= Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(Aseq[3][3]).AttValue ('GreenEnd')-1:             
                            Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(Aseq[3][0]).SetAttValue ('SigState','RED')
                            Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(Aseq[3][1]).SetAttValue ('SigState','RED')
                            Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(Aseq[3][2]).SetAttValue ('SigState','RED')
                            Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(Aseq[3][3]).SetAttValue ('SigState','RED')



                if  Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(Aseq[2][0]).AttValue ('SigState') == 'GREEN':
                    Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(Aseq[2][1]).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(Aseq[2][2]).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(Aseq[2][3]).SetAttValue ('SigState','RED')
                    if Seconds >= Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(Aseq[2][0]).AttValue ('GreenEnd')-1:
                        if Seconds < Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(Aseq[2][0]).AttValue ('GreenEnd')+2:
                            Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(Aseq[2][1]).SetAttValue ('SigState','RED')
                            Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(Aseq[2][0]).SetAttValue ('SigState','RED')
                            Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(Aseq[2][2]).SetAttValue ('SigState','RED')
                            Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(Aseq[2][3]).SetAttValue ('SigState','RED')


                if Seconds >= Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(Aseq[2][1]).AttValue ('GreenStart')-1:
                    if Seconds <= Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(Aseq[2][1]).AttValue ('GreenEnd')-1:
                            Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(Aseq[2][1]).SetAttValue ('SigState','GREEN')
                            Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(Aseq[2][0]).SetAttValue ('SigState','RED')
                            Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(Aseq[2][2]).SetAttValue ('SigState','RED')
                            Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(Aseq[2][3]).SetAttValue ('SigState','RED')


                if  Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(Aseq[2][1]).AttValue ('SigState') == 'GREEN':
                    Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(Aseq[2][0]).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(Aseq[2][2]).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(Aseq[2][3]).SetAttValue ('SigState','RED')             
                    if Seconds >= Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(Aseq[2][1]).AttValue ('GreenEnd')-1:
                        if Seconds < Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(Aseq[2][1]).AttValue ('GreenEnd')+2:                 
                            Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(Aseq[2][2]).SetAttValue ('SigState','RED')
                            Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(Aseq[2][0]).SetAttValue ('SigState','RED')
                            Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(Aseq[2][1]).SetAttValue ('SigState','RED')
                            Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(Aseq[2][3]).SetAttValue ('SigState','RED')


                if Seconds >= Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(Aseq[2][2]).AttValue ('GreenStart')-1:
                    if Seconds <= Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(Aseq[2][2]).AttValue ('GreenEnd')-1:
                            Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(Aseq[2][2]).SetAttValue ('SigState','GREEN')
                            Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(Aseq[2][0]).SetAttValue ('SigState','RED')
                            Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(Aseq[2][1]).SetAttValue ('SigState','RED')
                            Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(Aseq[2][3]).SetAttValue ('SigState','RED')


                if  Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(Aseq[2][2]).AttValue ('SigState') == 'GREEN':
                    Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(Aseq[2][0]).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(Aseq[2][1]).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(Aseq[2][3]).SetAttValue ('SigState','RED') 
                    if Seconds >= Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(Aseq[2][2]).AttValue ('GreenEnd')-1:
                        if Seconds < Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(Aseq[2][2]).AttValue ('GreenEnd')+2:             
                            Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(Aseq[2][3]).SetAttValue ('SigState','RED')
                            Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(Aseq[2][0]).SetAttValue ('SigState','RED')
                            Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(Aseq[2][1]).SetAttValue ('SigState','RED')
                            Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(Aseq[2][2]).SetAttValue ('SigState','RED')


                if Seconds >= Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(Aseq[2][3]).AttValue ('GreenStart')-1:
                    if Seconds <= Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(Aseq[2][3]).AttValue ('GreenEnd')-1:
                            Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(Aseq[2][3]).SetAttValue ('SigState','GREEN')
                            Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(Aseq[2][0]).SetAttValue ('SigState','RED')
                            Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(Aseq[2][1]).SetAttValue ('SigState','RED')
                            Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(Aseq[2][2]).SetAttValue ('SigState','RED')


                if  Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(Aseq[2][3]).AttValue ('SigState') == 'GREEN':
                    Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(Aseq[2][0]).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(Aseq[2][1]).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(Aseq[2][2]).SetAttValue ('SigState','RED')
                    if Seconds >= Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(Aseq[2][3]).AttValue ('GreenEnd')-1:             
                            Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(Aseq[2][0]).SetAttValue ('SigState','RED')
                            Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(Aseq[2][1]).SetAttValue ('SigState','RED')
                            Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(Aseq[2][2]).SetAttValue ('SigState','RED')
                            Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(Aseq[2][3]).SetAttValue ('SigState','RED')

                if  Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(Aseq[1][0]).AttValue ('SigState') == 'GREEN':
                    Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(Aseq[1][1]).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(Aseq[1][2]).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(Aseq[1][3]).SetAttValue ('SigState','RED')
                    if Seconds >= Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(Aseq[1][0]).AttValue ('GreenEnd')-1:
                        if Seconds < Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(Aseq[1][0]).AttValue ('GreenEnd')+2:
                            Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(Aseq[1][1]).SetAttValue ('SigState','RED')
                            Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(Aseq[1][0]).SetAttValue ('SigState','RED')
                            Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(Aseq[1][2]).SetAttValue ('SigState','RED')
                            Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(Aseq[1][3]).SetAttValue ('SigState','RED')


                if Seconds >= Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(Aseq[1][1]).AttValue ('GreenStart')-1:
                    if Seconds <= Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(Aseq[1][1]).AttValue ('GreenEnd')-1:
                            Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(Aseq[1][1]).SetAttValue ('SigState','GREEN')
                            Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(Aseq[1][0]).SetAttValue ('SigState','RED')
                            Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(Aseq[1][2]).SetAttValue ('SigState','RED')
                            Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(Aseq[1][3]).SetAttValue ('SigState','RED')


                if  Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(Aseq[1][1]).AttValue ('SigState') == 'GREEN':
                    Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(Aseq[1][0]).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(Aseq[1][2]).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(Aseq[1][3]).SetAttValue ('SigState','RED')             
                    if Seconds >= Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(Aseq[1][1]).AttValue ('GreenEnd')-1:
                        if Seconds < Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(Aseq[1][1]).AttValue ('GreenEnd')+2:                 
                            Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(Aseq[1][2]).SetAttValue ('SigState','RED')
                            Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(Aseq[1][0]).SetAttValue ('SigState','RED')
                            Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(Aseq[1][1]).SetAttValue ('SigState','RED')
                            Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(Aseq[1][3]).SetAttValue ('SigState','RED')


                if Seconds >= Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(Aseq[1][2]).AttValue ('GreenStart')-1:
                    if Seconds <= Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(Aseq[1][2]).AttValue ('GreenEnd')-1:
                            Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(Aseq[1][2]).SetAttValue ('SigState','GREEN')
                            Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(Aseq[1][0]).SetAttValue ('SigState','RED')
                            Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(Aseq[1][1]).SetAttValue ('SigState','RED')
                            Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(Aseq[1][3]).SetAttValue ('SigState','RED')


                if  Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(Aseq[1][2]).AttValue ('SigState') == 'GREEN':
                    Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(Aseq[1][0]).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(Aseq[1][1]).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(Aseq[1][3]).SetAttValue ('SigState','RED') 
                    if Seconds >= Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(Aseq[1][2]).AttValue ('GreenEnd')-1:
                        if Seconds < Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(Aseq[1][2]).AttValue ('GreenEnd')+2:             
                            Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(Aseq[1][3]).SetAttValue ('SigState','RED')
                            Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(Aseq[1][0]).SetAttValue ('SigState','RED')
                            Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(Aseq[1][1]).SetAttValue ('SigState','RED')
                            Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(Aseq[1][2]).SetAttValue ('SigState','RED')


                if Seconds >= Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(Aseq[1][3]).AttValue ('GreenStart')-1:
                    if Seconds <= Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(Aseq[1][3]).AttValue ('GreenEnd')-1:
                            Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(Aseq[1][3]).SetAttValue ('SigState','GREEN')
                            Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(Aseq[1][0]).SetAttValue ('SigState','RED')
                            Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(Aseq[1][1]).SetAttValue ('SigState','RED')
                            Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(Aseq[1][2]).SetAttValue ('SigState','RED')


                if  Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(Aseq[1][3]).AttValue ('SigState') == 'GREEN':
                    Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(Aseq[1][0]).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(Aseq[1][1]).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(Aseq[1][2]).SetAttValue ('SigState','RED')
                    if Seconds >= Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(Aseq[1][3]).AttValue ('GreenEnd')-1:             
                            Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(Aseq[1][0]).SetAttValue ('SigState','RED')
                            Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(Aseq[1][1]).SetAttValue ('SigState','RED')
                            Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(Aseq[1][2]).SetAttValue ('SigState','RED')
                            Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(Aseq[1][3]).SetAttValue ('SigState','RED')




                if  Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).AttValue ('SigState') == 'GREEN':
                    Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(2).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(3).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(4).SetAttValue ('SigState','RED')
                    if Seconds >= Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).AttValue ('GreenEnd')-1:
                        if Seconds < Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).AttValue ('GreenEnd')+2:
                            Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).SetAttValue ('SigState','RED')
                            Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(2).SetAttValue ('SigState','RED')
                            Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(3).SetAttValue ('SigState','RED')
                            Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(4).SetAttValue ('SigState','RED')

                if Seconds >= Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(2).AttValue ('GreenStart')-1:
                    if Seconds <= Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(2).AttValue ('GreenEnd')-1:
                            Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).SetAttValue ('SigState','RED')
                            Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(2).SetAttValue ('SigState','GREEN')
                            Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(3).SetAttValue ('SigState','GREEN')
                            Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(4).SetAttValue ('SigState','GREEN')



                if  Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(2).AttValue ('SigState') == 'GREEN':
                    Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).SetAttValue ('SigState','RED')
                    if Seconds >= Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(2).AttValue ('GreenEnd')-1:
                            Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).SetAttValue ('SigState','RED')
                            Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(2).SetAttValue ('SigState','RED')
                            Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(3).SetAttValue ('SigState','RED')
                            Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(4).SetAttValue ('SigState','RED')




                if  Vissim.Net.SignalControllers.ItemByKey(5).SGs.ItemByKey(1).AttValue ('SigState') == 'GREEN':
                    Vissim.Net.SignalControllers.ItemByKey(5).SGs.ItemByKey(2).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(5).SGs.ItemByKey(3).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(5).SGs.ItemByKey(4).SetAttValue ('SigState','RED')
                    if Seconds >= Vissim.Net.SignalControllers.ItemByKey(5).SGs.ItemByKey(1).AttValue ('GreenEnd')-1:
                        if Seconds < Vissim.Net.SignalControllers.ItemByKey(5).SGs.ItemByKey(1).AttValue ('GreenEnd')+2:
                            Vissim.Net.SignalControllers.ItemByKey(5).SGs.ItemByKey(1).SetAttValue ('SigState','RED')
                            Vissim.Net.SignalControllers.ItemByKey(5).SGs.ItemByKey(2).SetAttValue ('SigState','RED')
                            Vissim.Net.SignalControllers.ItemByKey(5).SGs.ItemByKey(3).SetAttValue ('SigState','RED')
                            Vissim.Net.SignalControllers.ItemByKey(5).SGs.ItemByKey(4).SetAttValue ('SigState','RED')

                if Seconds >= Vissim.Net.SignalControllers.ItemByKey(5).SGs.ItemByKey(2).AttValue ('GreenStart')-1:
                    if Seconds <= Vissim.Net.SignalControllers.ItemByKey(5).SGs.ItemByKey(2).AttValue ('GreenEnd')-1:
                            Vissim.Net.SignalControllers.ItemByKey(5).SGs.ItemByKey(1).SetAttValue ('SigState','RED')
                            Vissim.Net.SignalControllers.ItemByKey(5).SGs.ItemByKey(2).SetAttValue ('SigState','GREEN')
                            Vissim.Net.SignalControllers.ItemByKey(5).SGs.ItemByKey(3).SetAttValue ('SigState','GREEN')
                            Vissim.Net.SignalControllers.ItemByKey(5).SGs.ItemByKey(4).SetAttValue ('SigState','GREEN')



                if  Vissim.Net.SignalControllers.ItemByKey(5).SGs.ItemByKey(2).AttValue ('SigState') == 'GREEN':
                    Vissim.Net.SignalControllers.ItemByKey(5).SGs.ItemByKey(1).SetAttValue ('SigState','RED')
                    if Seconds >= Vissim.Net.SignalControllers.ItemByKey(5).SGs.ItemByKey(2).AttValue ('GreenEnd')-1:
                            Vissim.Net.SignalControllers.ItemByKey(5).SGs.ItemByKey(1).SetAttValue ('SigState','RED')
                            Vissim.Net.SignalControllers.ItemByKey(5).SGs.ItemByKey(2).SetAttValue ('SigState','RED')
                            Vissim.Net.SignalControllers.ItemByKey(5).SGs.ItemByKey(3).SetAttValue ('SigState','RED')
                            Vissim.Net.SignalControllers.ItemByKey(5).SGs.ItemByKey(4).SetAttValue ('SigState','RED')






                if  Vissim.Net.SignalControllers.ItemByKey(12).SGs.ItemByKey(1).AttValue ('SigState') == 'GREEN':
                    Vissim.Net.SignalControllers.ItemByKey(12).SGs.ItemByKey(2).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(12).SGs.ItemByKey(3).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(12).SGs.ItemByKey(4).SetAttValue ('SigState','RED')
                    if Seconds >= Vissim.Net.SignalControllers.ItemByKey(12).SGs.ItemByKey(1).AttValue ('GreenEnd')-1:
                        if Seconds < Vissim.Net.SignalControllers.ItemByKey(12).SGs.ItemByKey(1).AttValue ('GreenEnd')+2:
                            Vissim.Net.SignalControllers.ItemByKey(12).SGs.ItemByKey(1).SetAttValue ('SigState','RED')
                            Vissim.Net.SignalControllers.ItemByKey(12).SGs.ItemByKey(2).SetAttValue ('SigState','RED')
                            Vissim.Net.SignalControllers.ItemByKey(12).SGs.ItemByKey(3).SetAttValue ('SigState','RED')
                            Vissim.Net.SignalControllers.ItemByKey(12).SGs.ItemByKey(4).SetAttValue ('SigState','RED')

                if Seconds >= Vissim.Net.SignalControllers.ItemByKey(12).SGs.ItemByKey(2).AttValue ('GreenStart')-1:
                    if Seconds <= Vissim.Net.SignalControllers.ItemByKey(12).SGs.ItemByKey(2).AttValue ('GreenEnd')-1:
                            Vissim.Net.SignalControllers.ItemByKey(12).SGs.ItemByKey(1).SetAttValue ('SigState','RED')
                            Vissim.Net.SignalControllers.ItemByKey(12).SGs.ItemByKey(2).SetAttValue ('SigState','GREEN')
                            Vissim.Net.SignalControllers.ItemByKey(12).SGs.ItemByKey(3).SetAttValue ('SigState','GREEN')
                            Vissim.Net.SignalControllers.ItemByKey(12).SGs.ItemByKey(4).SetAttValue ('SigState','GREEN')



                if  Vissim.Net.SignalControllers.ItemByKey(12).SGs.ItemByKey(2).AttValue ('SigState') == 'GREEN':
                    Vissim.Net.SignalControllers.ItemByKey(12).SGs.ItemByKey(1).SetAttValue ('SigState','RED')
                    if Seconds >= Vissim.Net.SignalControllers.ItemByKey(12).SGs.ItemByKey(2).AttValue ('GreenEnd')-1:
                            Vissim.Net.SignalControllers.ItemByKey(12).SGs.ItemByKey(1).SetAttValue ('SigState','RED')
                            Vissim.Net.SignalControllers.ItemByKey(12).SGs.ItemByKey(2).SetAttValue ('SigState','RED')
                            Vissim.Net.SignalControllers.ItemByKey(12).SGs.ItemByKey(3).SetAttValue ('SigState','RED')
                            Vissim.Net.SignalControllers.ItemByKey(12).SGs.ItemByKey(4).SetAttValue ('SigState','RED')







                if  Vissim.Net.SignalControllers.ItemByKey(13).SGs.ItemByKey(1).AttValue ('SigState') == 'GREEN':
                    Vissim.Net.SignalControllers.ItemByKey(13).SGs.ItemByKey(2).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(13).SGs.ItemByKey(3).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(13).SGs.ItemByKey(4).SetAttValue ('SigState','RED')
                    if Seconds >= Vissim.Net.SignalControllers.ItemByKey(13).SGs.ItemByKey(1).AttValue ('GreenEnd')-1:
                        if Seconds < Vissim.Net.SignalControllers.ItemByKey(13).SGs.ItemByKey(1).AttValue ('GreenEnd')+2:
                            Vissim.Net.SignalControllers.ItemByKey(13).SGs.ItemByKey(1).SetAttValue ('SigState','RED')
                            Vissim.Net.SignalControllers.ItemByKey(13).SGs.ItemByKey(2).SetAttValue ('SigState','RED')
                            Vissim.Net.SignalControllers.ItemByKey(13).SGs.ItemByKey(3).SetAttValue ('SigState','RED')
                            Vissim.Net.SignalControllers.ItemByKey(13).SGs.ItemByKey(4).SetAttValue ('SigState','RED')

                if Seconds >= Vissim.Net.SignalControllers.ItemByKey(13).SGs.ItemByKey(2).AttValue ('GreenStart')-1:
                    if Seconds <= Vissim.Net.SignalControllers.ItemByKey(13).SGs.ItemByKey(2).AttValue ('GreenEnd')-1:
                            Vissim.Net.SignalControllers.ItemByKey(13).SGs.ItemByKey(1).SetAttValue ('SigState','RED')
                            Vissim.Net.SignalControllers.ItemByKey(13).SGs.ItemByKey(2).SetAttValue ('SigState','GREEN')
                            Vissim.Net.SignalControllers.ItemByKey(13).SGs.ItemByKey(3).SetAttValue ('SigState','GREEN')
                            Vissim.Net.SignalControllers.ItemByKey(13).SGs.ItemByKey(4).SetAttValue ('SigState','GREEN')



                if  Vissim.Net.SignalControllers.ItemByKey(13).SGs.ItemByKey(2).AttValue ('SigState') == 'GREEN':
                    Vissim.Net.SignalControllers.ItemByKey(13).SGs.ItemByKey(1).SetAttValue ('SigState','RED')
                    if Seconds >= Vissim.Net.SignalControllers.ItemByKey(13).SGs.ItemByKey(2).AttValue ('GreenEnd')-1:
                            Vissim.Net.SignalControllers.ItemByKey(13).SGs.ItemByKey(1).SetAttValue ('SigState','RED')
                            Vissim.Net.SignalControllers.ItemByKey(13).SGs.ItemByKey(2).SetAttValue ('SigState','RED')
                            Vissim.Net.SignalControllers.ItemByKey(13).SGs.ItemByKey(3).SetAttValue ('SigState','RED')
                            Vissim.Net.SignalControllers.ItemByKey(13).SGs.ItemByKey(4).SetAttValue ('SigState','RED')











