from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from linkedin_api import *

import os


def send_invites(region, keyword, username_user, password_user):
    driver_path = os.path.join('chromedriver.exe')
    driver = webdriver.Chrome(driver_path)
    driver.set_window_size(1600, 900)
    driver.get(
        'https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin')

    username = driver.find_element_by_xpath('//*[@id="username"]')
    password = driver.find_element_by_xpath('//*[@id="password"]')

    username.send_keys(username_user)
    password.send_keys(password_user)
    driver.find_element_by_xpath(
        '//*[@id="app__container"]/main/div/form/div[3]/button').submit()
    sleep(1)

    try:
        driver.get(
            f'https://www.linkedin.com/search/results/people/?facetGeoRegion=%5B%22{region}%3A0%22%5D&keywords={keyword}&origin=FACETED_SEARCH')
        sleep(1)

        driver.execute_script("window.scrollTo(0, 1100);")
        sleep(1)

        pages = int(driver.find_element_by_xpath(
            '//*[@class="ember-view"]/artdeco-pagination/ul/li[10]/button/span').text)

        for page in range(1, pages + 1):
            driver.get(
                f'https://www.linkedin.com/search/results/people/?facetGeoRegion=%5B%22{region}%3A0%22%5D&keywords={keyword}&origin=FACETED_SEARCH&page={page}')
            sleep(3)

            driver.execute_script("window.scrollTo(0, 1100)")
            sleep(1)

            ul = driver.find_element_by_xpath(
                '//*[@class="search-results__list list-style-none "]')
            lis = ul.find_elements_by_tag_name('li')
            sleep(1)

            for li in lis:
                try:
                    current = li.find_element_by_css_selector(
                        '.search-entity.search-result.search-result--person.search-result--occlusion-enabled.ember-view > div > div.search-result__actions > div.ember-view > button')
                    if current.text == 'Установить контакт':
                        current.click()
                        sleep(1)
                        driver.find_element_by_css_selector(
                            'button.ml1.artdeco-button.artdeco-button--3.artdeco-button--primary.ember-view').click()
                        sleep(1)
                except Exception as er:
                    print(er)
        driver.close()
    except Exception:
        driver.close()


def send_message(start_user: int, username_user, password_user, message):
    start_user = int(start_user)
    driver_path = os.path.join('chromedriver.exe')
    driver = webdriver.Chrome(driver_path)
    driver.set_window_size(1600, 900)
    driver.get(
        'https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin')

    username = driver.find_element_by_xpath('//*[@id="username"]')
    password = driver.find_element_by_xpath('//*[@id="password"]')

    username.send_keys(username_user)
    password.send_keys(password_user)
    driver.find_element_by_xpath(
        '//*[@id="app__container"]/main/div/form/div[3]/button').submit()
    sleep(1)

    driver.get('https://www.linkedin.com/mynetwork/invite-connect/connections/')

    count_contacts = int(driver.find_element_by_xpath(
        '//*[@class="mn-connections mb4 artdeco-card ember-view"]/header/h1').text.split(' ')[0])
    print(count_contacts)

    for item in range(0, count_contacts//40 + 1):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        sleep(1)

    ul_a = driver.find_element_by_xpath(
        '//*[@class="mn-connections mb4 artdeco-card ember-view"]/ul')
    lis_some = ul_a.find_elements_by_css_selector('.list-style-none')
    sleep(5)
    driver.find_element_by_tag_name('body').send_keys(Keys.HOME)
    sleep(3)
    iterator = start_user

    for li_c in lis_some:
        li_c.find_element_by_xpath(
            f'/html/body/div[5]/div[4]/div[3]/div/div/div/div/div/div/div/div/section/ul/li[{iterator}]/div/div[2]/div/button').click()
        sleep(1)
        li_c.find_element_by_xpath(
            '//*[@class="msg-form__message-texteditor relative flex-grow-1 display-flex ember-view"]/div[1]').send_keys(message)
        sleep(1)
        li_c.find_element_by_xpath(
            '//*[@class="msg-form__right-actions display-flex align-items-center"]//*[@class="ember-view"]/button').click()
        sleep(1)
        try:
            sleep(3)
            li_c.find_element_by_xpath(
                '//*[@class="artdeco-modal artdeco-modal--layer-default msg-modal-discard-message"]//*[@class="artdeco-button artdeco-button--2 artdeco-button--primary ember-view"]').click()
            sleep(1)
        except Exception:
            pass
        li_c.find_element_by_xpath(
            '//*[@class="msg-overlay-bubble-header__control js-msg-close artdeco-button artdeco-button--circle artdeco-button--inverse artdeco-button--1 artdeco-button--tertiary ember-view"]').click()
        iterator += 1
    driver.close()


def reply_on_invites(username_user, password_user):
    linked = Linkedin(username_user, password_user)
    invitationals = linked.get_invitations()

    for invite in invitationals:
        linked.reply_invitation(invitation_entity_urn=invite['entityUrn'],
                                invitation_shared_secret=invite['sharedSecret'])
