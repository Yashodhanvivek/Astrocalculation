import math
import numpy as np
from astropy import units as u
from astropy.coordinates import Angle

#rahu_deg = Angle('96d47m0.0s')
#moon_deg = Angle('136d48m0.0s')
#rashi = {}

#print (rahu_deg)
#print (moon_deg)
#rahu_deg
totalangle = Angle('360d0m0.0s')
arc = Angle('30d0m0.0s')
pada = arc/9
nakshatra_angle = 4*pada

rashi_start={'Mesh':Angle('0d0m0.0s'),'Vrushabh':Angle('30d0m0.0s'),'Mithun':Angle('60d0m0.0s'),'Kark':Angle('90d0m0.0s'),'Simha':Angle('120d0m0.0s'),'Kanya':Angle('150d0m0.0s'),'Tula':Angle('180d0m0.0s'),'Vrushchik':Angle('210d0m0.0s'),'Dhanu':Angle('240d0m0.0s'),'Makar':Angle('270d0m0.0s'),'Kumbha':Angle('300d0m0.0s'),'Meen':Angle('330d0m0.0s')}

rashi_end={'Mesh':Angle('30d0m0.0s'),'Vrushabh':Angle('60d0m0.0s'),'Mithun':Angle('90d0m0.0s'),'Kark':Angle('120d0m0.0s'),'Simha':Angle('150d0m0.0s'),'Kanya':Angle('180d0m0.0s'),'Tula':Angle('210d0m0.0s'),'Vrushchik':Angle('240d0m0.0s'),'Dhanu':Angle('270d0m0.0s'),'Makar':Angle('300d0m0.0s'),'Kumbha':Angle('330d0m0.0s'),'Meen':Angle('360d0m0.0s')}
rahu_deg = rashi_end['Kanya']+ Angle('15d5m0.0s')
moon_deg = rashi_end['Vrushchik']+ Angle('29d27m0.0s')
print ('Rahu is',rahu_deg)
print ('Moon is',moon_deg)
nakshtrapada = {'Ashwini1':pada,'Ashwini2':2*pada,'Ashwini3':3*pada,'Ashwini4':4*pada,'Bharani1':5*pada,'Bharani2':6*pada,'Bharani3':7*pada,'Bharani4':8*pada,
'Krittika1':9*pada,'Krittika2':10*pada,'Krittika3':11*pada,'Krittika4':12*pada,'Rohini1':13*pada,'Rohini2':14*pada,'Rohini3':15*pada,'Rohini4':16*pada,
'Mrigsira1':17*pada,'Mrigsira2':18*pada,'Mrigsira3':19*pada,'Mrigsira4':20*pada,'Aardra1':21*pada,'Aardra2':22*pada,'Aardra3':23*pada,'Aardra4':24*pada,
'Punarvasu1':25*pada,'Punarvasu2':26*pada,'Punarvasu3':27*pada,'Punarvasu4':28*pada,'Pushya1':29*pada,'Pushya2':30*pada,'Pushya3':31*pada,'Pushya4':32*pada,
'Ashlesha1':33*pada,'Ashlesha2':34*pada,'Ashlesha3':35*pada,'Ashlesha4':36*pada,'Magha1':37*pada,'Magha2':38*pada,'Magha3':39*pada,'Magha4':40*pada,
'Purvaphalguni1':41*pada,'Purvaphalguni2':42*pada,'Purvaphalguni3':43*pada,'Purvaphalguni4':44*pada,'Uttaraaphalguni1':45*pada,'Uttaraaphalguni2':46*pada,
'Uttaraaphalguni3':47*pada,'Uttaraaphalguni4':48*pada,'Hasta1':49*pada,'Hasta2':50*pada,'Hasta3':51*pada,'Hasta4':52*pada,'Chitra1':53*pada,'Chitra2':54*pada,
'Chitra3':55*pada,'Chitra4':56*pada,'Swati1':57*pada,'Swati2':58*pada,'Swati3':59*pada,'Swati4':60*pada,'Vishakha1':61*pada,'Vishakha2':62*pada,
'Vishakha3':63*pada,'Vishakha4':64*pada,'Anuradha1':65*pada,'Anuradha2':66*pada,'Anuradha3':67*pada,'Anuradha4':68*pada,'Jyeshtha1':69*pada,'Jyeshtha2':70*pada,
'Jyeshtha3':71*pada,'Jyeshtha4':72*pada,'Mula1':73*pada,'Mula2':74*pada,'Mula3':75*pada,'Mula4':76*pada,'Purvashadha1':77*pada,'Purvashadha2':78*pada,
'Purvashadha3':79*pada,'Purvashadha4':80*pada,'Uttarashadha1':81*pada,'Uttarashadha2':82*pada,'Uttarashadha3':83*pada,'Uttarashadha4':84*pada,
'Shravan1':85*pada,'Shravan2':86*pada,'Shravan3':87*pada,'Shravan4':88*pada,'Dhanishtha1':89*pada,'Dhanishtha2':90*pada,'Dhanishtha3':91*pada,'Dhanishtha4':92*pada,
'Shatbhisha1':93*pada,'Shatbhisha2':94*pada,'Shatbhisha3':95*pada,'Shatbhisha4':96*pada,'Purvabhadrapad1':97*pada,'Purvabhadrapad2':98*pada,
'Purvabhadrapad3':99*pada,'Purvabhadrapad4':100*pada,'Uttarabhadrapad1':101*pada,'Uttarabhadrapad2':102*pada,'Uttarabhadrapad3':103*pada,
'Uttarabhadrapad4':104*pada,'Revati1':105*pada,'Revati2':106*pada,'Revati3':107*pada,'Revati4':108*pada}

print(nakshtrapada)


def bb_calc (moondegrees,rahudegrees):  
	if moondegrees>rahudegrees:
		bb= (moondegrees-rahudegrees)/2 
	else:
		bb =((Angle('360d0m0.0s')-rahudegrees)+ (moondegrees))/2
	return bb

def bb_from(moondegrees,rahudegrees):
	if rahudegrees<bb_calc(moondegrees,rahudegrees):
		bbnew = bb_calc(moondegrees,rahudegrees) + rahudegrees
	else:
		bbnew = (Angle('360d0m0.0s') - rahudegrees)+bb_calc(moondegrees,rahudegrees)
	return bbnew

def searchpadas(bhrigubindu,nakshtrapada):
	index = math.floor(bhrigubindu/pada)	
	nakshatracharan = list(nakshtrapada)[index]
	return nakshatracharan
	
	

#value = next( v for i, v in enumerate(d.itervalues()) if i == index )	
bbmid = bb_calc(moon_deg,rahu_deg)
bhrigubindu = bb_from(moon_deg,rahu_deg)    #-(Angle('30d0m0.0s')-Angle('5d54m0.0s'))
#bhrigubindu = rahu_deg+bbmid
print(bbmid)
npbindu = searchpadas(bhrigubindu,nakshtrapada)
print(bhrigubindu)
print ('Mid point difference between Rahu and Moon is ',bbmid)
print ('Bhrigubindu is at',bhrigubindu)
print('Your Bhrigubindu lies in ',npbindu)

