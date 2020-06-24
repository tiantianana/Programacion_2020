# -*- coding: utf-8 -*-

dinero = float(input("Introduce un dato numérico: \n"))

if dinero < 0:
    print("Introduce un número positivo.")
    dinero = float(input("Introduce un dato numérico: \n"))
    
b_500 = int(dinero / 500) 
dinero -= (b_500 * 500)
if b_500 > 0: print("500€:",b_500)

b_200 = int(dinero / 200)
dinero -= (b_200 * 200)
if b_200 > 0: print("200€:",b_200)

b_100 = int(dinero / 100)
dinero -= (b_100 * 100)
if b_100 > 0: print("100€:",b_100)

b_50 = int(dinero / 50)
dinero -= (b_50 * 50)
if b_50 > 0: print("50€:",b_50)

b_20 = int(dinero / 20)
dinero -= (b_20 * 20)
if b_20 > 0: print("20€:",b_20)

b_10 = int(dinero / 10)
dinero -= (b_10 * 10)
if b_10 > 0: print("10€:",b_10)

b_5 = int(dinero / 5)
dinero -= (b_5 * 5)
if b_5 > 0: print("5€:",b_5)

b_2 = int(dinero / 2)
dinero -= (b_2 * 2)
if b_2 > 0: print("2€:",b_2)

b_1 = int(dinero / 1)
dinero -= (b_1 * 1)
if b_1 > 0: print("1€:",b_1)

m_50 = int(dinero / 0.5)
dinero -= (m_50 * 0.5)
if m_50 > 0: print("0.50€:",m_50)

m_20 = int(dinero / 0.2)
dinero -= (m_20 * 0.2)
if m_20 > 0: print("0.20€:",m_20)

m_10 = int(dinero / 0.1)
dinero -= (m_10 * 0.1)
if m_10 > 0: print("0.10€:",m_10)

m_5 = int(dinero / 0.05)
dinero -= (m_5 * 0.05)
if m_5 > 0: print("0.05€:",m_5)
                   
m_2 = int(dinero / 0.02)
dinero -= (m_2 * 0.02)
if m_2 > 0: print("0.02€:",m_2)

m_1 = int(dinero / 0.01)
dinero -= (m_1 * 0.01)
if m_1 > 0: print("0.01€:",m_1)