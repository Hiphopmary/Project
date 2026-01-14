import os
import base64


import pytest
from selenium import webdriver



from selenium.webdriver.chrome.options import Options as ChromeOptions


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Specify browser: chrome or firefox")
    #parser.addoption("--size-maximized", action="store_true", help="maximized")
    #parser.addoption("--disable-extentions", action="store_true", help="disable extentions")
   # parser.addoption("--disable-popup-blocking", action="store_true", help="disable popup blocking")




@pytest.fixture(scope="function")
def browserInstance(request):


    browser_name=request.config.getoption("--browser").lower()
    #is_maximized=request.config.getoption("--size-maximized")
    #disable_extensions  = request.config.getoption("--disable-extentions")
    #disable_popup_blocking  = request.config.getoption("--disable-popup-blocking")

    if browser_name == "chrome":
        driver = webdriver.Chrome()
    elif browser_name == "edge":
        driver = webdriver.Edge()
    else:
        driver = webdriver.Firefox()

    driver.implicitly_wait(20)
    driver.get('https://rahulshettyacademy.com/loginpagePractise/')
    driver.maximize_window()
    request.node.driver = driver

    yield driver
    driver.quit()

@pytest.fixture(scope="function")
def checkinstance(request):
    inst=request.config.getoption("--browser").lower()
    if inst=="chrome":
        driver=webdriver.Chrome()
    elif inst=="edge":
        driver=webdriver.Edge()
    else:
        driver = webdriver.Firefox()

    driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
    driver.implicitly_wait(30)
    driver.maximize_window()
    request.node.driver = driver

    yield driver
    driver.quit()
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    pytest_html = item.config.pluginmanager.getplugin("html")
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        driver = getattr(item, "driver", None)
        if not driver:
            return

        png = driver.get_screenshot_as_png()
        b64 = base64.b64encode(png).decode("utf-8")

        extra = getattr(report, "extra", [])
        extra.append(
            pytest_html.extras.html(
                f'<img src="data:image/png;base64,{b64}" '
                f'style="width:400px;" onclick="window.open(this.src)">'
            )
        )
        report.extra = extra
