import re

def get_resume_suggestions(resume_text):
    suggestions = []

    # Check if the resume is too short
    if len(resume_text.split()) < 150:
        suggestions.append("📄 Your resume seems too short. Consider adding more details about your education, skills, or experiences.")

    # Check if resume includes project/internship/experience
    if not re.search(r"(project|internship|experience)", resume_text, re.IGNORECASE):
        suggestions.append("🛠️ Try including details about projects, internships, or work experience to showcase practical knowledge.")

    # Check for technical skills
    if not re.search(r"(python|sql|java|ml|machine learning|excel|nlp)", resume_text, re.IGNORECASE):
        suggestions.append("💡 You haven't listed many technical skills. Add relevant skills such as Python, SQL, Excel, or NLP.")

    # Check for education details
    if not re.search(r"(bachelor|bsc|b\.tech|degree|college|university)", resume_text, re.IGNORECASE):
        suggestions.append("🎓 Education details seem missing. Include your degree, college/university name, and graduation year.")

    # Check for contact details
    if not re.search(r"(email|phone|contact)", resume_text, re.IGNORECASE):
        suggestions.append("📞 Add contact details like email or phone number at the top of your resume.")

    # If no suggestions, indicate it's good
    if not suggestions:
        suggestions.append("✅ Your resume looks good! Just ensure formatting and alignment are professional.")

    return "\n\n".join(suggestions)
