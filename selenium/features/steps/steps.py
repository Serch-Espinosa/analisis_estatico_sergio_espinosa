import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium_stealth import stealth
from behave import given, when, then

UNIVERSITY_DOMAINS = {
    "ITESO":            "iteso.mx",
    "UNAM":             "unam.mx",
    "Tec de Monterrey": "tec.mx",
}

UNIVERSITIES_CONFIG = {
    "ITESO": {
        "btn_lupa": [
            (By.ID, "icon-search"),
            (By.CSS_SELECTOR, "[aria-label*='search' i]"),
            (By.CSS_SELECTOR, ".search-icon, .icon-search"),
        ],
        "input_text": [
            (By.ID, "ipt-search"),
            (By.CSS_SELECTOR, "input[type='search']"),
            (By.CSS_SELECTOR, "input[name*='search']"),
        ],
        "btn_submit": None,
    },
    "UNAM": {
        "btn_lupa": [
            (By.CSS_SELECTOR, ".gsc-search-button, .gsst_a"),
            (By.CSS_SELECTOR, "button.gsc-search-button-v2"),
            (By.XPATH, "//button[contains(@class,'gsc')]"),
        ],
        "input_text": [
            (By.CSS_SELECTOR, "input.gsc-input, input.gsc-search-box"),
            (By.CSS_SELECTOR, "input[name='search'], input[name='q']"),
            (By.XPATH, "//input[contains(@class,'gsc')]"),
        ],
        "btn_submit": [
            (By.CSS_SELECTOR, "button.gsc-search-button, input.gsc-search-button"),
            (By.XPATH, "//button[contains(@class,'gsc-search')]"),
        ],
    },
    "Tec de Monterrey": {
        "btn_lupa": [
            (By.CSS_SELECTOR, "button.search-box__button"),
            (By.XPATH, "//button[contains(@class,'search-box__button')]"),
        ],
        "input_text": [
            (By.CSS_SELECTOR, "input.form-item__textfield"),
            (By.CSS_SELECTOR, "input[data-drupal-selector*='edit-search']"),
            (By.CSS_SELECTOR, "input[id*='edit-search']"),
            (By.XPATH, "//input[contains(@class,'form-item__textfield')]"),
        ],
        "btn_submit": [
            (By.CSS_SELECTOR,
             "input.search-box__button.button.js-form-submit.form-submit"),
            (By.CSS_SELECTOR, "input[data-drupal-selector*='edit-submit']"),
            (By.XPATH, "//input[contains(@class,'js-form-submit')]"),
        ],
    },
}

def human_type(element, text):
    """Escribe carácter por carácter simulando ritmo humano."""
    for char in text:
        element.send_keys(char)
        time.sleep(random.uniform(0.08, 0.18))
        if random.random() < 0.10:
            time.sleep(random.uniform(0.3, 0.6))
        if random.random() < 0.04:
            element.send_keys(Keys.BACK_SPACE)
            time.sleep(random.uniform(0.2, 0.4))
            element.send_keys(char)


def human_pause(min_s=0.8, max_s=2.0):
    """Pausa aleatoria para simular tiempo de lectura o decisión."""
    time.sleep(random.uniform(min_s, max_s))


def try_locate(driver, locators, visible=False, timeout=6):
    """Intenta cada localizador en orden y devuelve el primero que encuentre."""
    if not isinstance(locators, list):
        locators = [locators]
    condition = (EC.visibility_of_element_located if visible
                 else EC.presence_of_element_located)
    for loc in locators:
        try:
            return WebDriverWait(driver, timeout).until(condition(loc))
        except Exception:
            continue
    return None

@given("I open the Chrome browser")
def step_open_browser(context):
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option("useAutomationExtension", False)
    options.add_experimental_option("detach", True)

    context.driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options,
    )
    stealth(
        context.driver,
        languages=["es-MX", "es", "en-US", "en"],
        vendor="Google Inc.",
        platform="Win32",
        webgl_vendor="Intel Inc.",
        renderer="Intel Iris OpenGL Engine",
        fix_hairline=True,
    )
    context.wait = WebDriverWait(context.driver, 15)


