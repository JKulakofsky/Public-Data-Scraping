import requests
import re
from tabulate import tabulate
import unicodecsv
from cStringIO import StringIO
import time

r = requests.get('http://www.nrcan.gc.ca/earth-sciences/geography/place-names/education-resources/9237')
url = requests.get("http://www.en.wikipedia.org/wiki/List_of_U.S._state_abbreviations")
data = url.text

States_full = []
Abbreviations1_full = []
Abbreviations2_full = []
Abbreviations3_full = []
Provinces_full = []
Abbreviations_full = []
Symbols_full = []
FrenchAbbreviations_full = []
FrenchNames_full = []

i = 0
while i<4:
        countrygex = '<td><a href="/wiki/.+?" title=".+?">(.+?)</a></td>'
        uscompiled = re.compile(countrygex)
        country = re.findall(uscompiled,data)
        States_full.append(country[i])
        i+=2

for j in range(4, 59):
        statesgex = '<td><a href="/wiki/.+?" title=".+?">(.+?)</a></td>'
        statescompiled = re.compile(statesgex)
        states = re.findall(statescompiled,data)
        States_full.append(states[j])

USabbrevgex = '<td align="center"><tt>(.+?)<br />'
USabbrevcompiled = re.compile(USabbrevgex)
USabbrev = re.findall(USabbrevcompiled,data)
Abbreviations1_full.append(USabbrev[0])

i = 2
while i < 255:
        abbreviations1gex = '<td align="center"><tt>(.+?)</tt></td>'
        abbreviations1compiled = re.compile(abbreviations1gex)
        abbreviations1 = re.findall(abbreviations1compiled,data)
        Abbreviations1_full.append(abbreviations1[i])
        i+=5

i = 1
while i < 6:
        territoryabbrev1gex = '<td align="center"><tt>(.+?)<br />'
        territoryabbrev1compiled = re.compile(territoryabbrev1gex)
        territoryabbrev1 = re.findall(territoryabbrev1compiled,data)
        Abbreviations1_full.append(territoryabbrev1[i])
        i+=1

i = 0
while i < 257:
        abbreviations2gex = '<td align="center"><tt>(.+?)</tt></td>'
        abbreviations2compiled = re.compile(abbreviations2gex)
        abbreviations2 = re.findall(abbreviations2compiled,data)
        Abbreviations2_full.append(abbreviations2[i])
        i+=5

i = 257
while i < 282:
        territoryabbrev2gex = '<td align="center"><tt>(.+?)</tt></td>'
        territoryabbrev2compiled = re.compile(territoryabbrev2gex)
        territoryabbrev2 = re.findall(territoryabbrev2compiled,data)
        Abbreviations2_full.append(territoryabbrev2[i])
        i+=4

USabbrev3gex = '<td align="center"><tt>(\d+?)</tt></td>'
USabbrev3compiled = re.compile(USabbrev3gex)
USabbrev3 = re.findall(USabbrev3compiled,data)
Abbreviations3_full.append(USabbrev3[0])

i = 4
while i < 256:
        abbreviations3gex = '<td align="center"><tt>(.+?)</tt></td>'
        abbreviations3compiled = re.compile(abbreviations3gex)
        abbreviations3 = re.findall(abbreviations3compiled,data)
        Abbreviations3_full.append(abbreviations3[i])
        i+=5

i = 258
while i < 286:
        territoryabbrev3gex = '<td align="center"><tt>(.+?)</tt></td>'
        territoryabbrev3compiled = re.compile(territoryabbrev3gex)
        territoryabbrev3 = re.findall(territoryabbrev3compiled,data)
        Abbreviations3_full.append(territoryabbrev3[i])
        i+=4

headerlist = ["a1.1","a2.1"]
i = 0
while i<len(headerlist):
	albertatext = r.text
	oneprovincegex = '<th headers="a1.1" id="'+headerlist[i] +'">(.+?)</th>'
	oneprovince = re.compile(oneprovincegex)
	alberta = re.findall(oneprovince,albertatext)
	Provinces_full.append(alberta[0])
	i+=1

provincelist = ["a3.1","a4.1","a5.1","a6.1","a7.1","a8.1","a9.1","a10.1","a11.1","a12.1","a13.1"]
i=0
while i<len(provincelist):
	htmltext = r.text
	regex = '<th headers="a1.1 a1.1" id="'+provincelist[i] +'">(.+?)</th>'
	pattern = re.compile(regex)
	province = re.findall(pattern,htmltext)
	Provinces_full.append(province[0])
	i+=1

