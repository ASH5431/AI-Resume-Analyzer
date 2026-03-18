def extract_skills(text):
    skills_list = [
        "python", "c++", "java", "sql", "html", "css", "javascript",
        "machine learning", "deep learning", "data science",
        "flask", "tensorflow", "keras", "pandas", "numpy",
        "matplotlib", "seaborn", "scikit-learn",
        "power bi", "excel", "git", "mysql"
    ]

    text = text.lower()
    found_skills = []

    for skill in skills_list:
        if skill in text:
            found_skills.append(skill)

    return found_skills


def calculate_score(found_skills):
    required_skills = [
        "python", "sql", "machine learning", "deep learning",
        "pandas", "numpy", "scikit-learn", "tensorflow",
        "data visualization", "statistics"
    ]

    matched = 0
    missing_skills = []

    for skill in required_skills:
        if skill in found_skills:
            matched += 1
        else:
            missing_skills.append(skill)

    score = int((matched / len(required_skills)) * 100)

    return score, missing_skills


# ⭐ Section-wise scoring (like Resume Worded)
def section_scores(found_skills):
    return {
        "impact": 70,
        "brevity": 80,
        "style": 60,
        "skills": min(len(found_skills) * 5, 100)
    }


# ⭐ Recommendations
def get_recommendations(missing_skills):
    rec = []

    if "statistics" in missing_skills:
        rec.append("Learn statistics for better data analysis.")

    if "data visualization" in missing_skills:
        rec.append("Add Power BI / Tableau projects.")

    if "machine learning" not in missing_skills:
        rec.append("Add ML project explanations for stronger impact.")

    if not rec:
        rec.append("Great resume! Minor improvements needed.")

    return rec