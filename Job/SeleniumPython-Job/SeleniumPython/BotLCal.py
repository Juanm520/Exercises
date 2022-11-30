# -*- coding: utf-8 -*-
"""
Created on Tue Nov  2 09:08:26 2021
#Automatizacion para 
@author: JuanM
"""

# -*- coding: utf-8 -*-
# Librerias
from numpy import ediff1d
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


#Inicio del Navegador

start = webdriver.ChromeOptions()
start.add_argument('--start-minimized')
driver_path = 'RutaDel/chromedriver.exe'
driver = webdriver.Chrome(driver_path, chrome_options=start) 

#Inicio de Sesion en Moodle
    #Credenciales e ID del curso
User = "SusCredenciales"
Pass = "SusCredenciales"
Cursos = ["arreglo de cursos a afectar"]
NCBim = ["Nombre o nombres de ID de la categoria a agregar"]

def Login():
#Script login y administracion
 driver.get("https://sudominio.com/moodle")
 WebDriverWait(driver, 10)
# WaitPageLogin = .until(EC.presence_of_element_located((By.ID, "password")))
 input_User = driver.find_element_by_id('username')
 input_Pass = driver.find_element_by_id('password')
 input_User.send_keys(User)
 input_Pass.send_keys(Pass)
 SubmitB = driver.find_element_by_id("loginbtn").click()

def DlgncFrmlr(CursoID): 
#Entra a la interfaz de ediciè´¸n del curso.
 driver.get("https://sudominio.com/moodle/grade/edit/tree/index.php?id=" + CursoID)
 #Ingresa a la edicion del Total del Curso
 SelectCalTCClk = driver.find_element_by_class_name("cell.column-actions.level1.levelodd.cell.c2").click()
 SelectCalTC = driver.find_elements_by_class_name("cell.column-actions.level1.levelodd.cell.c2")
 EditCalTC = SelectCalTC[0].find_element_by_class_name("d-inline-block.dropdown-toggle.icon-no-margin").click()
 EditCLk = driver.find_element_by_partial_link_text("Editar c").click()
 #Agrega las ID de los totales de la categorias de bimestre
 SelectCat = driver.find_elements_by_class_name("catlevel2")
 for Bim in range (0,len(NCBim)):
  SelectClass = SelectCat[Bim].find_element_by_class_name("idnumber")
  SelectClass.send_keys(NCBim[Bim])
 AddIdN = driver.find_element_by_id("id_addidnumbers").click()
#Agrega el calculo de la categoria total del curso y enviar el formulario
 IngrsaCal = driver.find_element_by_id("id_calculation").send_keys("=average([[Tbim1]]; [[Tbim2]]; [[Tbim3]]; [[Tbim4]])")
 SubmCal = driver.find_element_by_id("id_submitbutton").click()

Login()
for CursoID in range (0,len(Cursos)):
    DlgncFrmlr(Cursos[CursoID])
print ("Script Finalizado")   
    
    

    # WaitPageLoad = WebDriverWait(driver, 10)