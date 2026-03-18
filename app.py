from flask import Flask, render_template, request, send_from_directory
import os
from resume_parser import extract_text_from_pdf
from skill_matcher import extract_skills, calculate_score, section_scores, get_recommendations

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


# ⭐ Route to serve uploaded files
@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(UPLOAD_FOLDER, filename)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        file = request.files.get("resume")

        if not file:
            return "❌ No file uploaded"

        file_path = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(file_path)

        text = extract_text_from_pdf(file_path)

        if text == "INVALID_PDF":
            return "❌ Invalid PDF file."

        if text == "NO_TEXT":
            return "❌ No readable text."

        skills = extract_skills(text)
        score, missing = calculate_score(skills)
        sections = section_scores(skills)
        recommendations = get_recommendations(missing)

        return render_template(
            "index.html",
            skills=skills,
            score=score,
            missing=missing,
            sections=sections,
            recommendations=recommendations,
            pdf_file=file.filename   # ⭐ IMPORTANT
        )

    return render_template("index.html")


import os

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))