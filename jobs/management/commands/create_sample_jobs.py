from django.core.management.base import BaseCommand
from jobs.models import Job
from django.contrib.auth import get_user_model
from datetime import date, timedelta

User = get_user_model()

class Command(BaseCommand):
    help = 'Creates sample jobs for testing'

    def handle(self, *args, **kwargs):
        # Create a superuser if it doesn't exist
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser('admin', 'admin@example.com', 'admin123')

        # Diverse, realistic jobs data
        jobs_data = [
            {
                'title': 'Senior Python Developer',
                'company': 'TechCorp Solutions',
                'description': 'Looking for an experienced Python developer to join our team.',
                'requirements': '5+ years Python, Django, Flask, SQL, AWS, Docker',
                'required_skills': 'python, django, flask, sql, aws, docker',
                'required_experience': '5+ years',
                'required_education': 'bachelor',
                'job_type': 'FULL_TIME',
                'location': 'San Francisco, CA',
                'salary_range': '$120,000 - $150,000',
                'notice_period': '2 months',
                'founders': 'Jane Doe, John Smith',
                'company_size': '201-500',
                'company_website': 'https://techcorp.com',
                'job_summary': 'Lead backend development for scalable SaaS products.',
                'benefits': 'Health, Dental, 401k, Stock Options, Remote Work',
                'work_mode': 'HYBRID',
                'industry': 'Software',
                'linkedin_url': 'https://linkedin.com/company/techcorp',
                'indeed_url': 'https://indeed.com/cmp/techcorp',
                'glassdoor_url': 'https://glassdoor.com/techcorp',
                'company_description': 'TechCorp is a leading SaaS provider for enterprise clients.',
                'job_highlights': 'Flexible hours, modern tech stack, diverse team',
                'application_deadline': date.today() + timedelta(days=30),
            },
            {
                'title': 'Frontend Developer',
                'company': 'WebTech Innovations',
                'description': 'Join our frontend team to build modern web applications.',
                'requirements': '3+ years JavaScript, React, HTML, CSS, TypeScript',
                'required_skills': 'javascript, react, html, css, typescript',
                'required_experience': '3+ years',
                'required_education': 'bachelor',
                'job_type': 'FULL_TIME',
                'location': 'New York, NY',
                'salary_range': '$90,000 - $120,000',
                'notice_period': '1 month',
                'founders': 'Alice Lee',
                'company_size': '51-200',
                'company_website': 'https://webtech.com',
                'job_summary': 'Develop and maintain user interfaces for B2B clients.',
                'benefits': 'Health, Vision, Paid Time Off',
                'work_mode': 'ONSITE',
                'industry': 'Web Development',
                'linkedin_url': 'https://linkedin.com/company/webtech',
                'indeed_url': 'https://indeed.com/cmp/webtech',
                'glassdoor_url': 'https://glassdoor.com/webtech',
                'company_description': 'WebTech builds web solutions for Fortune 500 companies.',
                'job_highlights': 'Modern office, team lunches, career growth',
                'application_deadline': date.today() + timedelta(days=20),
            },
            {
                'title': 'Data Scientist',
                'company': 'DataAnalytics Inc',
                'description': 'Work on cutting-edge machine learning projects.',
                'requirements': '4+ years Python, ML, Data Analysis, SQL, TensorFlow',
                'required_skills': 'python, machine learning, data analysis, sql, tensorflow',
                'required_experience': '4+ years',
                'required_education': 'master',
                'job_type': 'FULL_TIME',
                'location': 'Boston, MA',
                'salary_range': '$130,000 - $160,000',
                'notice_period': '2 months',
                'founders': 'Dr. Emily Carter',
                'company_size': '1001-5000',
                'company_website': 'https://dataanalytics.com',
                'job_summary': 'Analyze large datasets and build predictive models.',
                'benefits': 'Health, Dental, Gym Membership',
                'work_mode': 'REMOTE',
                'industry': 'Data Science',
                'linkedin_url': 'https://linkedin.com/company/dataanalytics',
                'indeed_url': 'https://indeed.com/cmp/dataanalytics',
                'glassdoor_url': 'https://glassdoor.com/dataanalytics',
                'company_description': 'DataAnalytics is a global leader in data-driven solutions.',
                'job_highlights': 'Remote-first, research budget, conference travel',
                'application_deadline': date.today() + timedelta(days=25),
            },
            {
                'title': 'DevOps Engineer',
                'company': 'CloudTech Solutions',
                'description': 'Manage and improve our cloud infrastructure.',
                'required_skills': 'aws, docker, kubernetes, jenkins, linux',
                'required_experience': '3+ years',
                'required_education': 'bachelor',
                'job_type': 'full-time',
                'location': 'Seattle, WA',
                'salary_range': '$110,000 - $140,000'
            },
            {
                'title': 'Full Stack Developer',
                'company': 'StartupX',
                'description': 'Build end-to-end solutions for our growing platform.',
                'required_skills': 'javascript, python, react, django, aws',
                'required_experience': '2+ years',
                'required_education': 'bachelor',
                'job_type': 'full-time',
                'location': 'Austin, TX',
                'salary_range': '$95,000 - $125,000'
            },
            {
                'title': 'Mobile App Developer',
                'company': 'AppWorks',
                'description': 'Create innovative mobile applications.',
                'required_skills': 'swift, kotlin, react native, firebase',
                'required_experience': '3+ years',
                'required_education': 'bachelor',
                'job_type': 'full-time',
                'location': 'Chicago, IL',
                'salary_range': '$100,000 - $130,000'
            },
            {
                'title': 'Backend Developer',
                'company': 'API Solutions',
                'description': 'Design and implement scalable backend services.',
                'required_skills': 'java, spring boot, sql, microservices, aws',
                'required_experience': '4+ years',
                'required_education': 'bachelor',
                'job_type': 'full-time',
                'location': 'Denver, CO',
                'salary_range': '$115,000 - $145,000'
            },
            {
                'title': 'UI/UX Designer',
                'company': 'DesignHub',
                'description': 'Create beautiful and intuitive user interfaces.',
                'required_skills': 'figma, adobe xd, html, css, javascript',
                'required_experience': '3+ years',
                'required_education': 'bachelor',
                'job_type': 'full-time',
                'location': 'Portland, OR',
                'salary_range': '$85,000 - $115,000'
            },
            {
                'title': 'Security Engineer',
                'company': 'SecureTech',
                'description': 'Protect our systems and data from threats.',
                'required_skills': 'security, python, linux, aws, networking',
                'required_experience': '5+ years',
                'required_education': 'bachelor',
                'job_type': 'full-time',
                'location': 'Washington, DC',
                'salary_range': '$130,000 - $160,000'
            },
            {
                'title': 'QA Engineer',
                'company': 'QualityFirst',
                'description': 'Ensure the quality of our software products.',
                'required_skills': 'testing, selenium, python, jenkins, sql',
                'required_experience': '2+ years',
                'required_education': 'bachelor',
                'job_type': 'full-time',
                'location': 'Raleigh, NC',
                'salary_range': '$80,000 - $110,000'
            },
            {
                'title': 'Machine Learning Engineer',
                'company': 'AI Solutions',
                'description': 'Build and deploy machine learning models.',
                'required_skills': 'python, tensorflow, pytorch, aws, docker',
                'required_experience': '4+ years',
                'required_education': 'master',
                'job_type': 'full-time',
                'location': 'San Jose, CA',
                'salary_range': '$140,000 - $170,000'
            },
            {
                'title': 'Cloud Architect',
                'company': 'CloudFirst',
                'description': 'Design and implement cloud solutions.',
                'required_skills': 'aws, azure, gcp, terraform, kubernetes',
                'required_experience': '6+ years',
                'required_education': 'bachelor',
                'job_type': 'full-time',
                'location': 'Dallas, TX',
                'salary_range': '$150,000 - $180,000'
            },
            {
                'title': 'Blockchain Developer',
                'company': 'CryptoTech',
                'description': 'Develop blockchain-based solutions.',
                'required_skills': 'solidity, javascript, web3, ethereum, smart contracts',
                'required_experience': '3+ years',
                'required_education': 'bachelor',
                'job_type': 'full-time',
                'location': 'Miami, FL',
                'salary_range': '$120,000 - $150,000'
            },
            {
                'title': 'Game Developer',
                'company': 'GameWorks',
                'description': 'Create engaging gaming experiences.',
                'required_skills': 'unity, c#, 3d modeling, game design',
                'required_experience': '3+ years',
                'required_education': 'bachelor',
                'job_type': 'full-time',
                'location': 'Los Angeles, CA',
                'salary_range': '$90,000 - $120,000'
            },
            {
                'title': 'Technical Lead',
                'company': 'TechLeaders Inc',
                'description': 'Lead development teams and projects.',
                'required_skills': 'python, java, aws, leadership, agile',
                'required_experience': '7+ years',
                'required_education': 'bachelor',
                'job_type': 'full-time',
                'location': 'Atlanta, GA',
                'salary_range': '$160,000 - $190,000'
            },
            {
                'title': 'Healthcare Data Analyst',
                'company': 'HealthFirst',
                'description': 'Analyze healthcare data to improve patient outcomes.',
                'required_skills': 'sql, python, healthcare analytics',
                'required_experience': '2+ years',
                'required_education': 'bachelor',
                'job_type': 'FULL_TIME',
                'location': 'Houston, TX',
                'salary_range': '$80,000 - $110,000',
                'notice_period': '1 month',
                'founders': 'Dr. Raj Patel',
                'company_size': '501-1000',
                'company_website': 'https://healthfirst.com',
                'job_summary': 'Support clinical teams with actionable data insights.',
                'benefits': 'Health, Dental, Tuition Reimbursement',
                'work_mode': 'HYBRID',
                'industry': 'Healthcare',
                'linkedin_url': 'https://linkedin.com/company/healthfirst',
                'indeed_url': 'https://indeed.com/cmp/healthfirst',
                'glassdoor_url': 'https://glassdoor.com/healthfirst',
                'company_description': 'HealthFirst is a leading healthcare provider in Texas.',
                'job_highlights': 'Work with doctors, impact lives, flexible schedule',
                'application_deadline': date.today() + timedelta(days=18),
            },
            {
                'title': 'Investment Banking Analyst',
                'company': 'FinServe Bank',
                'description': 'Support M&A and capital raising transactions.',
                'required_skills': 'excel, financial modeling, powerpoint',
                'required_experience': '1+ years',
                'required_education': 'bachelor',
                'job_type': 'FULL_TIME',
                'location': 'New York, NY',
                'salary_range': '$100,000 - $130,000',
                'notice_period': '3 months',
                'founders': 'Michael Lee',
                'company_size': '10001+',
                'company_website': 'https://finserve.com',
                'job_summary': 'Work on high-profile deals with senior bankers.',
                'benefits': 'Health, Dental, Bonus, Relocation',
                'work_mode': 'ONSITE',
                'industry': 'Finance',
                'linkedin_url': 'https://linkedin.com/company/finserve',
                'indeed_url': 'https://indeed.com/cmp/finserve',
                'glassdoor_url': 'https://glassdoor.com/finserve',
                'company_description': 'FinServe is a top global investment bank.',
                'job_highlights': 'Deal exposure, mentorship, fast-paced',
                'application_deadline': date.today() + timedelta(days=15),
            },
        ]

        # Remove all existing jobs to avoid duplicates
        Job.objects.all().delete()

        # Create jobs
        for job_data in jobs_data:
            Job.objects.create(**job_data)

        self.stdout.write(self.style.SUCCESS(f'Successfully created {len(jobs_data)} sample jobs with rich details')) 