# To calculate speed ~ cadence 

import numpy as np

durchmesser = 28 * 2.54 / 100

Umfang = durchmesser * np.pi

def geschwindigkeit_bei_kadenz(n_ritzel, n_kettenblatt):
  ratio = n_kettenblatt/n_ritzel
  # zurückgelegte Strecke pro Kurbelumdrehung
  strecke = ratio * Umfang
  # Kadenz als Umdrehungen pro Minute
  cadence = np.arange(50,151) 
  # zurückgelegte Strecke pro Minute
  strecke_pro_stunde = cadence * strecke
  # Umrechnung in km/h
  km_pro_stunde = strecke_pro_stunde * 60 / 1000
  return km_pro_stunde

geschwindigkeit_bei_kadenz(15, 49)

  
  

