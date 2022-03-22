RESULTS
=======


IRIS
====
Columns: ['sepallength', 'sepalwidth', 'petallength', 'petalwidth']
IBk KNN
	Best
		['petallength', 'petalwidth']: 96.6667%
		['sepallength', 'petallength', 'petalwidth']: 96.0000%
		['sepalwidth', 'petallength', 'petalwidth']: 96.0000%
		['petalwidth']: 95.3333%
		['sepallength', 'sepalwidth', 'petallength', 'petalwidth']: 95.3333%
	Worst
		['sepalwidth', 'petalwidth']: 92.0000%
		['sepalwidth', 'petallength']: 89.3333%
		['sepallength', 'sepalwidth']: 72.0000%
		['sepallength']: 68.0000%
		['sepalwidth']: 50.6667%
Naive Bayes
	Best
		['petallength', 'petalwidth']: 96.0000%
		['sepallength', 'petallength', 'petalwidth']: 96.0000%
		['petalwidth']: 95.3333%
		['sepallength', 'petalwidth']: 95.3333%
		['sepalwidth', 'petallength', 'petalwidth']: 95.3333%
	Worst
		['sepallength', 'sepalwidth', 'petallength']: 90.0000%
		['sepallength', 'petallength']: 89.3333%
		['sepallength', 'sepalwidth']: 77.3333%
		['sepallength']: 72.0000%
		['sepalwidth']: 57.3333%
J48 Decision Tree
	Best
		['petalwidth']: 94.6667%
		['sepallength', 'petalwidth']: 94.6667%
		['sepalwidth', 'petalwidth']: 94.6667%
		['petallength', 'petalwidth']: 94.6667%
		['sepallength', 'sepalwidth', 'petalwidth']: 94.6667%
	Worst
		['sepalwidth', 'petallength']: 92.6667%
		['sepallength', 'sepalwidth', 'petallength']: 92.6667%
		['sepallength']: 72.0000%
		['sepallength', 'sepalwidth']: 69.3333%
		['sepalwidth']: 54.6667%

Attribute importance (heuristic):
	petalwidth: 1067.1111
	petallength: 1050.0000
	sepallength: 953.5556
	sepalwidth: 900.6667

GLASS
=====
Columns: ['RI', 'Na', 'Mg', 'Al', 'Si', 'K', 'Ca', 'Ba', 'Fe']
IBk KNN
	Best
		['RI', 'Na', 'K', 'Ca']: 77.5701%
		['RI', 'Mg', 'K', 'Ca', 'Ba']: 77.5701%
		['RI', 'Mg', 'K', 'Ca']: 76.6355%
		['RI', 'Na', 'Mg', 'Si', 'Ca']: 76.6355%
		['RI', 'Na', 'Mg', 'Si', 'Ca', 'Ba']: 76.6355%
		['RI', 'Na', 'Mg', 'K', 'Ca', 'Ba']: 76.6355%
		['RI', 'Na', 'Ca']: 76.1682%
		['RI', 'Na', 'Mg', 'Ca']: 76.1682%
		['RI', 'Na', 'Mg', 'K', 'Ca']: 76.1682%
		['RI', 'Na', 'Mg', 'Ca', 'Ba']: 76.1682%
	Worst
		['Na', 'Ba']: 42.0561%
		['Si', 'Ba']: 42.0561%
		['Ba', 'Fe']: 42.0561%
		['Ca']: 41.5888%
		['Na', 'Fe']: 40.1869%
		['Si', 'Ba', 'Fe']: 40.1869%
		['Na']: 38.3178%
		['Fe']: 32.2430%
		['Si']: 28.0374%
		['Si', 'Fe']: 26.6355%
Naive Bayes
	Best
		['RI', 'Al']: 59.8131%
		['RI', 'Al', 'K']: 58.4112%
		['RI', 'Al', 'K', 'Fe']: 57.4766%
		['RI', 'Al', 'Si', 'K', 'Fe']: 57.4766%
		['RI', 'Na', 'Al']: 57.0093%
		['Al', 'K', 'Ca']: 57.0093%
		['RI', 'Na', 'Al', 'K']: 56.5421%
		['RI', 'Na', 'Al', 'Fe']: 56.0748%
		['RI', 'Al', 'Si', 'K']: 56.0748%
		['RI', 'Al', 'K', 'Ca', 'Ba']: 56.0748%
	Worst
		['RI', 'Si', 'Ba', 'Fe']: 29.4393%
		['RI', 'Ca', 'Ba', 'Fe']: 29.4393%
		['Ba', 'Fe']: 28.0374%
		['RI', 'Ba', 'Fe']: 27.1028%
		['Ca', 'Fe']: 26.1682%
		['Si', 'Ba', 'Fe']: 25.7009%
		['RI', 'Si', 'Fe']: 23.8318%
		['RI', 'Fe']: 22.4299%
		['Si', 'Fe']: 19.1589%
		['Fe']: 18.6916%
