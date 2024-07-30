# 使用selenium实现自动化登陆
from selenium import webdriver
from selenium.webdriver.common.by import By

user_name = 'xxxx'
password = '<PASSWORD>'

if __name__ == '__main__':
    # 设置一些配置
    options = webdriver.ChromeOptions()
    # #最大化启动
    options.add_argument("start-maximized")
    # 不显示 Chrome 启动日志,禁用 WebDriver 自动化标识，减少被检测的风险
    options.add_experimental_option('excludeSwitches', ['enable-logging', 'enable-automation'])
    # 禁用gpu
    options.add_argument('--disable-gpu')

    # options.chrome_driver_path = './chromedriver'
    driver = webdriver.Chrome(options=options)
    driver.get('https://kyfw.12306.cn/otn/resources/login.html')

    driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
        "source": """
        Object.defineProperty(navigator, 'webdriver', {
          get: () => undefined
        })
      """
    })

    login_user_name = driver.find_element(by=By.ID, value='J-userName')
    login_user_name.send_keys(user_name)
    login_password = driver.find_element(by=By.ID, value='J-password')
    login_password.send_keys(password)
    # 查询登陆接口实现登陆
    login_button = driver.find_element(by=By.ID, value='J-login')
    login_button.click()
    # 实现输入证件和短信验证码
    paper_work = input("请输入证件后4位帮助验证:")
    driver.find_element(by=By.ID, value='id_card').send_keys(paper_work)
    driver.find_element(by=By.ID, value='verification_code').click()
    code = input("请输入短信验证码:")
    driver.find_element(by=By.ID, value='sureClick').click()
    print('--------------------------------正在登陆-----------------------------------------------------')
    input("-----")
    driver.quit()
