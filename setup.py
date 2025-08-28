#!/usr/bin/env python3
"""
Job Automation Bot - Setup Script
Automated setup for Priyanshi's Job Application System
"""

import os
import json
import subprocess
import sys
from pathlib import Path

def check_python_version():
    """Check if Python version is compatible"""
    if sys.version_info < (3, 8):
        print("❌ Python 3.8+ required. Current version:", sys.version)
        return False
    print("✅ Python version:", sys.version.split()[0])
    return True

def create_directories():
    """Create necessary directories"""
    directories = [
        'resumes',
        'applications',
        'logs',
        'customized_resumes',
        'interview_prep',
        'aptitude_tests'
    ]
    
    for directory in directories:
        Path(directory).mkdir(exist_ok=True)
        print(f"✅ Created directory: {directory}")

def create_requirements_file():
    """Create requirements.txt file"""
    requirements = """
selenium==4.15.0
requests==2.31.0
openai==0.28.1
schedule==1.2.0
beautifulsoup4==4.12.2
pandas==2.1.0
python-dotenv==1.0.0
webdriver-manager==4.0.1
lxml==4.9.3
python-dateutil==2.8.2
pytz==2023.3
urllib3==2.0.4
fake-useragent==1.4.0
""".strip()
    
    with open('requirements.txt', 'w', encoding='utf-8') as f:
        f.write(requirements)
    print("✅ Created requirements.txt")

def install_requirements():
    """Install required packages"""
    try:
        print("📦 Installing required packages...")
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-r', 'requirements.txt'])
        print("✅ All packages installed successfully!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Error installing packages: {e}")
        return False

def create_env_file():
    """Create .env template file"""
    env_content = """# Job Automation Bot Configuration
# Copy this file and rename to .env, then fill in your actual values

# OpenAI API Key (Required for AI features)
OPENAI_API_KEY=your_openai_api_key_here

# Gmail Configuration for Email Notifications
EMAIL_ADDRESS=priyanshidwivedi0712@gmail.com
EMAIL_PASSWORD=your_gmail_app_password_here

# Optional API Keys
LINKEDIN_API_KEY=
INDEED_API_KEY=

# Security Settings
USE_PROXY=false
PROXY_URL=

# Debug Mode
DEBUG_MODE=true
"""
    
    if not os.path.exists('.env'):
        with open('.env.template', 'w', encoding='utf-8') as f:
            f.write(env_content)
        print("✅ Created .env.template file")
        print("📝 Please copy .env.template to .env and add your actual API keys")
    else:
        print("⚠️  .env file already exists")

