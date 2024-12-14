def match_job_titles(resume_jobs, jd_jobs):
    """Calculate job title match score."""
    if not resume_jobs or not jd_jobs:
        return 0

    matched_jobs = set(resume_jobs).intersection(set(jd_jobs))
    match_score = len(matched_jobs) / len(jd_jobs)
    return round(match_score, 2)
