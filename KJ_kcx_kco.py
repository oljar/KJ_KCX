#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import sqlite3
from tkinter import *
import tkinter.ttk as ttk
import datetime
from tkinter import messagebox

# git
# utworzenie połączenia z bazą przechowywaną na dysku
# lub w pamięci (':memory:')
con = sqlite3.connect('baza_kcx_kco.db')

# dostęp do kolumn przez indeksy i przez nazwy
con.row_factory = sqlite3.Row

# utworzenie obiektu kursora
cur = con.cursor()







# lista zagnieżdzona przekazywania stanow kontrolek
l=200     #parametry listy-ilosc zagniezdzen
x=200    #parametry listy- ilosc zmiennych(str) w zagniezdzeniu
State=[]
for s in range(l):
    sub_list=[""]
    for y in range(x):

        sub_list.append(int(y))

        State.append(sub_list)

n=-1  #zmienna odpow. za poruszanie po bazie






# Klasa okna glownego
class Application(Frame):
    """Aplikacja GUI , sekret długowiecznosci"""
    def __init__(self,master,State,n):
        """Inicjuję ramkę"""
        super(Application,self).__init__(master)
        self.grid()
        self.nr_fab(State)
        self.kod_prod(State)
        self.nr_zlec(State)
        self.identyfikacja(State)
        self.tab_znamionowa(State)
        self.zasleki_raczki(State)
        self.estetyka(State)
        self.kapturki_srub (State)
        self.izolacja_filtry_uszczelki(State)
        self.taca_ociekowa(State)
        self.bypass_montaz_dzialanie(State)
        self.wentylatory_montaz_dzialanie(State)
        self.czujniki_temperatur(State)
        self.nagrzewnica_wtorna(State)
        self.montaz_rozdzielnicy(State)
        self.zamki_drzwi_oznaczenia(State)
        self.wydatek_szczelnosc(State)
        self.oslona_rozdzielnicy(State)
        self.dtr_ka_karta_produktu(State)

        self.okno_uwagi(State)
        self.podpis_kontrolera(State)

        self.btn_akcept()



        self.n=n



########################################################################################################################################################################################

    # poziom lini nr fabryczny


    def nr_fab(self,State):
        """numer fabryczny"""

        # utworz etykiete z zapytniem o nr fabryczny
        self.lbl_dist_0=Label(self)
        self.lbl_dist_0.grid(row = 0, column = 0 , padx=6)                               #dystans col 0

        self.lbl_nr_fab = Label(self, text ="Podaj nr fabryczny")
        self.lbl_nr_fab.grid(row = 0, column = 1 , sticky = W )

        self.lbl_dist_2=Label(self)
        self.lbl_dist_2.grid(row = 0, column = 2 , padx=5)                               #dystans  col  2

        self.lbl_dist_3=Label(self)
        self.lbl_dist_3.grid(row = 0, column = 3 , padx=1)                               #dystans   col 3



        # utworz widzet Entry do przyjecia nr_fab

        var1=StringVar()    # zmienna pomocnicza - ukrywanie wywswl - zera

        if State[0][1]==0 :
            var1.set("")
        else:
            var1.set(State[0][1])


        self.ent_nr_fab= Entry(self,textvariable=var1)
        self.ent_nr_fab.grid(row=0, column = 4)



        self.lbl_dist_5=Label(self)
        self.lbl_dist_5.grid(row = 0, column = 5 , padx=4)                               #dystans col  5

        #utworz przyciski 'archiwum'0

        self.btn_up = Button(self,text= "UP", command=self.arch_UP )
        self.btn_up.grid(row = 0, column=6 , ipadx=20 , sticky=E)

        self.btn_dn = Button(self,text= "DN", command=self.arch_DOWN )
        self.btn_dn.grid(row = 0, column=7 ,ipadx=20, sticky=W)




        self.lbl_dist_8=Label(self)
        self.lbl_dist_8.grid(row = 0, column = 5 , padx=4, pady=3)                               #dystans col  8


