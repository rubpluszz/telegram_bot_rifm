from selenium import webdriver


class ParsersForRyhmes():

    def __init__(self, word):
        chromedriver = '/usr/local/bin/chromedriver'
        options = webdriver.ChromeOptions()
        options.add_argument('headless')  #headless
        self.browser = webdriver.Chrome(chrome_options=options)
        self.word = word

    def selenium_parser_uk(self):
        """Ukranian language parser"""
        self.browser.get('http://rymy.in.ua/')
        self.browser.find_element_by_css_selector("#query").send_keys(self.word)
        self.browser.find_element_by_css_selector("#search").click()
        rhymes=''
        for rhyme in self.browser.find_elements_by_css_selector(".three > a"):
            print(rhyme.text)
            rhymes += rhyme.text + ", "
        return(rhymes)

    def selenium_parser_ru(self):
        """Russian language parser"""
        self.browser.get('https://rifme.net')
        self.browser.find_element_by_css_selector("#text").send_keys(self.word)
        self.browser.find_element_by_css_selector("#submitShow > input:nth-child(2)").click()
        rhymes=''
        for rhyme in self.browser.find_elements_by_css_selector(".rifmypodryad:nth-child(4) > li"):
            if rhyme.text!='https://rifme.net/':
                rhymes += rhyme.text + ", "
        print(rhymes)
        return(rhymes)

    def selenium_parser_pl(self):
        """Polish language parser"""
        self.browser.get('https://polskierymy.pl/')
        self.browser.find_element_by_css_selector("#id_rymy").send_keys(self.word)
        self.browser.find_element_by_css_selector("button.submit").click()
        rhymes=''
        for rhyme in self.browser.find_elements_by_css_selector("div.col-xs-12:nth-child(3) > p:nth-child(1) .result-text"):
            print(rhyme)
            rhymes += rhyme.text + ", "
        return(rhymes)

    def selenium_parser_en(self):
        """English language parser"""
        self.browser.get('https://double-rhyme.com')
        self.browser.find_element_by_css_selector("#search-box").send_keys(self.word)
        self.browser.find_element_by_css_selector("#submitButton").click()
        number=1
        rhymes=''
        for rhyme in self.browser.find_elements_by_css_selector(".table>.tr>div"):
            if number==1 or number%2==1:
                rhymes += rhyme.text + ", "
        return(rhymes)

    def __del__(self):
        self.browser.quit()
