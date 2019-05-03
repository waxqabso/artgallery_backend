# Aleel Art Gallery (Back-End)

# Models (Draft)

## Artist

* artist_id (int)
* name (text)
* biography (text)
* profile_picture_path (text)
* address (text)
* phone number (text)
* twitter (text)
* instagram (text)
* facebook (text)
* gender (boolean)
* rating (calculated?)
* email_address (text)
* password (text)

## Art

* art_id  (int)
* description
  - name
* image_path
* artist_id
* rating
* availability
  * available_now
  * available_later
  * not_available
* timeframe_for_order (TEXT)
* price


# Creating db

`sudo -i -u postgrs psql`

```
CREATE DATABASE aleeldb;
CREATE USER aleeluser WITH PASSWORD '123';
ALTER ROLE aleeluser SET client_encoding TO 'utf8';
ALTER ROLE aleeluser SET default_transaction_isolation TO 'read committed';
ALTER ROLE aleeluser SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE aleeldb TO aleeluser;
\q
```

# Dev settings

```
from .settings import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'aleeldb',
        'USER': 'aleeluser',
        'PASSWORD': '123',
        'HOST': 'localhost',
        'PORT': '',
    }
}

DEVELOPMENT_APPS = ()

INSTALLED_APPS = EXTERNAL_APPS + INTERNAL_APPS + DEVELOPMENT_APPS

```