########################################################################################################################################################################################



    def kod_prod(self,State):


        self.lbl_kod_prod = Label(self, text ="Podaj kod produktu")
        self.lbl_kod_prod.grid(row = 1, column = 1 , sticky = W )



        var1=StringVar()    # zmienna pomocnicza - ukrywanie wywswl - zera

        if State[0][1]==0 :
            var1.set("")
            bad1_txt=""
        else:
            var1.set(State[0][2])
            bad1_txt ="Ostatnie badanie:"

        self.ent_kod_prod= Entry(self,textvariable=var1)
        self.ent_kod_prod.grid(row=1, column = 4)
        self.lbl_dist_9=Label(self)
        self.lbl_dist_9.grid(row = 1, column = 5,pady=3 )

        # Wyswietlanie komunikatu
        self.lbl_t1 = Label(self, text=bad1_txt)
        self.lbl_t1.grid(row = 1, column =6, columnspan=2)







########################################################################################################################################################################################


    def nr_zlec(self,State):

        # utworz etykiete z zapytniem o zlecenie
        self.lbl_nr_zlec = Label(self, text ="Podaj nr zlecenia")
        self.lbl_nr_zlec.grid(row = 2, column = 1 , columnspan = 1, sticky = W )


        # utworz widzet Entry do przyjecia zlecenia


        var2=StringVar()    # zmienna pomocnicza - ukrywanie wywswl - zera

        if State[0][1]==0 :
            var2.set("")
            bad2_txt=""
        else:
            var2.set(State[0][3])
            bad2_txt=str(State[0][22])+' '+str(State[0][23])



        self.ent_nr_zlec= Entry(self,textvariable=var2)
        self.ent_nr_zlec.grid(row=2, column = 4)

        self.lbl_dist_10=Label(self)
        self.lbl_dist_10.grid(row = 2, column = 5 , pady=3)




        self.lbl_t2 = Label(self, text = bad2_txt)
        self.lbl_t2.grid(row = 2, column =6, columnspan=2)


########################################################################################################################################################################################


    def identyfikacja(self,State):


        self.lbl_identity = Label(self, text ="Identyfikacja , nalepka z nr. fabrycznym ")
        self.lbl_identity.grid(row = 3, column = 1,sticky = W )
        self.identity = StringVar()
        self.identity.set(State[0][4])



        Radiobutton(self,
                    text =  "Tak",
                    variable = self.identity,
                    value = "Pozytyw",
                    ).grid(row = 3, column = 4,sticky=W)

        Radiobutton(self,
                    text =  "Nie",
                    variable = self.identity,
                    value = "Negatyw",
                    ).grid(row = 3, column = 4, sticky=E)



    # Wyswietlanie stanu   z bazy
        if State[0][1]!=0 :
            self.lbl_identyity_info = Label(self,text=State[0][4] )
            self.lbl_identyity_info.grid(row = 3, column = 7)

#######################################################################################################################################################################################



    #poziom lini filtry uszczelka
    def tab_znamionowa(self,State):

        self.lbl_filter_gasket = Label(self, text ="Tab. zn-wa, klasa ener-czna")
        self.lbl_filter_gasket.grid(row = 4, column = 1,sticky = W )

        self.filter_gasket = StringVar()

        self.filter_gasket.set(State[0][5])


        Radiobutton(self,
                    text =  "Tak",
                    variable = self.filter_gasket,
                    value = "Pozytyw",
                   # command = self.update_text
                    ).grid(row = 4, column = 4,sticky=W)

        Radiobutton(self,
                    text =  "Nie",
                    variable = self.filter_gasket,
                    value = "Negatyw",
                   #command = self.update_text
                    ).grid(row = 4, column = 4,sticky=E)


# Wyswietlanie stanu  z bazy

        if  State[0][1]!=0 :
            self.lbl_filter_gasket_info = Label(self,text=State[0][5])
            self.lbl_filter_gasket_info.grid(row = 4, column = 7)


        self.lbl_dist_9=Label(self)
        self.lbl_dist_9.grid(row = 100, column = 5 , pady=2)





