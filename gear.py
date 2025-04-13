# To calculate speed ~ cadence 

import numpy as np

durchmesser = 28*2.54

Umfang = durchmesser * np.pi

def geschwindigkeit(n_ritzel, n_kettenblatt):
  ratio = n_kettenblatt/n_ritzel
  # zurückgelegte Strecke pro Kurbelumdrehung
  strecke = ratio * Umfang
  cadence = np.arrange(50,151) 
  # zurückgelegte Strecke pro Minute
  strecke_pro_min = cadence * strecke
  

