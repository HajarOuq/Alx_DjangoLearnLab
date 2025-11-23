# Security Notes for LibraryProject

## Overview
This file documents security settings and practices applied to the Django project.

## settings.py
- `DEBUG = False` in production.
- `SECRET_KEY` should be set via environment variable `DJANGO_SECRET_KEY`.
- `ALLOWED_HOSTS` must be set to production host(s).
- `SESSION_COOKIE_SECURE = True` and `CSRF_COOKIE_SECURE = True` ensure cookies are sent only over HTTPS.
- `X_FRAME_OPTIONS = "DENY"`, `SECURE_CONTENT_TYPE_NOSNIFF` and `SECURE_BROWSER_XSS_FILTER` are enabled.

## CSRF protection
- All POST forms include `{% csrf_token %}` (see `form_example.html`).
- `django.middleware.csrf.CsrfViewMiddleware` is enabled (default).

## Input validation & SQL injection
- Use Django forms (`forms.py`) to validate input.
- Use the ORM for queries — avoid string formatting in queries.

## Content Security Policy
- CSP header is set using `django-csp` (recommended) or a custom middleware in `LibraryProject/middleware.py`.
- Test CSP thoroughly to ensure external scripts/styles are whitelisted if needed.

## Testing
1. Run server locally for functional checks:
   ```bash
   python manage.py runserver

---

## 8) Manual test checklist (quick)

1. `python manage.py makemigrations` and `python manage.py migrate`
2. `python manage.py createsuperuser` — create admin
3. `python manage.py runserver` (local dev; in dev you may temporarily set `DEBUG=True` and `SESSION_COOKIE_SECURE=False` so cookies work without HTTPS)
4. Login to `/admin/` and create groups/assign permissions (Viewers/Editors/Admins) as discussed previously.
5. Create user accounts, assign to groups, and test the `create_book`, `edit_book`, and `book_list` views:
   - User without `can_create` should receive 403 when attempting to access create view.
   - POST forms without CSRF token should be rejected (test with curl or by removing token in template).
6. Test search: try to inject SQL-like strings — ORM will treat them as strings (not SQL), so no injection.

---

## Quick notes about development vs production

- In **development** on `runserver` you often do not have HTTPS. To allow testing locally:
  - Temporarily set `DEBUG = True` and `SESSION_COOKIE_SECURE = False`, `CSRF_COOKIE_SECURE = False`.
  - **Never commit** these changes; use environment-specific settings or `.env` file with `django-environ` or split settings modules.

- In **production**:
  - `DEBUG = False`
  - All `SECURE_*` settings enabled as above and serve over HTTPS.

---

If you want, I can now:

- produce the exact `settings.py` file with your current `BASE_DIR`, `INSTALLED_APPS`, and other project specifics filled in, OR
- create the `middleware.py` file and `README_SECURITY.md` in your project and print exactly what to paste, OR
- generate test commands and example curl requests to verify CSRF and CSP enforcement.

Which of those would you like me to produce right now?