######################################################################################################################################################################################


    #poziom lini filtry uszczelka
    def tab_znamionowa(self,State):

        self.lbl_filter_gasket = Label(self, text ="Oznaczenie króćców")
        self.lbl_filter_gasket.grid(row = 4, column = 1,sticky = W )

        self.filter_gasket = StringVar()

        self.filter_gasket.set(State[0][5])


        Radiobutton(self,
                    text =  "Tak",
                    variable = self.filter_gasket,
                    value = "Pozytyw",
                   # command = self.update_text
                    ).grid(row = 4, column = 4,sticky=W)

        Radiobutton(self,
                    text =  "Nie",
                    variable = self.filter_gasket,
                    value = "Negatyw",
                   #command = self.update_text
                    ).grid(row = 4, column = 4,sticky=E)


# Wyswietlanie stanu  z bazy

        if  State[0][1]!=0 :
            self.lbl_filter_gasket_info = Label(self,text=State[0][5])
            self.lbl_filter_gasket_info.grid(row = 4, column = 7)


        self.lbl_dist_9=Label(self)
        self.lbl_dist_9.grid(row = 100, column = 5 , pady=2)




######################################################################################################################################################################################



    #poziom lini szczelnosc wymiennika
    def zasleki_raczki(self,State):

        self.lbl_czynnosc = Label(self, text ="Zaślepki srub, rączki, pozost.naklejki")
        self.lbl_czynnosc.grid(row = 5, column = 1,sticky = W )

        self.szczel_wymien = StringVar()

        self.szczel_wymien.set(State[0][6])


        Radiobutton(self,
                    text =  "Tak",
                    variable = self.szczel_wymien,
                    value = "Pozytyw",
                    ).grid(row = 5, column = 4,sticky=W)

        Radiobutton(self,
                    text =  "Nie",
                    variable = self.szczel_wymien,
                    value = "Negatyw",
                    ).grid(row = 5, column = 4,sticky=E)


# Wyswietlanie stanu  z bazy

        if  State[0][1]!=0 :
            self.lbl_czynnosc_info = Label(self,text=State[0][6])
            self.lbl_czynnosc_info.grid(row = 5, column = 7)





#######################################################################################################################################################################################





    #poziom lini Silikonowanie  i dławice
    def estetyka(self,State):


        self.lbl_czynnosc = Label(self, text ="Estetyka - silikonowanie , porysowania ")
        self.lbl_czynnosc.grid(row = 6, column = 1,sticky = W )

        self.prow_kon_przew = StringVar()

        self.prow_kon_przew.set(State[0][7])


        Radiobutton(self,
                    text =  "Tak",
                    variable = self.prow_kon_przew,
                    value = "Pozytyw",
                    ).grid(row = 6, column = 4,sticky=W)

        Radiobutton(self,
                    text =  "Nie",
                    variable = self.prow_kon_przew,
                    value = "Negatyw",
                    ).grid(row = 6, column = 4,sticky=E)


# Wyswietlanie stanu  z bazy

        if  State[0][1]!=0 :
            self.lbl_czynnosc_info = Label(self,text=State[0][7])
            self.lbl_czynnosc_info.grid(row = 6, column = 7)


########################################################################################################################################################################################



    #poziom lini Poprawność montażu NW
    def kapturki_srub (self,State):

        self.lbl_czynnosc = Label(self, text ="Kapturki srub nagrzew, znaczki uziemień" )
        self.lbl_czynnosc.grid(row = 7, column = 1,sticky = W )

        self.mon_NW = StringVar()

        self.mon_NW.set(State[0][8])


        Radiobutton(self,
                    text =  "Tak",
                    variable = self.mon_NW,
                    value = "Pozytyw",
                    ).grid(row = 7, column = 4,sticky=W)

        Radiobutton(self,
                    text =  "Nie",
                    variable = self.mon_NW,
                    value = "Negatyw",
                    ).grid(row = 7, column = 4,sticky=E)

        Radiobutton(self,
                    text =  "Brak",
                    variable = self.mon_NW,
                    value = "Brak",
                    ).grid(row = 7, column = 6,sticky=E, padx=15)


