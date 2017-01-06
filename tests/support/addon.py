from random import Random
from urlparse import urljoin

from lettuce import world


@world.absorb
def random_str(randomlength=8, chars=None):
    rstr = ''
    if not chars:
        chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
    length = len(chars) - 1
    random = Random()
    for _ in range(randomlength):
        rstr += chars[random.randint(0, length)]
    return rstr


@world.absorb
def get_page(path):
    if hasattr(world, 'path_mappings') and path in world.path_mappings:
        world.browser.get(world.path_mappings[path])
    else:
        url = urljoin(world.host, path)
        world.browser.get(url)


@world.absorb
def find_elements(attribute_value, attribute=None, element_name=None):
    prefix = attribute_value[0]
    if prefix == '.':
        attribute_value = ' '.join([attr.lstrip('.') for attr in attribute_value.split(' ')])
        return world.browser.find_elements_by_class_name(attribute_value)
    elif prefix == '#':
        attribute_value = attribute_value[1:]
        return world.browser.find_elements_by_id(attribute_value)
    elif prefix == '~':
        attribute_value = attribute_value[1:]
        return world.browser.find_elements_by_name(attribute_value)
    elif attribute_value and attribute and element_name:
        xpath = '//%(element_name)s[@%(attribute)s]="%(attribute_value)s"' % {
            'attribute_value': attribute_value,
            'attribute': attribute,
            'element_name': element_name,
        }
        return world.browser.find_elements_by_xpath(xpath)
    else:
        return world.browser.find_elements_by_xpath(attribute_value)


@world.absorb
def find_element(attribute_value, attribute=None, element_name=None):
    elements = find_elements(attribute_value, attribute, element_name)
    return elements[0] if elements else None
