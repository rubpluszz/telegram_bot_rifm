
from selenium import webdriver

class ParsersForRyhmes():
    
    def selenium_parser_ua(word):
    
        chromedriver = '/usr/local/bin/chromedriver'
        options = webdriver.ChromeOptions()
        options.add_argument('headless')  #headless
        browser = webdriver.Chrome(chrome_options=options)
        browser.get('http://rymy.in.ua/')
        browser.find_element_by_css_selector("#query").send_keys(word)
        browser.find_element_by_css_selector("#search").click()
        rhymes = []
        for rhyme in browser.find_elements_by_css_selector(".three > a"):
            rhymes.append(rhyme.text)
        browser.quit()
        return(rhymes)
    
    def selenium_parser_ru(word):
    
        chromedriver = '/usr/local/bin/chromedriver'
        options = webdriver.ChromeOptions()
        options.add_argument('headless')  #headless
        browser = webdriver.Chrome(chrome_options=options)
        browser.get('https://rifme.net')
        browser.find_element_by_css_selector("#text").send_keys(word)
        browser.find_element_by_css_selector("#submitShow > input:nth-child(2)").click()
        rhymes = []
        for rhyme in browser.find_elements_by_css_selector(".rifmypodryad:nth-child(4) > li"):
            if rhyme.text!='https://rifme.net/':
                rhymes.append(rhyme.text)
        browser.quit()
        return(rhymes)
        
    def selenium_parser_pl(word):
    
        chromedriver = '/usr/local/bin/chromedriver'
        options = webdriver.ChromeOptions()
        options.add_argument('headless')  #  headless
        browser = webdriver.Chrome(chrome_options=options)
        browser.get('https://polskierymy.pl/')
        browser.find_element_by_css_selector("#id_rymy").send_keys(word)
        browser.find_element_by_css_selector("button.submit").click()
        rhymes = []
        for rhyme in browser.find_elements_by_css_selector("div.col-xs-12:nth-child(3) > p:nth-child(1) .result-text"):
            rhymes.append(rhyme.text)
        browser.quit()
        return(rhymes)

    def selenium_parser_en(word):
    
        chromedriver = '/usr/local/bin/chromedriver'
        options = webdriver.ChromeOptions()
        options.add_argument('headless')  #  headless
        browser = webdriver.Chrome(chrome_options=options)
        browser.get('https://double-rhyme.com')
        browser.find_element_by_css_selector("#search-box").send_keys(word)
        browser.find_element_by_css_selector("#submitButton").click()
        rhymes = []
        for rhyme in browser.find_elements_by_css_selector(".table>.tr>div"):
            if number==1 or number%2==1:
                rhymes.append(rhyme.text)
        browser.quit()
        return(rhymes)