J48 Decision Tree
	Best
		['RI', 'Na', 'Mg', 'Ba', 'Fe']: 75.7009%
		['RI', 'Na', 'Mg', 'Ba']: 73.8318%
		['RI', 'Na', 'Mg', 'Fe']: 73.3645%
		['RI', 'Na', 'Mg', 'Si', 'Ba']: 73.3645%
		['RI', 'Na', 'Mg', 'Si', 'Ca', 'Fe']: 73.3645%
		['RI', 'Na', 'Mg', 'Si', 'Ba', 'Fe']: 73.3645%
		['RI', 'Na', 'Mg', 'Al', 'K']: 72.8972%
		['RI', 'Na', 'Mg', 'Al', 'Ca']: 72.8972%
		['RI', 'Na', 'Mg', 'Al', 'Si', 'K']: 72.8972%
		['RI', 'Na', 'Mg', 'Al', 'K', 'Ca']: 72.8972%
	Worst
		['K']: 45.7944%
		['Na', 'Ba']: 45.7944%
		['Ca', 'Fe']: 44.8598%
		['K', 'Fe']: 44.3925%
		['Na', 'K']: 43.9252%
		['Na']: 42.9907%
		['Na', 'Fe']: 39.7196%
		['Si']: 39.2523%
		['Fe']: 35.0467%
		['Si', 'Fe']: 34.1121%

Attribute importance (heuristic):
	RI: 10121.5545
	Al: 10072.2788
	Mg: 10010.3640
	Ca: 9909.2776
	K: 9831.3008
	Na: 9712.8184
	Ba: 9708.9299
	Si: 9548.4815
	Fe: 9242.0040

DIABETES
========
Columns: ['preg', 'plas', 'pres', 'skin', 'insu', 'mass', 'pedi', 'age']
IBk KNN
	Best
		['preg', 'plas', 'insu', 'mass']: 72.3958%
		['preg', 'plas', 'pres', 'insu']: 72.0052%
		['preg', 'plas', 'pres', 'insu', 'mass', 'pedi', 'age']: 71.7448%
		['plas', 'insu', 'age']: 71.3542%
		['preg', 'plas', 'insu', 'age']: 70.9635%
		['preg', 'plas', 'pres', 'mass', 'pedi', 'age']: 70.9635%
		['plas', 'pres', 'insu', 'mass', 'age']: 70.8333%
		['preg', 'plas', 'pres', 'insu', 'pedi', 'age']: 70.8333%
		['plas', 'skin', 'mass', 'pedi', 'age']: 70.7031%
	Worst
		['preg', 'pres', 'pedi']: 59.6354%
		['skin', 'mass', 'pedi']: 59.6354%
		['pres', 'skin', 'pedi', 'age']: 59.6354%
		['preg', 'insu', 'pedi']: 59.5052%
		['pres', 'insu']: 58.5938%
		['pres', 'skin', 'pedi']: 58.4635%
		['pedi']: 58.3333%
		['pres', 'skin', 'age']: 58.2031%
		['pres', 'pedi']: 55.3385%
Naive Bayes
	Best
		['plas', 'mass', 'pedi', 'age']: 77.3438%
		['preg', 'plas', 'pres', 'mass', 'pedi']: 77.0833%
		['preg', 'plas', 'pres', 'insu', 'mass', 'pedi']: 76.9531%
		['preg', 'plas', 'pres', 'skin', 'mass', 'pedi']: 76.6927%
		['preg', 'plas', 'pres', 'pedi']: 76.5625%
		['preg', 'plas', 'mass', 'pedi']: 76.5625%
		['plas', 'pres', 'skin', 'mass', 'pedi', 'age']: 76.5625%
		['plas', 'mass', 'pedi']: 76.4323%
		['preg', 'plas', 'pres', 'mass']: 76.4323%
	Worst
		['pres', 'pedi']: 65.1042%
		['skin', 'mass']: 64.9740%
		['skin']: 64.7135%
		['pres']: 64.5833%
		['pres', 'skin']: 64.3229%
		['age']: 64.0625%
		['pres', 'skin', 'age']: 63.9323%
		['skin', 'age']: 63.8021%
		['pres', 'age']: 63.2812%
J48 Decision Tree
	Best
		['plas', 'pres', 'mass', 'pedi', 'age']: 75.6510%
		['plas', 'pres', 'mass', 'age']: 75.5208%
		['plas', 'pres', 'skin', 'mass', 'age']: 75.5208%
		['preg', 'plas', 'pres', 'skin']: 75.3906%
		['plas', 'pres', 'skin', 'mass', 'pedi', 'age']: 75.3906%
		['preg', 'plas', 'pres', 'skin', 'insu']: 75.2604%
		['preg', 'plas', 'pres', 'mass', 'pedi', 'age']: 75.2604%
		['plas', 'mass', 'age']: 75.1302%
		['preg', 'plas', 'pres', 'mass', 'age']: 75.1302%
	Worst
		['skin', 'age']: 62.7604%
		['pres', 'skin', 'age']: 62.7604%
		['age']: 62.6302%
		['pres', 'pedi', 'age']: 62.5000%
		['pres', 'skin', 'insu', 'pedi']: 62.5000%
		['skin', 'pedi', 'age']: 62.3698%
		['pres', 'insu', 'pedi']: 62.2396%
		['pres', 'skin', 'pedi', 'age']: 62.2396%
		['pres', 'age']: 61.7188%

Attribute importance (heuristic):
	plas: 6919.9380
	mass: 6600.2365
	preg: 6579.5027
	insu: 6556.4481
	age: 6552.0908
	pedi: 6534.2603
	skin: 6519.8146
	pres: 6515.4433

