# -*- coding: utf-8 -*-
#El trabajo de Cron de Moodle no se había ejecutado en casi año y medio, por lo tanto las tareas programadas y Ad Hoc estaban acumuladas, el sevidor compartido no estaba ejecutando el cron, para tener información en tiempo real de las tareas ejecutadas hice este pequeño codigo para hacer ejecuciones del cron mediante script web y depurar rapidamente las tareas. 

#Al terminar con las tareas, se configura adecuadamente el cron en el servidor y se soluciona todos los problemas que este presentaba, ej: "Borrado en Progreso", "Copia del curso", "Copias de Seguridad programadas sin resolver impidiendo la copia de seguridad manual, etc..."

#Emula la ejecución del Cron desde el Servidor.
# Librerias
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

#Inicio del Navegador
start = webdriver.ChromeOptions()
start.add_argument('--start-maximized')
driver_path = 'RutaDel/chromedriver.exe'
driver = webdriver.Chrome(driver_path, chrome_options=start) 

#Inicio de Cron
    #Credenciales del Cron Web
Pass = "Si tiene contraseña configurada para el cron en Administracion>Seguridad"
#Contador
Cntdr=0
Ejccn=4 #Ejecuciones que desea
    #Ejecutar Cron
while Cntdr <= Ejccn:
 driver.get("https://www.sudominio.com/moodle/admin/cron.php?password=" + Pass)
 WaitPageLogin = WebDriverWait(driver, 200) #El cron tiene un ejecución de 2min aprox, configuré 200s para evitar solapamiento.
 Cntdr +=  1
 print(Cntdr) #Informa en consola el numero de la ejecución en curso.














