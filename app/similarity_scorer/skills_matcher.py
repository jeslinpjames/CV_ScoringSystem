def match_skills(resume_skills, jd_skills):
    """Calculate skill match score."""
    if not resume_skills or not jd_skills:
        return 0

    matched_skills = set(resume_skills).intersection(set(jd_skills))
    match_score = len(matched_skills) / len(jd_skills)
    return round(match_score, 2)
