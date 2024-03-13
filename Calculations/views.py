from django.http import request
from django.shortcuts import render, HttpResponse
from django.contrib import messages
import numpy as np




Ro = 2000000 / np.pi

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



def Fundamental_Computations(request):
    if request.method == "POST":
        if request.POST.get("YA1") != "":
            YA1 = request.POST.get("YA1")
        else:
            YA1 = None
        if request.POST.get("XA1") != "":
            XA1 = request.POST.get("XA1")
        else:
            XA1 = None
        if request.POST.get("tAB1") != "":
            tAB1 = request.POST.get("tAB1")
        else:
            tAB1 = None
        if request.POST.get("SAB1") != "":
            SAB1 = request.POST.get("SAB1")
        else:
            SAB1 = None

        try:
            YB = float(YA1) + float(SAB1) * np.sin(Grad2Radyan(float(tAB1))) 
            YB = np.round(YB, 3)
            XB = float(XA1) + float(SAB1) * np.cos(Grad2Radyan(float(tAB1))) 
            XB = np.round(XB, 3)
        except:
            YB = None
            YB = None
            XB = None
            XB = None

        if request.POST.get("YA2"):
            YA2 = request.POST.get("YA2")
        else:
            YA2 = None
        if request.POST.get("XA2"):
            XA2 = request.POST.get("XA2")
        else:
            XA2 = None
        if request.POST.get("YB2"):
            YB2 = request.POST.get("YB2")
        else:
            YB2 = None
        if request.POST.get("XB2"):
            XB2 = request.POST.get("XB2")
        else:
            XB2 = None

        try:
            DeltaYAB = (float(YB2) - float(YA2))
            DeltaXAB = (float(XB2) - float(XA2))
            DeltaYBA = (float(YA2) - float(YB2))
            DeltaXBA = (float(XA2) - float(XB2))
            SAB = np.round((DeltaYAB ** 2 + DeltaXAB ** 2) ** 0.5, 3)
            tAB = np.round(Radyan2Grad(np.round(np.arctan(DeltaYAB / DeltaXAB), 4)), 4)
            tBA = np.round(Radyan2Grad(np.round(np.arctan(DeltaYBA / DeltaXBA), 4)), 4)
            if DeltaYAB >= 0:
                if DeltaXAB >= 0:
                    tAB = tAB
                else:
                    tAB = tAB + 200
            else:
                if DeltaXAB >= 0:
                    tAB = tAB + 400
                else:
                    tAB = tAB + 200
            if DeltaYBA >= 0:
                if DeltaXBA >= 0:
                    tBA = tBA
                else:
                    tBA = tBA + 200
            else:
                if DeltaXBA >= 0:
                    tBA = tBA + 400
                else:
                    tBA = tBA + 200
        except:
            SAB = None
            tAB = None
            tBA = None

        if request.POST.get("tAB3") != "":
            tAB3 = request.POST.get("tAB3")
        else:
            tAB3 = None
        if request.POST.get("BetaB") != "":
            BetaB = request.POST.get("BetaB")
        else:
            BetaB = None

        try:
            tBC = float(tAB3) + float(BetaB)
            if tBC >= 200:
                tBC = tBC - 200
                if tBC >= 400:
                    tBC = tBC - 400
            elif tBC < 200:
                tBC = tBC + 200
            else:
                tBC = tBC
            tBC = np.round(tBC, 4)
        except:
            tBC = None

        context = {
            "YA1" : YA1,
            "XA1" : XA1,
            "tAB1" : tAB1,
            "SAB1" : SAB1,
            "YA2" : YA2,
            "XA2" : XA2,
            "YB2" : YB2,
            "XB2" : XB2,
            "tAB3" : tAB3,
            "BetaB" : BetaB,
            "YB" : YB,
            "XB" : XB,
            "SAB" : SAB,
            "tAB" : tAB,
            "tBA" : tBA,
            "tBC" : tBC
        }  

        for key in context.keys():
            if context[key] == None:
                context[key] = ""

        return render(request,"Fundamental_Computations.html", context)
    else:
        return render(request,"Fundamental_Computations.html")




