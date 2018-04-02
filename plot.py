from matplotlib import pyplot as plt
import matplotlib.lines as mpatches
import numpy as np
from XxlSearch import GetDF


BaseLig = np.array([-0.09999,	-0.0914,	-0.09089,	-0.08379])*(-627.5)
DonLigCycle = np.array([-0.10598,	-0.09769,	-0.09722,	-0.09095])*(-627.5)
AccLigCycle = np.array([-0.09311,	-0.08534,	-0.08488,	-0.07893])*(-627.5)
DonLigBase = np.array([-0.10168	,-0.09324,	-0.09232,	-0.08619])*(-627.5)
AccLigBase = np.array([-0.08512	,-0.07642,	-0.07586,	-0.06927])*(-627.5)

lanthRad = [0, 3, 6, 14]

plt.plot(lanthRad, BaseLig, "b-", lanthRad, DonLigCycle, "r-",
         lanthRad, AccLigCycle, "g-", lanthRad, AccLigBase, "g:", lanthRad, DonLigBase, "r:")

plt.ylabel("Ebind, kkal / mol")
plt.xlabel("Number of f-electrons")
plt.title("Dependence of binding energy on metal radius for \n pyridine dilactams")

red_patch = mpatches.Line2D([],[], color='blue', marker="_", label='Core lig')
blue_patch = mpatches.Line2D([],[], color='red',marker="_",  label='OCH3 cycle lig')
green_patch = mpatches.Line2D([],[], color='green',marker="_", label='NO2 cycle lig')
blue_dots = mpatches.Line2D([],[], color='red',marker=".",  label='OCH3 base lig')
green_dots = mpatches.Line2D([],[], color='green',marker=".", label='NO2 base lig')
plt.legend(handles=[red_patch, blue_patch, green_patch, blue_dots, green_dots])

plt.text(lanthRad[0],BaseLig[0], str(BaseLig[0]))
plt.text(lanthRad[0],DonLigCycle[0], str(DonLigCycle[0]))
plt.text(lanthRad[0],DonLigBase[0], str(DonLigBase[0]))
plt.text(lanthRad[0],AccLigCycle[0], str(AccLigCycle[0]))
plt.text(lanthRad[0],AccLigBase[0], str(AccLigBase[0]))

plt.text(lanthRad[-1],BaseLig[-1], str(BaseLig[-1]))
plt.text(lanthRad[-1],DonLigCycle[-1], str(DonLigCycle[-1]))
plt.text(lanthRad[-1],DonLigBase[-1], str(DonLigBase[-1]))
plt.text(lanthRad[-1],AccLigCycle[-1], str(AccLigCycle[-1]))
plt.text(lanthRad[-1],AccLigBase[-1], str(AccLigBase[-1]))
plt.show()

