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
