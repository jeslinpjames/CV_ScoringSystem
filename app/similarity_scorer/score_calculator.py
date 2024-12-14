def calculate_total_score(skills_score, education_score, job_score, weights=None):
    """Calculate total score based on weights."""
    if weights is None:
        weights = {"skills": 0.5, "education": 0.3, "jobs": 0.2}

    total_score = (
        weights["skills"] * skills_score +
        weights["education"] * education_score +
        weights["jobs"] * job_score
    )
    return round(total_score, 2)
