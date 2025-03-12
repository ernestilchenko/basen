# Basen Project Guide

## Commands
- Run server: `python manage.py runserver`
- Create migrations: `python manage.py makemigrations`
- Apply migrations: `python manage.py migrate`
- Run all tests: `python manage.py test`
- Run specific test: `python manage.py test basen_app.tests.TestClassName.test_method_name`
- Check for problems: `python manage.py check`
- Create translations: `python manage.py makemessages -l [locale]`
- Compile translations: `python manage.py compilemessages`

## Code Style
- **Formatting**: PEP 8 standard with 4-space indentation
- **Imports**: Group by Django, third-party, local (each sorted alphabetically)
- **Naming**: 
  - Classes: CamelCase (e.g., `ContactForm`)
  - Variables/functions: snake_case (e.g., `email_message`)
- **Error Handling**: Use specific exception handlers in try/except blocks
- **Templates**: Follow Django template patterns with block inheritance
- **Internationalization**: Mark user-facing strings with gettext (`_()`)

## Project Structure
- Django 5.1.3 multilingual website about pools
- Languages: Polish, English, French, German
- Custom templates with form handling for contact functionality