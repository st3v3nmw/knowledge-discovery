98.33333333333333
array([[73.,  2.],
       [ 0., 45.]])

Correctly Classified Instances         118               98.3333 %
Incorrectly Classified Instances         2                1.6667 %
Kappa statistic                          0.9648
Mean absolute error                      0.0201
Root mean squared error                  0.1287
Relative absolute error                  4.2854 %
Root relative squared error             26.582  %
Total Number of Instances              120     

96.66666666666667
array([[75.,  0.],
       [ 4., 41.]])

Correctly Classified Instances         116               96.6667 %
Incorrectly Classified Instances         4                3.3333 %
Kappa statistic                          0.9276
Mean absolute error                      0.038 
Root mean squared error                  0.1093
Relative absolute error                  8.1079 %
Root relative squared error             22.5742 %
Total Number of Instances              120     

100.0
array([[75.,  0.],
       [ 0., 45.]])

Correctly Classified Instances         120              100      %
Incorrectly Classified Instances         0                0      %
Kappa statistic                          1     
Mean absolute error                      0.0073
Root mean squared error                  0.0397
Relative absolute error                  1.5516 %
Root relative squared error              8.2097 %
Total Number of Instances              120     

98.33333333333333 weka.attributeSelection.OneRAttributeEval 7


=== Attribute Selection on all input data ===

Search Method:
        Attribute ranking.

Attribute Evaluator (supervised, Class (nominal): 25 class):
        OneR feature evaluator.

        Using 10 fold cross validation for evaluating attributes.
        Minimum bucket size for OneR: 6

Ranked attributes:
92       15 hemo
89.75    16 pcv
89.25    18 rbcc
88.25     3 sg
87.5     12 sc
85.25     4 al
82.75     6 rbc
75.5     14 pot
74.75    13 sod
74.25    19 htn
71.75    20 dm
70.25    11 bu
69.5      2 bp
68.25     7 pc
67.5     10 bgr
67.25    17 wbcc
65.75     1 age
63.5      8 pcc
63.5      9 ba
63       21 cad
62.5     22 appet
62.5     23 pe
62.5     24 ane
61.25     5 su

Selected attributes: 15,16,18,3,12,4,6,14,13,19,20,11,2,7,10,17,1,8,9,21,22,23,24,5 : 24


=== Attribute selection 10 fold cross-validation (stratified), seed: 42 ===

average merit      average rank  attribute
91.944 +- 0.621      1   +- 0       15 hemo
90.222 +- 0.877      2.3 +- 0.64    16 pcv
89.806 +- 0.542      2.9 +- 0.3     18 rbcc
88.25  +- 0.556      4   +- 0.77     3 sg
87.25  +- 0.8        4.8 +- 0.4     12 sc
85.25  +- 0.685      6   +- 0        4 al
82.75  +- 0.614      7   +- 0        6 rbc
75.806 +- 1.828      8.4 +- 0.8     13 sod
74.194 +- 0.562      9.3 +- 0.46    19 htn
74.611 +- 1.677      9.4 +- 0.92    14 pot
71.694 +- 0.708     11.1 +- 0.54    20 dm
69.5   +- 0.553     12.8 +- 0.75     2 bp
68.694 +- 2.094     14   +- 1.9     11 bu
68.083 +- 1.898     14.6 +- 2.11     1 age
68.25  +- 0.609     14.7 +- 0.9      7 pc
67.556 +- 1.871     14.9 +- 1.7     10 bgr
66.694 +- 1.989     16.1 +- 1.7     17 wbcc
63.5   +- 0.184     18.2 +- 0.6      8 pcc
63.5   +- 0.184     18.7 +- 0.64     9 ba
62.944 +- 0.222     20   +- 0.77    21 cad
62.5   +- 0         21   +- 0.45    22 appet
62.5   +- 0         22.3 +- 0.64    23 pe
62.5   +- 0         22.7 +- 0.78    24 ane
60.583 +- 1.22      23.8 +- 0.6      5 su
