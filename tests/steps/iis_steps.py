# pylint: disable=missing-docstring

from lettuce import step, world
from nose.tools import assert_equal, assert_in, assert_true



@step('Navigate to (.*)')
def navigate_to_page(step, path):
    'Navigate to (.*)'
    world.get_page(path)


@step('Have account username: (.*), password: (.*)')
def set_account(step, username, password):
    world.username = username
    world.password = password


@step('Create a random account')
def create_random_account(step):
    world.username = world.random_str(8)
    world.password = world.random_str(16)


@step('Register with website account')
def register_with_account(step):
    world.find_element('~username').send_keys(world.username)
    world.find_element('~password1').send_keys(world.password)
    world.find_element('~password2').send_keys(world.password)
    world.find_element('//form[@class="form-signup"]//button').click()


@step('Login with website account')
def login_with_account(step):
    world.find_element('~username').send_keys(world.username)
    world.find_element('~password').send_keys(world.password)
    world.find_element('//form[@class="form-signin"]//button').click()


@step('See user-bar of website account')
def check_login_status(step):
    element = world.find_element('//div[@class="user-cta"]//i[@class="username"]')
    assert_equal(
        element.text,
        world.username,
        'login user should be %s, got %s' % (world.username, element.text)
    )


@step('Logout website')
def logout_website(step):
    world.find_element('//div[@class="user-cta"]//a[@href="/accounts/logout/"]').click()


@step('See (.*) in webpage')
def check_fragment_in_page(step, fragment):
    assert_in(
        fragment,
        world.browser.page_source,
        'cannot find %s in page' % fragment
    )


@step('See (.*) in title')
def check_fragment_in_title(step, fragment):
    assert_in(
        fragment,
        world.browser.title,
        'cannot find %s in title' % fragment
    )


@step('See title (.*)')
def check_title(step, title):
    title = '%s |' % title
    assert_true(
        world.browser.title.startswith(title),
        'title should be %s, got %s' % (title, world.browser.title)
    )
