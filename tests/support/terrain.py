from selenium import webdriver

from lettuce import before, after, world

from pyutils.ie_clear import clear_cookies


@before.all  # pylint: disable=no-member
def setup_host():
    world.host = ''
    # world.path_mappings = {}


@before.all  # pylint: disable=no-member
def setup_browser():
    world.browser = webdriver.Ie()


@before.all  # pylint: disable=no-member
def clear_browser():
    if isinstance(world.browser, webdriver.Ie):
        clear_cookies()


@before.each_scenario  # pylint: disable=no-member
def clear_session(scenario):
    world.browser.delete_all_cookies()


@after.all  # pylint: disable=no-member
def close_browser(total):
    world.browser.delete_all_cookies()
    world.browser.close()
