# ResumeMatcher

AI-Powered Resume Analyzer & Job Matcher

---

## 🚀 Project Overview
ResumeMatcher is a Django-based web application that leverages Natural Language Processing (NLP) to analyze resumes and intelligently match them to a rich set of job postings. It provides:
- Automated resume parsing (skills, experience, education)
- Smart job matching with detailed scoring
- A modern, user-friendly dashboard for job seekers
- Admin tools for managing job listings

This project is ideal for:
- Job seekers wanting to optimize their job search
- Recruiters and HR teams
- Developers learning Django, NLP, and job-matching logic

---

## ✨ Features
- **Resume Upload:** Upload PDF, DOC, or DOCX resumes
- **NLP Resume Parsing:** Extracts skills, experience, and education using spaCy
- **Review & Edit:** Users can review and edit extracted data before saving
- **Job Matching:** Matches resumes to 35+ realistic jobs using a weighted algorithm
- **Detailed Match Scores:** See breakdowns for skills, experience, and education
- **Job Board:** Browse rich job postings with company info, benefits, founders, and more
- **Admin Tools:** Add/edit/delete jobs, manage users
- **Responsive UI:** Built with Bootstrap 5 for a modern look
- **Security:** User authentication, file validation, and access control

---

## 🛠️ Tech Stack
- **Backend:** Django 5.x (Python 3.12+)
- **Frontend:** Bootstrap 5, HTML5, CSS3
- **NLP:** spaCy (`en_core_web_sm` model)
- **Database:** SQLite (default, easy to swap for Postgres/MySQL)
- **Other:** PyPDF2, python-docx, scikit-learn, pandas, numpy, crispy-forms

---

## 🏗️ Architecture & Key Components
- `core/` – User authentication, dashboard, profile
- `resumes/` – Resume upload, parsing, review, and management
- `jobs/` – Job model, CRUD, and management commands for sample data
- `matching/` – Job matching logic and match detail views
- `templates/` – All HTML templates (Bootstrap 5)
- `static/` – Static files (CSS, JS, images)
- `media/` – Uploaded resumes

### Data Flow
1. **User uploads resume** →
2. **spaCy parses text** →
3. **Extracted data shown for review/edit** →
4. **Resume saved** →
5. **Matching algorithm runs** →
6. **User sees matches and scores**

---

## 🖥️ Local Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/Yash-Shindey/ResumeMatcher.git
cd ResumeMatcher
```

### 2. Create and activate a virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Download spaCy model (required for resume parsing)
```bash
python -m spacy download en_core_web_sm
```

### 5. Run migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Create a superuser (for admin access)
```bash
python manage.py createsuperuser
```

### 7. (Optional) Populate sample jobs
```bash
python manage.py create_sample_jobs
```

### 8. Start the development server
```bash
python manage.py runserver
```

Visit [http://127.0.0.1:8000/](http://127.0.0.1:8000/) in your browser.

---

## 📝 Usage Guide

### For Job Seekers
1. **Register/Login**
2. **Upload Resume:** Go to "My Resumes" → Upload Resume
3. **Review/Edit:** Check and edit extracted skills, experience, education
4. **Save:** Resume is saved and matched to jobs
5. **View Matches:** See job matches, scores, and details
6. **Browse Jobs:** Explore all job postings, view company info, and apply

### For Admins
- Access `/admin/` for full Django admin
- Add/edit/delete jobs via the web UI or admin
- Use `python manage.py create_sample_jobs` to seed rich job data

---

## 🔍 Matching Algorithm
- **Skills (50%):** Overlap between resume and job required skills
- **Experience (30%):** Years of experience vs. job requirement
- **Education (20%):** Education level vs. job requirement
- **Weighted Score:** Final match score is a weighted sum
- **Details:** Matching skills, experience, and education are shown for transparency

---

## 🧩 Customization
- **Add More Jobs:** Edit `jobs/management/commands/create_sample_jobs.py`
- **Change Matching Logic:** Edit `resumes/views.py` → `create_job_matches()`
- **Add More Resume Fields:** Update `resumes/models.py` and forms/templates
- **Switch Database:** Update `DATABASES` in `resume_analyzer/settings.py`
- **Styling:** Edit templates in `templates/` and static files in `static/`

---

## 🛡️ Security & Best Practices
- Uploaded files are validated for type and size
- User data is protected by Django's authentication system
- Admin-only actions are protected by permissions
- `.env` and sensitive files are gitignored

---

## 🐞 Troubleshooting
- **spaCy model not found:** Run `python -m spacy download en_core_web_sm`
- **File upload errors:** Check file type/size and permissions on `media/`
- **Migrations:** If you change models, run `makemigrations` and `migrate`
- **Static files not loading:** Use `python manage.py collectstatic` for production

---

## 🤝 Contributing
Pull requests are welcome! For major changes, please open an issue first to discuss what you'd like to change.

---

## 📄 License
MIT

---

**Made with ❤️ by [Yash-Shindey](https://github.com/Yash-Shindey)** 