"""
Level 3 - Civil Rights, 1963
"""

LEVEL_3 = {
    'title': '1963 - CIVIL RIGHTS',
    'platforms': [
        # Ground platforms
        {'x': 0, 'y': 550, 'width': 350, 'height': 50},
        {'x': 450, 'y': 500, 'width': 200, 'height': 100},
        {'x': 750, 'y': 450, 'width': 250, 'height': 150},
        {'x': 1100, 'y': 400, 'width': 300, 'height': 200},
        {'x': 1500, 'y': 350, 'width': 200, 'height': 250},
        {'x': 1800, 'y': 500, 'width': 400, 'height': 100},

        # Floating platforms - stepping stones
        {'x': 350, 'y': 450, 'width': 80, 'height': 20},
        {'x': 500, 'y': 400, 'width': 100, 'height': 20},
        {'x': 650, 'y': 350, 'width': 80, 'height': 20},
        {'x': 850, 'y': 300, 'width': 120, 'height': 20},
        {'x': 1000, 'y': 250, 'width': 100, 'height': 20},
        {'x': 1200, 'y': 300, 'width': 150, 'height': 20},
        {'x': 1400, 'y': 250, 'width': 80, 'height': 20},
        {'x': 1600, 'y': 200, 'width': 100, 'height': 20}
    ],
    'timeHoles': [
        {'x': 350, 'y': 550, 'width': 100, 'height': 50},
        {'x': 650, 'y': 500, 'width': 100, 'height': 100},
        {'x': 1000, 'y': 450, 'width': 100, 'height': 150},
        {'x': 1400, 'y': 400, 'width': 100, 'height': 200},
        {'x': 1700, 'y': 500, 'width': 100, 'height': 100}
    ],
    'stones': [
        {'x': 550, 'y': 360},
        {'x': 925, 'y': 260},
        {'x': 1300, 'y': 260},
        {'x': 1650, 'y': 160}
    ],
    'enemies': [
        {'x': 600, 'y': 470, 'vx': 1, 'range': 100},
        {'x': 900, 'y': 270, 'vx': -1, 'range': 100},
        {'x': 1100, 'y': 370, 'vx': 1, 'range': 150},
        {'x': 1500, 'y': 320, 'vx': -1, 'range': 120}
    ],
    'portal': {'x': 2000, 'y': 430},
    'background': {
        'trees': [
            {'x': 350, 'y': 450},
            {'x': 700, 'y': 400},
            {'x': 1200, 'y': 350},
            {'x': 1700, 'y': 400}
        ],
        'signs': [  # Protest signs
            {'x': 500, 'y': 480, 'text': 'EQUALITY'},
            {'x': 1000, 'y': 380, 'text': 'FREEDOM'},
            {'x': 1600, 'y': 480, 'text': 'JUSTICE'}
        ],
        'march': True  # Special flag for civil rights march elements
    },
    'exercises': [
        {
            'question': 'If we _____ (march), change will come.',
            'answer': 'march',
            'hint': 'First conditional: present simple'
        },
        {
            'question': 'If laws _____ (be) fair, we wouldn\'t protest.',
            'answer': 'were',
            'hint': 'Second conditional: use "were"'
        },
        {
            'question': 'If people _____ (unite) now, justice would win.',
            'answer': 'united',
            'hint': 'Mixed conditional: past simple'
        },
        {
            'question': 'If you _____ (join) us, history changes.',
            'answer': 'join',
            'hint': 'First conditional: present simple'
        }
    ]
}