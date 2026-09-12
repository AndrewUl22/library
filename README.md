# Library — Odoo training module

## What's inside
- `library.book` — books (title, author, ISBN, availability — a computed field)
- `library.member` — members
- `library.loan` — loans (book ↔ member, status ongoing/returned)
- A constraint: a book can't be lent out if it's already on loan to another member
- Access rights for the `base.group_user` group (regular internal user)

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

## What to do next (plan, days 1-7)
This code is already a working scaffold, a bit past Day 1 on purpose,
so there's something to practice on. Suggested next steps:
- **Day 1-2**: go through every line of `library_book.py`, remove it all,
  and rewrite it from scratch by hand instead of copying — it sticks better that way.
- **Day 3**: try adding a kanban view for books on your own.
- **Day 4**: extend security — make a regular member see only their own
  loans (record rule), while a librarian sees all of them.
- **Day 5**: add another computed field — e.g. whether a loan
  is overdue (`is_overdue`), based on `due_date`.
- **Day 6**: switch `library.member` to `_inherits` from `res.partner`
  instead of its own name/email/phone fields — a common pattern in real Odoo.
- **Day 10**: add a "Lend a book" wizard instead of creating `library.loan` directly.

## Known simplifications (left in on purpose, as room for improvement)
- No loan-period limit (`due_date` isn't filled in automatically)
- No automatic overdue notifications
- No tests yet — write your own (see Day 12 of the plan)
