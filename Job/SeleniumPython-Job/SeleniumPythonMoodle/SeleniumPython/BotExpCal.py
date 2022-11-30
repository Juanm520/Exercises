# -*- coding: utf-8 -*-
# Librerias

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from csv import reader

#Inicio del Navegador
start = webdriver.ChromeOptions()
start.add_argument('--start-maximized')
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

#Inicio de Sesion en Moodle
    #Credenciales e ID del curso
User = ""
Pass = ""
CursosID = []
Clave = 'Total Cognitivo Bimestre 1'

#     #Script login y administración
driver.get("https://formarinnovar.com/moodle")

WebDriverWait(driver,(1)).until(EC.presence_of_element_located((By.ID, "password")))

input_User = driver.find_element(By.ID, 'username')
input_Pass = driver.find_element(By.ID, 'password')
input_User.send_keys(User)
input_Pass.send_keys(Pass)
SubmitB = driver.find_element(By.ID, "loginbtn")
SubmitB.click()

    #Entrar a la interfaz de exportar calificaciones del Curso.
def CursoCatTree(CursoId):
 driver.get("https://formarinnovar.com/moodle/grade/export/xls/index.php?id=" + str(CursoID))
 WebDriverWait(driver, 10)
    
def SelCategorias():
    #Deseleccionar categorias
 WebDriverWait(driver, 10)
 DeselectCats = driver.find_element(By.LINK_TEXT, "Seleccionar todos/ninguno")
 DeselectCats.click()
 driver.execute_script("window.scrollTo({ top: 0});")
 #Crea arreglo de los elementos de la clase.
 SelectCatsClass = driver.find_elements(By.CLASS_NAME, "form-check.d-flex")
 #Busca el indice de la clave.
 IndexClave = 0
 for i in range (0, len(SelectCatsClass)):
    if SelectCatsClass[i].find_element(By.TAG_NAME, 'label').text == Clave:
        IndexClave = i
        print (IndexClave)
        break
 #Selecciona los demas componetes del bimestre
 for i in range (0, 5): 
    SelectCatsClass[IndexClave].find_element(By.TAG_NAME,'label').click()
    IndexClave = IndexClave + 1

def Download():
    driver.find_element(By.ID, "id_submitbutton").click()
    


for CursoID in CursosID:
 CursoCatTree(CursoID)
 SelCategorias()
 Download()
 print(CursoID)
print("Finalizado")

