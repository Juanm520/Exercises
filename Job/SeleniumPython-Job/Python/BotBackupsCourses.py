# -*- coding: utf-8 -*-
# Librerias

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


#Inicio del Navegador
start = webdriver.ChromeOptions()
start.add_argument('--start-maximized')
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

#Inicio de Sesion en Moodle
    #Credenciales e ID del curso
User = ""
Pass = ""
CursosID = []

#Script login y administración
driver.get("https://....moodle")

WebDriverWait(driver,(1)).until(EC.presence_of_element_located((By.ID, "password")))
input_User = driver.find_element(By.ID, 'username')
input_Pass = driver.find_element(By.ID, 'password')
input_User.send_keys(User)
input_Pass.send_keys(Pass)
SubmitB = driver.find_element(By.ID, "loginbtn")
SubmitB.click()

    #Entrar a la interfaz de backups de cursos.
def CursoCatTree(CursoId):
 driver.get('https://....com/moodle/backup/backup.php?id=%a' % (CursoID))
 WebDriverWait(driver, 10)
    
def SelOpciones():
    #Deseleccionar categoria Usuarios Inscritos
    driver.find_elements(By.CLASS_NAME, "form-check-input ")[1].click()
 #Selecciona los demas componetes del bimestre


def GenerarBackup():
    driver.find_element(By.ID, "id_submitbutton").click()
    driver.find_element(By.ID, "id_submitbutton").click()
    driver.find_element(By.ID, "id_submitbutton").click()
    

for CursoID in CursosID:
    CursoCatTree(CursoID)
    SelOpciones()
    GenerarBackup()
    
    print(CursoID)
