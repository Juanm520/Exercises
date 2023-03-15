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
driver.get("https://.....com/moodle")

WebDriverWait(driver,(1)).until(EC.presence_of_element_located((By.ID, "password")))
input_User = driver.find_element(By.ID, 'username')
input_Pass = driver.find_element(By.ID, 'password')
input_User.send_keys(User)
input_Pass.send_keys(Pass)
SubmitB = driver.find_element(By.ID, "loginbtn")
SubmitB.click()

#----------------------------------------------------------- Funciones generales -------#
    #Entra a la interfaz de creación de categorias.
def add_category_interface(CursoId):
    driver.get('https://...com/moodle/grade/edit/tree/category.php?courseid=%a' % (CursoId))
    WebDriverWait(driver, 10)
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
    #Retorna los nombres de los totales de categoria según el curso.
def get_total_names_categories():
    basic_courses = ['Naturales', 'Sociales', 'Matemáticas', 'Lenguaje', 'English']
    course_name = driver.find_element(By.CLASS_NAME, 'page-header-headings').find_element(By.TAG_NAME, 'h1').text
    for basic_course in basic_courses:
        if(course_name.find(basic_course) != -1):
            return ['Cognitivo', 'Procedimental', 
                    'Evaluación Bimestral Cognitivo y Procedimental',
                    'Actitudinal', 'Axiológico']
    if (is_ABI_ABP_course()):
        return ['Cognitivo', 'Procedimental', 
            'Autoevaluación y coevaluación del componente cognitivo y procedimental',
            'Autoevaluación y coevaluación componente actitudinal', 
            'Autoevaluación y coevaluación componente axiológico']
    return ['Cognitivo', 'Procedimental', 
            'Evaluación concertada componente cognitivo y procedimental',
            'Autoevaluación y coevaluación componente actitudinal', 
            'Autoevaluación y coevaluación componente axiológico']
    #Valida si es un curso complementario.
def is_complementary_course():
    course_name_pairing = ['Artes', 'Robótica', 'Integralidad']
    course_title = driver.find_element(By.CLASS_NAME, 'page-header-headings').find_element(By.TAG_NAME, 'h1').text
    is_pairing = False
    for course_name in course_name_pairing:
        if(course_title.find(course_name) != -1):
                is_pairing = True
    return is_pairing
#----------------------------------------------------------- Funciones estructura libro de calificaciones -------#
   #Crea las categorias a nivel de bimestres. 
def build_bimester_cat(CursoId):
    add_category_interface(CursoId)
    #Inicializa el libro creando el primer bimestre.
    driver.find_element(By.ID, "id_fullname").send_keys("Bimestre 1")
    driver.find_element(By.CLASS_NAME, "moreless-toggler").click()
    driver.find_element(By.ID, "id_grade_item_idnumber").send_keys("TBim1")
    submint_btn()
    #Itera por los bimestres faltantes.
    for bimester in range(2, 5):
        add_category_interface(CursoId)
        driver.find_element(By.ID, "id_fullname").send_keys(f"Bimestre {bimester}")
        driver.find_element(By.PARTIAL_LINK_TEXT, 'Total categor').click()
        driver.find_element(By.CLASS_NAME, "moreless-toggler").click()
        driver.find_element(By.ID, "id_grade_item_idnumber").send_keys(f"TBim{bimester}")
        submint_btn()   
    #Crea las categorias a nivel de las semanas por bimestre.
def build_week_cat(CursoId, star_week, endweek, bimester):
    if driver.current_url != 'https://...com/moodle/grade/edit/tree/category.php?courseid=%a' % (CursoId):
        add_category_interface(CursoId)
    for week in range (star_week, endweek + 1):
        add_category_interface(CursoId)
        driver.find_element(By.ID, "id_fullname").send_keys(f"Semana {week}")
        driver.find_element(By.PARTIAL_LINK_TEXT, 'padre').click()
        driver.find_element(By.ID, 'id_parentcategory').send_keys(bimester)
        submint_btn()
    #Crea las categorias a nivel de los componentes (Cog y Pro) por cada Semana.
