# -*- coding: utf-8 -*-
"""
Created on Tue Nov  2 09:08:26 2021
Automatizaci贸n para 
@author: JuanM
"""

# -*- coding: utf-8 -*-
# Librerias

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


#Inicio del Navegador

start = webdriver.ChromeOptions()
start.add_argument('--start-maximized')
driver_path = 'RutaDel/chromedriver.exe'
driver = webdriver.Chrome(driver_path, chrome_options=start) 

#Inicio de Sesion en Moodle
    #Credenciales e ID del curso
User = ""
Pass = ""
Cursos = []

#Array de Id de Catgorias (idnumber):
B1= ["=average([[TcogSem1]]; [[TcogSem2]]; [[TcogSem3]]; [[TcogSem4]]; [[TcogSem5]]; [[TcogSem6]]; [[TcogSem7]]; [[TcogSem8]])",
 "=average([[TproSem1]];[[TproSem2]];[[TproSem3]];[[TproSem4]];[[TproSem5]];[[TproSem6]];[[TproSem7]];[[TproSem8]])",
 "=average([[TaxiSem1]];[[TaxiSem2]];[[TaxiSem3]];[[TaxiSem4]];[[TaxiSem5]];[[TaxiSem6]];[[TaxiSem7]];[[TaxiSem8]])",
 "=average([[TactSem1]]; [[TactSem2]];[[TactSem3]];[[TactSem4]];[[TactSem5]];[[TactSem6]];[[TactSem7]];[[TactSem8]])",
 "=average([[TcomSem1]];[[TcomSem2]];[[TcomSem3]];[[TcomSem4]];[[TcomSem5]];[[TcomSem6]];[[TcomSem7]];[[TcomSem8]])"]
B2= ["=average([[TcogSem9]]; [[TcogSem10]]; [[TcogSem11]]; [[TcogSem12]]; [[TcogSem13]]; [[TcogSem14]]; [[TcogSem15]]; [[TcogSem16]])",
 "=average([[TproSem9]]; [[TproSem10]]; [[TproSem11]]; [[TproSem12]]; [[TproSem13]]; [[TproSem14]]; [[TproSem15]]; [[TproSem16]])",
 "=average([[TaxiSem9]]; [[TaxiSem10]]; [[TaxiSem11]]; [[TaxiSem12]]; [[TaxiSem13]]; [[TaxiSem14]]; [[TaxiSem15]]; [[TaxiSem16]])",
 "=average([[TactSem9]]; [[TactSem10]]; [[TactSem11]]; [[TactSem12]]; [[TactSem13]]; [[TactSem14]]; [[TactSem15]]; [[TactSem16]])",
 "=average([[TcomSem9]]; [[TcomSem10]]; [[TcomSem11]]; [[TcomSem12]]; [[TcomSem13]]; [[TcomSem14]]; [[TcomSem15]]; [[TcomSem16]])"]
B3= ["=average([[TcogSem17]]; [[TcogSem18]]; [[TcogSem19]]; [[TcogSem20]]; [[TcogSem21]]; [[TcogSem22]]; [[TcogSem23]]; [[TcogSem24]])",
 "=average([[TproSem17]]; [[TproSem18]]; [[TproSem19]]; [[TproSem20]]; [[TproSem21]]; [[TproSem22]]; [[TproSem23]]; [[TproSem24]])",
 "=average([[TaxiSem17]]; [[TaxiSem18]]; [[TaxiSem19]]; [[TaxiSem20]]; [[TaxiSem21]]; [[TaxiSem22]]; [[TaxiSem23]]; [[TaxiSem24]])",
 "=average([[TactSem17]]; [[TactSem18]]; [[TactSem19]]; [[TactSem20]]; [[TactSem21]]; [[TactSem22]]; [[TactSem23]]; [[TactSem24]])",
 "=average([[TcomSem17]]; [[TcomSem18]]; [[TcomSem19]]; [[TcomSem20]]; [[TcomSem21]]; [[TcomSem22]]; [[TcomSem23]]; [[TcomSem24]])"]
B4= ["=average([[TcogSem25]]; [[TcogSem26]]; [[TcogSem27]]; [[TcogSem28]]; [[TcogSem29]]; [[TcogSem30]]; [[TcogSem31]]; [[TcogSem32]])",
 "=average([[TproSem25]]; [[TproSem26]]; [[TproSem27]]; [[TproSem28]]; [[TproSem29]]; [[TproSem30]]; [[TproSem31]]; [[TproSem32]])",
 "=average([[TaxiSem25]]; [[TaxiSem26]]; [[TaxiSem27]]; [[TaxiSem28]]; [[TaxiSem29]]; [[TaxiSem30]]; [[TaxiSem31]]; [[TaxiSem32]])",
 "=average([[TactSem25]]; [[TactSem26]]; [[TactSem27]]; [[TactSem28]]; [[TactSem29]]; [[TactSem30]]; [[TactSem31]]; [[TactSem32]])",
 "=average([[TcomSem25]]; [[TcomSem26]]; [[TcomSem27]]; [[TcomSem28]]; [[TcomSem29]]; [[TcomSem30]]; [[TcomSem31]]; [[TcomSem32]])"]

def Login():
#Script login y administraci贸n
 driver.get("https://sudominio.com/moodle")
 WebDriverWait(driver, 10)
# WaitPageLogin = .until(EC.presence_of_element_located((By.ID, "password")))
 input_User = driver.find_element_by_id('username')
 input_Pass = driver.find_element_by_id('password')
 input_User.send_keys(User)
 input_Pass.send_keys(Pass)
 SubmitB = driver.find_element_by_id("loginbtn").click()
 

def ArblCurso(CursoID): 
#Entra a la interfaz de edici贸n del curso.
  driver.get("https://sudominio.com/moodle/grade/edit/tree/index.php?id=" + str(CursoID))
 
 #Ingresa a la edici贸n del calculo de cada componente.
def selectCalculoBimT(iEdit): 
  selectTbim = driver.find_elements_by_class_name("cell.column-actions.level3.levelodd.cell.c2")
  selectTbim[iEdit].click()
  driver.find_element_by_partial_link_text("Editar c").click()
def cambiarCalculoTBIM(Bx, ix):
  calBim = driver.find_element_by_id("id_calculation")
  calBim.clear()
  calBim.send_keys(Bx[ix])  
  driver.find_element_by_id("id_submitbutton").click()
  driver.find_element_by_class_name("btn.btn-primary").click()
  print("Componente reestablecido")

Login()
for CursoID in range (0,len(Cursos)):
    ArblCurso(Cursos[CursoID])
    iEdit=8
    print(iEdit)
    for iCal in range (0,5):
        selectCalculoBimT(iEdit)
        cambiarCalculoTBIM(B1,iCal)
        iEdit +=1 
        print(iEdit)
    iEdit +=8
    print(iEdit)
    for iCal in range (0,5):
        selectCalculoBimT(iEdit)
        cambiarCalculoTBIM(B2,iCal)
        iEdit +=1 
        print(iEdit)
    iEdit +=8
    print(iEdit)
    for iCal in range (0,5):
        selectCalculoBimT(iEdit)
        cambiarCalculoTBIM(B3,iCal)
        iEdit +=1 
        print(iEdit)
    iEdit +=8
    print(iEdit)
    for iCal in range (0,5):
        selectCalculoBimT(iEdit)
        cambiarCalculoTBIM(B4,iCal)
        iEdit +=1 
        print(iEdit)

print ("Script Finalizado")   
    
    



