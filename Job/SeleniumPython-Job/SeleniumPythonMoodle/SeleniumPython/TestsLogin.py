# -*- coding: utf-8 -*-
"""
Created on Tue Nov  2 09:08:26 2021

@author: JuanM
"""

# -*- coding: utf-8 -*-
# Librerias
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
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
CursoID = ""

    #Script login y administraciรณn
driver.get("https://sudominio.com/moodle")

WaitPageLogin = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "password")))
input_User = driver.find_element_by_id('username')
input_Pass = driver.find_element_by_id('password')
input_User.send_keys(User)
input_Pass.send_keys(Pass)
SubmitB = driver.find_element_by_id("loginbtn")
SubmitB.click()

    #Entrar al Curso

driver.get("https://sudominio.com/moodle/grade/edit/tree/index.php?id=" + CursoID)
WaitPageLogin = WebDriverWait(driver, 10)