"""
Demo of the errorbar function.
"""
from matplotlib import cm, mpl
from matplotlib.colors import LogNorm
import numpy as np
import matplotlib.pyplot as plt
import pymongo
from pymatgen import MPRester

connection = pymongo.Connection("mongodb://localhost", safe=True)
db = connection.coordination
cddb = db.Zn

# example data

cursor = cddb.find()


API_KEY = "Neo5xcHNOTE41tZi"
mpr = MPRester(api_key=API_KEY, host="www.materialsproject.org")


#print "coordination number = 2, e^hull < 50meV/atom"
#for ic in cursor:
#    if ic["c_num"] == 2 and ic["ehull"] <0.05:
#        print mpr.get_entry_by_material_id(ic["task_id"]).composition.reduced_formula
#        print "https://materialsproject.org/materials/"+ic["task_id"]+"/"
#cursor = cddb.find()
#print "coordination number = 3, e^hull < 50meV/atom"
#for ic in cursor:
#    if ic["c_num"] == 3 and ic["ehull"] <0.05:
#        print mpr.get_entry_by_material_id(ic["task_id"]).composition.reduced_formula
#        print "https://materialsproject.org/materials/"+ic["task_id"]+"/"
cursor = cddb.find()
print "coordination number = 5, e^hull < 50meV/atom"
for ic in cursor:
    if ic["c_num"] == 5 and ic["ehull"] <0.05:
        print mpr.get_entry_by_material_id(ic["task_id"]).composition.reduced_formula
        print "https://materialsproject.org/materials/"+ic["task_id"]+"/"
cursor = cddb.find()
print "coordination number = 8, e^hull < 50meV/atom"
for ic in cursor:
    if ic["c_num"] == 8 and ic["ehull"] <0.05:
        print mpr.get_entry_by_material_id(ic["task_id"]).composition.reduced_formula
        print "https://materialsproject.org/materials/"+ic["task_id"]+"/"

'''
for c in cursor:
    #if c["c_num"]== 3:
    #    plt.errorbar(c["c_dis"], c["ehull"], xerr=c["c_dis_"], yerr=0.0,color="blue",fmt="-o",alpha=0.5)
    #if c["c_num"]== 4:
    #    plt.errorbar(c["c_dis"], c["ehull"], xerr=c["c_dis_"], yerr=0.0,linewidth=1,color="green",ms= 2,marker="o",alpha=0.1)
    #if c["c_num"]== 5:
    #    plt.errorbar(c["c_dis"], c["ehull"], xerr=c["c_dis_"], yerr=0.0,linewidth=1,color="red",ms= 2,marker="o",alpha=0.1)
    if c["c_num"]== 6:
        plt.errorbar(c["c_dis"], c["ehull"], xerr=c["c_dis_"], yerr=0.0,color="blue", linewidth=1,ms= 2,marker="o",alpha=0.1)
    #if c["c_num"]== 7:
    #    plt.errorbar(c["c_dis"], c["ehull"], xerr=c["c_dis_"], yerr=0.0,color="magenta",fmt="-o",alpha=0.5)
    #if c["c_num"]== 8:
    #    plt.errorbar(c["c_dis"], c["ehull"], xerr=c["c_dis_"], yerr=0.0,color="black",fmt="-o",alpha=0.5)
    #if c["c_num"]== 9:
    #    plt.errorbar(c["c_dis"], c["ehull"], xerr=c["c_dis_"], yerr=0.0,color="yellow",fmt="-o",alpha=0.5)
    #if c["c_num"]== 10:
    #    plt.errorbar(c["c_dis"], c["ehull"], xerr=c["c_dis_"], yerr=0.0,color="yellow",fmt="-o",alpha=0.5)
    #if c["c_num"]== 11:
    #    plt.errorbar(c["c_dis"], c["ehull"], xerr=c["c_dis_"], yerr=0.0,color="yellow",fmt="-o",alpha=0.5)
    #if c["c_num"]== 12:
    #    plt.errorbar(c["c_dis"], c["ehull"], xerr=c["c_dis_"], yerr=0.0,color="yellow",fmt="-o",alpha=0.5)

plt.xlabel('Coordination distance',fontsize=18)
plt.ylabel('E^hull (meV/atom)',fontsize=18)
#plt.xlim(1.5,8.5)
plt.ylim(0,0.5)
#plt.title('Working ion species',fontsize=18)
plt.grid(True)
plt.show()


'''



