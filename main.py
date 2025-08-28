
import os
import time
import random
import requests
from bs4 import BeautifulSoup
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


# Suppress TensorFlow/other noisy logs
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"


# ---------- Helper ----------
def ask_openai(prompt: str, model="gpt-4o-mini"):
    """Send a prompt to OpenAI and return response text."""
    try:
        response = client.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": prompt}],
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        print(f"⚠️ Error generating response: {e}")
        return ""


# ---------- Resume Manager ----------
class ResumeManager:
    def __init__(self, template: str = ""):
        self.template = template or "Generic Resume Template"

    def customize_resume(self, job_description: str) -> str:
        prompt = f"""
        Given this job description:
        {job_description}

        Tailor the following resume template:
        {self.template}

        Focus on matching key skills, experiences, and achievements.
        """
        return ask_openai(prompt)


# ---------- Job Scraper ----------
class JobScraper:
    def __init__(self):
        self.base_urls = [
            "https://remoteok.com",
            "https://weworkremotely.com",
            "https://www.indeed.com",
        ]

    def scrape_jobs(self, keyword: str = "software engineer") -> list:
        jobs = []
        for url in self.base_urls:
            try:
                response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
                soup = BeautifulSoup(response.text, "html.parser")
                titles = [t.get_text(strip=True) for t in soup.find_all("h2")[:5]]
                for t in titles:
                    jobs.append({"title": t, "company": url.split("//")[1], "url": url})
            except Exception as e:
                print(f"⚠️ Error scraping {url}: {e}")
        return jobs

    def extract_requirements(self, description: str) -> list:
        prompt = f"""
        Extract the key technical requirements and skills from this job description:

        {description[:1000]}

        Return only a comma-separated list of skills and requirements.
        """
        requirements_text = ask_openai(prompt)
        return [r.strip() for r in requirements_text.split(",") if r.strip()]


# ---------- Interview Prep ----------
class InterviewCrackerAI:
    def generate_interview_questions(self, job_title: str, company: str, experience_level: str = "mid") -> list:
        prompt = f"""
        Generate 10 interview questions for a {job_title} position at {company}.
        Experience level: {experience_level}

        Include:
        - Technical questions
        - Behavioral questions
        - Company-specific questions
        - Situational questions

        Return only the questions, one per line.
        """
        questions_text = ask_openai(prompt)
        return [q.strip() for q in questions_text.split("\n") if q.strip()]

    def generate_aptitude_test(self, num_questions: int = 5) -> list:
        prompt = f"""
        Generate {num_questions} multiple-choice aptitude test questions.
        Each should have 4 options (A-D) and specify the correct answer.

        Format:
        Q: <question>
        A. ...
        B. ...
        C. ...
        D. ...
        Answer: <correct option>
        """
        return ask_openai(prompt)

    def provide_interview_tips(self, job_title: str) -> str:
        prompt = f"""
        Give me 5 specific interview preparation tips for a {job_title} role.
        Format as a numbered list.
        """
        return ask_openai(prompt)


# ---------- History ----------
class ApplicationHistory:
    def __init__(self):
        self.history = []

    def add_entry(self, job, status="Applied"):
        self.history.append({"job": job, "status": status, "timestamp": time.ctime()})

    def show_history(self):
        if not self.history:
            print("📂 No application history yet.")
        for entry in self.history:
            print(f"- {entry['job']['title']} at {entry['job']['company']} | {entry['status']} | {entry['timestamp']}")


# ---------- Main Bot ----------
def main():
    print("🤖 Job Automation Bot - InterviewCracker.AI")
    print("=" * 50)
    print("Created for Priyanshi Dwivedi")
    print("=" * 50)

    scraper = JobScraper()
    resume_manager = ResumeManager("My Resume Template")
    interview_ai = InterviewCrackerAI()
    history = ApplicationHistory()

    while True:
        print("\nOptions:")
        print("1. Run job search cycle")
        print("2. Start automatic scheduler")
        print("3. Prepare for interview")
        print("4. Take aptitude test")
        print("5. View application history")
        print("6. Exit")

        choice = input("\nEnter your choice (1-6): ").strip()

        if choice == "1":
            jobs = scraper.scrape_jobs("python developer")
            if not jobs:
                print("⚠️ No jobs found.")
                continue
            for i, job in enumerate(jobs, 1):
                print(f"{i}. {job['title']} at {job['company']} ({job['url']})")
            pick = input("Pick a job number to customize resume (or press Enter to skip): ")
            if pick.isdigit() and 1 <= int(pick) <= len(jobs):
                selected = jobs[int(pick) - 1]
                resume = resume_manager.customize_resume(selected["title"])
                print("\n📄 Customized Resume:\n")
                print(resume)
                history.add_entry(selected)

        elif choice == "2":
            print("⚙️ Automatic scheduler coming soon...")

        elif choice == "3":
            role = input("Enter job title: ")
            company = input("Enter company: ")
            questions = interview_ai.generate_interview_questions(role, company)
            print("\n📋 Practice Interview Questions:\n")
            for q in questions:
                print("-", q)
            tips = interview_ai.provide_interview_tips(role)
            print("\n💡 Interview Tips:\n", tips)

        elif choice == "4":
            test = interview_ai.generate_aptitude_test()
            print("\n📝 Aptitude Test:\n", test)

        elif choice == "5":
            history.show_history()

        elif choice == "6":
            print("👋 Exiting...")
            break
        else:
            print("⚠️ Invalid choice. Try again.")


if __name__ == "__main__":
    main()
