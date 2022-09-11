import random
import string

from selenium import webdriver


def before_scenario(context, scenario):
    """Actions before every scenarios"""
    # object of ChromeOptions class
    op = webdriver.ChromeOptions()

    # browser preference
    p = {'download.default.directory': 'C:\\Users\\ValMar\\Downloads\\amazon_tests'}
    op.add_experimental_option('prefs', p)

    context.driver = webdriver.Chrome('C:\\Users\\ValMar\\Downloads\\chromedriver.exe', options=op)
    context.driver.maximize_window()
    amazon_url = 'https://www.amazon.com'
    context.driver.get(amazon_url)

    if 'skip' in scenario.tags:
        scenario.skip(reason='has @skip tag')
        return

    # Use uuid for random names generation
    context.uuid = '1' + ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(5))
    print(f'uuid: {context.uuid}')


def after_scenario(context, scenario):
    """Add test log creation"""
    print(f"Duration: {round(scenario.duration)} sec -> {context.scenario.name}")
    actual_log = context.driver.get.log('browser')
    messages = [_['message'] for _ in actual_log]
    print(f"\n" + 20 * '* ' + 'Start Log' + 20 * '* ')
    for msg in messages:
        print(msg)

    print(f"\n" + 20 * '* ' + 'End Log' + 20 * '* ')

    context.driver.quit()
