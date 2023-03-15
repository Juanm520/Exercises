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

#----------------------------------------------------------- Funciones generales -------#

    #Entra a la interfaz de Configuracion de Libro de calificaciones.
def config_grade_tree_interface(CursoId):
    driver.get('https://...com/moodle/grade/edit/tree/index.php?id=%a' % (CursoId))
    WebDriverWait(driver, 10)
    #Envia el formulario con submit button.
def submint_btn():
    driver.find_element(By.ID, "id_submitbutton").click() 
    #Valida si se trata de un curso de ABI o ABP.
def is_ABI_ABP_course():
    ABI_ABP_name_pairing = 'Aprendizaje Basado'
    course_name = driver.find_element(By.CLASS_NAME, 'page-header-headings').find_element(By.TAG_NAME, 'h1').text
    if(course_name.find(ABI_ABP_name_pairing) != -1):
            return True
    return False
    #Valida si se trata de un curso de basico.
def is_basic_course():
    basic_courses = ['Naturales', 'Sociales', 'Matemáticas', 'Lenguaje', 'English']
    course_name = driver.find_element(By.CLASS_NAME, 'page-header-headings').find_element(By.TAG_NAME, 'h1').text
    for basic_course in basic_courses:
        if(course_name.find(basic_course) != -1):
            return True
    return False
    #Retorna los nombres de los totales de categoria según el curso.
def is_complementary_course():
    course_name_pairing = ['Artes', 'Robótica', 'Integralidad']
    course_title = driver.find_element(By.CLASS_NAME, 'page-header-headings').find_element(By.TAG_NAME, 'h1').text
    for course_name in course_name_pairing:
        if(course_title.find(course_name) != -1):
                return True
    return False
#Valida si es un curso complementario.
def get_total_names_categories():
    return ['Actitudinal', 'Axiológico']
     
def toogles_ids():
    if (is_complementary_course()):
        return [[], [10, 12], [22, 24], [34, 36], [46, 48]]
    return [[], [58, 60], [118, 120], [178, 180], [238, 240]]
#----------------------------------------------------------- Funciones estructura libro de calificaciones -------#
   #Crea las categorias a nivel de bimestres. 
def fix_cat_names_bim(CursoId, toogles_ids, bimester):  
    #Itera por los bimestres.
    index = 0
    for toogle in toogles_ids[int(bimester[9])]: 
        config_grade_tree_interface(CursoId)
        driver.find_element(By.ID, f'action-menu-toggle-{toogle}').click()
        driver.find_element(By.PARTIAL_LINK_TEXT, 'Editar ajustes').click()
        driver.find_element(By.ID, 'id_fullname').clear()
        driver.find_element(By.ID, 'id_fullname').send_keys(f'{get_total_names_categories()[index]} del {bimester}')
        index += 1
        submint_btn() 
    
#----------------------------------------------------------- Ejecución del script -------#

    #Algoritmo para crear el libro de calificaciones en cada curso.
for CursoID in CursosID:

    config_grade_tree_interface(CursoID)

    if(is_basic_course() or is_ABI_ABP_course()):
         print(f'Curso {CursoID} no afectado.')
    else:
        fix_cat_names_bim(CursoID, toogles_ids(), 'Bimestre 1')
        fix_cat_names_bim(CursoID, toogles_ids(), 'Bimestre 2')
        fix_cat_names_bim(CursoID, toogles_ids(), 'Bimestre 3')
        fix_cat_names_bim(CursoID, toogles_ids(), 'Bimestre 4')
        # #Imprime el id del curso finalizado.
        print(f'Curso {CursoID} finalizado.')


print("Arreglo de cursos ingresados finalizado.")