yukontext = r.text
secondgex = '<th id="a14.1">(.+?)<strong>\*\*\*</strong>'
twice = re.compile(secondgex)
yukon = re.findall(twice,yukontext)
Provinces_full.append(yukon[0])

abbrevtext = r.text
abbrevgex = '<th id="a1.2">(.+?)</th>'
abbrev = re.compile(abbrevgex)
abbreviation = re.findall(abbrev,abbrevtext)
Abbreviations_full.append(abbreviation[0])

abbrevlist = ["a2.1","a3.1"]
i=0
while i<len(abbrevlist):
	abbrevstext = r.text
	abbrevsgex = '<td headers="'+abbrevlist[i] +' a1.2">(.+?)</td>'
	abbrevs = re.compile(abbrevsgex)
	abbreviations = re.findall(abbrevs,abbrevstext)
	Abbreviations_full.append(abbreviations[0])
	i+=1

abbrevslist = ["a4.1","a5.1"]
i = 0
while i<len(abbrevslist):
	abbrevtext = r.text
	abbrevgex = '<td headers="a1.2 '+abbrevslist[i] +'">(.+?)</td>'
	abbrev = re.compile(abbrevgex)
	abbreviations = re.findall(abbrev,abbrevtext)
	Abbreviations_full.append(abbreviations[0])
	i+=1

nltext = r.text
nlgex = '<td headers="a1.2 a6.1">(.+?)<strong>\*</strong>'
nl = re.compile(nlgex)
newlabrador = re.findall(nl,nltext)
Abbreviations_full.append(newlabrador[0])

abrevlist = ["a7.1","a8.1","a9.1","a10.1","a11.1","a12.1","a13.1","a14.1"]
i = 0
while i<len(abrevlist):
	abrevtext = r.text
	abrevgex = '<td headers="a1.2 '+abrevlist[i] +'">(.+?)</td>'
	abrev = re.compile(abrevgex)
	abbreviationss = re.findall(abrev,abrevtext)
	Abbreviations_full.append(abbreviationss[0])
	i+=1
	
frenchtext = r.text
frenchgex = '<th id="a1.5">(.+?)</th>'
french = re.compile(frenchgex)
french_name = re.findall(french,frenchtext)
FrenchNames_full.append(french_name[0])

frenchslist = ["a2.1","a3.1"]
i = 0
while i<len(frenchslist):
	frenchstext = r.text
	frenchsgex = '<td headers="'+frenchslist[i] +' a1.5">(.+?)</td>'
	frenchs = re.compile(frenchsgex)
	french_names = re.findall(frenchs,frenchstext)
	FrenchNames_full.append(french_names[0])
	i+=1

frenchsslist = ["a4.1","a5.1","a6.1","a7.1","a8.1","a9.1","a10.1","a11.1","a12.1","a13.1","a14.1"]
i = 0
while i<len(frenchsslist):
	frenchsstext = r.text
	frenchssgex = '<td headers="a1.5 '+frenchsslist[i] +'">(.+?)</td>'
	frenchss = re.compile(frenchssgex)
	french_namess = re.findall(frenchss,frenchsstext)
	FrenchNames_full.append(french_namess[0])
	i+=1

frenchabbrevtext = r.text
frenchabbrevgex = '<th id="a1.4">(.+?)</th>'
frenchabbrev = re.compile(frenchabbrevgex)
french_abbrev = re.findall(frenchabbrev,frenchabbrevtext)
FrenchAbbreviations_full.append(french_abbrev[0])

frenchabbrevslist = ["a2.1","a3.1"]
i = 0
while i<len(frenchabbrevslist):
	frenchabbrevstext = r.text
	frenchabbrevsgex = '<td headers="'+frenchabbrevslist[i] +' a1.4">(.+?)</td>'
	frenchabbrevs = re.compile(frenchabbrevsgex)
	french_abbreviations = re.findall(frenchabbrevs,frenchabbrevstext)
	FrenchAbbreviations_full.append(french_abbreviations[0])
	i+=1

