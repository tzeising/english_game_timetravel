"""
Level 1 - Philadelphia, 1776
"""

LEVEL_1 = {
    'title': 'PHILADELPHIA, 1776',
    'platforms': [
        # Ground level platforms
        {'x': 0, 'y': 520, 'width': 250, 'height': 80},
        {'x': 350, 'y': 520, 'width': 200, 'height': 80},
        {'x': 650, 'y': 520, 'width': 150, 'height': 80},
        {'x': 900, 'y': 520, 'width': 200, 'height': 80},
        {'x': 1200, 'y': 520, 'width': 300, 'height': 80},
        {'x': 1600, 'y': 520, 'width': 250, 'height': 80},
        {'x': 1950, 'y': 520, 'width': 300, 'height': 80},

        # Mid-level floating platforms
        {'x': 400, 'y': 400, 'width': 100, 'height': 20},
        {'x': 700, 'y': 350, 'width': 120, 'height': 20},
        {'x': 1000, 'y': 300, 'width': 100, 'height': 20},
        {'x': 1300, 'y': 400, 'width': 150, 'height': 20},
        {'x': 1550, 'y': 450, 'width': 100, 'height': 20},
        {'x': 1700, 'y': 350, 'width': 100, 'height': 20},

        # Upper level platforms
        {'x': 550, 'y': 250, 'width': 100, 'height': 20},
        {'x': 850, 'y': 200, 'width': 120, 'height': 20},
        {'x': 1150, 'y': 250, 'width': 100, 'height': 20},
        {'x': 1450, 'y': 200, 'width': 120, 'height': 20}
    ],
    'timeHoles': [
        {'x': 250, 'y': 520, 'width': 100, 'height': 80},
        {'x': 550, 'y': 520, 'width': 100, 'height': 80},
        {'x': 800, 'y': 520, 'width': 100, 'height': 80},
        {'x': 1100, 'y': 520, 'width': 100, 'height': 80},
        {'x': 1500, 'y': 520, 'width': 100, 'height': 80},
        {'x': 1850, 'y': 520, 'width': 100, 'height': 80}
    ],
    'stones': [
        {'x': 450, 'y': 360},
        {'x': 600, 'y': 210},
        {'x': 1050, 'y': 260},
        {'x': 1375, 'y': 360},
        {'x': 1750, 'y': 310}
    ],
    'enemies': [
        {'x': 700, 'y': 326, 'vx': 1, 'range': 80},
        {'x': 850, 'y': 176, 'vx': -1, 'range': 80},
        {'x': 1200, 'y': 488, 'vx': 1, 'range': 200},
        {'x': 1450, 'y': 176, 'vx': 1, 'range': 80}
    ],
    'portal': {'x': 2100, 'y': 450},
    'background': {
        'colonialBuildings': [
            {'x': 200, 'y': 440},
            {'x': 800, 'y': 440},
            {'x': 1400, 'y': 440},
            {'x': 1900, 'y': 440}
        ],
        'libertyBell': {'x': 1100, 'y': 420},
        'streetLamps': [
            {'x': 100, 'y': 470},
            {'x': 600, 'y': 470},
            {'x': 1300, 'y': 470},
            {'x': 1800, 'y': 470}
        ],
        'horses': [
            {'x': 450, 'y': 470},
            {'x': 1000, 'y': 470}
        ]
    },
    'exercises': [
        {
            'question': 'If the colonies _____ (unite), they will gain freedom.',
            'answer': 'unite',
            'hint': 'First conditional: present simple'
        },
        {
            'question': 'If people _____ (believe) in liberty, they will fight.',
            'answer': 'believe',
            'hint': 'Present simple'
        },
        {
            'question': 'If the Declaration _____ (be) signed, history will change.',
            'answer': 'is',
            'hint': 'Use "is" for singular'
        },
        {
            'question': 'If citizens _____ (stand) together, they will succeed.',
            'answer': 'stand',
            'hint': 'Present simple'
        },
        {
            'question': 'If leaders _____ (speak) truth, people will follow.',
            'answer': 'speak',
            'hint': 'Present simple'
        }
    ]
}