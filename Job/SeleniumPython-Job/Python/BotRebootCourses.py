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
    driver.get('https://...com/moodle/course/reset.php?id=%a' % (CursoID))
    WebDriverWait(driver, 10)
    
def SelOpciones():
#Deseleccionar opciones de reinicilizar
    #Seleccionar Elminar eventos
    driver.find_element(By.ID, "id_reset_events").click()
    #Seleccionar Elminar anotaciones
    driver.find_element(By.ID, "id_reset_notes").click()
    #Seleccionar Elminar comentarios
    driver.find_element(By.ID, "id_reset_comments").click()
    #Borrar datos de Finalizacion
    driver.find_element(By.ID, "id_reset_completion").click()
    
    #Libros de calificaciones
    driver.find_element(By.LINK_TEXT , "Libro de calificaciones").click()
    driver.find_element(By.ID, "id_reset_gradebook_items").click()  

    #Grupos
    driver.find_element(By.LINK_TEXT , "Grupos").click()
    driver.find_element(By.ID, "id_reset_groups_remove").click()
    driver.find_element(By.ID, "id_reset_groupings_remove").click()  
    
    #Tareas
    driver.find_element(By.LINK_TEXT , "Tareas").click()
    driver.find_element(By.ID, "id_reset_assign_submissions").click()

    #Foros
    driver.find_element(By.LINK_TEXT , "Foros").click()
    driver.find_element(By.ID, "id_reset_forum_all").click()
    
    #Cuestionarios
    driver.find_element(By.LINK_TEXT , "Cuestionarios").click()
    driver.find_element(By.ID, "id_reset_quiz_attempts").click()

def submintBtn():
    driver.find_element(By.ID, "id_submitbutton").click()

for CursoID in CursosID:
    CursoCatTree(CursoID)
    SelOpciones()
    submintBtn()    
    print(CursoID)

print("Finalizado")