# Wyswietlanie stanu  z bazy

        if  State[0][1]!=0 :
            self.lbl_czynnosc_info = Label(self,text=State[0][8])
            self.lbl_czynnosc_info.grid(row = 7, column = 7)


        self.lbl_dist_9=Label(self)
        self.lbl_dist_9.grid(row = 100, column = 5 , pady=2)                                       #dystans col  9




########################################################################################################################################################################################



    #poziom lini Poprawność montażu NW
    def kapturki_srub (self,State):

        self.lbl_czynnosc = Label(self, text ="poprawnosc ułożenia izolacji" )
        self.lbl_czynnosc.grid(row = 7, column = 1,sticky = W )

        self.mon_NW = StringVar()

        self.mon_NW.set(State[0][8])


        Radiobutton(self,
                    text =  "Tak",
                    variable = self.mon_NW,
                    value = "Pozytyw",
                    ).grid(row = 7, column = 4,sticky=W)

        Radiobutton(self,
                    text =  "Nie",
                    variable = self.mon_NW,
                    value = "Negatyw",
                    ).grid(row = 7, column = 4,sticky=E)

        Radiobutton(self,
                    text =  "Brak",
                    variable = self.mon_NW,
                    value = "Brak",
                    ).grid(row = 7, column = 6,sticky=E, padx=15)


# Wyswietlanie stanu  z bazy

        if  State[0][1]!=0 :
            self.lbl_czynnosc_info = Label(self,text=State[0][8])
            self.lbl_czynnosc_info.grid(row = 7, column = 7)


        self.lbl_dist_9=Label(self)
        self.lbl_dist_9.grid(row = 100, column = 5 , pady=2)                                       #dystans col  9




########################################################################################################################################################################################



    #poziom lini Poprawność motażu układu sterownia - wart. zabezp. nadprąd.
    def izolacja_filtry_uszczelki(self,State):


        self.lbl_czynnosc = Label(self, text ="Filtry, uszczelki " )
        self.lbl_czynnosc.grid(row = 8, column = 1,sticky = W )

        self.mon_roz = StringVar()

        self.mon_roz.set(State[0][9])


        Radiobutton(self,
                    text =  "Tak",
                    variable = self.mon_roz,
                    value = "Pozytyw",
                    ).grid(row = 8, column = 4,sticky=W)

        Radiobutton(self,
                    text =  "Nie",
                    variable = self.mon_roz,
                    value = "Negatyw",
                    ).grid(row = 8, column = 4,sticky=E)


# Wyswietlanie stanu  z bazy

        if  State[0][1]!=0 :
            self.lbl_czynnosc_info = Label(self,text=State[0][9])
            self.lbl_czynnosc_info.grid(row = 8, column = 7)



########################################################################################################################################################################################



    #poziom lini Działanie wentylatorów i presostatów.
    def taca_ociekowa(self,State):


        self.lbl_czynnosc = Label(self, text ="Taca ociekowa - szczel.-malow.-silk-nie, " )
        self.lbl_czynnosc.grid(row = 9, column = 1,sticky = W )

        self.dzial_went = StringVar()

        self.dzial_went.set(State[0][10])


        Radiobutton(self,
                    text =  "Tak",
                    variable = self.dzial_went,
                    value = "Pozytyw",
                    ).grid(row = 9, column = 4,sticky=W)

        Radiobutton(self,
                    text =  "Nie",
                    variable = self.dzial_went,
                    value = "Negatyw",
                    ).grid(row = 9, column = 4,sticky=E)


# Wyswietlanie stanu  z bazy

        if  State[0][1]!=0 :
            self.lbl_czynnosc_info = Label(self,text=State[0][10])
            self.lbl_czynnosc_info.grid(row = 9, column = 7)



########################################################################################################################################################################################



    #poziom lini montaż czujniki
    def bypass_montaz_dzialanie(self,State):


        self.lbl_czynnosc = Label(self, text ="Bypass - montaż i działanie, szczelność" )
        self.lbl_czynnosc.grid(row = 10, column = 1,sticky = W )

        self.mon_czujn = StringVar()

        self.mon_czujn.set(State[0][11])


        Radiobutton(self,
                    text =  "Tak",
                    variable = self.mon_czujn,
                    value = "Pozytyw",
                    ).grid(row = 10, column = 4,sticky=W)

        Radiobutton(self,
                    text =  "Nie",
                    variable = self.mon_czujn,
                    value = "Negatyw",
                    ).grid(row = 10, column = 4,sticky=E)


