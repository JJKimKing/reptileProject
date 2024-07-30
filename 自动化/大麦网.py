# 实现自动登录购票

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

login_url = "https://passport.damai.cn/login?ru=https%3A%2F%2Fsearch.damai.cn"


def login_pass_word():
    options = webdriver.ChromeOptions()
    options.add_argument("start-maximized")
    options.add_experimental_option("excludeSwitches", ['enable-logging', 'enable-automation'])
    options.add_argument('--disable-gpu')
    user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.79 Safari/537.36"
    options.add_argument(f'user-agent={user_agent}')
    driver = webdriver.Chrome(options=options)
    # cookie = {
    #     "umdata_": "T2gAjScb7hY9qpUk11ttCUvUPuLzS7PAwunwB6NtbbzP08LfqZwGrWNM6DYTdib9ihQ=",
    #     "Max-Age": "31536000",
    #     "Expires": "Thu, 24-Jul-2025 03:03:06 GMT",
    #     "Domain": "ynuf.aliapp.org",
    #     "Path": "/",
    #     "SameSite": "None"
    # }
    # for key,value in cookie.items():
    #     driver.add_cookie({"name": key, "value": value})
    driver.get(login_url)
    # 等待页面完全加载
    WebDriverWait(driver, 10).until(
        lambda d: d.execute_script('return document.readyState') == 'complete'
    )

    # 增加调试信息
    # html_source = driver.page_source
    # print(html_source)

    iframe = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'alibaba-login-box'))
    )
    driver.switch_to.frame(iframe)

    try:
        driver.find_element(By.XPATH, value='//*[@id="fm-login-id"]').send_keys('18556503100')
        # driver.find_element(By.XPATH, value='//*[@id="fm-login-password"]').send_keys('xxxxx')
        # 滑块验证 一直提示错误不知道那里被标记了!
        input("--------")
        print("元素已找到")
    except:
        print("元素未找到")


if __name__ == "__main__":
    login_pass_word()
    input("--")