def Horizontal_layout_with_Polar_Coordinates(request):
    if request.method == "POST":
        if request.POST.get("Gauss_Krueger") != "":
            R = request.POST.get("Gauss_Krueger")
        else:
            R = None
        if request.POST.get("Geoid_Undulation") != "":
            NA = request.POST.get("Geoid_Undulation")
        else:
            NA = None
        if request.POST.get("YP101") != "":
            YP101 = request.POST.get("YP101")
        else:
            YP101 = None
        if request.POST.get("XP101") != "":
            XP101 = request.POST.get("XP101")
        else:
            XP101 = None
        if request.POST.get("H_orth_P101") != "":
            HA = request.POST.get("H_orth_P101")
        else:
            HA = None
        if request.POST.get("YP102") != "":
            YP102 = request.POST.get("YP102")
        else:
            YP102 = None
        if request.POST.get("XP102") != "":
            XP102 = request.POST.get("XP102")
        else:
            XP102 = None
        if request.POST.get("YP") != "":
            YP = request.POST.get("YP")
        else:
            YP = None
        if request.POST.get("XP") != "":
            XP = request.POST.get("XP")
        else:
            XP = None

        try:
            if YP101 != None and XP101 != None and YP != None and XP != None:
                Sp = np.round(np.sqrt((float(YP101) - float(YP)) ** 2 + (float(XP101) - float(XP)) ** 2), 3)
                Ym = np.round(- ((float(YP101) - 500000) + (float(YP) - 500000)) / 2, 3)
            else:
                Sp = None
                Ym = None
            if Ym != None and R != None:
                Se = np.round(Sp / (1 + (float(Ym) ** 2 / (2 * (float(R) * 1000) ** 2))), 3)
            else:
                Se = None
            if Se != None and NA != None and R != None:
                Sg = np.round(Se * (1 + (float(NA) / (float(R) * 1000))), 3)
            else:
                Sg = None
            if Sg != None and R != None and HA != None:
                SAP = np.round(Sg * (((float(R) * 1000) + float(HA)) / (float(R) * 1000)), 3)
            else:
                SAP = None

            DeltaY_P101_P102 = float(YP102) - float(YP101)
            DeltaX_P101_P102 = float(XP102) - float(XP101)
            DeltaY_P101_P = float(YP) - float(YP101)
            DeltaX_P101_P = float(XP) - float(XP101)
            
            t_P101_P = np.round(Radyan2Grad(np.arctan(DeltaY_P101_P / DeltaX_P101_P)), 4)
            t_P101_P102 = np.round(Radyan2Grad(np.arctan(DeltaY_P101_P102 / DeltaX_P101_P102)), 4)

            if DeltaY_P101_P102 >= 0:
                if DeltaX_P101_P102 >= 0:
                    t_P101_P102 = t_P101_P102
                else:
                    t_P101_P102 = t_P101_P102 + 200

            else:
                if DeltaX_P101_P102 >= 0:
                    t_P101_P102 = t_P101_P102 + 400
                else:
                    t_P101_P102 = t_P101_P102 + 200

            if DeltaY_P101_P >= 0:
                if DeltaX_P101_P >= 0:
                    t_P101_P = t_P101_P
                else:
                    t_P101_P= t_P101_P + 200
            else:
                if DeltaX_P101_P >= 0:
                    t_P101_P = t_P101_P + 400
                else:
                    t_P101_P = t_P101_P + 200

            Beta = np.round(t_P101_P - t_P101_P102, 4)
            if Beta < 0:
                Beta += 400

        except:
            messages.error(request, "Eksik veya hatalı değer girdiniz!")
            t_P101_P = None
            t_P101_P102 = None
            Beta = None

        context = {
            "R" : R,
            "NA" : NA,
            "YP101" : YP101,
            "XP101" : XP101,
            "HA" : HA,
            "YP102" : YP102,
            "XP102" : XP102,
            "YP" : YP,
            "XP" : XP,
            "Sp" : Sp,
            "Ym" : Ym,
            "Se" : Se,
            "Sg" : Sg,
            "SAP" : SAP,
            "t_P101_P" : t_P101_P,
            "t_P101_P102" : t_P101_P102,
            "Beta" : Beta
        }

        for key in context.keys():
            if context[key] == None:
                context[key] = ""

        return render(request,"Horizontal_Layout_with_Polar_Coordinates.html", context)

    else:
        return render(request, "Horizontal_Layout_with_Polar_Coordinates.html")


