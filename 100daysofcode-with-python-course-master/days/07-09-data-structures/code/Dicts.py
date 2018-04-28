import re

people = {}
people['George Washington'] = 345
people['MOther Teresa'] = 102
people['Donald Trump'] = 73
for k,v in people.items():
    print(f'Behold the great {k} is {v} years old')


cars = {
    'Ford': ['Falcon', 'Focus', 'Festiva', 'Fairlane'],
    'Holden': ['Commodore', 'Captiva', 'Barina', 'Trailblazer'],
    'Nissan': ['Maxima', 'Pulsar', '350Z', 'Navara'],
    'Honda': ['Civic', 'Accord', 'Odyssey', 'Jazz'],
    'Jeep': ['Grand Cherokee', 'Cherokee', 'Trailhawk', 'Trackhawk']
}


def get_all_jeeps():
    """return a comma separated string of jeep models (original order)"""
    for k,v in cars.items():
        if k == 'Jeep':
            print(v)
    pass


def get_first_model_each_manufacturer():
    """return a list of matching models (original ordering)"""
    for v in cars.values():
        print(v[0])
    pass


def get_all_matching_models(grep='trail'):
    """return a list of all models containing the case insensitive
       'grep' string which defaults to 'trail' for this exercise,
       sort the resulting sequence alphabetically"""
    for v in cars.values():
        for car in v:
            search_term = r'^'+re.escape(grep.capitalize())
            match = re.search(search_term,car)
            if match is not None:
                print(car)
    pass

def sort_car_models():
    """sort the car models (values) and return the resulting cars dict"""
    for k,v in cars.items():
        v.sort()
        print(f'{k}:{v}')
    pass


#get_all_jeeps()
#get_first_model_each_manufacturer()
get_all_matching_models()
sort_car_models()