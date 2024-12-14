from input_pdf import process_resume
from section_identifiers import identify_sections

def process_file(filepath):
    """Process resume and identify sections."""
    raw_text = process_resume(filepath)
    if raw_text:
        sections = identify_sections(raw_text)
        return sections
    return None

if __name__ == "__main__":
    filepath = "C:/Users/jesli/Downloads/Jeslin_Resume.pdf"  
    sections = process_file(filepath)
    if sections:
        for section, content in sections.items():
            print(f"=== {section.upper()} ===")
            print(content)
    else:
        print("Failed to process the resume.")