'''
x = []
y = []
for c in cursor:
    if c["c_num"]< 9.5 and c["c_num"] >0.5:
        x.append(c["c_num"])
        y.append(c["ehull"])


x.append(9.5)
y.append(0)
x.append(-0.5)
y.append(0)




#plt.hist2d(x, y, bins=[30,100])

plt.hist2d(x, y, bins=[30,100], norm=LogNorm())

plt.colorbar()





plt.xlabel('Coordination number',fontsize=18)
plt.ylabel('E^hull (eV/atom)',fontsize=18)
plt.xlim(1.5,8.5)
plt.ylim(0,0.5)
#plt.title('Working ion species',fontsize=18)
plt.grid(True)
plt.show()
'''





'''
x = []
y = []
for c in cursor:
    if c["c_num"]< 9.5 and c["c_num"] >0.5:
        x.append(c["c_num"])
        y.append(c["ehull"])


x.append(9.5)
y.append(1.0)
x.append(-0.5)
y.append(0)




#plt.hist2d(x, y, bins=[30,100])
#cmap = plt.get_cmap('Blues')
#cmap = plt.get_cmap('BuGn')
#cmap = plt.get_cmap('Oranges')
#cmap = plt.get_cmap('Purples')

cmap = plt.get_cmap('YlGnBu')

plt.hist2d(x, y, bins=[30,100],norm=LogNorm(),cmap=cmap)

#plt.hist2d(x, y, bins=[30,150], norm=LogNorm(),cmap=mpl.cm.blue)

plt.colorbar()



plt.xlabel('Coordination number',fontsize=18)
plt.ylabel('E^hull (eV/atom)',fontsize=18)
plt.xlim(1.5,8.5)
plt.ylim(0,0.5)
#plt.title('Working ion species',fontsize=18)
plt.grid(True)
plt.show()
'''





'''

for c in cursor:
    plt.errorbar(c["c_num"], c["ehull"], xerr=0.0, yerr=0.0,color="purple",ms= 10,marker="s",alpha=0.01)


plt.xlabel('Coordination number',fontsize=18)
plt.ylabel('E^hull (eV/atom)',fontsize=18)
plt.xlim(1.5,8.5)
plt.ylim(0,0.5)
#plt.title('Working ion species',fontsize=18)
plt.grid(True)
plt.show()
'''
'''
redox_ion_dic = {"Ti": [ 2, 3, 4],"V" : [ 2, 3, 4, 5],"Cr": [ 2, 3, 4, 5, 6],"Mn": [ 2, 3, 4],"Fe": [ 2, 3, 4],"Co": [ 2, 3, 4],"Ni": [ 2, 3, 4],"Cu": [ 1, 2, 3],"Nb": [ 3, 4, 5],"Mo": [ 3, 4, 5, 6],"Sn": [ 2, 3, 4],"Sb": [ 3, 4, 5],"Bi": [ 3, 4, 5],"W": [ 2, 3, 4, 5, 6]}

redox_ion = redox_ion_dic.keys()

redox_ion.remove("Cu")
redox_ion.remove("Sn")
redox_ion.remove("Bi")



API_KEY = "Neo5xcHNOTE41tZi"

mpr = MPRester(api_key=API_KEY, host="www.materialsproject.org")



compounds = []

for c in cursor:
    if c["c_num"] in [2,3,7,8] and c["ehull"]<0.100:

        compounds.append(c["task_id"])

        entry = mpr.get_entries(c["task_id"],inc_structure=True)[0]
        elements =  entry.structure.composition.keys()
        els = [element.symbol for element in elements]

        for el in els:
            if el in redox_ion:
                print entry.structure.composition.reduced_formula,",          https://materialsproject.org/materials/"+c["task_id"]+"/"

print len(compounds)

'''