frenchabbrevsslist = ["a4.1","a5.1"]
i = 0
while i<len(frenchabbrevsslist):
	frenchabbrevsstext = r.text
	frenchabbrevssgex = '<td headers="a1.4 '+frenchabbrevsslist[i] +'">(.+?)</td>'
	frenchabbrevss = re.compile(frenchabbrevssgex)
	french_abbreviationss = re.findall(frenchabbrevss,frenchabbrevsstext)
	FrenchAbbreviations_full.append(french_abbreviationss[0])
	i+=1

frenchnltext = r.text
frenchnlgex = '<td headers="a1.4 a6.1">(.+?)<strong>\*</strong>'
frenchnl = re.compile(frenchnlgex)
french_newlabrador = re.findall(frenchnl,frenchnltext)
FrenchAbbreviations_full.append(french_newlabrador[0])

frenchabbrevssslist = ["a7.1","a8.1","a9.1","a10.1","a11.1","a12.1","a13.1","a14.1"]
i = 0
while i<len(frenchabbrevssslist):
	frenchabbrevssstext = r.text
	frenchabbrevsssgex = '<td headers="a1.4 '+frenchabbrevssslist[i] +'">(.+?)</td>'
	frenchabbrevsss = re.compile(frenchabbrevsssgex)
	french_abbreviationsss = re.findall(frenchabbrevsss,frenchabbrevssstext)
	FrenchAbbreviations_full.append(french_abbreviationsss[0])
	i+=1

symboltext = r.text
symbolgex = '<th id="a1.3">(.+?)</th>'
symbolc = re.compile(symbolgex)
symbol = re.findall(symbolc,symboltext)
Symbols_full.append(symbol[0])

symbolslist = ["a2.1","a3.1"]
i = 0
while i<len(symbolslist):
	symbolstext = r.text
	symbolsgex = '<td headers="'+symbolslist[i] +' a1.3">(.+?)</td>'
	symbolsc = re.compile(symbolsgex)
	symbols = re.findall(symbolsc,symbolstext)
	Symbols_full.append(symbols[0])
	i+=1

symbolsslist = ["a4.1","a5.1","a6.1","a7.1","a8.1"]
i = 0
while i<len(symbolsslist):
	symbolsstext = r.text
	symbolssgex = '<td headers="a1.3 '+symbolsslist[i] +'">(.+?)</td>'
	symbolssc = re.compile(symbolssgex)
	symbolss = re.findall(symbolssc,symbolsstext)
	Symbols_full.append(symbolss[0])
	i+=1

nusymboltext = r.text
nusymbolgex = '<td headers="a1.3 a9.1">(.+?)<strong>\*\*</strong>'
nusymbolc = re.compile(nusymbolgex)
nusymbol = re.findall(nusymbolc,nusymboltext)
Symbols_full.append(nusymbol[0])

symbolssslist = ["a10.1","a11.1","a12.1","a13.1","a14.1"]
i = 0
while i<len(symbolssslist):
	symbolssstext = r.text
	symbolsssgex = '<td headers="a1.3 '+symbolssslist[i] +'">(.+?)</td>'
	symbolsssc = re.compile(symbolsssgex)
	symbolsss = re.findall(symbolsssc,symbolssstext)
	Symbols_full.append(symbolsss[0])
	i+=1

# print u', '.join(States_full)
# print u', '.join(Abbreviations1_full)
# print u', '.join(Abbreviations2_full)
# print u', '.join(Abbreviations3_full)
# print u', '.join(Provinces_full)
# print u', '.join(Abbreviations_full)
# print u', '.join(Symbols_full)
# print u', '.join(FrenchAbbreviations_full)
# print u', '.join(FrenchNames_full)