def build_cog_pro_by_week(CursoId, star_week, endweek):
    #Define array de los componentes evaluativos de la semana.
    componentes = ["Cognitivo", "Procedimental"]
    #Itera por las ocho semanas del bimestre.
    for week in range(star_week, endweek + 1):
        #Itera por los componentes del array.
        for componente in componentes:
            #Define el prefijo del Id del componente.
            if(componente == "Cognitivo"):
                id_prefix="CogSem"
            else: id_prefix = "ProSem"
            add_category_interface(CursoId)
            driver.find_element(By.ID, "id_fullname").send_keys(f'{componente} de la Semana {week}')
            driver.find_element(By.PARTIAL_LINK_TEXT, 'Total categor').click()
            driver.find_element(By.CLASS_NAME, "moreless-toggler").click()
            driver.find_element(By.ID, "id_grade_item_idnumber").send_keys(f'{id_prefix}{week}')
            driver.find_element(By.PARTIAL_LINK_TEXT, 'padre').click()
            driver.find_element(By.ID, 'id_parentcategory').send_keys(f"Semana {week}")
            submint_btn()
    #Crea las categorias para totales del Bimestre.
def build_totals_categories_by_bimester(CursoId, bimester):
    if driver.current_url != 'https://...com/moodle/grade/edit/tree/category.php?courseid=%a' % (CursoId):
        add_category_interface(CursoId)

    total_categories = get_total_names_categories()
    for total_category in total_categories:
        if(total_category == total_categories[0]):
            id_prefix = 'TCogBim'
        if(total_category == total_categories[1]):
            id_prefix = 'TProBim'
        if(total_category == total_categories[2]):
            id_prefix = 'TEvaBim'
        if(total_category == total_categories[3]):
            id_prefix = 'TActBim'
        if(total_category == total_categories[4]):
            id_prefix = 'TAxiBim'     
        add_category_interface(CursoId)
        driver.find_element(By.ID, "id_fullname").send_keys(f'{total_category} del {bimester}')
        WebDriverWait(driver, 1).until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, 'Total categor')))
        driver.find_element(By.PARTIAL_LINK_TEXT, 'Total categor').click()
        WebDriverWait(driver, 1).until(EC.element_to_be_clickable((By.CLASS_NAME, "moreless-toggler")))
        driver.find_element(By.CLASS_NAME, "moreless-toggler").click()
        #El indice [9] de bimestre indica el numero del bimestre a afectar.
        driver.find_element(By.ID, "id_grade_item_idnumber").send_keys(f'{id_prefix}{bimester[9]}') 
        driver.find_element(By.PARTIAL_LINK_TEXT, 'padre').click()
        driver.find_element(By.ID, 'id_parentcategory').send_keys(bimester)
        submint_btn()
    #Crea la categoria para las actividades sin peso evaluativo.
def build_category_no_grading(CursoId):
    if driver.current_url != 'https://...com/moodle/grade/edit/tree/category.php?courseid=%a' % (CursoId):
        add_category_interface(CursoId)
    driver.find_element(By.ID, "id_fullname").send_keys('Recursos pedagógicos sin peso evaluativo')
    submint_btn()
    driver.find_elements(By.CLASS_NAME, 'itemselect.ignoredirty')[0].click()
    driver.find_elements(By.ID, 'menumoveafter')[0].send_keys('Recursos pedagógicos sin peso evaluativo')
    driver.find_elements(By.CLASS_NAME, 'd-inline-block.dropdown-toggle.icon-no-margin')[10].click()
    driver.find_element(By.PARTIAL_LINK_TEXT, 'Ocultar').click()

#----------------------------------------------------------- Función calculo de los totales -------#
    #Define la clase para alojar el id del editor del calculo y sus formula.
class set_formulas_by_id_edit:
        def __init__ (self, id_link_index, formulas):
            self.id_link_index = id_link_index
            self.formulas = formulas   
    #Agrega calculo a total de categoría.
def add_calculus(CursoId, formulas_by_id_edit, start_range):
        config_grade_tree_interface(CursoId)
        driver.find_element(By.ID, f'action-menu-toggle-{formulas_by_id_edit.id_link_index[start_range]}').click()
        driver.find_element(By.PARTIAL_LINK_TEXT, 'Editar c').click()
        driver.find_element(By.ID, 'id_calculation').send_keys(formulas_by_id_edit.formulas[start_range])
        submint_btn()
    #Define formulas y agrega calculos a los totales del curso. 
