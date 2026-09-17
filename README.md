# Library — Odoo training module

## What's inside
- `library.book` — books (title, author, ISBN, availability — a computed field), with a kanban view alongside list/form
- `library.member` — members, delegated from `res.partner` via `_inherits`
  (same pattern `res.users` uses), optionally linked to a login account (`user_id`)
- `library.loan` — loans (book ↔ member, status ongoing/returned, `is_overdue` computed field)
- A "Lend a Book" wizard (`library.loan.wizard`) for creating loans through a small dialog
  instead of a raw `library.loan` form
- A constraint: a book can't be lent out if it's already on loan to another member
- Two security groups — **User** and **Librarian** — with record rules:
  a regular member only sees loans linked to their own account,
  a librarian sees every loan
- Unit tests (`tests/test_library.py`) covering the constraint, availability,
  `is_overdue`, the wizard, and the record rule that restricts a member to
  their own loans

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

## Running the tests
```bash
./odoo-bin -d mydb --addons-path=addons,odoo/addons -i library --test-enable --stop-after-init
```

## Known simplifications
- No loan-period limit (`due_date` isn't filled in automatically)
- No automatic overdue notifications