def create_config_file():
    """Create personalized config.json for Priyanshi"""
    config = {
        "personal_info": {
            "name": "Priyanshi Dwivedi",
            "phone": "9424448976",
            "email": "priyanshidwivedi0712@gmail.com",
            "location": "Indore, MP",
            "linkedin": "https://linkedin.com/in/priyanshii-dwivedi/",
            "github": "https://github.com/priyanshidwivedi",
            "years_experience": {
                "fullstack": 1,
                "cybersecurity": 1,
                "it_support": 1
            }
        },
        "job_keywords": {
            "fullstack": [
                "full stack developer", "python developer", "web developer",
                "flask developer", "javascript developer", "frontend developer",
                "backend developer", "software engineer"
            ],
            "cybersecurity": [
                "cybersecurity analyst", "security engineer", "SOC analyst",
                "information security", "cyber security", "security specialist",
                "penetration tester", "ethical hacker", "security consultant"
            ],
            "it_support": [
                "IT support specialist", "technical support", "help desk",
                "desktop support", "system administrator", "IT technician",
                "technical analyst", "support engineer"
            ]
        },
        "target_companies": [
            # Indian IT Companies
            "TCS", "Infosys", "Wipro", "HCL Technologies", "Tech Mahindra",
            "Cognizant", "Capgemini", "Accenture", "IBM", "DXC Technology",
            
            # Global Tech Giants
            "Microsoft", "Google", "Amazon", "Apple", "Meta",
            "Oracle", "SAP", "Adobe", "Salesforce", "ServiceNow",
            
            # Cybersecurity Companies
            "Palo Alto Networks", "CrowdStrike", "Fortinet", "Check Point",
            "Symantec", "McAfee", "Trend Micro", "FireEye", "Rapid7",
            
            # Indian Startups & Mid-size
            "Zomato", "Swiggy", "Paytm", "PhonePe", "Flipkart",
            "BYJU'S", "Ola", "MakeMyTrip", "BookMyShow", "Nykaa"
        ],
        "location_preferences": {
            "primary": "Indore, MP",
            "secondary": ["Mumbai", "Pune", "Bangalore", "Hyderabad", "Delhi NCR"],
            "remote_preferred": True
        },
        "application_settings": {
            "minimum_match_score": 0.25,
            "max_applications_per_day": 12,
            "max_applications_per_company_per_month": 2,
            "check_interval_hours": 6,
            "apply_on_weekends": False
        },
        "skills": {
            "fullstack_skills": [
                "Python", "HTML5", "CSS3", "JavaScript", "Flask", "MySQL",
                "Web Development", "Full-Stack Development", "Database Integration",
                "UI Design", "Form Handling", "APIs", "Git", "Docker"
            ],
            "cybersecurity_skills": [
                "Network Security", "Ethical Hacking", "SOC Operations", 
                "Network Monitoring", "Vulnerability Assessment", "Threat Detection",
                "Digital Forensics", "Incident Handling", "Threat Analysis",
                "Cloud Security", "Blockchain", "Quantum Cryptography",
                "Nmap", "Wireshark", "Scapy", "Python", "Cryptography"
            ],
            "it_support_skills": [
                "Windows Administration", "Linux Administration", "MacOS Support",
                "Network Troubleshooting", "System Monitoring", "Technical Documentation",
                "Customer Support", "Problem Solving", "ITIL Framework",
                "Computer Networks", "Microsoft Office 365", "Google Workspace",
                "Python", "Bash", "C/C++", "Database Management"
            ]
        },
        "email_notifications": {
            "enabled": True,
            "daily_summary": True,
            "application_confirmations": True,
            "interview_reminders": True
        },
        "interview_prep": {
            "generate_questions": True,
            "difficulty_levels": ["beginner", "intermediate"],
            "focus_areas": ["technical", "behavioral", "situational"]
        }
    }

    with open('config.json', 'w', encoding='utf-8') as f:
        json.dump(config, f, indent=4)
    print("✅ Created personalized config.json")

