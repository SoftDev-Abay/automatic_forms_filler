import random

from selenium import webdriver
import time
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By

options = Options()
options.add_experimental_option("detach", True)

web = webdriver.Edge(options=options)


web.get('https://forms.gle/ZiT75w4ScuMEZsCy5')
#
time.sleep(2)


# FirstName = "Rishab"
#
# first = web.find_element("xpath", '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div[2]/textarea')
# first.send_keys(FirstName)

# RadioButtonPeriod = web.find_element("xpath",'//*[@id="i12"]/div[3]/div')
# RadioButtonPeriod.click()



terror_radioButtons_xpath = ['//*[@id="i5"]/div[3]/div','//*[@id="i8"]/div[3]/div']
policy_radioButtons_xpath = ['//*[@id="i15"]/div[3]/div','//*[@id="i18"]/div[3]/div']
mass_radioButtons_xpath = ['//*[@id="i25"]/div[3]/div','//*[@id="i28"]/div[3]/div']
consequences_checkbox_xpath = ['//*[@id="i40"]/div[2]','//*[@id="i43"]/div[2]','//*[@id="i46"]/div[2]','//*[@id="i49"]/div[2]','//*[@id="i52"]/div[2]']
information_checkbox_xpath = ['//*[@id="i64"]/div[2]','//*[@id="i67"]/div[2]','//*[@id="i70"]/div[2]','//*[@id="i73"]/div[2]','//*[@id="i76"]/div[2]']
informed_scale_xpath = ['//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div[1]/span/div/label[1]/div[2]/div/div/div[3]/div','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div[1]/span/div/label[2]/div[2]/div/div/div[3]/div','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div[1]/span/div/label[3]/div[2]/div/div/div[3]/div','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div[1]/span/div/label[4]/div[2]/div/div/div[3]/div','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div[1]/span/div/label[5]/div[2]/div/div/div[3]/div']
important_scale_xpath = ['//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div[1]/span/div/label[1]/div[2]/div/div/div[3]/div','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div[1]/span/div/label[2]/div[2]/div/div/div[3]/div','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div[1]/span/div/label[3]/div[2]/div/div/div[3]/div','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div[1]/span/div/label[4]/div[2]/div/div/div[3]/div','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div[1]/span/div/label[5]/div[2]/div/div/div[3]/div']

opinion_xpath = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[8]/div/div/div[2]/div/div[1]/div[2]/textarea'
opinions_answer = ['It promotes empathy and compassion by fostering a deeper understanding of the pain endured by individuals and communities',
'The history of Stalinist repression serves as a reminder of the importance of protecting human rights and upholding justice',
'It contributes to the process of healing and reconciliation for those affected by the repressive regime',
'By examining this history, we can challenge distorted narratives and promote a more accurate understanding of the past',
'It enables us to appreciate the progress and freedom achieved in present-day Kazakhstan by contrasting it with the oppressive past.',
'Помнить и изучать историю сталинистских репрессий в Казахстане важно, чтобы чтить память жертв и признать их страдания.',
'Это позволяет нам учиться на опыте прошлого и предотвращать повторение подобных ужасов в будущем',
'Понимание истории сталинистских репрессий помогает нам понять устойчивость и силу казахстанского народа',
'Это предоставляет возможность сохранить коллективную память нации и не допустить забвения правды.',
'Қазақстандағы сталин репрессияларының тарихын зерттеу - бұл өту құрылымдарын маңыздылықпен есте сақтау үшін маңызды']


