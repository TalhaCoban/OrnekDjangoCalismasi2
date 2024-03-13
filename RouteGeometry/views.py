from django.shortcuts import render, HttpResponse
from django.contrib import messages
import numpy as np



def Grad2Radyan(angle):
    return (angle * np.pi) / 200

def Radyan2Grad(Radyan):
    return (Radyan * 200) / np.pi

def Grad2Degree(Grad):
    return (Grad * 9) / 10

def Degree2Grad(Degree):
    return (Degree * 10) / 9

def Azimuth(YA, XA, YB, XB):

    DeltaY = (YB - YA)
    DeltaX = (XB - XA)
    
    tAB = np.round(Radyan2Grad(np.arctan(DeltaY / DeltaX)), 4)

    if DeltaY >= 0:
        if DeltaX >= 0:
            tAB = tAB
        else:
            tAB = tAB + 200
    else:
        if DeltaX >= 0:
            tAB = tAB + 400
        else:
            tAB = tAB + 200
    
    return tAB


def Horizontal_Route_Geometry(request):
    if request.method == "POST":
        t = None
        L = None
        alfa = None
        STOn_TFn = None
        t_Sn_Sn_1 = None
        t_Sn1_Sn = None
        t_TOn_TFn = None
        t_TFn_TOn = None
        SSn_M = None
        STFn_1_Sn = None
        SSn_TOn1 = None
        SSn_1_TOn = None
        STFn_Sn1 = None
        XP = None
        YP = None

        try:
            R = float(request.POST.get("R_1"))
        except:
            R = None
        try:
            Delta = float(request.POST.get("Delta_1"))
        except:
            Delta = None
        try:
            KSn_1 = float(request.POST.get("KSn_1_1"))
        except:
            KSn_1 = None
        try:
            YSn_1 = float(request.POST.get("YSn_1_1"))
        except:
            YSn_1 = None
        try:
            XSn_1 = float(request.POST.get("XSn_1_1"))
        except:
            XSn_1 = None
        try:
            KTFn_1 = float(request.POST.get("KTFn_1_1"))
        except:
            KTFn_1 = None
        try:
            YTFn_1 = float(request.POST.get("YTFn_1_1"))
        except:
            YTFn_1 = None
        try:
            XTFn_1 = float(request.POST.get("XTFn_1_1"))
        except:
            XTFn_1 = None
        try:
            KTFn = float(request.POST.get("KTFn_1"))
        except:
            KTFn = None
        try:
            YTFn = float(request.POST.get("YTFn_1"))
        except:
            YTFn = None
        try:
            XTFn = float(request.POST.get("XTFn_1"))
        except:
            XTFn = None
        try:
            KSn = float(request.POST.get("KSn_1"))
        except:
            KSn = None
        try:
            YSn = float(request.POST.get("YSn_1"))
        except:
            YSn = None
        try:
            XSn = float(request.POST.get("XSn_1"))
        except:
            XSn = None
        try:
            KTOn = float(request.POST.get("KTOn_1"))
        except:
            KTOn = None
        try:
            YTOn = float(request.POST.get("YTOn_1"))
        except:
            YTOn = None
        try:
            XTOn = float(request.POST.get("XTOn_1"))
        except:
            XTOn = None
        try:
            KTOn1 = float(request.POST.get("KTOn1_1"))
        except:
            KTOn1 = None
        try:
            YTOn1 = float(request.POST.get("YTOn1_1"))
        except:
            YTOn1 = None
        try:
            XTOn1 = float(request.POST.get("XTOn1_1"))
        except:
            XTOn1 = None
        try:
            KSn1 = float(request.POST.get("KSn1_1"))
        except:
            KSn1 = None
        try:
            YSn1 = float(request.POST.get("YSn1_1"))
        except:
            YSn1 = None
        try:
            XSn1 = float(request.POST.get("XSn1_1"))
        except:
            XSn1 = None
        try:
            YM = float(request.POST.get("YM_1"))
        except:
            YM = None
        try:
            XM = float(request.POST.get("XM_1"))
        except:
            XM = None
        try:
            SSn_1_TFn_1 = float(request.POST.get("SSn_1_TFn_1_1"))
        except:
            SSn_1_TFn_1 = None
        try:
            STFn_1_TOn = float(request.POST.get("STFn_1_TOn_1"))
        except:
            STFn_1_TOn = None
        try:
            STFn_TOn1 = float(request.POST.get("STFn_TOn1_1"))
        except:
            STFn_TOn1 = None
        try:
            STOn1_Sn1 = float(request.POST.get("STOn1_Sn1_1"))
        except:
            STOn1_Sn1 = None
        try:
            SSn_Sn_1 = float(request.POST.get("SSn_Sn_1_1"))
        except:
            SSn_Sn_1 = None
        try:
            SSn_Sn1 = float(request.POST.get("SSn_Sn1_1"))
        except:
            SSn_Sn1 = None
        try:
            t_Sn_1_Sn = float(request.POST.get("t_Sn_1_Sn_1"))
        except:
            t_Sn_1_Sn = None
        try:
            t_Sn_Sn1 = float(request.POST.get("t_Sn_Sn1_1"))
        except:
            t_Sn_Sn1 = None

        Curve = request.POST.get("combobox_left_or_right")

        for _ in range(25):

            if R != None and Delta != None:
                t = np.round(R * np.tan(Grad2Radyan(Delta) / 2), 3)

            if Delta != None:
                alfa = Delta / 2

            if YM != None and XM != None and YSn != None and XSn != None:
                SSn_M = np.round(((YM - YSn) ** 2 + (XM - XSn) ** 2) ** 0.5, 3)
                if Delta != None:
                    t = np.round(SSn_M * np.sin(Grad2Radyan(Delta / 2)), 3)
                    R = np.round(SSn_M * np.cos(Grad2Radyan(Delta / 2)), 3)

            if R != None and Delta != None:
                L = np.round((Delta * np.pi * R) / 200, 3)

            if SSn_Sn_1 == None:
                if YSn_1 != None and YSn != None and XSn_1 != None and XSn != None:
                    SSn_Sn_1 = np.round(((YSn_1 - YSn) ** 2 + (XSn_1 - XSn) ** 2) ** 0.5, 3)
                elif SSn_1_TFn_1 != None and STFn_1_TOn != None and t != None:
                    SSn_Sn_1 = np.round(SSn_1_TFn_1 + STFn_1_TOn + t, 3)
                elif SSn_1_TOn != None and t != None:
                    SSn_Sn_1 = np.round(SSn_1_TOn + t, 3)
                    
            if SSn_1_TFn_1 == None:
                if SSn_1_TOn != None and STFn_1_TOn != None:
                    SSn_1_TFn_1 = np.round(SSn_1_TOn - STFn_1_TOn, 3)
                elif STFn_1_Sn != None and t != None:
                    SSn_1_TFn_1 = np.round(STFn_1_Sn -t, 3)
                elif YTFn_1 != None and XTFn_1 != None and YTOn != None and XTOn != None:
                    SSn_1_TFn_1 = np.round(((YTFn_1 - YTOn) ** 2 + (XTFn_1 - XTOn) ** 2) ** 0.5, 3)
                elif KTFn_1 != None and KSn_1 != None:
                    SSn_1_TFn_1 = np.round(KTFn_1 - KSn_1, 3)

            if STFn_1_TOn == None:
                if SSn_Sn_1 != None and t != None and SSn_1_TFn_1 != None:
                    STFn_1_TOn = np.round(SSn_Sn_1 - t - SSn_1_TFn_1, 3)
                elif SSn_1_TOn != None and SSn_1_TFn_1 != None:
                    STFn_1_TOn = np.round(SSn_1_TOn - SSn_1_TFn_1, 3)
                elif YTOn != None and XTOn != None and YTFn_1 != None and XTFn_1 != None:
                    STFn_1_TOn = np.round(((YTOn - YTFn_1) ** 2 + (XTOn - XTFn_1) ** 2) ** 0.5, 3)
                elif KTOn != None and KTFn_1 != None:
                    STFn_1_TOn = np.round(KTOn - KTFn_1, 3)

            if STOn_TFn == None:
                if R != None and Delta != None:
                    STOn_TFn = np.round(2 * R * np.sin(Grad2Radyan(Delta) / 2), 3)
                elif YTOn != None and XTOn != None and YTFn != None and XTFn != None:
                    STOn_TFn = np.round(((YTOn - YTFn) ** 2 + (XTOn - XTFn) ** 2) ** 0.5, 3)

            if t == None:
                if R != None and Delta != None:
                    t = np.round(R * np.tan(Grad2Radyan(Delta) / 2), 3)
                elif SSn_Sn_1 != None and SSn_1_TOn != None:
                    t = np.round(SSn_Sn_1 - SSn_1_TOn)
                elif SSn_Sn1 != None and STFn_Sn1 != None:
                    t = np.round(SSn_Sn1 - STFn_Sn1)
                elif STFn_1_Sn != None and STFn_1_TOn != None:
                    t = np.round(STFn_1_Sn - STFn_1_TOn)
                elif SSn_TOn1 != None and STFn_TOn1 != None:
                    t = np.round(SSn_TOn1 - STFn_TOn1)
                elif YTOn != None and XTOn != None and YSn != None and XSn != None:
                    t = np.round(((YTOn - YSn) ** 2 + (XTOn - XSn) ** 2) ** 0.5, 3)
                elif YTFn != None and XTFn != None and YSn != None and XSn != None:
                    t = np.round(((YTFn - YSn) ** 2 + (XTFn - XSn) ** 2) ** 0.5, 3)

            if STFn_TOn1 == None:
                if SSn_TOn1 != None and t != None:
                    STFn_TOn1 = np.round(SSn_TOn1 - t, 3)
                elif STFn_Sn1 != None and STOn1_Sn1 != None:
                    STFn_TOn1 = np.round(STFn_Sn1 - STOn1_Sn1, 3)
                elif SSn_TOn1 != None and t != None:
                    STFn_TOn1 = np.round(SSn_TOn1 - t, 3)
                elif YTFn != None and XTFn != None and YTOn1 != None and XTOn1 != None:
                    STFn_TOn1 = np.round(((YTFn - YTOn1) ** 2 + (XTFn - XTOn1) ** 2) ** 0.5, 3)
                elif KTOn1 != None and KTFn != None:
                    STFn_TOn1 = np.round(KTOn1 - KTFn, 3)

            if STOn1_Sn1 == None:
                if STFn_Sn1 != None and STFn_TOn1 != None:
                    STOn1_Sn1 = np.round(STFn_Sn1 - STFn_TOn1, 3)
                elif SSn_TOn1 != None and SSn_Sn1 != None:
                    STOn1_Sn1 = np.round(SSn_Sn1 - SSn_TOn1, 3)
                elif YSn1 != None and XSn1 != None and YTOn1 != None and XTOn1 != None:
                    STOn1_Sn1 = np.round(((YSn1 - YTOn1) ** 2 + (XSn1 - XTOn1) ** 2) ** 0.5, 3)
                elif KSn1 != None and KTOn1 != None:
                    STOn1_Sn1 = np.round(KSn1 - KTOn1, 3)

            if SSn_Sn1 == None:
                if YSn != None and XSn != None and YSn1 != None and XSn1 != None:
                    SSn_Sn1 = np.round(((YSn - YSn1) ** 2 + (XSn - XSn1) ** 2) ** 0.5, 3)
                elif t != None and STFn_TOn1 != None and STOn1_Sn1 != None:
                    SSn_Sn1 = np.round(t + STFn_TOn1 + STOn1_Sn1, 3)
                elif t != None and STFn_Sn1 != None:
                    SSn1_Sn1 = np.round(t + STFn_Sn1, 3)

            if KSn_1 == None:
                if KTFn_1 != None and SSn_1_TFn_1 != None:
                    KSn_1 = np.round(KTFn_1 - SSn_1_TFn_1, 3)

            if KTFn_1 == None:
                if KSn_1 != None and SSn_1_TFn_1 != None:
                    KTFn_1 = np.round(KSn_1 + SSn_1_TFn_1, 3)
                elif KTOn != None and STFn_1_TOn != None:
                    KTFn_1 = np.round(KTOn - STFn_1_TOn, 3)
                elif KSn != None and STFn_1_Sn != None:
                    KTFn_1 = np.round(KSn - STFn_1_Sn, 3)

            if KTOn == None:
                if KTFn_1 != None and STFn_1_TOn != None:
                    KTOn = np.round(KTFn_1 + STFn_1_TOn, 3)
                elif KSn_1 != None and SSn_1_TOn != None:
                    KTOn = np.round(KSn_1 + SSn_1_TOn, 3)
                elif KSn != None and t != None:
                    KTOn = np.round(KSn - t, 3)
                elif KTFn != None and L != None:
                    KTOn = np.round(KTFn - L, 3)

            if KSn == None:
                if KTOn != None and t != None:
                    KSn = np.round(KTOn + t)
                elif KTFn != None and t != None:
                    KSn = np.round(KTFn - t)

            if KTFn == None:
                if KTOn != None and L != None:
                    KTFn = np.round(KTOn + L, 3)
                elif KSn != None and t != None:
                    KTFn = np.round(KSn + t, 3)
                elif KTOn1 != None and STFn_TOn1 != None:
                    KTFn = np.round(KTOn1 - STFn_TOn1, 3)
                elif KSn1 != None and STFn_Sn1 != None:
                    KTFn =np.round(KSn1 - STFn_Sn1, 3)

            if KTOn1 == None:
                if KTFn != None and STFn_TOn1 != None:
                    KTOn1 = np.round(KTFn + STFn_TOn1, 3)
                elif KSn != None and SSn_TOn1 != None:
                    KTOn1 = np.round(KSn + SSn_TOn1, 3)
                elif KSn1 != None and STOn1_Sn1 != None:
                    KTOn1 = np.round(KSn1 - STOn1_Sn1, 3)

            if t_Sn_1_Sn == None:
                if YSn_1 != None and XSn_1 != None and YSn != None and XSn != None:
                    t_Sn_1_Sn = Azimuth(YSn_1, XSn_1, YSn, XSn)
                elif YTFn_1 != None and XTFn_1 != None and YTOn != None and XTOn != None:
                    t_Sn_1_Sn = Azimuth(YTFn_1, XTFn_1, YTOn, XTOn)
                elif YSn_1 != None and XSn_1 != None and YTFn_1 != None and XTFn_1 != None:
                    t_Sn_1_Sn = Azimuth(YSn_1, XSn_1, YTFn_1, XTFn_1)
                elif YTOn != None and XTOn != None and YSn != None and XSn != None:
                    t_Sn_1_Sn = Azimuth(YTOn, XTOn, YSn, XSn)

            if t_Sn_Sn1 == None:
                if YSn != None and XSn != None and YSn1 != None and XSn1 != None:
                    t_Sn_Sn1 = Azimuth(YSn, XSn, YSn1, XSn1)
                elif YTFn != None and XTFn != None and YTOn1 != None and XTOn1 != None:
                    t_Sn_Sn1 = Azimuth(YTFn, XTFn, YTOn1, XTOn1)
                elif YSn != None and XSn != None and YTFn != None and XTFn != None:
                    t_Sn_Sn1 = Azimuth(YSn, XSn, YTFn, XTFn)
                elif YTOn1 != None and XTOn1 != None and YSn1 != None and XSn1 != None:
                    t_Sn_Sn1 = Azimuth(YTOn1, XTOn1, YSn1, XSn1)

            if t_Sn_1_Sn  != None:
                t_Sn_Sn_1 = t_Sn_1_Sn + 200
                if t_Sn_Sn_1 >= 400:
                    t_Sn_Sn_1 = t_Sn_Sn_1 - 400
                if Curve == "Right Curve" and alfa != None:
                    t_TOn_TFn = t_Sn_1_Sn + alfa
                    t_TFn_TOn = t_TOn_TFn + 200
                    if t_TFn_TOn >= 400:
                        t_TFn_TOn = t_TFn_TOn - 400
                if Curve == "Left Curve" and alfa != None:
                    t_TOn_TFn = t_Sn_1_Sn - alfa
                    t_TFn_TOn = t_TOn_TFn + 200
                    if t_TFn_TOn >= 400:
                        t_TFn_TOn = t_TFn_TOn - 400

            if t_Sn_Sn1 != None:
                t_Sn1_Sn = t_Sn_Sn1 + 200
                if t_Sn1_Sn >= 400:
                    t_Sn1_Sn = t_Sn1_Sn - 400

            if YSn_1 == None:
                if YTFn_1 != None and SSn_1_TFn_1 != None and t_Sn_Sn_1 != None:
                    YSn_1 = np.round(YTFn_1 + SSn_1_TFn_1 * np.sin(Grad2Radyan(t_Sn_Sn_1)), 3)

            if XSn_1 == None:
                if XTFn_1 != None and SSn_1_TFn_1 != None and t_Sn_Sn_1 != None:
                    XSn_1 = np.round(XTFn_1 + SSn_1_TFn_1 * np.cos(Grad2Radyan(t_Sn_Sn_1)), 3)

            if YTFn_1 == None:
                if YSn_1 != None and SSn_1_TFn_1 != None and t_Sn_1_Sn != None:
                    YTFn_1 = np.round(YSn_1 + SSn_1_TFn_1 * np.sin(Grad2Radyan(t_Sn_1_Sn)), 3)
                elif YTOn != None and STFn_1_TOn != None and t_Sn_Sn_1 != None:
                    YTFn_1 = np.round(YTOn + STFn_1_TOn * np.sin(Grad2Radyan(t_Sn_Sn_1)), 3)

            if XTFn_1 == None:
                if XSn_1 != None and SSn_1_TFn_1 != None and t_Sn_1_Sn != None:
                    XTFn_1 = np.round(XSn_1 + SSn_1_TFn_1 * np.cos(Grad2Radyan(t_Sn_1_Sn)), 3)
                elif XTOn != None and STFn_1_TOn != None and t_Sn_Sn_1 != None:
                    XTFn_1 = np.round(XTOn + STFn_1_TOn * np.cos(Grad2Radyan(t_Sn_Sn_1)), 3)

            if YTOn == None:
                if YTFn_1 != None and STFn_1_TOn != None and t_Sn_1_Sn != None:
                    YTOn = np.round(YTFn_1 + STFn_1_TOn * np.sin(Grad2Radyan(t_Sn_1_Sn)), 3)
                elif YSn != None and t != None and t_Sn_Sn_1 != None:
                    YTOn = np.round(YSn + t * np.sin(Grad2Radyan(t_Sn_Sn_1)), 3)
                elif YTFn != None and STOn_TFn != None and t_TFn_TOn != None:
                    YTOn = np.round(YTFn + STOn_TFn * np.sin(Grad2Radyan(t_TFn_TOn)), 3)

            if XTOn == None:
                if XTFn_1 != None and STFn_1_TOn != None and t_Sn_1_Sn != None:
                    XTOn = np.round(XTFn_1 + STFn_1_TOn * np.cos(Grad2Radyan(t_Sn_1_Sn)), 3)
                elif XSn != None and t != None and t_Sn_Sn_1 != None:
                    XTOn = np.round(XSn + t * np.cos(Grad2Radyan(t_Sn_Sn_1)), 3)
                elif XTFn != None and STOn_TFn != None and t_TFn_TOn != None:
                    XTOn = np.round(XTFn + STOn_TFn * np.cos(Grad2Radyan(t_TFn_TOn)), 3)

            if YSn == None:
                if YTOn != None and t != None and t_Sn_1_Sn != None:
                    YSn = np.round(YTOn + t * np.sin(Grad2Radyan(t_Sn_1_Sn)), 3)
                if YTFn != None and t != None and t_Sn1_Sn != None:
                    YSn = np.round(YTFn + t * np.sin(Grad2Radyan(t_Sn1_Sn)), 3)

            if XSn == None:
                if XTOn != None and t != None and t_Sn_1_Sn != None:
                    XSn = np.round(XTOn + t * np.cos(Grad2Radyan(t_Sn_1_Sn)), 3)
                if XTFn != None and t != None and t_Sn1_Sn != None:
                    XSn = np.round(XTFn + t * np.cos(Grad2Radyan(t_Sn1_Sn)), 3)

            if YTFn == None:
                if YSn != None and t != None and t_Sn_Sn1 != None:
                    YTFn = np.round(YSn + t * np.sin(Grad2Radyan(t_Sn_Sn1)), 3)
                elif YTOn != None and STOn_TFn != None and t_TOn_TFn != None:
                    YTFn = np.round(YTOn + STOn_TFn * np.sin(Grad2Radyan(t_TOn_TFn)), 3)
                elif YTOn1 != None and STFn_TOn1 != None and t_Sn_Sn1 != None:
                    YTFn = np.round(YTOn1 + STFn_TOn1 * np.sin(Grad2Radyan(t_Sn_Sn1)), 3)

            if XTFn == None:
                if XSn != None and t != None and t_Sn_Sn1 != None:
                    XTFn = np.round(XSn + t * np.cos(Grad2Radyan(t_Sn_Sn1)), 3)
                elif XTOn != None and STOn_TFn != None and t_TOn_TFn != None:
                    XTFn = np.round(XTOn + STOn_TFn * np.cos(Grad2Radyan(t_TOn_TFn)), 3)
                elif XTOn1 != None and STFn_TOn1 != None and t_Sn_Sn1 != None:
                    XTFn = np.round(XTOn1 + STFn_TOn1 * np.cos(Grad2Radyan(t_Sn_Sn1)), 3)

            if YTOn1 == None:
                if YTFn != None and STFn_TOn1 != None and t_Sn_Sn1 != None:
                    YTOn1 = np.round(YTFn + STFn_TOn1 * np.sin(Grad2Radyan(t_Sn_Sn1)), 3)
                elif YSn1 != None and STOn1_Sn1 != None and t_Sn1_Sn != None:
                    YTOn1 = np.round(YSn1 + STOn1_Sn1 * np.sin(Grad2Radyan(t_Sn1_Sn)), 3)

            if XTOn1 == None:
                if XTFn != None and STFn_TOn1 != None and t_Sn_Sn1 != None:
                    XTOn1 = np.round(XTFn + STFn_TOn1 * np.cos(Grad2Radyan(t_Sn_Sn1)), 3)
                elif XSn1 != None and STOn1_Sn1 != None and t_Sn1_Sn != None:
                    XTOn1 = np.round(XSn1 + STOn1_Sn1 * np.cos(Grad2Radyan(t_Sn1_Sn)), 3)

            if YSn1 == None:
                if YTOn1 != None and STOn1_Sn1 != None and t_Sn_Sn_1 != None:
                    YSn1 = np.round(YTOn1 + STOn1_Sn1 * np.sin(Grad2Radyan(t_Sn_Sn_1)), 3)

            if XSn1 == None:
                if XTOn1 != None and STOn1_Sn1 != None and t_Sn_Sn_1 != None:
                    XSn1 = np.round(XTOn1 + STOn1_Sn1 * np.cos(Grad2Radyan(t_Sn_Sn_1)), 3)

            context = {
                "R_1" : R,
                "Delta_1" : Delta,
                "KSn_1_1" : KSn_1,
                "YSn_1_1" : YSn_1,
                "XSn_1_1" : XSn_1,
                "KTFn_1_1" : KTFn_1,
                "YTFn_1_1" : YTFn_1,
                "XTFn_1_1" : XTFn_1,
                "KTFn_1" : KTFn,
                "YTFn_1" : YTFn,
                "XTFn_1" : XTFn,
                "KSn_1" : KSn,
                "YSn_1" : YSn,
                "XSn_1" : XSn,
                "KTOn_1" : KTOn,
                "YTOn_1" : YTOn,
                "XTOn_1" : XTOn,
                "KTOn1_1" : KTOn1,
                "YTOn1_1" : YTOn1,
                "XTOn1_1" : XTOn1,
                "KSn1_1" : KSn1,
                "YSn1_1" : YSn1,
                "XSn1_1" : XSn1,
                "YM_1" : YM,
                "XM_1" : XM,
                "SSn_1_TFn_1_1" : SSn_1_TFn_1,
                "STFn_1_TOn_1" : STFn_1_TOn,
                "STFn_TOn1_1" : STFn_TOn1,
                "STOn1_Sn1_1" : STOn1_Sn1,
                "SSn_Sn_1_1" : SSn_Sn_1,
                "SSn_Sn1_1" : SSn_Sn1,
                "t_Sn_1_Sn_1" : t_Sn_1_Sn,
                "t_Sn_Sn1_1" : t_Sn_Sn1
            }

            print(context)
            for key in context.keys():
                if context[key] == None:
                    context[key] = ""
                context[key] = str(context[key])
            

        return render(request, "Horizontal_Route_Geometry.html", context)

    else:
        return render(request, "Horizontal_Route_Geometry.html")

"""
R_1
Delta_1
KSn_1_1
YSn_1_1
XSn_1_1
KTFn_1_1
YTFn_1_1
XTFn_1_1
KTFn_1
YTFn_1
XTFn_1
KSn_1
YSn_1
XSn_1
KTOn_1
YTOn_1
XTOn_1
KTOn1_1
YTOn1_1
XTOn1_1
KSn1_1
YSn1_1
XSn1_1
YM_1
XM_1
SSn_1_TFn_1_1
STFn_1_TOn_1
STFn_TOn1_1
STOn1_Sn1_1
SSn_Sn_1_1
SSn_Sn1_1
t_Sn_1_Sn_1
t_Sn_Sn1_1
"""

def Vertical_Route_Geometry(request):
    return HttpResponse("<h1 style='color: orange;'> Burası çalışıyor sıkıntı yok dayı devam et </h1>")




def Transition_Curves(request):
    return HttpResponse("<h1 style='color: orange;'> Burası çalışıyor sıkıntı yok dayı devam et </h1>")