# Wyswietlanie stanu  z bazy

        if  State[0][1]!=0 :
            self.lbl_czynnosc_info = Label(self,text=State[0][11])
            self.lbl_czynnosc_info.grid(row = 10, column = 7)


####################################################################################################################################################################################


    #poziom Działanie nagrzewnicy i wywołanie alarmu
    def wentylatory_montaz_dzialanie(self,State):


        self.lbl_czynnosc = Label(self, text ="Wentylatory- montaż , działnie" )
        self.lbl_czynnosc.grid(row = 11, column = 1,sticky = W )

        self.dzial_NW = StringVar()

        self.dzial_NW.set(State[0][12])


        Radiobutton(self,
                    text =  "Tak",
                    variable = self.dzial_NW,
                    value = "Pozytyw",
                    ).grid(row = 11, column = 4,sticky=W)

        Radiobutton(self,
                    text =  "Nie",
                    variable = self.dzial_NW,
                    value = "Negatyw",
                    ).grid(row = 11, column = 4,sticky=E)
        Radiobutton(self,
                    text =  "Brak",
                    variable = self.dzial_NW,
                    value = "Brak",
                    ).grid(row = 11 , column = 6,sticky=E, padx=15)


# Wyswietlanie stanu  z bazy

        if  State[0][1]!=0 :
            self.lbl_czynnosc_info = Label(self,text=State[0][12])
            self.lbl_czynnosc_info.grid(row = 11, column = 7)


#######################################################################################################################################################################################



    #poziom Działanie nagrzewnicy i wywołanie alarmu
    def czujniki_temperatur(self,State):


        self.lbl_czynnosc = Label(self, text ="Czujniki temeratur -montaż, działanie" )
        self.lbl_czynnosc.grid(row = 12, column = 1,sticky = W )

        self.ustaw_ster = StringVar()

        self.ustaw_ster.set(State[0][13])


        Radiobutton(self,
                    text =  "Tak",
                    variable = self.ustaw_ster,
                    value = "Pozytyw",
                    ).grid(row = 12, column = 4,sticky=W)

        Radiobutton(self,
                    text =  "Nie",
                    variable = self.ustaw_ster,
                    value = "Negatyw",
                    ).grid(row = 12, column = 4,sticky=E)


# Wyswietlanie stanu  z bazy

        if  State[0][1]!=0 :
            self.lbl_czynnosc_info = Label(self,text=State[0][13])
            self.lbl_czynnosc_info.grid(row = 12, column = 7)


#######################################################################################################################################################################################


    #poziom Kontrola urządzeniem Metrel
    def nagrzewnica_wtorna (self,State):


        self.lbl_czynnosc = Label(self, text ="Nagrzewnica- montaż, działenie, alarm " )
        self.lbl_czynnosc.grid(row = 13, column = 1,sticky = W )

        self.kontr_metrel = StringVar()

        self.kontr_metrel.set(State[0][14])


        Radiobutton(self,
                    text =  "Tak",
                    variable = self.kontr_metrel,
                    value = "Pozytyw",
                    ).grid(row = 13, column = 4,sticky=W)

        Radiobutton(self,
                    text =  "Nie",
                    variable = self.kontr_metrel,
                    value = "Negatyw",
                    ).grid(row = 13, column = 4,sticky=E)


# Wyswietlanie stanu  z bazy

        if  State[0][1]!=0 :
            self.lbl_czynnosc_info = Label(self,text=State[0][14])
            self.lbl_czynnosc_info.grid(row = 13, column = 7)


#######################################################################################################################################################################################


