from resume_parser import extract_text_from_pdf
from skill_matcher import extract_skills, calculate_score

file_path = "sample_resume.pdf"

text = extract_text_from_pdf(file_path)

skills = extract_skills(text)

score, missing = calculate_score(skills)

print("Extracted Skills:")
print(skills)

print("\nResume Score:", score, "%")

print("\nMissing Skills:")
print(missing)