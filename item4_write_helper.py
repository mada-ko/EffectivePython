# item 4 write helper function insted of complex expressions

from urllib.parse import parse_qs
my_values = parse_qs('red=5&blue=0&green=', keep_blank_values=True)
print(repr(my_values))

# # a default value of 0 was assigned when a parameter is not supply or is blank
# red = my_values.get('red', [''])[0] or 0
# green = my_values.get('green', [''])[0] or 0
# opacity = my_values.get('opacity', [''])[0] or 0
# print('Red:    %r' % red)
# print('Green:  %r' % green)
# print('Opacity:%r' % opacity)


# a default value of 0 was assigned when a parameter is not supply or is blank
def get_first_int(values, key, default=0):
    found = values.get(key, [''])
    if found[0]:
        found = int(found[0])
    else:
        found = default
    return found


red = get_first_int(my_values, 'red')
green = get_first_int(my_values, 'green')
opacity = get_first_int(my_values, 'opacity')
