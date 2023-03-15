# -*- coding: utf-8 -*-
# Librerias
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


#Inicio del Navegador
start = webdriver.ChromeOptions()
start.add_argument('--start-minimized')
driver_path = 'C:/Users/JuanM/Desktop/codex/chromedriver_win32/chromedriver.exe'
driver = webdriver.Chrome(driver_path, chrome_options=start) 
driver.execute_script("document.body.style.zoom='80%'")

#Inicio de Sesion en Moodle
    #Credenciales e ID del curso
User = ""
Pass = ""
CursoID = ""

    #Script login y administración
driver.get("https://...com/moodle")

WaitPageLogin = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "password")))
input_User = driver.find_element_by_id('username')
input_Pass = driver.find_element_by_id('password')
input_User.send_keys(User)
input_Pass.send_keys(Pass)
SubmitB = driver.find_element_by_id("loginbtn")
SubmitB.click()

    #Entrar al Curso
driver.get("https://formarinnovar.com/moodle/course/reset.php?id=" + CursoID)
WaitPageLogin = WebDriverWait(driver, 10)

    #Metodo: Checkhbox
def CheckBox_Check():
    #Tomar default checkbox
    WebDriverWait(driver, 10)
    Check_Def = driver.find_element_by_name("selectdefault")
    Check_Def.click()
    WebDriverWait(driver, 10)
    #Tomar cada Checkbox requerido
    Check_Com = driver.find_element_by_name("reset_comments")
    Check_Fin = driver.find_element_by_name("reset_completion")
    Check_Del = driver.find_element_by_name("delete_blog_associations")
    Check_Comp = driver.find_element_by_name("reset_competency_ratings")
    #Clickea CheckBox
    Check_Com.click()
    Check_Fin.click()
    Check_Del.click()
    Check_Comp.click()
CheckBox_Check()
#Reiniciar Curso
SubmitBReset = driver.find_element_by_name("submitbutton")
SubmitBReset.click()



   
    


    
    


    









