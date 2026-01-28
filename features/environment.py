from behave import fixture, use_fixture
from selenium.webdriver import Chrome
from django.contrib.auth import get_user_model

User = get_user_model()

@fixture
def browser_chrome(context):
    context.browser = Chrome()
    yield context.browser
    context.browser.quit()


def before_scenario(context, scenario):
    use_fixture(browser_chrome, context)
    if scenario.name == 'Вход под админом':
        User.objects.create_user(username='admin', password='admin')