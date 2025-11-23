# Permissions Setup

## Custom Permissions
Defined in `Book` model (bookshelf/models.py):

- can_view
- can_create
- can_edit
- can_delete

## Groups
Created via Django Admin:

- Viewers → can_view
- Editors → can_view, can_create, can_edit
- Admins → all permissions

## Views
Permissions enforced using @permission_required in views.py:

- book_list → can_view
- create_book → can_create
- edit_book → can_edit
- delete_book → can_delete
