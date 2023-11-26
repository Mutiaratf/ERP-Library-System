{
    "name": "Library System (LS)",
    "version": "16.0.1.0.0",
    "author": "Mutiara Tari Fadilah",
    "category": "Extra Tools",
    "license": "LGPL-3",
    "depends": ["contacts"],
    "data": [
        'security/ir.model.access.csv',
        'security/access_group.xml',
        'security/security.xml',
        'views/admin/book_admin.xml',
        'views/admin/member_admin.xml',
        'views/admin/author_admin.xml',
        'views/admin/publisher_admin.xml',
        'views/admin/pinjam_admin.xml',
        'views/admin/pengembalian_admin.xml',
        'views/menu.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
    'icon': 'library_system,static/description/icon.png'
}
