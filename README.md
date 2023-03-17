# Boilerplate

### Setup
 1. Initialize virtual env: `make venv`
 2. Activate it with: `. env/bin/activate`
 3. Install dependencies: `make install`

### Notes
- Run application: `make run`
- Run unit tests (whole codebase): `make test`
<!-- - Run unit tests (specifc directory/file):`FLASK_ENV=test pytest app/app.py` -->
- Make code pretty: `make format`
- Lint code: `make lint`

### Postgres setup:
1. `brew install postgresql`
2. `brew services start postgresql`
3. Create db user `test_user` with password `test_user`: `createuser -sP test_user`
4. Create unit test db: `createdb -O test_user test_test`
5. Create development db: `createdb -O test_user test_dev`
<!-- 6. `./seed.py --rebuild-db` -->
