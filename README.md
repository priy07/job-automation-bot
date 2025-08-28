# Job Automation Bot 🤖

A Python-based bot that helps users generate customized resumes and prepare for job interviews.

## 🚀 Features
- Generate tailored resumes for different job roles (Cybersecurity, Fullstack, IT Support, etc.)
- Aptitude test practice
- Interview preparation resources
- Custom resume builder
- Automated job-related tasks

## 🛠️ Tech Stack
- **Python 3**
- **Flask** (for web framework, if applicable)
- **OpenAI API** (if used)
- Other libraries listed in `requirements.txt`

## 📂 Project Structure
```
JOB-AUTOMATION-BOT/
│── aptitude_tests/          # Aptitude practice material
│── customized_resumes/      # Templates for resumes
│── interview_prep/          # Interview resources
│── job_bot_env/             # Local Python environment (ignored in git)
│── resumes/                 # Generated resumes (ignored in git)
│── config.json              # Config file (ignored in git)
│── main.py                  # Main script
│── setup.py                 # Setup script
│── start.py                 # Entry point
│── requirements.txt         # Dependencies
│── README.md                # Project documentation
│── .gitignore               # Ignore rules
```

## ⚡ Getting Started

1. Clone the repository:
   ```bash
   git clone https://github.com/priy07/Job-Automation-Bot.git
   cd Job-Automation-Bot
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate   # Mac/Linux
   venv\Scripts\activate      # Windows
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the bot:
   ```bash
   python start.py
   ```

## 📜 License
This project is for educational purposes. Add a license (MIT, Apache, etc.) if you plan to share it publicly.