US_table = [["##Name","ISO","ANSI","ANSI#"],
        [States_full[0],Abbreviations1_full[0],Abbreviations2_full[0],Abbreviations3_full[0]],
        [States_full[1],Abbreviations1_full[1],Abbreviations2_full[1],Abbreviations3_full[1]],
        [States_full[2],Abbreviations1_full[2],Abbreviations2_full[2],Abbreviations3_full[2]],
        [States_full[3],Abbreviations1_full[3],Abbreviations2_full[3],Abbreviations3_full[3]],
        [States_full[4],Abbreviations1_full[4],Abbreviations2_full[4],Abbreviations3_full[4]],
        [States_full[5],Abbreviations1_full[5],Abbreviations2_full[5],Abbreviations3_full[5]],
        [States_full[6],Abbreviations1_full[6],Abbreviations2_full[6],Abbreviations3_full[6]],
        [States_full[7],Abbreviations1_full[7],Abbreviations2_full[7],Abbreviations3_full[7]],
        [States_full[8],Abbreviations1_full[8],Abbreviations2_full[8],Abbreviations3_full[8]],
        [States_full[9],Abbreviations1_full[9],Abbreviations2_full[9],Abbreviations3_full[9]],
        [States_full[10],Abbreviations1_full[10],Abbreviations2_full[10],Abbreviations3_full[10]],
        [States_full[11],Abbreviations1_full[11],Abbreviations2_full[11],Abbreviations3_full[11]],
        [States_full[12],Abbreviations1_full[12],Abbreviations2_full[12],Abbreviations3_full[12]],
        [States_full[13],Abbreviations1_full[13],Abbreviations2_full[13],Abbreviations3_full[13]],
        [States_full[14],Abbreviations1_full[14],Abbreviations2_full[14],Abbreviations3_full[14]],
        [States_full[15],Abbreviations1_full[15],Abbreviations2_full[15],Abbreviations3_full[15]],
        [States_full[16],Abbreviations1_full[16],Abbreviations2_full[16],Abbreviations3_full[16]],
        [States_full[17],Abbreviations1_full[17],Abbreviations2_full[17],Abbreviations3_full[17]],
        [States_full[18],Abbreviations1_full[18],Abbreviations2_full[18],Abbreviations3_full[18]],
        [States_full[19],Abbreviations1_full[19],Abbreviations2_full[19],Abbreviations3_full[19]],
        [States_full[20],Abbreviations1_full[20],Abbreviations2_full[20],Abbreviations3_full[20]],
        [States_full[21],Abbreviations1_full[21],Abbreviations2_full[21],Abbreviations3_full[21]],
        [States_full[22],Abbreviations1_full[22],Abbreviations2_full[22],Abbreviations3_full[22]],
        [States_full[23],Abbreviations1_full[23],Abbreviations2_full[23],Abbreviations3_full[23]],
        [States_full[24],Abbreviations1_full[24],Abbreviations2_full[24],Abbreviations3_full[24]],
        [States_full[25],Abbreviations1_full[25],Abbreviations2_full[25],Abbreviations3_full[25]],
        [States_full[26],Abbreviations1_full[26],Abbreviations2_full[26],Abbreviations3_full[26]],
        [States_full[27],Abbreviations1_full[27],Abbreviations2_full[27],Abbreviations3_full[27]],
        [States_full[28],Abbreviations1_full[28],Abbreviations2_full[28],Abbreviations3_full[28]],
        [States_full[29],Abbreviations1_full[29],Abbreviations2_full[29],Abbreviations3_full[29]],
        [States_full[30],Abbreviations1_full[30],Abbreviations2_full[30],Abbreviations3_full[30]],
        [States_full[31],Abbreviations1_full[31],Abbreviations2_full[31],Abbreviations3_full[31]],
        [States_full[32],Abbreviations1_full[32],Abbreviations2_full[32],Abbreviations3_full[32]],
        [States_full[33],Abbreviations1_full[33],Abbreviations2_full[33],Abbreviations3_full[33]],
        [States_full[34],Abbreviations1_full[34],Abbreviations2_full[34],Abbreviations3_full[34]],
        [States_full[35],Abbreviations1_full[35],Abbreviations2_full[35],Abbreviations3_full[35]],
        [States_full[36],Abbreviations1_full[36],Abbreviations2_full[36],Abbreviations3_full[36]],
        [States_full[37],Abbreviations1_full[37],Abbreviations2_full[37],Abbreviations3_full[37]],
        [States_full[38],Abbreviations1_full[38],Abbreviations2_full[38],Abbreviations3_full[38]],
        [States_full[39],Abbreviations1_full[39],Abbreviations2_full[39],Abbreviations3_full[39]],
        [States_full[40],Abbreviations1_full[40],Abbreviations2_full[40],Abbreviations3_full[40]],
        [States_full[41],Abbreviations1_full[41],Abbreviations2_full[41],Abbreviations3_full[41]],
        [States_full[42],Abbreviations1_full[42],Abbreviations2_full[42],Abbreviations3_full[42]],
        [States_full[43],Abbreviations1_full[43],Abbreviations2_full[43],Abbreviations3_full[43]],
        [States_full[44],Abbreviations1_full[44],Abbreviations2_full[44],Abbreviations3_full[44]],
        [States_full[45],Abbreviations1_full[45],Abbreviations2_full[45],Abbreviations3_full[45]],
        [States_full[46],Abbreviations1_full[46],Abbreviations2_full[46],Abbreviations3_full[46]],
        [States_full[47],Abbreviations1_full[47],Abbreviations2_full[47],Abbreviations3_full[47]],
        [States_full[48],Abbreviations1_full[48],Abbreviations2_full[48],Abbreviations3_full[48]],
        [States_full[49],Abbreviations1_full[49],Abbreviations2_full[49],Abbreviations3_full[49]],
        [States_full[50],Abbreviations1_full[50],Abbreviations2_full[50],Abbreviations3_full[50]],
        [States_full[51],Abbreviations1_full[51],Abbreviations2_full[51],Abbreviations3_full[51]],
        [States_full[52],Abbreviations1_full[52],Abbreviations2_full[52],Abbreviations3_full[52]],
        [States_full[53],Abbreviations1_full[53],Abbreviations2_full[53],Abbreviations3_full[53]],
	[States_full[54],Abbreviations1_full[54],Abbreviations2_full[54],Abbreviations3_full[54]],
        [States_full[55],Abbreviations1_full[55],Abbreviations2_full[55],Abbreviations3_full[55]],
        [States_full[56],Abbreviations1_full[56],Abbreviations2_full[56],Abbreviations3_full[56]]]

