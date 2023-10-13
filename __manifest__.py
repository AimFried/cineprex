# -*- coding: utf-8 -*-
{
    'name': "CinePrex",
    'summary': """
        Module de gestion de salles de cinema
        """,
    'description': """
       Module de gestion de salles de cinema
    """,
    'author': "CinePrex",
    'website': "http://www.cineprex.fr",
    'category': 'Custom',
    'version': '1.0',
    'depends': ['base','hr'],
    'data': [
        'views/templates.xml',
        'views/villes.xml',
        'views/cinemas.xml',
        'views/salles.xml',
        'views/seances.xml',
        'views/films.xml',
        'views/menu.xml',
        'security/ir.model.access.csv',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    "installable": True,
    "application": True,
}
