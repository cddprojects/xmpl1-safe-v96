# Nimbly Quest

Independent information site about work in Poland: part-time employment, remote work, civil contracts and sole proprietorship. It explains the terms. It does not list vacancies or recruit.

## Structure

- Static site served from the project root. Each page is a folder with its own `index.html` (clean URLs), e.g. `about/`, `services/`, `privacy-policy/`.
- `index.html`: homepage, served at `/`.
- `assets/`: shared static files (`assets/css/`, `assets/img/`, `assets/js/`).
- `tools/`: Python scripts used to generate the HTML pages.

## Local preview

The site uses root-relative paths (`/assets/...`) and folder URLs (`/about/`), so preview it through a web server rather than opening files directly:

```bash
python -m http.server 8099
```

Then open http://localhost:8099/ in your browser.