#Montaż rozdzielnicy


    def montaz_rozdzielnicy (self,State):

        self.lbl_czynnosc = Label(self, text ="Montaż rozdzielnicy")
        self.lbl_czynnosc.grid(row = 14, column = 1,sticky = W )

        self.kontr_metrel = StringVar()

        self.kontr_metrel.set(State[0][14])


        Radiobutton(self,
                    text =  "Tak",
                    variable = self.kontr_metrel,
                    value = "Pozytyw",
                    ).grid(row = 14, column = 4,sticky=W)

        Radiobutton(self,
                    text =  "Nie",
                    variable = self.kontr_metrel,
                    value = "Negatyw",
                    ).grid(row = 14, column = 4,sticky=E)


# Wyswietlanie stanu  z bazy

        if  State[0][1]!=0 :
            self.lbl_czynnosc_info = Label(self,text=State[0][14])
            self.lbl_czynnosc_info.grid(row = 13, column = 7)












#######################################################################################################################################################################################


    def zamki_drzwi_oznaczenia  (self,State):


        self.lbl_czynnosc = Label(self, text ="Spasowanie dzwi i zamków, oznacznia, rączki" )
        self.lbl_czynnosc.grid(row = 15, column = 1,sticky = W )

        self.kontr_ozn = StringVar()

        self.kontr_ozn.set(State[0][15])


        Radiobutton(self,
                    text =  "Tak",
                    variable = self.kontr_ozn,
                    value = "Pozytyw",
                    ).grid(row = 15, column = 4,sticky=W)

        Radiobutton(self,
                    text =  "Nie",
                    variable = self.kontr_ozn,
                    value = "Negatyw",
                    ).grid(row = 15, column = 4,sticky=E)


# Wyswietlanie stanu  z bazy

        if  State[0][1]!=0 :
            self.lbl_czynnosc_info = Label(self,text=State[0][15])
            self.lbl_czynnosc_info.grid(row = 15, column = 7)



#######################################################################################################################################################################################


    def wydatek_szczelnosc  (self,State):


        self.lbl_czynnosc = Label(self, text ="Wydatek i szczelność" )
        self.lbl_czynnosc.grid(row = 16, column = 1,sticky = W )

        self.estetyka = StringVar()

        self.estetyka.set(State[0][16])


        Radiobutton(self,
                    text =  "Tak",
                    variable = self.estetyka,
                    value = "Pozytyw",
                    ).grid(row = 16, column = 4,sticky=W)

        Radiobutton(self,
                    text =  "Nie",
                    variable = self.estetyka,
                    value = "Negatyw",
                    ).grid(row = 16, column = 4,sticky=E)


# Wyswietlanie stanu  z bazy

        if  State[0][1]!=0 :
            self.lbl_czynnosc_info = Label(self,text=State[0][16])
            self.lbl_czynnosc_info.grid(row = 16, column = 7)


#######################################################################################################################################################################################

# Osłona rozdzielnicy z pikt. ostrzegawczym

    def oslona_rozdzielnicy  (self,State):


        self.lbl_czynnosc = Label(self, text ="Osłona rozdzielnicy z z-kiem ostrzegawczym" )
        self.lbl_czynnosc.grid(row = 17, column = 1,sticky = W )

        self.estetyka = StringVar()

        self.estetyka.set(State[0][16])


        Radiobutton(self,
                    text =  "Tak",
                    variable = self.estetyka,
                    value = "Pozytyw",
                    ).grid(row = 17, column = 4,sticky=W)

        Radiobutton(self,
                    text =  "Nie",
                    variable = self.estetyka,
                    value = "Negatyw",
                    ).grid(row = 17, column = 4,sticky=E)


# Wyswietlanie stanu  z bazy

        if  State[0][1]!=0 :
            self.lbl_czynnosc_info = Label(self,text=State[0][16])
            self.lbl_czynnosc_info.grid(row = 16, column = 7)






#######################################################################################################################################################################################
    #poziom Kontrola dokręcenia paskow osłon

    def dtr_ka_karta_produktu  (self,State):


        self.lbl_czynnosc = Label(self, text ="DTR-ka i karta produktu, oznaczene KJ" )
        self.lbl_czynnosc.grid(row = 16, column = 1,sticky = W )

        self.dokr_pas = StringVar()

        self.dokr_pas.set(State[0][17])


        Radiobutton(self,
                    text =  "Tak",
                    variable = self.dokr_pas,
                    value = "Pozytyw",
                    ).grid(row = 16, column = 4,sticky=W)

        Radiobutton(self,
                    text =  "Nie",
                    variable = self.dokr_pas,
                    value = "Negatyw",
                    ).grid(row = 16, column = 4,sticky=E)