radiobuttons_xpath_list = [['//*[@id="i5"]/div[3]/div','//*[@id="i8"]/div[3]/div'],['//*[@id="i15"]/div[3]/div','//*[@id="i18"]/div[3]/div'],['//*[@id="i25"]/div[3]/div','//*[@id="i28"]/div[3]/div']]
checkboxs_xpath_list = [['//*[@id="i40"]/div[2]','//*[@id="i43"]/div[2]','//*[@id="i46"]/div[2]','//*[@id="i49"]/div[2]','//*[@id="i52"]/div[2]'],['//*[@id="i64"]/div[2]','//*[@id="i67"]/div[2]','//*[@id="i70"]/div[2]','//*[@id="i73"]/div[2]','//*[@id="i76"]/div[2]']]
scales_xpaths = [['//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div[1]/span/div/label[1]/div[2]/div/div/div[3]/div','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div[1]/span/div/label[2]/div[2]/div/div/div[3]/div','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div[1]/span/div/label[3]/div[2]/div/div/div[3]/div','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div[1]/span/div/label[4]/div[2]/div/div/div[3]/div','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div[1]/span/div/label[5]/div[2]/div/div/div[3]/div'],['//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div[1]/span/div/label[1]/div[2]/div/div/div[3]/div','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div[1]/span/div/label[2]/div[2]/div/div/div[3]/div','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div[1]/span/div/label[3]/div[2]/div/div/div[3]/div','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div[1]/span/div/label[4]/div[2]/div/div/div[3]/div','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div[1]/span/div/label[5]/div[2]/div/div/div[3]/div']]
opinion_xpaths = [[opinion_xpath,opinions_answer]]



def getUnigueRandomCheckBox(uniqueSet,checkBoxsLength):
    randomNumber = random.randrange(0, checkBoxsLength)
    if randomNumber in uniqueSet:
        return getUnigueRandomCheckBox(uniqueSet,checkBoxsLength)
    return randomNumber

def clickRadioButton(buttons_xpaths_array,specific_choice = -1):

    if specific_choice >=0:
        numOfChoice = specific_choice
    else:
        length_xpath_array = len(buttons_xpaths_array)
        numOfChoice = random.randrange(0,length_xpath_array)

    xpath= buttons_xpaths_array[numOfChoice]
    RadioButton = web.find_element("xpath",xpath )
    RadioButton.click()
    print("succes")
    return numOfChoice

def clickCheckBox(checkBox_xpaths_array):
    length_xpath_array = len(checkBox_xpaths_array)
    amoountOfChoices = random.randrange(2, length_xpath_array)
    alreadyClicled = []
    for _ in range(amoountOfChoices):
        numOfChoice = getUnigueRandomCheckBox(alreadyClicled,length_xpath_array)
        xpath = checkBox_xpaths_array[numOfChoice]
        chechBox = web.find_element("xpath", xpath)
        chechBox.click()
        alreadyClicled.append(numOfChoice)
    print("succes")

def clickOpinion(input_xpath,opinions):
    length_opinions = len(opinions)
    numOfOpinion = random.randrange(0, length_opinions)

    opinion_input = web.find_element("xpath", input_xpath)
    opinion_input.send_keys(opinions[numOfOpinion])
    print("succes")

while True:

    for index in range (len(radiobuttons_xpath_list)):
        clickRadioButton(radiobuttons_xpath_list[index])

    for index in range (len(scales_xpaths)):
        clickRadioButton(scales_xpaths[index])

    for index in range(len(checkboxs_xpath_list)):
        clickCheckBox(checkboxs_xpath_list[index])

    for index in range(len(opinion_xpaths)):
        clickOpinion(opinion_xpaths[index][0],opinion_xpaths[index][1])



    Submit_button = web.find_element("xpath",'//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span')
    Submit_button.click()


    get_confirmation_div_text = web.find_element(By.CLASS_NAME, 'vHW8K')
    print(get_confirmation_div_text.text)
    confirmation_text = get_confirmation_div_text.text
    if ((confirmation_text) == "Your response has been recorded." or (confirmation_text) == "Ответ записан."):
        print ("Test Was Successful")
        sendNew = web.find_element("xpath", '/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
        sendNew.click()
        time.sleep(2)
    else:
        print("Test Was Not Successful")
