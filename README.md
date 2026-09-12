# Library — Odoo training module

## What's inside
- `library.book` — books (title, author, ISBN, availability — a computed field)
- `library.member` — members, optionally linked to a login account (`user_id`)
- `library.loan` — loans (book ↔ member, status ongoing/returned, `is_overdue` computed field)
- A constraint: a book can't be lent out if it's already on loan to another member
- Two security groups — **User** and **Librarian** — with record rules:
  a regular member only sees loans linked to their own account,
  a librarian sees every loan

## Installation
1. Copy the `library` folder into `addons/` in your Odoo clone:
   ```bash
   cp -r library /path/to/odoo/addons/
   ```
2. Run Odoo with this addons-path and the install flag:
   ```bash
   ./odoo-bin -d mydb --addons-path=addons,odoo/addons -i library --dev=all
   ```
3. Open `http://localhost:8069` — "Library" will appear in the top menu.

## Roadmap

Ideas for extending the module further:

- Add a kanban view for books
- Switch `library.member` to `_inherits` from `res.partner` instead of its own name/email/phone fields
- Add a "Lend a book" wizard instead of creating `library.loan` records directly
- Add unit tests

## Known simplifications
- No loan-period limit (`due_date` isn't filled in automatically)
- No automatic overdue notifications
- No tests yet
