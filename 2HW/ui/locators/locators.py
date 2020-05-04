from selenium.webdriver.common.by import By


class BaseLocators:
    COMPANY_BUTTON = (By.XPATH, '//div/a[@href="/campaigns/full"]')
    AUDIT_BUTTON = (By.CLASS_NAME, 'center-module-button-cQDNvq.center-module-segments-3y1hDo')
    SUGGESTION = (By.CLASS_NAME, 'suggester-ts__item__name')


class EnterLocators:
    ENTER_BUTTON = (By.CLASS_NAME, "responseHead-module-button-1BMAy4")
    EMAIL_FORM = (By.CLASS_NAME, "authForm-module-input-9t5W5U.input-module-input-1xGLR8")
    PASSWORD_FORM = (By.CLASS_NAME, "authForm-module-inputPassword-2Atq4Q.input-module-input-1xGLR8")
    CLICK_BUTTON = (By.CLASS_NAME, "authForm-module-button-2G6lZu")


class CompanyLocators(BaseLocators):
    CREATE_COMPANY_BUTTON = (By.CLASS_NAME, "campaigns-page__create-button")
    TARGET = (By.CLASS_NAME, "column-list-item._traffic")
    ADDRESS_FORM = (By.XPATH, '//input[@data-gtm-id="ad_url_text"]')
    CLEAR = (By.CLASS_NAME, 'input__clear.js-input-clear')
    COMP_NAME = (By.XPATH, '//div[@class="input input_campaign-name input_with-close"]/div'
                           '//input[@class="input__inp js-form-element"]')
    FORM_ADV = (By.ID, '192')
    PICTURE = (By.XPATH, '//input[@data-gtm-id="load_image_btn_240_400"]')
    SAVE = (By.CLASS_NAME, 'image-cropper__save.js-save')
    ADD_ADV = (By.XPATH, '//div[@class="banner-form__footer js-footer-wrap"]')
    SUBMIT = (By.XPATH, '//div[@class="footer__buttons-wrap"]')

    SEARCH = (By.CLASS_NAME, 'suggester-ts__input.suggester-ts__input_campaign-list-search')
    MY_COMP = (By.CLASS_NAME, 'campaign-title__name.js-campaign-name-title')


class AuditLocators(BaseLocators):
    CREATE_AUDIT = (By.XPATH, '//a[@href="/segments/segments_list/new"]')
    CREATE_OM_AUDIT = (By.CLASS_NAME, 'button.button_submit')
    AUDIT_NAME = (By.XPATH, '//div[@class="input input_create-segment-form"]/div'
                            '//input[@class="input__inp js-form-element"]')
    CREATE_AUDIT_BUTTON = (By.CLASS_NAME, 'create-segment-form__block.'
                                          'create-segment-form__block_add.js-add-segments-button')
    ADD_MY_LIST = (By.CLASS_NAME, 'adding-segments-source__checkbox.js-main-source-checkbox')
    SUBMIT_LIST = (By.CLASS_NAME, 'adding-segments-modal__btn-wrap.js-add-button')
    SUBMIT_CREATION = (By.CLASS_NAME, 'button.button_submit')
    SEARCH_AUDIT = (By.CLASS_NAME, 'suggester-ts__input')
    DELETE_AUDIT = (By.CLASS_NAME, 'icon-cross')
    CONFIRM_DELETING = (By.CLASS_NAME, 'button.button_confirm-remove.button_general')
    MY_AUDIT = (By.XPATH, '//td[@class="js-cell js-cell-name flexi-table__cell flexi-table__cell_name '
                          'js-cell-group-name js-cell-normal flexi-table__'
                          'cell_normal flexi-table__column-width _left"]'
                          '//a[@class="adv-camp-cell adv-camp-cell_name"]')
