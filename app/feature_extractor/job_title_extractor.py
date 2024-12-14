import re

COMMON_JOB_TITLES = ["developer", "engineer", "intern", "analyst", "manager", "consultant"]

def extract_job_titles(experience_section):
    """Extract job titles from the experience section."""
    job_titles = []
    if experience_section:
        for line in experience_section.split("\n"):
            if any(title in line.lower() for title in COMMON_JOB_TITLES):
                job_titles.append(line.strip())
            elif re.match(r"^[A-Z][a-z]+(?: [A-Z][a-z]+)*$", line):  # Titles with proper noun capitalization
                job_titles.append(line.strip())
    return list(set(job_titles))  # Remove duplicates


