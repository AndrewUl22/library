{
    'name': 'Library',
    'version': '1.0',
    'summary': 'Training module: library book management',
    'description': """
Training module for practicing the Odoo framework.
Includes:
- library.book (books)
- library.member (members)
- library.loan (book loans)
- Two security groups (User / Librarian) with record rules,
  so a regular member only sees their own loans
""",
    'category': 'Tools',
    'author': 'Andrew',
    'depends': ['base', 'mail'],
    'data': [
        'security/library_security.xml',
        'security/ir.model.access.csv',
        'views/library_book_views.xml',
        'views/library_member_views.xml',
        'views/library_loan_views.xml',
        'views/library_menus.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
