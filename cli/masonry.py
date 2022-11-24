from __future__ import print_function, unicode_literals

from pprint import pprint

from PyInquirer import prompt, Separator

from examples import custom_style_4

def get_options(answers):

    if answers['type'] == 'A new DataBricks library':
         options = ['to a new DataBrick notebook', 'to an existing DataBrick notebook', 'skip for now']
    else:
         options = ['new DataBrick library', 'existing DataBrick library', 'skip for now']
    return options

print("Welcome to Masonry!")
questions = [
    {
        'type': 'list',
        'name': 'type',
        'message': 'What do you want to build?',
        'choices': [
            'A new DataBricks library',
            'A new DataBricks orchestrator notebook',
            Separator(),
            {
                'name': 'Add an exsiting library to a exsiting notebook',
                'disabled': 'Unavailable at this time'
            },
        ]
    },
    {
        'type': 'list',
        'name': 'addTo',
        'message': 'Add?',
        'choices': get_options,
    }
]

answers = prompt(questions, style=custom_style_4)
pprint(answers)
