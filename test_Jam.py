##IMPORT STATEMENTS##
##Run on command line with command: pytest --headed --base-url https://www.saucedemo.com/ --browser chromium --browser firefox --slowmo(3000) --tracing on
##View logs and tracing with command: playwright show-trace dir\trace.zip

from playwright.sync_api import Page
import pytest

##DECLARE VARIABLES & ENV URLS 
##urlDEV
##urlStage
##urlProd


##TC1: OPEN PAGE & Validate title matches expected string
def test_title(page: Page):
    page.goto("/")
    assert page.title() == "Swag Labs"

##TC2: OPEN PAGE & Validates a login error prompt is shown to users
def test_inventory_site(page: Page):
    page.goto("/inventory.html")
    assert page.inner_text('h3') == "Epic sadface: You can only access '/inventory.html' when you are logged in."


