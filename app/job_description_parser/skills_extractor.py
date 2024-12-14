import re

# Predefined skills list
TECHNICAL_SKILLS = [
    "python", "tensorflow", "django", "react", "sql", "aws", "docker", "kubernetes"
]

def extract_skills(jd_text):
    """Extract skills from job description."""
    skills = []
    words = re.split(r"[,\s\n]", jd_text.lower())
    for word in words:
        if word in TECHNICAL_SKILLS:
            skills.append(word.capitalize())
    return list(set(skills))  # Remove duplicates
