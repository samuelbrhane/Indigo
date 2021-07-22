import os
import sys
import errno

sys.path.append('../../common')
from env_indigo import *

indigo = Indigo()
indigo.setOption("molfile-saving-skip-date", True)

print("****** Change basis of Sgroup ********")

indigo.setOption("molfile-saving-mode", "3000")
m = indigo.loadMoleculeFromFile(joinPath("molecules/all_features_mol.mol"))

print(m.molfile());
print("****** remove fisrt atom from sgroup ********")
m.removeAtoms([174])
print(m.molfile());
print("****** remove second atom from sgroup and sgroup itself********")
m.removeAtoms([175])
print(m.molfile());
print("****** remove bond from sgroup ********")
m.removeBonds([229])
print(m.molfile());

m = indigo.loadMolecule('''
  Ketcher 10271618342D 1   1.00000     0.00000     0

 41 39  0     0  0            999 V2000
    8.7000  -10.5750    0.0000 C   0  0  0  0  0  0  0  0  0  0  0  0
    9.5660  -11.0750    0.0000 C   0  0  0  0  0  0  0  0  0  0  0  0
   10.4321  -10.5750    0.0000 C   0  0  0  0  0  0  0  0  0  0  0  0
   11.2981  -11.0750    0.0000 C   0  0  0  0  0  0  0  0  0  0  0  0
   12.1641  -10.5750    0.0000 C   0  0  0  0  0  0  0  0  0  0  0  0
   13.0301  -11.0750    0.0000 C   0  0  0  0  0  0  0  0  0  0  0  0
   13.8962  -10.5750    0.0000 C   0  0  0  0  0  0  0  0  0  0  0  0
   14.7622  -11.0750    0.0000 C   0  0  0  0  0  0  0  0  0  0  0  0
   15.6282  -10.5750    0.0000 C   0  0  0  0  0  0  0  0  0  0  0  0
   16.4942  -11.0750    0.0000 C   0  0  0  0  0  0  0  0  0  0  0  0
   17.3603  -10.5750    0.0000 C   0  0  0  0  0  0  0  0  0  0  0  0
   18.2263  -11.0750    0.0000 C   0  0  0  0  0  0  0  0  0  0  0  0
   19.0923  -10.5750    0.0000 C   0  0  0  0  0  0  0  0  0  0  0  0
   19.9583  -11.0750    0.0000 C   0  0  0  0  0  0  0  0  0  0  0  0
   20.8244  -10.5750    0.0000 C   0  0  0  0  0  0  0  0  0  0  0  0
   21.6904  -11.0750    0.0000 C   0  0  0  0  0  0  0  0  0  0  0  0
   22.5564  -10.5750    0.0000 C   0  0  0  0  0  0  0  0  0  0  0  0
   23.4224  -11.0750    0.0000 C   0  0  0  0  0  0  0  0  0  0  0  0
   24.2885  -10.5750    0.0000 C   0  0  0  0  0  0  0  0  0  0  0  0
   25.1545  -11.0750    0.0000 C   0  0  0  0  0  0  0  0  0  0  0  0
   26.0205  -10.5750    0.0000 C   0  0  0  0  0  0  0  0  0  0  0  0
   26.8865  -11.0750    0.0000 C   0  0  0  0  0  0  0  0  0  0  0  0
   27.7526  -10.5750    0.0000 C   0  0  0  0  0  0  0  0  0  0  0  0
   28.6186  -11.0750    0.0000 C   0  0  0  0  0  0  0  0  0  0  0  0
   11.8000  -15.9500    0.0000 C   0  0  0  0  0  0  0  0  0  0  0  0
   12.6660  -16.4500    0.0000 C   0  0  0  0  0  0  0  0  0  0  0  0
   13.5321  -15.9500    0.0000 C   0  0  0  0  0  0  0  0  0  0  0  0
   14.3981  -16.4500    0.0000 C   0  0  0  0  0  0  0  0  0  0  0  0
   15.2641  -15.9500    0.0000 C   0  0  0  0  0  0  0  0  0  0  0  0
   16.1301  -16.4500    0.0000 C   0  0  0  0  0  0  0  0  0  0  0  0
   16.9962  -15.9500    0.0000 C   0  0  0  0  0  0  0  0  0  0  0  0
   17.8622  -16.4500    0.0000 C   0  0  0  0  0  0  0  0  0  0  0  0
   18.7282  -15.9500    0.0000 C   0  0  0  0  0  0  0  0  0  0  0  0
   19.5942  -16.4500    0.0000 C   0  0  0  0  0  0  0  0  0  0  0  0
   20.4603  -15.9500    0.0000 C   0  0  0  0  0  0  0  0  0  0  0  0
   14.3981  -16.4500    0.0000 C   0  0  0  0  0  0  0  0  0  0  0  0
   15.2641  -15.9500    0.0000 C   0  0  0  0  0  0  0  0  0  0  0  0
   16.1301  -16.4500    0.0000 C   0  0  0  0  0  0  0  0  0  0  0  0
   14.3981  -16.4500    0.0000 C   0  0  0  0  0  0  0  0  0  0  0  0
   15.2641  -15.9500    0.0000 C   0  0  0  0  0  0  0  0  0  0  0  0
   16.1301  -16.4500    0.0000 C   0  0  0  0  0  0  0  0  0  0  0  0
  1  2  1  0     0  0
  2  3  1  0     0  0
  3  4  1  0     0  0
  4  5  1  0     0  0
  5  6  1  0     0  0
  6  7  1  0     0  0
  7  8  1  0     0  0
  8  9  1  0     0  0
  9 10  1  0     0  0
 10 11  1  0     0  0
 11 12  1  0     0  0
 12 13  1  0     0  0
 13 14  1  0     0  0
 14 15  1  0     0  0
 15 16  1  0     0  0
 16 17  1  0     0  0
 17 18  1  0     0  0
 18 19  1  0     0  0
 19 20  1  0     0  0
 20 21  1  0     0  0
 21 22  1  0     0  0
 22 23  1  0     0  0
 23 24  1  0     0  0
 25 26  1  0     0  0
 26 27  1  0     0  0
 27 39  1  0     0  0
 28 29  1  0     0  0
 29 30  1  0     0  0
 30 31  1  0     0  0
 31 32  1  0     0  0
 32 33  1  0     0  0
 33 34  1  0     0  0
 34 35  1  0     0  0
 36 37  1  0     0  0
 37 38  1  0     0  0
 28 38  1  0     0  0
 39 40  1  0     0  0
 40 41  1  0     0  0
 36 41  1  0     0  0
M  STY  1   1 SRU
M  SLB  1   1   1
M  SCN  1   1 HT 
M  SMT   1 n
M  SAL   1  5   3   4   5   6   7
M  SBL   1  2   2   7
M  SDI   1  4    9.9990  -11.5750    9.9990  -10.0750
M  SDI   1  4   14.3292  -10.0750   14.3292  -11.5750
M  STY  1   2 SRU
M  SLB  1   2   2
M  SCN  1   2 HT 
M  SMT   2 k
M  SAL   2  7  15  16  17  18  19  20  21
M  SBL   2  2  14  21
M  SDI   2  4   20.3913  -11.5750   20.3913  -10.0750
M  SDI   2  4   26.4535  -10.0750   26.4535  -11.5750
M  STY  1   3 MUL
M  SLB  1   3   3
M  SAL   3  9  28  29  30  36  37  38  39  40  41
M  SPA   3  3  28  29  30
M  SBL   3  2  26  29
M  SMT   3 3
M  SDI   3  4   13.9651  -16.9500   13.9651  -15.4500
M  SDI   3  4   16.5631  -15.4500   16.5631  -16.9500
M  END
''')
for g in m.iterateRepeatingUnits():
   	print(g.getRepeatingUnitSubscript())
   	print(g.getRepeatingUnitConnectivity())
   	for a in g.iterateAtoms():
   		print('{0} {1}'.format(a.index(), a.symbol()))
for g in m.iterateMultipleGroups():
   	print(g.getSGroupMultiplier())
   	for a in g.iterateAtoms():
	   	print('{0} {1}'.format(a.index(), a.symbol()))