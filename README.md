# AI-Powered Resume Analyzer & Job Matcher

A Django-based application that analyzes resumes and matches them with job listings using AI.

## Features

- Resume upload and parsing (PDF, DOC, DOCX)
- Job listing management
- AI-powered resume analysis
- Job matching algorithm
- Admin dashboard with insights
- User authentication

## Setup Instructions

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Download spaCy model:
```bash
python -m spacy download en_core_web_sm
```

4. Set up environment variables:
Create a `.env` file in the project root with:
```
SUPABASE_URL=your_supabase_url
SUPABASE_KEY=your_supabase_key
```

5. Run migrations:
```bash
python manage.py migrate
```

6. Create superuser:
```bash
python manage.py createsuperuser
```

7. Run the development server:
```bash
python manage.py runserver
```

## Project Structure

- `resume_analyzer/` - Main Django project
- `core/` - Core application
- `resumes/` - Resume handling app
- `jobs/` - Job listing app
- `matching/` - Job matching algorithm
- `templates/` - HTML templates
- `static/` - Static files (CSS, JS)

## Technologies Used

- Django
- Supabase
- spaCy for NLP
- scikit-learn for matching algorithm
- Bootstrap 5 for frontend 