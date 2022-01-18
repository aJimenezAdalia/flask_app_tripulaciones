def web_scraping(image, domain):
    '''
    '''
    from selenium import webdriver 
    from webdriver_manager.chrome import ChromeDriverManager
    from selenium.webdriver.chrome.options import Options
    import time
 
    options = Options()
    options.headless = True
    options.add_argument('window-size=1920x1080')

    #driver = webdriver.Chrome(ChromeDriverManager().install())
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

    # indicamos la URL de la página web a la que queremos acceder:
    url = "https://www.google.com/imghp?hl=en"

    # el objeto driver nos va a permitir alterar el estado del la página
    driver.get(url)

    elements_by_tag = driver.find_elements_by_tag_name("button")

    #for i in range(0, len(elements_by_tag)):
    #    print(elements_by_tag[i].text)  

    boton_aceptar = elements_by_tag[6]
    boton_aceptar.text

    boton_aceptar.click()

    elements_by_class_name = driver.find_elements_by_class_name('tdPRye')
    search = elements_by_class_name[0]
    search.click()

    time.sleep(5)

    inputElement = driver.find_element_by_id("Ycyxxc")
    img_url = image
    inputElement.send_keys(img_url)

    #from selenium.webdriver.common.keys import Keys
    #inputElement.send_keys(Keys.ENTER)

    bt_search = driver.find_element_by_id("RZJ9Ub")
    bt_search.click()

    urls_completas = []
    elements = driver.find_elements_by_class_name('yuRUbf')
    for i in elements:
        urls_completas.append(i.find_element_by_tag_name('a').get_attribute('href'))

    elements_by_class_name = driver.find_elements_by_class_name('iUh30 qLRx3b tjvcx')
    #dom = elements_by_class_name[0]
    #print(elements_by_class_name)

    elements_by_tag = driver.find_elements_by_tag_name("cite")
    #for i in range(0, len(elements_by_tag)):
    #    print(elements_by_tag[i].text)

    dominios = []
    direcciones = []

    for i in range(0, len(elements_by_tag)):
        lista = elements_by_tag[i].text.split(' ')
        dominios.append(lista[0][8::])

    dominios = dominios[::2]

    for elemento in urls_completas:
        if domain not in elemento:
            direcciones.append(elemento)

    # FILTRO
    copia = dominios.copy()
    
    url_filtro = domain
    for i in copia:
        if i == url_filtro:
            dominios.remove(url_filtro)
    nueva = []
    for i in dominios:
        if i[:4] == 'www.':
            nueva.append(i[4:])
        else:
            nueva.append(i)

    dominios = nueva

    dominios_nuevos = []
    for elemento in dominios:
        if domain not in elemento:
            dominios_nuevos.append(elemento)

    json_devolver = {}

    for dominio, direccion in zip(dominios_nuevos, direcciones):
        json_devolver[dominio] = direccion

    return json_devolver