def create_resume_files():
    """Create resume template files"""
    
    # Full-Stack Resume
    fullstack_resume = """PRIYANSHI DWIVEDI
Full-Stack Web Developer

Contact: 9424448976 | priyanshidwivedi0712@gmail.com | Indore, MP
LinkedIn: linkedin.com/in/priyanshii-dwivedi/

OBJECTIVE
Security-focused aspiring Software Engineer with hands-on experience in Python, Full-Stack web development, and network defense. Passionate about building secure, scalable applications and integrating cybersecurity practices from day one.

EDUCATION
B.Tech in Information Technology | Medi-Caps University | 2026
Relevant Courses: Cloud Security, Computer Networks, Blockchain, Distributed Computing

TECHNICAL SKILLS
• Programming: Python, HTML5, CSS3, JavaScript
• Frameworks: Flask
• Database: MySQL
• Tools: Git, Docker, Nmap, Wireshark
• Platforms: Windows, macOS, Linux

PROFESSIONAL EXPERIENCE
Cyber Security Virtual Intern | Palo Alto Networks | Apr-May 2025
• Gained hands-on experience in SOC operations and network monitoring
• Enhanced knowledge in Cloud Security and Network Security

PROJECTS
Skill Swap Platform - Full-stack web application for talent exchange
• Implemented secure user authentication and profile management
• Integrated MySQL database with secure query practices
• Technologies: HTML5, CSS3, JavaScript, Flask, MySQL

CERTIFICATIONS
• Fortinet Certified Associate Cybersecurity
• Python Programming - Cisco Networking Academy
• Network Security Fundamentals - Palo Alto Networks"""

    # Cybersecurity Resume
    cybersecurity_resume = """PRIYANSHI DWIVEDI
Cybersecurity Analyst

Contact: 9424448976 | priyanshidwivedi0712@gmail.com | Indore, MP
LinkedIn: linkedin.com/in/priyanshii-dwivedi/

OBJECTIVE
Cybersecurity enthusiast with hands-on internship experience in SOC operations, threat detection, and vulnerability assessment. Proficient in network monitoring, incident handling, and digital forensics.

EDUCATION
B.Tech in Information Technology | Medi-Caps University | 2026
Relevant Courses: Information Security, Computer Networks, Blockchain, Cybersecurity Fundamentals

PROFESSIONAL EXPERIENCE
Cyber Security Virtual Intern | Palo Alto Networks | Apr-May 2025
• SOC operations and network monitoring experience
• Threat detection and incident response procedures
• Security log analysis and pattern identification

Cyber Security Intern | Crime Branch, Indore | May 2025
• Assisted in cybercrime case analysis and digital forensics
• Supported forensic data collection and analysis

TECHNICAL SKILLS
• Security Tools: Nmap, Wireshark, Scapy, Hashcat, Hydra
• Programming: Python, C/C++, Bash
• Specializations: Network Security, Ethical Hacking, Cryptography
• Platforms: Windows Security, Linux Security

PROJECTS
Network Packet Analyzer - Python tool using Scapy for traffic analysis
Keylogger Development - Educational cybersecurity demonstration
Hash Generator - Cryptographic security tool for data integrity

CERTIFICATIONS
• Fortinet Certified Associate Cybersecurity
• Network Security Fundamentals - Palo Alto Networks
• Cryptography and Network Security - NPTEL"""

    # IT Support Resume
    it_support_resume = """PRIYANSHI DWIVEDI
IT Support Engineer

Contact: 9424448976 | priyanshidwivedi0712@gmail.com | Indore, MP
LinkedIn: linkedin.com/in/priyanshii-dwivedi/

OBJECTIVE
Tech-savvy IT professional with hands-on experience in system monitoring, technical troubleshooting, and user support. Strong communicator with excellent problem-solving skills and passion for delivering exceptional technical support.

EDUCATION
B.Tech in Information Technology | Medi-Caps University | 2026
Relevant Courses: Computer Networks, Operating Systems, Information Security

PROFESSIONAL EXPERIENCE
Cyber Security Virtual Intern | Palo Alto Networks | Apr-Jun 2025
• SOC operations, threat detection, and log analysis
• System monitoring and security tool administration
• Improved incident response time through log pattern analysis

TECHNICAL SKILLS
• Operating Systems: Windows, Linux, macOS
• Programming: Python, Bash, C/C++
• Tools: Network troubleshooting, System monitoring
• Platforms: Microsoft Office 365, Google Workspace
• Specializations: Network Security, Technical Support

CORE COMPETENCIES
• System Administration and Network Management
• Help Desk Support and Incident Resolution  
• Technical Documentation and User Training
• Customer Service and Communication

CERTIFICATIONS
• IT Support Technician - Alison
• Network Security Fundamentals - Palo Alto Networks
• Python Programming - Cisco Networking Academy
• CCNA (Currently Pursuing)"""

    # Save resume files
    resume_files = {
        'resumes/fullstack_resume.txt': fullstack_resume,
        'resumes/cybersecurity_resume.txt': cybersecurity_resume,
        'resumes/it_support_resume.txt': it_support_resume
    }
    
    for filename, content in resume_files.items():
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"✅ Created {filename}")

