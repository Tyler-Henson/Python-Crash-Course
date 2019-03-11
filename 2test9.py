from collections import OrderedDict
# keeps order like a list but is still a dictionary
favorite_languages = OrderedDict()

favorite_languages['jen'] = 'python'
favorite_languages['alice'] = 'c++'
favorite_languages['xai'] = 'python'

for person in favorite_languages.items():
    print(person)
