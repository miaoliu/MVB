import os
from matplotlib import cm
import numpy as np
from openpyxl import Workbook
from pymatgen.analysis.bond_valence import BVAnalyzer
from pymatgen import Structure
import pymongo
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

__author__ = 'miaoliu'

redox_ion_pool = ['Mn','V','Fe','Co','Ti','Cr','Mo','Ni','Cu','Ag','Te','Se','Bi','Sb','Ta','W','Re','Sn']




connection= pymongo.Connection('mongodb://admin_alia:xJxj5N2PtJUTHd@mongodb03.nersc.gov:27017/mg_core_dev')
db = connection['mg_core_dev']

electrodes = db.electrodes

cursor = electrodes.find({"working_ion":{"$in":["Li"]}})
for ic in cursor:
    print {"formula":ic["formula_discharge"],"battid":ic["battid"],"task_id_discharge":ic["id_discharge"],"task_id_charge":ic["id_charge"]}