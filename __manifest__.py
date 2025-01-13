# -*- coding: utf-8 -*-
{
    'name': "admin_hotel",

    'summary': "Short (1 phrase/line) summary of the module's purpose",

    'description': """
Long description of module's purpose
    """,

    'author': "My Company",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/groups.xml',
        # 'security/hotel_security.xml',
        # 'security/record_rules.xml',
        'security/ir.model.access.csv',
        # 'views/views.xml',
        'views/menu_views.xml',
    'views/hotel_management_views.xml',
    'views/hotel_room_views.xml',
    'views/hotel_reservation_views.xml',
    'views/hotel_room_feature_views.xml',
    'views/booked_list_views.xml',
    'views/approve_reservation_views.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}

