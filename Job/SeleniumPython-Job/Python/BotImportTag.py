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
driver.get("https://...com/moodle")

WebDriverWait(driver,(1)).until(EC.presence_of_element_located((By.ID, "password")))
input_User = driver.find_element(By.ID, 'username')
input_Pass = driver.find_element(By.ID, 'password')
input_User.send_keys(User)
input_Pass.send_keys(Pass)
SubmitB = driver.find_element(By.ID, "loginbtn")
SubmitB.click()

    #Entrar a la interfaz de reiniciar en moodle
def CursoCatTree(CursoId):
    driver.get('https://...com/moodle/backup/import.php?id=%a' % (CursoID))
    WebDriverWait(driver, 10)
    
def SelOpciones():
#Seleccionar curso
    #Escribir busqueda
    form_input = driver.find_element(By.CLASS_NAME, "form-control")
    form_input.send_keys('Nat1')
    #Enviar busqueda
    driver.find_element(By.CLASS_NAME, "btn.btn-secondary.ml-1").click()
    #Seleccionar curso y enviar formulario
    driver.find_element(By.ID, "import-course-0").click()
    driver.find_element(By.ID, "import-course-0").click()
    driver.find_element(By.CLASS_NAME, "btn.btn-primary").click()
    #Seleccionar configuraciones
    driver.find_element(By.ID, "id_submitbutton").click()
    #Seleccionar recurso a importar
    driver.find_element(By.PARTIAL_LINK_TEXT, "Ninguno").click()
    driver.find_element(By.ID, "id_setting_section_section_98_included").click()
    driver.find_element(By.ID, "id_setting_activity_label_90778_included").click()
    driver.find_element(By.ID, "id_submitbutton").click()

def submintBtn():
    driver.find_element(By.ID, "id_submitbutton").click()    
    
for CursoID in CursosID:
    CursoCatTree(CursoID)
    SelOpciones()
    submintBtn()    
    print(CursoID)

print("Finalizado")