@when('I search for "{university}" on Google')
def step_search_google(context, university):
    context.current_university = university
    driver = context.driver

    driver.get("https://www.google.com")
    human_pause(1.5, 2.5)

    try:
        accept_btn = WebDriverWait(driver, 4).until(
            EC.element_to_be_clickable(
                (By.XPATH, "//button[.//span[contains(text(),'Aceptar') "
                           "or contains(text(),'Accept') "
                           "or contains(text(),'Acepto')]]")
            )
        )
        accept_btn.click()
        human_pause(0.8, 1.5)
    except Exception:
        pass

    search_box = context.wait.until(
        EC.visibility_of_element_located((By.NAME, "q"))
    )
    search_box.click()
    human_pause(0.4, 0.9)
    human_type(search_box, university)
    human_pause(0.5, 1.2)
    search_box.send_keys(Keys.RETURN)
    human_pause(1.5, 2.5)


@then('I should see the official link for "{university}" in the results')
def step_verify_link_in_results(context, university):
    domain = UNIVERSITY_DOMAINS.get(university)
    assert domain, f"No domain configured for: {university}"
    assert domain.lower() in context.driver.page_source.lower(), (
        f"'{domain}' not found in Google results for: {university}"
    )
    print(f"  [OK] Domain '{domain}' visible in Google results")


@then('I click on the first result for "{university}"')
def step_click_first_result(context, university):
    driver = context.driver
    domain = UNIVERSITY_DOMAINS.get(university)

    links = driver.find_elements(By.CSS_SELECTOR, "a[href]")
    clicked = False
    for link in links:
        href = link.get_attribute("href") or ""
        if domain in href:
            driver.execute_script(
                "arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});",
                link
            )
            human_pause(0.5, 1.0)
            driver.execute_script("arguments[0].click();", link)
            clicked = True
            human_pause(2.5, 4.0)
            break

    assert clicked, f"No link containing '{domain}' found in Google results"


@then('I verify that I am on the "{university}" website')
def step_verify_page(context, university):
    driver = context.driver
    domain = UNIVERSITY_DOMAINS.get(university)
    assert domain in driver.current_url.lower(), (
        f"Expected '{domain}' but current URL is: {driver.current_url}"
    )
    print(f"  [OK] Successfully navigated to {university}: {driver.current_url}")


@then('I search for "{term}" using the internal search bar')
def step_internal_search(context, term):
    driver = context.driver
    university = context.current_university
    config = UNIVERSITIES_CONFIG.get(university)
    assert config, f"No internal search config for: {university}"

    try:
        lupa = try_locate(driver, config["btn_lupa"])
        if lupa:
            driver.execute_script(
                "arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});",
                lupa
            )
            human_pause(0.4, 0.8)
            driver.execute_script("arguments[0].click();", lupa)
            human_pause(1.0, 1.8)
        else:
            print(f"  [WARN] No search icon found for {university}, "
                  "trying input directly.")

        search_input = try_locate(driver, config["input_text"], visible=True)
        assert search_input, (
            f"Search input not found for {university}"
        )
        driver.execute_script(
            "arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});",
            search_input
        )
        human_pause(0.3, 0.7)
        search_input.clear()
        human_type(search_input, term)
        human_pause(0.5, 1.0)

        if config["btn_submit"]:
            btn = try_locate(driver, config["btn_submit"])
            if btn:
                driver.execute_script("arguments[0].click();", btn)
            else:
                search_input.send_keys(Keys.RETURN)
        else:
            search_input.send_keys(Keys.RETURN)

        human_pause(3.0, 4.5)

    except AssertionError:
        raise
    except Exception as e:
        driver.save_screenshot(f"error_{university}_{term}.png")
        raise AssertionError(
            f"Error searching '{term}' on {university}: {e}"
        )


@then('I should see results related to "{term}"')
def step_verify_results(context, term):
    driver = context.driver
    assert term.lower() in driver.page_source.lower(), (
        f"'{term}' not found on {context.current_university}. "
        f"URL: {driver.current_url}"
    )
    print(f"  [OK] '{term}' found on {context.current_university}")
