import re

# Predefined set of technical skills
TECHNICAL_SKILLS = [
    "python", "c++", "java", "javascript", "tensorflow", "pytorch", "docker",
    "kubernetes", "react", "django", "fastapi", "aws", "gcp", "azure",
    "sql", "numpy", "pandas", "opencv", "scikit-learn", "langchain", "matplotlib"
]


def extract_skills(skills_section, other_sections=None):
    """Extract and standardize skills from the skills section or fallback to other sections."""
    extracted_skills = []
    sections_to_check = [skills_section] + (other_sections or [])
    
    for section in sections_to_check:
        if section:
            words = re.split(r"[,;\n\s]", section.lower())
            for word in words:
                if word.strip() in TECHNICAL_SKILLS:
                    extracted_skills.append(word.capitalize())
    return list(set(extracted_skills))  # Remove duplicates

