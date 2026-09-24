# Library — Odoo training module

![Tests](https://github.com/AndrewUl22/library/actions/workflows/tests.yml/badge.svg)

## What's inside
- `library.book` — books (title, author, ISBN, availability — a computed field), with a kanban view alongside list/form
- `library.member` — members, delegated from `res.partner` via `_inherits`
  (same pattern `res.users` uses), optionally linked to a login account (`user_id`)
- `library.loan` — loans (book ↔ member, status ongoing/returned, `is_overdue` computed field)
- A "Lend a Book" wizard (`library.loan.wizard`) for creating loans through a small dialog
  instead of a raw `library.loan` form
- A PDF "Reading Card" report per member, listing their current loans
- A constraint: a book can't be lent out if it's already on loan to another member
- Two security groups — **User** and **Librarian** — with record rules:
  a regular member only sees loans linked to their own account,
  a librarian sees every loan
- Demo data (5 books, 3 members, 3 loans — one ongoing, one overdue, one returned)
- Unit tests (`tests/test_library.py`) covering the constraint, availability,
  `is_overdue`, the wizard, and the record rule that restricts a member to
  their own loans
- A GitHub Actions workflow that runs the test suite on every push

## Installation
1. Copy the `library` folder into `addons/` in your Odoo clone:
   ```bash
   cp -r library /path/to/odoo/addons/
   ```
2. Run Odoo with this addons-path and the install flag (Odoo 19 requires
   `--with-demo` explicitly, unlike earlier versions):
   ```bash
   ./odoo-bin -d mydb --addons-path=addons,odoo/addons -i library --with-demo --dev=all
   ```
3. Open `http://localhost:8069` — "Library" will appear in the top menu, already
   populated with sample books, members, and loans.
4. From a member's form, use **Print → Reading Card** to generate their PDF.

## Running the tests
```bash
./odoo-bin -d mydb --addons-path=addons,odoo/addons -i library --test-enable --test-tags /library --stop-after-init
```

## Screenshots

<!-- TODO: add screenshots once the module is running, e.g.:
![Books kanban](screenshots/books-kanban.png)
![Lend a Book wizard](screenshots/lend-a-book.png)
![Reading Card PDF](screenshots/reading-card.png)
-->

## Known simplifications
- No loan-period limit (`due_date` isn't filled in automatically)
- No automatic overdue notifications