def Centering_Errors(request):
    if request.method == "POST":
        def Forward():
            if S != None and n != None and sigma_r != None:
                sigma_qq = np.round((S * ((2 / n) ** 0.5) * (sigma_r / Ro)) * 1000, 2)
            else:
                sigma_qq = ""
            if sigma_qs != "" and sigma_qt != "" and sigma_ql != "" and sigma_qq != "":
                sigma_q = np.round(np.sqrt((sigma_qs + sigma_qt + sigma_ql) ** 2 + sigma_qq ** 2), 3)
            else:
                sigma_q = ""
            if sigma_ls != "" and sigma_ll != "" and sigma_lsigma != "":
                sigma_l = np.round(np.sqrt((sigma_ls + sigma_ll) ** 2 + sigma_lsigma ** 2), 3)
            else:
                sigma_l = ""
            if sigma_q != "" and sigma_l != "":
                sigma_p_calculated = np.round(np.sqrt(sigma_q ** 2 + sigma_l ** 2), 3)
            else:
                sigma_p_calculated = ""

            context = {
                "sigma_lq" : sigma_lq,
                "sigma_r" : sigma_r,
                "es" : es,
                "et" : et,
                "el" : el,
                "S" : S,
                "b" : b,
                "Beta" : Beta,
                "n" : n,
                "sigma_qs" : sigma_qs,
                "sigma_qq" : sigma_qq,
                "sigma_qt" : sigma_qt,
                "sigma_ls" : sigma_ls,
                "sigma_ll" : sigma_ll,
                "sigma_ql" : sigma_ql,
                "sigma_lsigma" : sigma_lsigma,
                "sigma_q" : sigma_q,
                "sigma_l" : sigma_l,
                "sigma_p_calculated" : sigma_p_calculated
            }

            for key in context.keys():
                if context[key] == None:
                    context[key] = ""

            return context

        def Backward():
            sigma_l = np.round(np.sqrt((sigma_ls + sigma_ll) ** 2 + sigma_lsigma ** 2), 2)
            if sigma_p != None:
                sigma_q = np.round(np.sqrt(sigma_p ** 2 - sigma_l ** 2), 2)
            else:
                sigma_q = ""

            sigma_qq = np.round((sigma_q ** 2 - (sigma_qs + sigma_qt + sigma_ql) ** 2) ** 0.5, 2)
            n_calculated = np.round(((S * np.sqrt(2) * sigma_r) / ((sigma_qq / 1000) * Ro)) ** 2, 2)

            context = {
                "sigma_lq" : sigma_lq,
                "sigma_r" : sigma_r,
                "es" : es,
                "et" : et,
                "el" : el,
                "S" : S,
                "b" : b,
                "Beta" : Beta,
                "n" : n,
                "sigma_qs" : sigma_qs,
                "sigma_qq" : sigma_qq,
                "sigma_qt" : sigma_qt,
                "sigma_ls" : sigma_ls,
                "sigma_ll" : sigma_ll,
                "sigma_ql" : sigma_ql,
                "sigma_lsigma" : sigma_lsigma,
                "sigma_q" : sigma_q,
                "sigma_l" : sigma_l,
                "sigma_p" : sigma_p,
                "n_calculated" : n_calculated
            }

            for key in context.keys():
                if context[key] == None:
                    context[key] = ""

            return context

        if request.POST.get("sigma_lq") != "":
            sigma_lq = request.POST.get("sigma_lq")
            try:
                a = float(sigma_lq.split("+")[0])
                c = float(sigma_lq.split("+")[1][0])
            except:
                messages.warning(request, "Lütfen \u03C3lq değerini a+cppm (örnek: 3+4ppm) şeklinde giriniz.")
        else:
            sigma_lq = None
            a = None
            c = None
        if request.POST.get("sigma_r") != "":
            sigma_r = request.POST.get("sigma_r")
        else:
            sigma_r = None
        if request.POST.get("es") != "":
            es = request.POST.get("es")
        else:
            es = None
        if request.POST.get("et") != "":
            et = request.POST.get("et")
        else:
            et = None
        if request.POST.get("el") != "":
            el = request.POST.get("el")
        else:
            el = None
        if request.POST.get("SP101_A_22") != "":
            S = request.POST.get("SP101_A_22")
        else:
            S = None
        if request.POST.get("SP101_P102_22") != "":
            b = request.POST.get("SP101_P102_22")
        else:
            b = None
        if request.POST.get("Beta_22") != "":
            Beta = request.POST.get("Beta_22")
        else:
            Beta = None
        if request.POST.get("n_22") != "":
            n = request.POST.get("n_22")
        else:
            n = None

        try:
            sigma_r = float(sigma_r)
            es = float(es)
            et = float(et)
            el = float(el)
            S = float(S)
            b = float(b)
            Beta = float(Beta)

            if es != None and b != None and Beta != None and S != None:
                sigma_qs = np.round((((es / 1000) / (3 * b)) * np.sqrt(b ** 2 - 2 * b * S * np.cos(Grad2Radyan(Beta)) + S ** 2)) * 1000, 2)
                sigma_ls = np.round(((es / 1000) / 3) * 1000, 2)
            else:
                sigma_qs = ""
                sigma_ls = ""
            if et != None and b != None:
                sigma_qt = np.round(((S * (et / 1000)) / (3 * b)) * 1000, 2)
            else:
                sigma_qt = ""
            if el != None:
                sigma_ll = np.round(((el / 1000) / 3) * 1000, 2)
                sigma_ql = np.round(((el / 1000) / 3) * 1000, 2)
            else:
                sigma_ll = ""
                sigma_ql = ""
            if a != None and c != None and S != None:
                sigma_lsigma = np.round((a ** 2 + c ** 2 * (S / 1000) ** 2) ** 0.5, 3)
            else:
                sigma_lsigma = ""

            if request.POST.get("sigma_p") == "":
                n = float(n)
                context = Forward()
            else:
                try:
                    sigma_p = float(request.POST.get("sigma_p"))
                    context = Backward()
                except:
                    n = float(n)
                    context = Forward()
        
        except:
            messages.error(request, "Eksik veya hatalı değer girdiniz")
            context = {
                "sigma_lq" : sigma_lq,
                "sigma_r" : sigma_r,
                "es" : es,
                "et" : et,
                "el" : el,
                "S" : S,
                "b" : b,
                "Beta" : Beta,
                "n" : n
            }

            for key in context.keys():
                if context[key] == None:
                    context[key] = ""

        for key in context.keys():
            context[key] = str(context[key])

        return render(request, "Centering_Errors.html", context)

    else:
        return render(request, "Centering_Errors.html")


