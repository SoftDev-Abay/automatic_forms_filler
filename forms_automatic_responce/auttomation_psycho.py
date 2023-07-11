import random

from selenium import webdriver
import time
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By

options = Options()
options.add_experimental_option("detach", True)

web = webdriver.Edge(options=options)

# web.get('https://forms.gle/DTyBDmv2XdrZmTst6')
web.get('https://forms.gle/ov8MzCJ3L4zLfp2k8')
#
time.sleep(2)


# FirstName = "Rishab"
#
# first = web.find_element("xpath", '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div[2]/textarea')
# first.send_keys(FirstName)

# RadioButtonPeriod = web.find_element("xpath",'//*[@id="i12"]/div[3]/div')
# RadioButtonPeriod.click()

age_radioButtons_xpath = ['//*[@id="i5"]/div[3]/div','//*[@id="i8"]/div[3]/div','//*[@id="i11"]/div[3]/div','//*[@id="i14"]/div[3]/div']
gender_radioButtons_xpath = ['//*[@id="i21"]/div[3]/div','//*[@id="i24"]/div[3]/div']
education_radioButtons_xpath = ['//*[@id="i34"]/div[3]/div  ','//*[@id="i37"]/div[3]/div']
beenbullyied_radioButtons_xpath = ['//*[@id="i50"]/div[3]/div','//*[@id="i53"]/div[3]/div','//*[@id="i56"]/div[3]/div']
types_radioButtons_xpath = ['//*[@id="i63"]/div[3]/div','//*[@id="i66"]/div[3]/div','//*[@id="i69"]/div[3]/div','//*[@id="i72"]/div[3]/div']
factors_checkbox_xpath = ['//*[@id="i80"]/div[2]','//*[@id="i83"]/div[2]','//*[@id="i86"]/div[2]','//*[@id="i89"]/div[2]','//*[@id="i92"]/div[2]','//*[@id="i95"]/div[2]','//*[@id="i98"]/div[2]','//*[@id="i101"]/div[2]','//*[@id="i104"]/div[2]','//*[@id="i107"]/div[2]','//*[@id="i110"]/div[2]']
impacts_checkbox_xpath = ['//*[@id="i121"]/div[2]','//*[@id="i124"]/div[2]','//*[@id="i127"]/div[2]']
lognterm_radioButtons_xpath = ['//*[@id="i137"]/div[3]/div','//*[@id="i140"]/div[3]/div']
prevalent_radioButtons_xpath = ['//*[@id="i147"]/div[3]/div','//*[@id="i150"]/div[3]/div','//*[@id="i153"]/div[3]/div','//*[@id="i156"]/div[3]/div']
intervention_radioButtons_xpath = ['//*[@id="i163"]/div[3]/div','//*[@id="i166"]/div[3]/div']
famillyImpr_radioButtons_xpath = ['//*[@id="i176"]/div[3]/div','//*[@id="i179"]/div[3]/div','//*[@id="i182"]/div[3]/div','//*[@id="i185"]/div[3]/div']
antibully_radioButtons_xpath = ['//*[@id="i192"]/div[3]/div','//*[@id="i195"]/div[3]/div','//*[@id="i198"]/div[3]/div']
additionalMeasures_checkbox_xpath = ['//*[@id="i206"]/div[2]','//*[@id="i209"]/div[2]','//*[@id="i212"]/div[2]','//*[@id="i215"]/div[2]','//*[@id="i218"]/div[2]']
scale_xpath = ['//*[@id="mG61Hd"]/div[2]/div/div[2]/div[14]/div/div/div[2]/div/span/div/label[1]/div[2]/div/div/div[3]/div','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[14]/div/div/div[2]/div/span/div/label[2]/div[2]/div/div/div[3]/div','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[14]/div/div/div[2]/div/span/div/label[3]/div[2]/div/div/div[3]/div','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[14]/div/div/div[2]/div/span/div/label[4]/div[2]/div/div/div[3]/div','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[14]/div/div/div[2]/div/span/div/label[5]/div[2]/div/div/div[3]/div']
opinion_xpath = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[15]/div/div/div[2]/div/div[1]/div[2]/textarea'
opinions_answer = ['.','?','0',',','dont know','незнаю']
# time.sleep(5)
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

def clickOpinion(opinions,input_xpath):
    length_opinions = len(opinions)
    numOfOpinion = random.randrange(0, length_opinions)

    opinion_input = web.find_element("xpath", input_xpath)
    opinion_input.send_keys(opinions[numOfOpinion])
    print("succes")

while True:
    clickRadioButton(age_radioButtons_xpath)
    clickRadioButton(gender_radioButtons_xpath)
    clickRadioButton(education_radioButtons_xpath)
    clickRadioButton(beenbullyied_radioButtons_xpath)
    clickRadioButton(types_radioButtons_xpath)
    clickRadioButton(lognterm_radioButtons_xpath)
    clickRadioButton(prevalent_radioButtons_xpath)
    clickRadioButton(intervention_radioButtons_xpath)
    clickRadioButton(famillyImpr_radioButtons_xpath)
    clickRadioButton(antibully_radioButtons_xpath)
    clickRadioButton(scale_xpath)

    clickCheckBox(factors_checkbox_xpath) # error
    clickCheckBox(impacts_checkbox_xpath)
    clickCheckBox(additionalMeasures_checkbox_xpath)
    clickOpinion(opinions_answer,opinion_xpath)


    Submit = web.find_element("xpath",'//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span')
    Submit.click()


    get_confirmation_div_text = web.find_element(By.CLASS_NAME, 'vHW8K')
    print(get_confirmation_div_text.text)
    confirmation_text = get_confirmation_div_text.text
    if ((confirmation_text) == "Ответ записан."):
        print ("Test Was Successful")
        sendNew = web.find_element("xpath", '/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
        sendNew.click()
        time.sleep(2)
    else:
        print("Test Was Not Successful")
