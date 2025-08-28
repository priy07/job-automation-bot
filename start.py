#!/usr/bin/env python3
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
        print("\n👋 Application stopped by user")
    except Exception as e:
        print(f"❌ Error running application: {e}")

if __name__ == "__main__":
    main()