# Wyswietlanie stanu  z bazy

        if  State[0][1]!=0 :
            self.lbl_czynnosc_info = Label(self,text=State[0][17])
            self.lbl_czynnosc_info.grid(row = 16, column = 7)
                                             #dystans col  9


#######################################################################################################################################################################################

#######################################################################################################################################################################################
    #poziom Kontrola dokręcenia paskow osłon

    def Oznaczenie_KJ (self,State):


        self.lbl_czynnosc = Label(self, text ="Oznaczene KJ" )
        self.lbl_czynnosc.grid(row = 16, column = 1,sticky = W )

        self.dokr_pas = StringVar()

        self.dokr_pas.set(State[0][17])


        Radiobutton(self,
                    text =  "Tak",
                    variable = self.dokr_pas,
                    value = "Pozytyw",
                    ).grid(row = 16, column = 4,sticky=W)

        Radiobutton(self,
                    text =  "Nie",
                    variable = self.dokr_pas,
                    value = "Negatyw",
                    ).grid(row = 16, column = 4,sticky=E)


# Wyswietlanie stanu  z bazy

        if  State[0][1]!=0 :
            self.lbl_czynnosc_info = Label(self,text=State[0][17])
            self.lbl_czynnosc_info.grid(row = 16, column = 7)
                                             #dystans col  9


    #poziom Kompletnosc dostawy
    def   kompletnosc_dostawy(self,State):


        self.lbl_czynnosc = Label(self, text ="Kompletność dostawy" )
        self.lbl_czynnosc.grid(row = 17, column = 1,sticky = W )

        self.kmpl_dost = StringVar()

        self.kmpl_dost.set(State[0][18])


        Radiobutton(self,
                    text =  "Tak",
                    variable = self.kmpl_dost,
                    value = "Pozytyw",
                    ).grid(row = 17, column = 4,sticky=W)

        Radiobutton(self,
                    text =  "Nie",
                    variable = self.kmpl_dost,
                    value = "Negatyw",
                    ).grid(row = 17, column = 4,sticky=E)


# Wyswietlanie stanu  z bazy

        if  State[0][1]!=0 :
            self.lbl_czynnosc_info = Label(self,text=State[0][18])
            self.lbl_czynnosc_info.grid(row = 17, column = 7)
                                     #dystans col  9


#######################################################################################################################################################################################

    def okno_uwagi(self,State):

        self.lbl_dist_9=Label(self,text ="Uwagi")
        self.lbl_dist_9.grid(row = 18, column = 1 , sticky =W)  # dystans


     #utworz widzet Entry do przyjecia textu z okna uwag

        var3=StringVar() # zmienna pomocnicza - ukrywanie wywswl - zera
        var3=State [0][19]
        self.uwagi_txt = Text(self, width = 48, height = 5, wrap=WORD )
        self.uwagi_txt.grid(row = 19, column = 1, columnspan = 6 , sticky =W)

        if State[0][1]==0 :
            self.uwagi_txt.insert(END," ")
        else:
            self.uwagi_txt.insert(END,var3)

        self.lbl_dist_10=Label(self)
        self.lbl_dist_10.grid(row = 20, column = 1)



        self.uwagi_bool = StringVar()
        self.uwagi_bool.set(State[0][20])


        Radiobutton(self,
                    text =  "Tak",
                    variable = self.uwagi_bool,
                    value = "Pozytyw",
                    ).grid(row = 18, column = 4,sticky=W)

        Radiobutton(self,
                    text =  "Nie",
                    variable = self.uwagi_bool,
                    value = "Negatyw",
                    ).grid(row = 18, column = 4,sticky=E)



        if  State[0][1]!=0 :
            self.lbl_czynnosc_info = Label(self,text=State[0][20])
            self.lbl_czynnosc_info.grid(row = 18, column = 7)



