{
    'name': 'Arista Resource Master Module',
    'version': '14.0.2.3.0',
    'license': 'OPL-1',
    'summary': "Add several Master Data for Arista",
    'category': 'base',
    'author': "Jodhi",
    'website': "https://www.arista-group.co.id",
    'support': 'app.support@arista-group.co.id',
    'description': '''
        Added:
            1. Area
    ''',
    'depends': [
        'base'
    ],
    'data': [
        'views/res_area_views.xml',
        'views/res_company_views.xml',
        'security/ir.model.access.csv'
    ],
    'images': [
        # 'static/description/indonesian_tax_screenshot.png'
    ],
    'demo': [
    ],
    'application': False,
}
