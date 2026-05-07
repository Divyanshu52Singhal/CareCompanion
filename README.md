# CareCompanion

## Possible Features
- Improve AI doctor-finder: better symptom parsing, confidence scores, and intent classification.
- User accounts & medical records: register/login, save past consultations and BMI history.
- Appointment booking: search providers, request appointments, integrate calendar reminders.
- Medication & pill reminders with notifications (email/SMS/push).
- Teleconsultation: in-app chat/voice/video with doctors.
- Multi-language support and accessibility improvements.
- Integration with EHR/HL7/FHIR and provider directories.
- Dockerize and add CI/CD, tests, and rate limiting for production.

## Project Overview

CareCompanion is a small Flask-based healthcare helper app that provides:

- An AI-powered doctor finder (symptom -> suggested department) using Google Generative AI.
- A simple BMI calculator.
- A responsive frontend using the templates in `templates/` and static assets in `static/`.

Key routes:
- `/` - Home page (templates/index.html)
- `/chat` - Symptom input and AI doctor-finder (templates/chat.html)
- `/bmi` - BMI calculator (templates/bmi.html)

Main server file: `app.py`

## Tech Stack
- Python 3.x
- Flask
- Google Generative AI (`google-generativeai`)
- Frontend: Bootstrap and custom CSS/JS in `static/`

## Requirements
Install Python dependencies from `requirements.txt`:

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

## Environment
Create a `.env` file in the project root with your Google/Generative AI API key:

```
API=your_api_key_here
```

The app loads this variable and configures `google.generativeai` in `app.py`.

## Run (development)

```bash
python app.py
# then open http://127.0.0.1:5000/
```

## Run (production)
You can run with `gunicorn` (installed via `requirements.txt`):

```bash
gunicorn -w 4 -b 0.0.0.0:8000 app:app
```

## Notes & Next Steps
- The AI model is configured in `app.py` and expects an environment variable named `API`.
- `requirements.txt` includes `psycopg2` and `gunicorn` — consider adding a database backend (Postgres) for records.
- Consider adding tests, linting, and a `Dockerfile` for reproducible deployments.