import xlrd
import numpy as np
import pandas as pd

def GetDF(filename):
    File = xlrd.open_workbook(filename)
    sheet = File.sheet_by_index(0)

    EbindLa = np.array(sheet.col_values(2))*(-627.5)
    EbindNd = np.array(sheet.col_values(3))*(-627.5)
    EbindEu = np.array(sheet.col_values(4))*(-627.5)
    EbindLu = np.array(sheet.col_values(5))*(-627.5)
    DipMom = np.array(sheet.col_values(6))
    Ehomo = np.array(sheet.col_values(7))*(-1)

    DF = pd.DataFrame()
    DF["EbindLa"] = EbindLa
    DF["EbindNd"] = EbindNd
    DF["EbindEu"] = EbindEu
    DF["EbindLu"] = EbindLu
    DF["DipoleMom"] = DipMom
    DF["Ehomo"] = Ehomo



    return DF


