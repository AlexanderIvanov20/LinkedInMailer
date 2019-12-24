from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep


driver = webdriver.Chrome(
    r'C:\Users\user\Documents\LinkedInMailer\chromedriver.exe')
driver.set_window_size(1280, 720)
driver.get(
    'https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin')

username = driver.find_element_by_xpath('//*[@id="username"]')
password = driver.find_element_by_xpath('//*[@id="password"]')

# username.send_keys('alexander.ivanov.289@gmail.com')
# password.send_keys('Domestos03')
username.send_keys('mup.folesta@gmail.com')
password.send_keys('Nikita777')
driver.find_element_by_xpath(
    '//*[@id="app__container"]/main/div/form/div[3]/button').submit()
sleep(1)


def send_invites(region, keyword):
    try:
        driver.get(
            f'https://www.linkedin.com/search/results/people/?facetGeoRegion=%5B%22{region}%3A0%22%5D&keywords={keyword}&origin=FACETED_SEARCH')
        sleep(1)

        driver.execute_script("window.scrollTo(0, 1100);")
        sleep(1)

        pages = int(driver.find_element_by_xpath(
            '//*[@class="ember-view"]/artdeco-pagination/ul/li[10]/button/span').text)
        print(pages)

        for page in range(1, pages + 1):
            driver.get(
                f'https://www.linkedin.com/search/results/people/?facetGeoRegion=%5B%22ua%3A0%22%5D&keywords=CEO&origin=FACETED_SEARCH&page={page}')
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
                        hello = current.click()
                        print(current.text)
                        sleep(1)
                        driver.find_element_by_css_selector(
                            'button.ml1.artdeco-button.artdeco-button--3.artdeco-button--primary.ember-view').click()
                        sleep(1)
                except Exception as er:
                    print(er)
        driver.close()
    except Exception:
        driver.close()


def send_message(start_user):
    driver.get('https://www.linkedin.com/mynetwork/invite-connect/connections/')

    count_contacts = int(driver.find_element_by_xpath(
        '//*[@class="mn-connections mb4 artdeco-card ember-view"]/header/h1').text.split(' ')[0])
    print(count_contacts)

    for item in range(0, count_contacts//40 + 1):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        sleep(1.5)

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
            '//*[@class="msg-form__message-texteditor relative flex-grow-1 display-flex ember-view"]/div[1]').send_keys('''Добрый день!
Меня зовут Никита, я работаю в Freshman Digital

Мы продвигаем бизнес-блогеров и увеличиваем выручку онлайн-бизнеса посредством маркетинга и рекламы. Для нас важно, чтобы клиенты получали услуги с хорошим соотношением цены к качеству, поэтому уже полтора года стабильно приносим им прибыли. 

Я знаю, что Вы уже поняли, что это рассылка, но если Вы планируете рекламировать свой бизнес или продвигать личный бренд не боясь, что случайно попадёте на безответственных исполнителей, а то и на дилетантов, то обратите внимание на наше коммерческое предложение: http://freshmansmm.com/offer

В конце короткой презентации, помимо предложения, видов услуг и кейсов есть контакты, по которым я с радостью Вас проконсультирую в течении часа после того, как Вы напишете.

Если же Вы хотите продвигать личный бренд в Instagram, то вот предложение для Вас: http://freshmansmm.com

Спасибо, что Вам хватило терпения дочитать это сообщение в мире, где реклама на каждом шагу. 

Пишите, звоните, я всегда на связи.''')
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
    sleep(10)


send_message(20)
# send_invites('ua', 'A,CEO')
