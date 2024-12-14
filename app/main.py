from input_pdf import process_resume
from section_identifiers import identify_sections
from feature_extractor import extract_skills, extract_education, extract_job_titles

def process_file(filepath):
    """Process resume, identify sections, and extract features."""
    # Step 1: Extract raw text
    raw_text = process_resume(filepath)
    if not raw_text:
        return None

    # Step 2: Identify sections
    sections = identify_sections(raw_text)
    if not sections:
        return None

    # Step 3: Extract features
    features = extract_features(sections)
    return sections, features

def extract_features(sections):
    """Extract structured features from sections."""
    skills = extract_skills(sections.get("skills", ""), [sections.get("languages", "")])
    education = extract_education(sections.get("education", ""))
    job_titles = extract_job_titles(sections.get("experience", ""))
    return {
        "skills": skills,
        "education": education,
        "job_titles": job_titles
    }

def clean_section_content(content):
    """Format section content for better readability."""
    lines = [line.strip() for line in content.split("\n") if line.strip()]
    return "\n- " + "\n- ".join(lines)

if __name__ == "__main__":
    filepath = "C:/Users/jesli/Downloads/Jeslin_Resume.pdf"  # Replace with actual file path
    result = process_file(filepath)

    if result:
        sections, features = result

        # Print identified sections
        print("=== IDENTIFIED SECTIONS ===")
        for section, content in sections.items():
            print(f"\n=== {section.upper()} ===")
            print(clean_section_content(content))

        # Print extracted features
        print("\n=== EXTRACTED FEATURES ===")
        print(f"Skills: {features['skills']}")
        print(f"Education: {features['education']}")
        print(f"Job Titles: {features['job_titles']}")
    else:
        print("Failed to process the resume.")
