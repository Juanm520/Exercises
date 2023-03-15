# -*- coding: utf-8 -*-
"""
Created on Tue Nov  2 09:08:26 2021

Automatización para cambiar los valores de Finalización de la Actividad de todos los recursos en un curso. Se requeria marcar todos los recursos como
No hacer Rastero de Finalización.

@author: JuanM
"""

# -*- coding: utf-8 -*-
# Librerias
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select



#Inicio del Navegador
start = webdriver.ChromeOptions()
start.add_argument('--start-maximized')
driver_path = 'C:/Users/JuanM/Desktop/codex/chromedriver_win32/chromedriver.exe'
driver = webdriver.Chrome(driver_path, chrome_options=start) 

#Inicio de Sesion en Moodle
    #Credenciales e ID del curso
User = ""
Pass = ""
Cursos = [""]

def Login():
#Script login y administración
 driver.get("https://....com/moodle")
 WebDriverWait(driver, 10)
# WaitPageLogin = .until(EC.presence_of_element_located((By.ID, "password")))
 input_User = driver.find_element_by_id('username')
 input_Pass = driver.find_element_by_id('password')
 input_User.send_keys(User)
 input_Pass.send_keys(Pass)
 SubmitB = driver.find_element_by_id("loginbtn").click()

def DlgncFrmlr(CursoID): 
#Entra a la interfaz de edición del curso.
 driver.get("https://...com/moodle/course/edit.php?id=" + CursoID)
#Toma las menus para marcar las opciones de desactivación del rastreo de finalización y envia el formulario. 
 WebDriverWait(driver, 10)
 DesplFormCur = driver.find_element_by_link_text("Formato de curso").click()
 SelectNoImg = Select(driver.find_element_by_id("id_newactivity")).select_by_value('1')
 DesplRastFin = driver.find_element_by_partial_link_text("Rastreo de fin").click()
 SelectNoCompl = Select(driver.find_element_by_id("id_enablecompletion")).select_by_value('0')
 SubmitForm = driver.find_element_by_id("id_saveanddisplay").click()
  
Login()
for CursoID in range (0,len(Cursos)):
    DlgncFrmlr(Cursos[CursoID])
    # WaitPageLoad = WebDriverWait(driver, 10)