def create_startup_script():
    """Create startup script for easy launching"""
    
    startup_content = """#!/usr/bin/env python3
# Quick Start Script for Job Automation Bot

import os
import sys

def main():
    print("🤖 Job Automation Bot - InterviewCracker.AI")
    print("=" * 50)
    print("Created for Priyanshi Dwivedi")
    print("=" * 50)
    
    # Check if main.py exists
    if not os.path.exists('main.py'):
        print("❌ main.py not found!")
        print("Please ensure you have downloaded the main application file.")
        return
    
    # Check if .env exists
    if not os.path.exists('.env'):
        print("⚠️  .env file not found!")
        print("Please copy .env.template to .env and configure your API keys.")
        response = input("Continue anyway? (y/n): ")
        if response.lower() != 'y':
            return
    
    # Run the main application
    try:
        os.system(f"{sys.executable} main.py")
    except KeyboardInterrupt:
        print("\\n👋 Application stopped by user")
    except Exception as e:
        print(f"❌ Error running application: {e}")

if __name__ == "__main__":
    main()
"""

    with open('start.py', 'w', encoding='utf-8') as f:
        f.write(startup_content)
    print("✅ Created start.py launcher script")

def create_readme():

    """Create a quick README file"""
    readme_content = """# Job Automation Bot for Priyanshi Dwivedi

## Quick Start
1. Run `python setup.py` (you just did this!)
2. Copy `.env.template` to `.env` and add your API keys
3. Run `python start.py` to launch the application

## Features
- 🔍 Automated job searching across multiple platforms
- 📝 AI-powered resume customization
- 📧 Email notifications for applications
- 🎯 Interview preparation with AI-generated questions
- 📊 Aptitude tests for skill assessment
- 📈 Application tracking and analytics

## Your Profile
- **Name**: Priyanshi Dwivedi
- **Skills**: Full-Stack Development, Cybersecurity, IT Support
- **Location**: Indore, MP
- **Target**: Top tech companies and cybersecurity firms

## Configuration
- Check `config.json` for job preferences
- Update resume templates in `resumes/` folder
- Modify target companies and skills as needed

## Support
- Review the deployment guide for detailed setup
- Check logs in `logs/` folder for troubleshooting
- Update skills and preferences regularly for better matches

Good luck with your job search! 🚀
"""
    
    with open('README.md', 'w', encoding='utf-8') as f:
        f.write(readme_content)
    print("✅ Created README.md")

def main():
    """Main setup function"""
    print("🚀 Setting up Job Automation Bot for Priyanshi Dwivedi")
    print("=" * 60)
    
    # Check Python version
    if not check_python_version():
        return
    
    # Create directories
    print("\n📁 Creating project directories...")
    create_directories()
    
    # Create configuration files
    print("\n⚙️  Creating configuration files...")
    create_requirements_file()
    create_env_file()
    create_config_file()
    
    # Create resume templates
    print("\n📄 Creating resume templates...")
    create_resume_files()
    
    # Create utility scripts
    print("\n🛠️  Creating utility scripts...")
    create_startup_script()
    create_readme()
    
    # Install packages
    print("\n📦 Installing required packages...")
    install_success = install_requirements()
    
    print("\n" + "=" * 60)
    print("🎉 Setup Complete!")
    print("=" * 60)
    
    if install_success:
        print("✅ All packages installed successfully")
    else:
        print("⚠️  Some packages failed to install - check manually")
    
    print("\n📋 Next Steps:")
    print("1. Copy .env.template to .env")
    print("2. Add your OpenAI API key and Gmail app password to .env")
    print("3. Download the main.py file and place it in this directory")
    print("4. Run: python start.py")
    
    print("\n📚 Important Files Created:")
    print("• config.json - Your personalized job search configuration")
    print("• resumes/ - Your resume templates for each career path")
    print("• .env.template - Environment variables template")
    print("• requirements.txt - Python dependencies")
    print("• start.py - Quick launcher script")
    
    print("\n🎯 Your Job Search Profile:")
    print("• Target Roles: Full-Stack Developer, Cybersecurity Analyst, IT Support")
    print("• Location: Indore, MP (Remote preferred)")
    print("• Focus: Top tech companies + Indian IT giants")
    print("• Features: AI resume customization + Interview prep")
    
    print("\n🔑 Required API Keys:")
    print("• OpenAI API key for AI features")
    print("• Gmail app password for notifications")
    
    print("\nHappy job hunting! 🚀")

if __name__ == "__main__":
    main()