CA_table = [["## %s" % Provinces_full[0],Abbreviations_full[0],Symbols_full[0],FrenchAbbreviations_full[0],FrenchNames_full[0]],
	[Provinces_full[1],Abbreviations_full[1],Symbols_full[1],FrenchAbbreviations_full[1],FrenchNames_full[1]],
	[Provinces_full[2],Abbreviations_full[2],Symbols_full[2],FrenchAbbreviations_full[2],FrenchNames_full[2]],
	[Provinces_full[3],Abbreviations_full[3],Symbols_full[3],FrenchAbbreviations_full[3],FrenchNames_full[3]],
	[Provinces_full[4],Abbreviations_full[4],Symbols_full[4],FrenchAbbreviations_full[4],FrenchNames_full[4]],
	[Provinces_full[5],Abbreviations_full[5],Symbols_full[5],FrenchAbbreviations_full[5],FrenchNames_full[5]],
	[Provinces_full[6],Abbreviations_full[6],Symbols_full[6],FrenchAbbreviations_full[6],FrenchNames_full[6]],
	[Provinces_full[7],Abbreviations_full[7],Symbols_full[7],FrenchAbbreviations_full[7],FrenchNames_full[7]],
	[Provinces_full[8],Abbreviations_full[8],Symbols_full[8],FrenchAbbreviations_full[8],FrenchNames_full[8]],
	[Provinces_full[9],Abbreviations_full[9],Symbols_full[9],FrenchAbbreviations_full[9],FrenchNames_full[9]],
	[Provinces_full[10],Abbreviations_full[10],Symbols_full[10],FrenchAbbreviations_full[10],FrenchNames_full[10]],
	[Provinces_full[11],Abbreviations_full[11],Symbols_full[11],FrenchAbbreviations_full[11],FrenchNames_full[11]],
	[Provinces_full[12],Abbreviations_full[12],Symbols_full[12],FrenchAbbreviations_full[12],FrenchNames_full[12]],
	[Provinces_full[13],Abbreviations_full[13],Symbols_full[13],FrenchAbbreviations_full[13],FrenchNames_full[13]]]

print "The list of US states and their abbreviations is:"
print tabulate(US_table, headers="firstrow")
print "The list of Canadian provinces and territories is:"
print tabulate(CA_table, headers="firstrow")

US_datfile = "US_States_%s.dat" % time.strftime("%Y_%m_%d")
CA_datfile = "CA_Provinces_And_Territories_%s.dat" % time.strftime("%Y_%m_%d")

with open(US_datfile, "w") as output:
	writer = unicodecsv.writer(output, delimiter='|')
	writer.writerows(US_table)

with open(CA_datfile, "w") as output:
        writer = unicodecsv.writer(output, delimiter='|')
        writer.writerows(CA_table)
