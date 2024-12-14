COMMON_JOB_TITLES = ["developer", "engineer", "analyst", "manager", "consultant"]

def extract_jobs(jd_text):
    """Extract job roles from job description."""
    jobs = []
    for title in COMMON_JOB_TITLES:
        if title in jd_text.lower():
            jobs.append(title.capitalize())
    return list(set(jobs))  # Remove duplicates
