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
driver_path = 'C:/Users/JuanM/Desktop/codex/chromedriver99_win32/chromedriver.exe'
driver = webdriver.Chrome(driver_path, chrome_options=start) 

#Inicio de Sesion en Moodle
    #Credenciales e ID del curso
User = ""
Pass = ""
Cursos = []



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
  driver.get("https://sudominio.com/moodle/grade/edit/tree/index.php?id=" + (CursoID))
 
 #Ingresa a la edici贸n del calculo de cada componente.
def limpiarComponente(iEdit): 
  selectCalSems = driver.find_elements_by_class_name("cell.column-actions.level4.leveleven.cell.c2")
  selectCalSems[iEdit].click()
  driver.find_element_by_partial_link_text("Editar c").click()
  driver.find_element_by_id("id_calculation").clear()
  driver.find_element_by_id("id_submitbutton").click()
  driver.find_element_by_class_name("btn.btn-primary").click()
  print("Componente reestablecido")

Login()
for CursoID in range (0,len(Cursos)):
    ArblCurso(Cursos[CursoID])
    iEdit=5
    for iCal in range (0,16):
        limpiarComponente(iEdit)
        iEdit= iEdit +1
        print(iEdit)
        limpiarComponente(iEdit)
        iEdit= iEdit +3
        print(iEdit)
        limpiarComponente(iEdit)
        iEdit= iEdit +6
        print(iEdit)
    TCal=driver.find_elements_by_class_name("icon.fa.fa-calculator.fa-fw.icon.itemicon")
    print(len(TCal))
   
print ("Script Finalizado")   
    
    