def add_bimester_calculus(CursoId, bimester):
    #Definición de formulas para el curso.       
        #Total de los Bimestres
    nmb_bimester = bimester[9]
    if(nmb_bimester == '1'):
        bimester_info = set_formulas_by_id_edit(
                    ['53', '55', '3'],
                    ['=([[CogSem1]]+[[CogSem2]]+[[CogSem3]]+[[CogSem4]]+[[CogSem5]]+[[CogSem6]]+[[CogSem7]]+[[CogSem8]]) / 8',
                    '=([[ProSem1]]+[[ProSem2]]+[[ProSem3]]+[[ProSem4]]+[[ProSem5]]+[[ProSem6]]+[[ProSem7]]+[[ProSem8]]) / 8',
                    f'=([[TCogBim{nmb_bimester}]] * 0.25) + ([[TProBim{nmb_bimester}]] * 0.25) + ([[TEvaBim{nmb_bimester}]] * 0.20) + ([[TActBim{nmb_bimester}]] * 0.15) + ([[TAxiBim{nmb_bimester}]] * 0.15)'])                    
    if(nmb_bimester == '2'):
         bimester_info = set_formulas_by_id_edit(
                    ['113', '115', '63'],
                    ['=([[CogSem9]]+[[CogSem10]]+[[CogSem11]]+[[CogSem12]]+[[CogSem13]]+[[CogSem14]]+[[CogSem15]]+[[CogSem16]]) / 8',
                    '=([[ProSem9]]+[[ProSem10]]+[[ProSem11]]+[[ProSem12]]+[[ProSem13]]+[[ProSem14]]+[[ProSem15]]+[[ProSem16]]) / 8',
                    f'=([[TCogBim{nmb_bimester}]] * 0.25) + ([[TProBim{nmb_bimester}]] * 0.25) + ([[TEvaBim{nmb_bimester}]] * 0.20) + ([[TActBim{nmb_bimester}]] * 0.15) + ([[TAxiBim{nmb_bimester}]] * 0.15)'])   
    if(nmb_bimester == '3'):
         bimester_info = set_formulas_by_id_edit(
                    ['173', '175', '123'],
                    ['=([[CogSem17]]+[[CogSem18]]+[[CogSem19]]+[[CogSem20]]+[[CogSem21]]+[[CogSem22]]+[[CogSem23]]+[[CogSem24]]) / 8',
                    '=([[ProSem17]]+[[ProSem18]]+[[ProSem19]]+[[ProSem20]]+[[ProSem21]]+[[ProSem22]]+[[ProSem23]]+[[ProSem24]]) / 8',
                    f'=([[TCogBim{nmb_bimester}]] * 0.25) + ([[TProBim{nmb_bimester}]] * 0.25) + ([[TEvaBim{nmb_bimester}]] * 0.20) + ([[TActBim{nmb_bimester}]] * 0.15) + ([[TAxiBim{nmb_bimester}]] * 0.15)'])   
    if(nmb_bimester == '4'):
         bimester_info = set_formulas_by_id_edit(
                    ['233', '235', '183'],
                    ['=([[CogSem25]]+[[CogSem26]]+[[CogSem27]]+[[CogSem28]]+[[CogSem29]]+[[CogSem30]]+[[CogSem31]]+[[CogSem32]]) / 8',
                    '=([[ProSem25]]+[[ProSem26]]+[[ProSem27]]+[[ProSem28]]+[[ProSem29]]+[[ProSem30]]+[[ProSem31]]+[[ProSem32]]) / 8',
                    f'=([[TCogBim{nmb_bimester}]] * 0.25) + ([[TProBim{nmb_bimester}]] * 0.25) + ([[TEvaBim{nmb_bimester}]] * 0.20) + ([[TActBim{nmb_bimester}]] * 0.15) + ([[TAxiBim{nmb_bimester}]] * 0.15)'])    
    #Agrega calculo a los totales de categorias de los bimestres.
    for id_index in range(0, 3):
        add_calculus(CursoId, bimester_info, id_index)
    
#----------------------------------------------------------- Ejecución del script -------#

    #Algoritmo para crear el libro de calificaciones en cada curso.