####################################################################################################################################################################################

    def podpis_kontrolera(self,State):
        self.podpis = StringVar()
        self.combobox = ttk.Combobox(self, textvariable = self.podpis)
        self.combobox.grid(row = 21, column = 4, columnspan = 6 , sticky =W)
        self.combobox['values'] = ('','Jarosław Olszewski', 'Piotr Tylak')
        self.combobox.current(0)
        a=State[0][21]
        if a=='Jarosław Olszewski':
            self.combobox.current(1)
        if a=='Piotr Tylak':
            self.combobox.current(2)





######################################################################################################################################################################################






    #poziom lini przycisk akceptuj

    def btn_akcept(self):
        #utworz przycisk - akceptuj- poziom
        self.submit_bttn = Button(self, text ="Akceptuj", command = self.ostrzezenie_zapis)
        self.submit_bttn.grid(row = 21, column = 1)


    def ostrzezenie_zapis(self):
        if messagebox.askyesno("Zapis danych", "Czy zapisać dane ?"):
            self.akcept()






    # funkcja przycisku akeptuj
    def akcept (self):

        dt = datetime.datetime.now()
        now_d = dt.strftime("%d-%m-%Y")
        now_h = dt.strftime("%H:%M")

        contens1 = str(self.ent_nr_fab.get())
        contens2 = str(self.ent_kod_prod.get())
        contens3 = str(self.ent_nr_zlec.get())
        id1 = self.identity.get()
        id2 = self.filter_gasket.get()
        id3 = self.szczel_wymien.get()
        id4 = self.prow_kon_przew.get()
        id5 = self.mon_NW.get()
        id6 = self.mon_roz.get()
        id7 = self.dzial_went.get()
        id8 = self.mon_czujn.get()
        id9 = self.dzial_NW.get()
        id10 = self.ustaw_ster.get()
        id11 = self.kontr_metrel.get()
        id12 = self.kontr_ozn.get()
        id13 = self.estetyka.get()
        id14 = self.dokr_pas.get()
        id15 = self.kmpl_dost.get()
        id16 = self.uwagi_txt.get(1.0, END)
        id17 = self.uwagi_bool.get()
        id18 = self.podpis.get()
        id19 = now_d
        id20 = now_h
       # messagebox.showinfo("Check window", contens1+";"+contens2+";"+ contens3+";"+id1+";"+id2+";"+id3\
       # +";" + id4+";"+id5+";"+id6+";"+id7+";"+id8+";"+id9+";"+id10+";"+id11+";"+id12+";"+id13+";"+id14+";"+id15+"")
        cur.execute('INSERT INTO tab VALUES (NULL,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?);',(contens1,contens2,contens3,\
        id1,id2,id3,id4,id5,id6,id7,id8,id9,id10,id11,id12,id13,id14,id15,id16,id17,id18,id19,id20))

        messagebox.showinfo("Zapis danych", "Zapisano")
        con.commit()






    #  funkcja zwiększająca zmeinną sterującą bazą
    def arch_UP(self):
        self.n+=1
        self.arch(n)

    #  funkcja zmniejszająca zmeinną sterującą bazą
    def arch_DOWN(self):
        self.n-=1
        self.arch(n)




########################################################################################################################################################################################

    # funkcja przycisku archiwizacja - THE END
    def arch (self,n):
        State=[]


        cur.execute(
            """
            SELECT ID,nr_fabr,kod_prod, nr_zlec,identyfikacja,filtry_uszczelki,szczel_wymien,prowadz_przew_kon, mon_NW, mon_roz,\
            dzial_went,mon_czujn,dzial_NW,ustaw_ster, kontr_metrel,kontr_ozn, estetyka, kontr_pas, kmpl_dost, uwagi, uwagi_bool, podpis, now_d, now_h FROM tab

            """)
        State_Train = cur.fetchall()
        State=State_Train[self.n:]


        self.grid_remove()

        app1 = Application(root,State,self.n)
        return State,app1,n







# czesc glowna


root = Tk()
root.title("KJ KCX KCO")
root.geometry("580x670")



app = Application(root,State,n)



root.mainloop()

