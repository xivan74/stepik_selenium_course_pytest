import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options



def pytest_addoption(parser):
    parser.addoption('--language', action='store', default="en",
                     help="Choose browser language")

@pytest.fixture(scope="function")
def browser(request):
    browser_lang = request.config.getoption("language")
    print(print("\nstart browser with language - {}".format(browser_lang)))
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': browser_lang})
    browser = webdriver.Chrome(options=options)
    yield browser
    print("\nquit browser..")
    browser.quit()