for CursoID in CursosID:

    #Crea las categorias de los bimestres y recursos sin peso evaluativo.
    build_bimester_cat(CursoID)
    build_category_no_grading(CursoID)
    #Crea las categorias de las semanas anidadas en cada bimestre en rango de 1 a 32.
        #Crea componentes cog y pro anidos en cada semana.
    #-------------------Agrega categorias de las semanas al curso excepto a curso complementarios------
    #-------------------Componentes de las semanas del Bimestre 1-------
    if(not(is_complementary_course())): 
        build_week_cat(CursoID, 1, 8, 'Bimestre 1')
        build_cog_pro_by_week(CursoID, 1, 8)
        #-------------------Componentes de las semanas del Bimestre 2-------
        build_week_cat(CursoID, 9, 16,'Bimestre 2')
        build_cog_pro_by_week(CursoID, 9, 16)
        #-------------------Componentes de las semanas del Bimestre 3-------
        build_week_cat(CursoID, 17, 24, 'Bimestre 3')
        build_cog_pro_by_week(CursoID, 17, 24)
        #-------------------Componentes de las semanas del Bimestre 4-------
        build_week_cat(CursoID, 25, 32, 'Bimestre 4')
        build_cog_pro_by_week(CursoID, 25, 32) 
    #-------------------Totales de los componentes de los bimestres-------
    build_totals_categories_by_bimester(CursoID, 'Bimestre 1')
    build_totals_categories_by_bimester(CursoID, 'Bimestre 2')
    build_totals_categories_by_bimester(CursoID, 'Bimestre 3')
    build_totals_categories_by_bimester(CursoID, 'Bimestre 4')   
    #-------------------Recursos pedagógicos sin peso evaluativo-------
    #-------------------Agrega calculos al curso excepto a curso complementarios------
    if (not(is_complementary_course())):
        add_bimester_calculus(CursoID, 'Bimestre 1')
        add_bimester_calculus(CursoID, 'Bimestre 2')
        add_bimester_calculus(CursoID, 'Bimestre 3')
        add_bimester_calculus(CursoID, 'Bimestre 4')
    else:
        nmb_bimester = '1'
        bimester1_info = set_formulas_by_id_edit(['3'], [f'=([[TCogBim{nmb_bimester}]] * 0.25) + ([[TProBim{nmb_bimester}]] * 0.25) + ([[TEvaBim{nmb_bimester}]] * 0.20) + ([[TActBim{nmb_bimester}]] * 0.15) + ([[TAxiBim{nmb_bimester}]] * 0.15)'])
        add_calculus(CursoID, bimester1_info, 0)
        nmb_bimester = '2'
        bimester2_info = set_formulas_by_id_edit(['15'], [f'=([[TCogBim{nmb_bimester}]] * 0.25) + ([[TProBim{nmb_bimester}]] * 0.25) + ([[TEvaBim{nmb_bimester}]] * 0.20) + ([[TActBim{nmb_bimester}]] * 0.15) + ([[TAxiBim{nmb_bimester}]] * 0.15)'])
        add_calculus(CursoID, bimester2_info, 0)
        nmb_bimester = '3'
        bimester3_info = set_formulas_by_id_edit(['27'], [f'=([[TCogBim{nmb_bimester}]] * 0.25) + ([[TProBim{nmb_bimester}]] * 0.25) + ([[TEvaBim{nmb_bimester}]] * 0.20) + ([[TActBim{nmb_bimester}]] * 0.15) + ([[TAxiBim{nmb_bimester}]] * 0.15)'])
        add_calculus(CursoID, bimester3_info, 0)
        nmb_bimester = '4'
        bimester4_info = set_formulas_by_id_edit(['39'], [f'=([[TCogBim{nmb_bimester}]] * 0.25) + ([[TProBim{nmb_bimester}]] * 0.25) + ([[TEvaBim{nmb_bimester}]] * 0.20) + ([[TActBim{nmb_bimester}]] * 0.15) + ([[TAxiBim{nmb_bimester}]] * 0.15)'])
        add_calculus(CursoID, bimester4_info, 0)

        #-------------------Total del curso----------
    total_course_info = set_formulas_by_id_edit(['1'], ['=([[TBim1]]+[[TBim2]]+[[TBim3]]+[[TBim4]]) / 4'])
    add_calculus(CursoID, total_course_info, 0)
    
    # #Imprime el id del curso finalizado.
    print(f'Curso {CursoID} finalizado.')

print("Arreglo de cursos ingresados finalizado.")

