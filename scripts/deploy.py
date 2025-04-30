import subprocess
import os

def deploy():
    """Deployment script for production."""
    # Install dependencies
    subprocess.run(["pip", "install", "-r", "requirements.txt"])
    
    # Install Playwright browsers
    subprocess.run(["playwright", "install"])
    
    print("Deployment complete. Start bot with: python src/main.py")

if __name__ == "__main__":
    deploy()