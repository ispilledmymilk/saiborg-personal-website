# Sai Pranavi Kasturi · Portfolio

A personal portfolio site built with Flask and Jinja2 for the MLH Production Engineering Fellowship (Week 1). It includes an about page, work experience, education, hobbies, projects, and an interactive travel map.

**Live site:** https://ispilledmymilk.github.io/saiborg-personal-website/

## Features

- Profile photo and about section on the home page
- Work experience and education rendered with Jinja templates
- Dedicated hobbies page with images and Spotify link
- Projects page with tech tags and highlights
- Travel map powered by Leaflet and OpenStreetMap
- Dynamic navigation bar driven by `PAGES` in `app/data.py`
- Deployed to GitHub Pages via GitHub Actions

## Project structure

```
saiborg-personal-website/
├── app/
│   ├── __init__.py          # Flask routes
│   ├── data.py              # Portfolio content (edit this!)
│   ├── templates/           # Jinja HTML templates
│   └── static/              # CSS, images, and assets
├── .github/workflows/       # GitHub Pages deploy workflow
├── freeze.py                # Static site generator for GitHub Pages
├── requirements.txt
├── example.env
└── README.md
```

## Run locally

### Prerequisites

- Python 3.12+ ([download](https://www.python.org/downloads/))
- `pip`

Check your version:

```bash
python3 --version
```

### 1. Clone the repository

```bash
git clone https://github.com/ispilledmymilk/saiborg-personal-website.git
cd saiborg-personal-website
```

### 2. Create and activate a virtual environment

```bash
python3 -m venv python3-virtualenv
source python3-virtualenv/bin/activate
```

On Windows:

```bash
python3 -m venv python3-virtualenv
python3-virtualenv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Set up environment variables

```bash
cp example.env .env
```

The `.env` file sets `URL` for Open Graph meta tags. For local development, the default is fine:

```
URL=localhost:5001
```

### 5. Start the Flask server

```bash
export FLASK_APP=app
export FLASK_ENV=development
flask run --port 5001
```

> **macOS note:** Port 5000 is often used by AirPlay Receiver. Use `--port 5001` to avoid conflicts.

You should see:

```
 * Running on http://127.0.0.1:5001
```

Open **http://127.0.0.1:5001** in your browser.

### 6. Stop the server

Press `Ctrl + C` in the terminal.

## Customize your content

Most site content lives in [`app/data.py`](app/data.py):

| Variable | What it controls |
|---|---|
| `PROFILE` | Name, email, links, photo path |
| `ABOUT` | About Me text |
| `EXPERIENCES` | Work history |
| `EDUCATION` | School info |
| `HOBBIES` | Hobbies page entries |
| `PROJECTS` | Projects page entries |
| `TRAVEL_LOCATIONS` | Map markers |
| `PAGES` | Navigation menu items |

After editing, refresh the browser. Restart Flask if changes don't appear.

## Pages

| Route | Description |
|---|---|
| `/` | Home — photo, about, experience, education |
| `/hobbies/` | Hobbies with images |
| `/projects/` | Project portfolio |
| `/travel/` | Interactive travel map |

## Deployment

The site deploys automatically to GitHub Pages when changes are pushed to `main`. The workflow builds a static version of the site using [Frozen-Flask](https://pythonhosted.org/Frozen-Flask/) and publishes it via GitHub Actions.

To deploy manually, push to `main`:

```bash
git push origin main
```

Check deploy status under the **Actions** tab on GitHub.

## Tech stack

- [Flask](https://flask.palletsprojects.com/) — web framework
- [Jinja2](https://jinja.palletsprojects.com/) — templating
- [Leaflet](https://leafletjs.com/) — travel map
- [GitHub Pages](https://pages.github.com/) — hosting
- [Frozen-Flask](https://pythonhosted.org/Frozen-Flask/) — static export for deployment

## License

MIT
