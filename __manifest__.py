# -*- coding: utf-8 -*-
{
    'name': "ToDo Users",

    'summary': """
            Extend  the To-Do   app to  multiuser.
        """,

    'description': """
        Our To-Do   application now allows  users   to  privately   manage  their   own to-do
        tasks.  Won't   it  be  great   to  take    the app to  another level   by  adding  collaboration
        and social  networking  features    to  it, we  will    be  able    to  share   tasks   and discuss
        them    with    other   people.
    """,

    'author': "OTB Africa",
    'website': "http://www.otbafricadeveloper.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','todo_app','mail'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
        'security/todo.task.csv'
    ],
}