# -*- coding: utf-8 -*-
# Librerias
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select



#Inicio del Navegador
start = webdriver.ChromeOptions()
start.add_argument('--start-maximized')
driver_path = 'RutaDel/chromedriver.exe'
driver = webdriver.Chrome(driver_path, chrome_options=start) 

#Inicio de Sesion en Moodle
    #Credenciales e ID del curso
User = ""
Pass = ""
CursosID = []

    #Script login y administraciรณn
driver.get("https://sudominio.com/moodle")

WaitPageLogin = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "password")))

input_User = driver.find_element_by_id('username')
input_Pass = driver.find_element_by_id('password')
input_User.send_keys(User)
input_Pass.send_keys(Pass)
SubmitB = driver.find_element_by_id("loginbtn")
SubmitB.click()

    #Entrar a la configraciรณnm de calificaciones del Curso.
def CursoTree(CursoId):
 driver.get("https://sudominio.com/moodle/grade/edit/tree/index.php?id=" + str(CursoID))
 WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[3]/div[2]/div/div/section/div/div/div/div[2]/form/div/div/input")))
    
def Categoria():
    #Filtra recursos fuera de las categorias y los lleva a No Calificables.
 WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[3]/div[2]/div/div/section/div/div/div/div[2]/form/div/table/tbody/tr[1]/td[4]/input"))).click()
 checkBoxsCatBim = driver.find_elements_by_class_name("cell.column-select.level2.leveleven.cell.c4.lastcol")
 for i in range(0,len(checkBoxsCatBim)):
    checkBoxsCatBim[i].find_element_by_class_name("itemselect.ignoredirty").click()
 driver.find_element_by_id("menumoveafter").click()
 Select(driver.find_element_by_id("menumoveafter")).select_by_visible_text("SuCategoria")
 WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.CLASS_NAME,"btn.btn-primary"))).click()

def VisualCategoria():
    #Vuelve a Configuraciรณn de calificaciones y organiza las categorias a Ocultar (SuCategoria)
 WebDriverWait(driver, 20).until(EC.presence_of_all_elements_located((By.CLASS_NAME,"cell.column-actions.level2.leveleven.cell.c3")))
 driver.execute_script("window.scrollTo({ top: 0});")
 cursoEdit= driver.find_element_by_class_name("cell.column-actions.level1.levelodd.cell.c3")
 cursoEdit.find_element_by_id("action-menu-toggle-0").click() 
 driver.find_element_by_link_text("Ocultar").click()
 WebDriverWait(driver, 20).until(EC.presence_of_all_elements_located((By.CLASS_NAME,"cell.column-actions.level2.leveleven.cell.c3")))
 cursoEdit= driver.find_element_by_class_name("cell.column-actions.level1.levelodd.cell.c3")
 cursoEdit.find_element_by_id("action-menu-toggle-0").click()
 driver.find_element_by_link_text("Mostrar").click()
 WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME,"cell.column-actions.level2.leveleven.cell.c3")))
 ncEdit = driver.find_elements_by_class_name("cell.column-actions.level2.leveleven.cell.c3")
 ncEdit[4].find_element_by_class_name("action-menu.moodle-actionmenu.d-inline").click()
 driver.find_element_by_link_text("Ocultar").click()
 
for CursoID in CursosID:
 CursoTree(CursoID)
 Categoria()
 VisualCategoria()
 print(CursoID)


