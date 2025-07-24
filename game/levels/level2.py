"""
Level 2 - Civil War, 1865
"""

LEVEL_2 = {
    'title': '1865 - CIVIL WAR',
    'platforms': [
        # Ground platforms
        {'x': 0, 'y': 500, 'width': 300, 'height': 100},
        {'x': 400, 'y': 550, 'width': 150, 'height': 50},
        {'x': 650, 'y': 450, 'width': 250, 'height': 150},
        {'x': 1000, 'y': 400, 'width': 200, 'height': 200},
        {'x': 1300, 'y': 350, 'width': 300, 'height': 250},
        {'x': 1700, 'y': 500, 'width': 400, 'height': 100},

        # Floating platforms
        {'x': 350, 'y': 400, 'width': 100, 'height': 20},
        {'x': 550, 'y': 350, 'width': 120, 'height': 20},
        {'x': 900, 'y': 300, 'width': 100, 'height': 20},
        {'x': 1200, 'y': 250, 'width': 150, 'height': 20}
    ],
    'timeHoles': [
        {'x': 300, 'y': 500, 'width': 100, 'height': 100},
        {'x': 550, 'y': 550, 'width': 100, 'height': 50},
        {'x': 900, 'y': 450, 'width': 100, 'height': 150},
        {'x': 1600, 'y': 500, 'width': 100, 'height': 100}
    ],
    'stones': [
        {'x': 475, 'y': 360},
        {'x': 775, 'y': 250},
        {'x': 1100, 'y': 200},
        {'x': 1450, 'y': 300}
    ],
    'enemies': [
        {'x': 700, 'y': 420, 'vx': -1, 'range': 100},
        {'x': 1000, 'y': 370, 'vx': 1, 'range': 120},
        {'x': 1400, 'y': 320, 'vx': -1, 'range': 150}
    ],
    'portal': {'x': 1900, 'y': 430},
    'background': {
        'trees': [
            {'x': 200, 'y': 400},
            {'x': 600, 'y': 350},
            {'x': 1100, 'y': 300},
            {'x': 1500, 'y': 250}
        ],
        'windmill': {'x': 1000, 'y': 150},
        'battlefield': True  # Special flag for battlefield elements
    },
    'exercises': [
        {
            'question': 'If the war _____ (end), families would reunite.',
            'answer': 'ended',
            'hint': 'Second conditional: past simple'
        },
        {
            'question': 'If people _____ (have) peace, they\'d be happy.',
            'answer': 'had',
            'hint': 'Past simple'
        },
        {
            'question': 'If unity _____ (be) possible, hope would grow.',
            'answer': 'were',
            'hint': 'Use "were" for all subjects'
        },
        {
            'question': 'If we _____ (work) together, we\'d heal.',
            'answer': 'worked',
            'hint': 'Past simple'
        }
    ]
}