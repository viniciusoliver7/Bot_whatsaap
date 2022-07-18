from selenium.webdriver.common.by import By


class PaneLocators(object):
    # parent
    PANE = (By.CSS_SELECTOR, "#pane-side")

    # childs
    # #pane-side ._210SC
    #new tag = _2nY6U vq6sj
    OPENED_CHATS = (By.CSS_SELECTOR, "#pane-side ._2nY6U")


    # grand child of each child
    ## left side
    #nova tag : _3GlyB
    ICON = (By.CSS_SELECTOR, "._3GlyB img")  # attr(src)
    ## right side

    ### upper side
    #tag: ._3OvU8 ._3vPI2 .zoWT4
    NAME = (By.CSS_SELECTOR, "._3OvU8 ._3vPI2 .zoWT4")

    #._3OvU8. _3vPI2. _1i_wG
    LAST_MESSAGE_TIME = (By.CSS_SELECTOR, "._3OvU8 ._3vPI2 ._1i_wG")

    ### bottom side
    # ARROW_STATUS = (By.CSS_SELECTOR, "._210SC ._1582E .zFnXi")

    #._3OvU8._37FrU._1qB8f
    LAST_MESSAGE = (By.CSS_SELECTOR, "._3OvU8 ._37FrU ._1qB8f")
    #(By.XPATH,'/html/body/div[1]/div/div/div[3]/div/div[2]/div[2]/div/div/div[11]/div/div/div[2]/div[2]/div[2]/span[1]/div')
    NOTIFICATION = (By.CSS_SELECTOR, "._2nY6U ._3OvU8 ._37FrU ._1i_wG ._1pJ9J")
    #(By.CSS_SELECTOR, "._2nY6U ._3OvU8 ._37FrU ._1i_wG ._1pJ9J")

    