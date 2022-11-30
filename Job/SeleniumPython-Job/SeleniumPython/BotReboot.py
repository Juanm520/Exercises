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
User = "SusCredencialesParaIngresarAMoodle"
Pass = "SuContraseÃ±aParaIngresarAMoodle"
CursoID = "IDdelCursoQueDeseaAfectar"

    #Script login en Moodle.
driver.get("https://www.direccion/de/moodle")

WaitPageLogin = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "password")))
input_User = driver.find_element_by_id('username')
input_Pass = driver.find_element_by_id('password')
input_User.send_keys(User)
input_Pass.send_keys(Pass)
SubmitB = driver.find_element_by_id("loginbtn")
SubmitB.click()

    #Entrar al Curso

driver.get("https://www.direccion/de/moodle/grade/edit/tree/index.php?id=" + CursoID)
WaitPageLogin = WebDriverWait(driver, 10)

    #Metodo: oculta las categorias de las semanas pares.
def Ocultar_Cat():
    #Hace una lista o array de los elementos en el level3 de la categorizacion.
    WebDriverWait(driver, 10)
    index_lv3 = driver.find_elements_by_class_name("cell.column-actions.level3.levelodd.cell.c3")
    #Click editar en los elementos Level 3 impares.  
    index_lv3[b].click()
    try:
        #Ocultar semanas si estan en Mostrar, de lo contrario sigue al siguiente elemento en el array.
        WebDriverWait(driver, 10)
        Sem_hide = driver.find_element_by_link_text("Ocultar")
        Sem_hide.click()
    except NoSuchElementException:
        pass

#Ejecuta el metodo anterior en el intervalo que se desea. En este caso en las categorias impares. (Sem_ Se refiere a Semanas que es el nombre de las categorias para el moodle que interviene.    
for b in range(1,8,2):
    Ocultar_Cat()
    
for b in range(14,21,2):
    Ocultar_Cat()
    
for b in range(27,34,2):
    Ocultar_Cat()
    
for b in range(40,47,2):
    Ocultar_Cat()
    
    


    









