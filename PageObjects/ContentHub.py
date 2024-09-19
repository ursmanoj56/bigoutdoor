import time

from selenium.webdriver.common.by import By

from PageObjects.BasePage import BasePage


class ContentHub(BasePage):

    UPLOAD_BUTTON=(By.XPATH,"//button[text()=' Upload']")
    BACK_BUTTON = (By.XPATH,"//button[text()=' Back']")
    SEARCH_BAR = (By.XPATH,"//input[@placeholder='Search Creatives']")
    RESOLUTION_WIDTH= (By.XPATH,"//input[@placeholder='Resolution Width']")
    RESOLUTION_HEIGHT = (By.XPATH,"//input[@placeholder='Resolution Height']")
    JPEG_IMAGE =(By.XPATH,"(//span[@class='respadding'])[1]")
    PNG_IMAGE = (By.XPATH, "(//span[@class='respadding'])[2]")
    MP4_VIDEO = (By.XPATH, "(//span[@class='respadding'])[3]")
    CLOSE_BUTTON= (By.XPATH, "//button[text()=' Close ']")
    APPLY_BUTTON = (By.XPATH, "//button[text()='Apply ']")
    PREVIOUS_PAGE = (By.XPATH,"//a[@aria-label='Previous']")
    NEXT_PAGE = (By.XPATH,"//a[@aria-label='Next']//child::i")
    INPUT_GO_PAGE = (By.XPATH,"//input[@type='number']")
    GO_BUTTON =(By.XPATH,"//button[text()='Go']")
    DELETE_CREATIVES = (By.XPATH,"(//button[contains(text(),'Delete')])[1]")
    THUMBNAIL_IMAGE= (By.XPATH,"(//img[contains(@class,'billboard-thumbnail')])[1]")
    CREATIVE_NAME=(By.XPATH,"(//span[@class='list-img-cont'])[1]")
    CREATIVE_TYPE= (By.XPATH,"(//span[@class='list-img-cont']//following::td[1])[1]")
    CREATIVE_RESOLUTION=(By.XPATH,"(//span[@class='list-img-cont']//following::td[2])[1]")
    FILTER_OPTION= (By.XPATH,"//i[contains(@class,'search-icon-right')]")
    RESET_FILTER= (By.XPATH,"//button[text()='Reset']")
    DELETE_YES = (By.XPATH ,"//button[text()='Yes ']")
    DELETE_NO =(By.XPATH,"//button[text()=' No ']")
    UPLOAD_FILE= (By.XPATH,"//button[text()='Browse']")
    UPLOAD =(By.XPATH,"//button[text()='Upload']")


    def __init__(self, driver):
        super().__init__(driver)

    def upload_button_is_displayed(self):
        return self.is_displayed(self.UPLOAD_BUTTON)

    def upload_button_clickable(self):
        return self.clickable(self.UPLOAD_BUTTON)

    def back_button_is_displayed(self):
        return self.is_displayed(self.BACK_BUTTON)

    def back_button_is_clickable(self):
        return self.clickable(self.BACK_BUTTON)

    def back_button_click_operation(self):
        self.click_button(self.BACK_BUTTON)
        return self.get_current_url()

    def search_bar_is_displayed(self):
        return self.is_displayed(self.SEARCH_BAR)

    def search_bar_is_enterable(self,name):
        self.text_inputs(self.SEARCH_BAR,name)

    def validate_search_item(self,name):
        self.text_inputs(self.SEARCH_BAR, name)
        self.press_enter()
        time.sleep(2)
        return self.get_text(self.CREATIVE_NAME)


    def filter_option_is_displayed(self):
        return self.is_displayed(self.FILTER_OPTION)

    def filter_option_clickable(self):
        return self.clickable(self.FILTER_OPTION)

    def resolution_width_option_displayed(self):
        self.click_button(self.FILTER_OPTION)
        return self.is_displayed(self.RESOLUTION_WIDTH)

    def resolution_height_option_displayed(self):
        self.click_button(self.FILTER_OPTION)
        return self.is_displayed(self.RESOLUTION_HEIGHT)

    def resolution_width_option_enterable(self,value):
        self.click_button(self.FILTER_OPTION)
        self.text_input(self.RESOLUTION_WIDTH,value)

    def resolution_height_option_enterable(self,value):
        self.click_button(self.FILTER_OPTION)
        self.text_input(self.RESOLUTION_HEIGHT,value)

    def png_image_option_displayed(self):
        self.click_button(self.FILTER_OPTION)
        return self.is_displayed(self.PNG_IMAGE)

    def png_image_option_clickable(self):
        self.click_button(self.FILTER_OPTION)
        return self.clickable(self.PNG_IMAGE)

    def jpeg_image_option_displayed(self):
        self.click_button(self.FILTER_OPTION)
        return self.is_displayed(self.JPEG_IMAGE)

    def jpeg_image_option_clickable(self):
        self.click_button(self.FILTER_OPTION)
        return self.clickable(self.JPEG_IMAGE)

    def video_option_is_displayed(self):
        self.click_button(self.FILTER_OPTION)
        return self.is_displayed(self.MP4_VIDEO)

    def video_option_is_clickable(self):
        self.click_button(self.FILTER_OPTION)
        return self.clickable(self.MP4_VIDEO)

    def close_button_is_displayed(self):
        self.click_button(self.FILTER_OPTION)
        self.scroll_into_view(self.CLOSE_BUTTON)
        return self.is_displayed(self.CLOSE_BUTTON)

    def apply_button_is_displayed(self):
        self.click_button(self.FILTER_OPTION)
        self.scroll_into_view(self.CLOSE_BUTTON)
        return self.is_displayed(self.APPLY_BUTTON)

    def close_button_is_clickable(self):
        self.click_button(self.FILTER_OPTION)
        self.scroll_into_view(self.CLOSE_BUTTON)
        return self.is_displayed(self.CLOSE_BUTTON)

    def apply_button_is_clickable(self):
        self.click_button(self.FILTER_OPTION)
        self.scroll_into_view(self.CLOSE_BUTTON)
        return self.is_displayed(self.APPLY_BUTTON)

    def next_page_is_displayed(self):
        self.scroll_into_view(self.NEXT_PAGE)
        return self.is_displayed(self.NEXT_PAGE)

    def previous_page_is_displayed(self):
        self.scroll_into_view(self.PREVIOUS_PAGE)
        return self.is_displayed(self.PREVIOUS_PAGE)

    def next_page_is_clickable(self):
        self.scroll_into_view(self.NEXT_PAGE)
        return self.clickable(self.NEXT_PAGE)

    def previous_page_is_clickable(self):
        self.scroll_into_view(self.PREVIOUS_PAGE)
        return self.clickable(self.PREVIOUS_PAGE)

    def next_page_click_operation(self):
        self.scroll_into_view(self.NEXT_PAGE)
        time.sleep(3)
        self.click_button(self.NEXT_PAGE)

    def prevoius_page_click_operation(self):
        self.scroll_into_view(self.NEXT_PAGE)
        time.sleep(2)
        self.click_button(self.NEXT_PAGE)
        time.sleep(2)
        self.click_button(self.PREVIOUS_PAGE)

    def input_go_option_displayed(self):
        self.scroll_into_view(self.INPUT_GO_PAGE)
        return self.is_displayed(self.INPUT_GO_PAGE)

    def go_button_is_displayed(self):
        self.scroll_into_view(self.GO_BUTTON)
        return self.is_displayed(self.GO_BUTTON)

    def go_button_is_clickable(self):
        self.scroll_into_view(self.GO_BUTTON)
        return self.clickable(self.GO_BUTTON)

    def performance_of_input_go_operation(self,value):
        self.scroll_into_view(self.INPUT_GO_PAGE)
        time.sleep(2)
        self.text_input(self.INPUT_GO_PAGE,value)
        self.click_button(self.GO_BUTTON)

    def filter_by_jpeg_image(self):
        self.click_button(self.FILTER_OPTION)
        self.click_button(self.JPEG_IMAGE)
        self.click_button(self.APPLY_BUTTON)
        time.sleep(2)
        return self.get_text(self.CREATIVE_TYPE)

    def filter_by_png_image(self):
        self.click_button(self.FILTER_OPTION)
        self.click_button(self.PNG_IMAGE)
        self.click_button(self.APPLY_BUTTON)
        time.sleep(2)
        return self.get_text(self.CREATIVE_TYPE)

    def filter_by_mp4_video(self):
        self.click_button(self.FILTER_OPTION)
        self.click_button(self.MP4_VIDEO)
        self.click_button(self.APPLY_BUTTON)
        time.sleep(2)
        return self.get_text(self.CREATIVE_TYPE)

    def thubnails_is_displayed_in_table(self):
        return self.is_displayed(self.THUMBNAIL_IMAGE)

    def creative_name_is_displayed_in_table(self):
        return self.is_displayed(self.CREATIVE_NAME)

    def creative_type_displayed_in_table(self):
        return self.is_displayed(self.CREATIVE_TYPE)

    def resolution_is_displayed_in_table(self):
        return self.is_displayed(self.CREATIVE_RESOLUTION)

    def delete_option_is_displayed_in_table(self):
        return self.is_displayed(self.DELETE_CREATIVES)

    def filter_by_resolution(self,value1,value2):
        self.click_button(self.FILTER_OPTION)
        self.text_input(self.RESOLUTION_WIDTH,value1)
        self.text_input(self.RESOLUTION_HEIGHT,value2)
        self.click_button(self.APPLY_BUTTON)
        return self.get_text(self.CREATIVE_RESOLUTION)

    def reset_filter_is_displayed(self):
        self.click_button(self.FILTER_OPTION)
        self.click_button(self.PNG_IMAGE)
        self.click_button(self.APPLY_BUTTON)
        return self.is_displayed(self.RESET_FILTER)

    def reset_filter_is_clickable(self):
        self.click_button(self.FILTER_OPTION)
        self.click_button(self.PNG_IMAGE)
        self.click_button(self.APPLY_BUTTON)
        return self.clickable(self.RESET_FILTER)

    def reset_filter_operation(self):
        self.click_button(self.FILTER_OPTION)
        self.click_button(self.PNG_IMAGE)
        self.click_button(self.APPLY_BUTTON)
        self.clickable(self.RESET_FILTER)

    def close_button_operation(self):
        self.click_button(self.FILTER_OPTION)
        self.click_button(self.PNG_IMAGE)
        self.click_button(self.CLOSE_BUTTON)
        return self.is_displayed(self.CLOSE_BUTTON)

    def no_option_in_delete_creatives_is_displayed(self):
        self.click_button(self.DELETE_CREATIVES)
        return self.is_displayed(self.DELETE_NO)

    def yes_option_in_delete_creatives_is_displayed(self):
        self.click_button(self.DELETE_CREATIVES)
        return self.is_displayed(self.DELETE_YES)

    def no_option_in_delete_creatives_is_clickable(self):
        self.click_button(self.DELETE_CREATIVES)
        return self.clickable(self.DELETE_NO)

    def yes_option_in_delete_creatives_is_clickable(self):
        self.click_button(self.DELETE_CREATIVES)
        return self.clickable(self.DELETE_YES)

    def no_option_in_delete_creatives_operation(self):
        self.click_button(self.DELETE_CREATIVES)
        self.click_button(self.DELETE_NO)

    def yes_option_in_delete_creatives_operation(self):
        self.click_button(self.DELETE_CREATIVES)
        self.click_button(self.DELETE_YES)
        time.sleep(2)
        return self.get_text(self.CREATIVE_NAME)

    def upload_file_button_is_displayed(self):
        self.click_button(self.UPLOAD_BUTTON)
        return self.is_displayed(self.UPLOAD_FILE)

    def upload_file_button_is_clickable(self):
        self.click_button(self.UPLOAD_BUTTON)
        return self.clickable(self.UPLOAD_FILE)

    def validate_upload_file(self,path):
        self.click_button(self.UPLOAD_BUTTON)
        self.upload_file(self.UPLOAD_FILE,path)
        time.sleep(6)






















