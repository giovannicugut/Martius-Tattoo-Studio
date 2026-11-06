# Martius Tattoo Studio — sito web

Sito statico (HTML + CSS + JS), nessun server necessario: apri `index.html` nel browser
oppure carica la cartella su qualsiasi hosting (Netlify, Aruba, GitHub Pages, ecc.).

## Pagine (menu)
Home · Artisti · Cover-up e Restauro · Piercing e Gioielli · Flash settimanali da 50€ ·
Eventi Flash e Piercing da 20€ · Cura post-tatuaggio · Contatti

## Da completare (segnaposto)
Tutti i dati si cambiano in un solo punto, in cima a `build.py`:
- `ADDRESS_1`, `MAP_QUERY` — via e numero civico reali (la mappa si aggiorna da sola)
- `EMAIL`, `FACEBOOK`, `TIKTOK`
- `ARTISTS` — stili, biografie e foto (nomi, Instagram, telefono e orari sono già quelli veri)
- `GALLERY` / `IMG_*` / `IMG_AC_*` — le foto sono in `img/`; per aggiungerne altre mettile lì e scrivi
  `"img/nomefile.jpg"` al posto del codice Unsplash

Poi rigenera le pagine:

    python3 build.py

## Note
- Il modulo prenotazione apre l'email del cliente già compilata verso `EMAIL`.
- Foto: Unsplash (licenza gratuita). Font: Bebas Neue + Montserrat (Google Fonts).
