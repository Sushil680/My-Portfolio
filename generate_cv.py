#!/usr/bin/env python3
"""
Script to generate Sushil Nath Yogi's CV PDF.
Run: python generate_cv.py
"""

from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, HRFlowable, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
import os

def generate_cv(output_path='static/assets/cv.pdf'):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    doc = SimpleDocTemplate(
        output_path,
        pagesize=letter,
        rightMargin=45,
        leftMargin=45,
        topMargin=40,
        bottomMargin=40
    )

    styles = getSampleStyleSheet()
    title_style = ParagraphStyle(
        'DocTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=20,
        leading=24,
        textColor=colors.HexColor('#111827')
    )
    subtitle_style = ParagraphStyle(
        'DocSubTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=10.5,
        leading=14,
        textColor=colors.HexColor('#059669')
    )
    contact_style = ParagraphStyle(
        'Contact',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9,
        leading=13,
        textColor=colors.HexColor('#4b5563')
    )
    section_head = ParagraphStyle(
        'SecHead',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=12,
        leading=15,
        textColor=colors.HexColor('#111827'),
        spaceBefore=8,
        spaceAfter=4
    )
    body_bold = ParagraphStyle(
        'BodyBold',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=9.5,
        leading=13,
        textColor=colors.HexColor('#1f2937')
    )
    body_text = ParagraphStyle(
        'BodyText',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9,
        leading=13,
        textColor=colors.HexColor('#374151')
    )
    date_style = ParagraphStyle(
        'DateStyle',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8.5,
        leading=12,
        textColor=colors.HexColor('#6b7280'),
        alignment=2
    )

    story = []

    # Header
    story.append(Paragraph('SUSHIL NATH YOGI', title_style))
    story.append(Spacer(1, 2))
    story.append(Paragraph('Aspiring Data Scientist | Python Developer | Graphic Design Enthusiast', subtitle_style))
    story.append(Spacer(1, 4))
    story.append(Paragraph('Kathmandu, Nepal &nbsp;&bull;&nbsp; sushilyogi56@gmail.com &nbsp;&bull;&nbsp; https://github.com/Sushil680', contact_style))
    story.append(Spacer(1, 6))
    story.append(HRFlowable(width='100%', thickness=1.5, color=colors.HexColor('#059669'), spaceAfter=8))

    # Profile Summary
    story.append(Paragraph('PROFILE SUMMARY', section_head))
    story.append(Paragraph('Bachelor of Information Technology (BIT) student passionate about software engineering, data science, and graphic design. Proficient in Python, Flask, SQL, data analysis, and creating user-centered digital solutions. Proven capability in building web applications, machine learning workflows, and engaging visual graphics.', body_text))

    # Education
    story.append(Paragraph('EDUCATION', section_head))
    edu_data = [
        [Paragraph('<b>Bachelor of Information Technology (BIT)</b><br/><font color="#4b5563">Texas College of Management &amp; IT &mdash; Kathmandu, Nepal</font>', body_text), Paragraph('Nov 2024 &ndash; Present', date_style)]
    ]
    t = Table(edu_data, colWidths=[380, 140])
    t.setStyle(TableStyle([('VALIGN', (0,0), (-1,-1), 'TOP'), ('PADDING', (0,0), (-1,-1), 0)]))
    story.append(t)

    # Technical Skills
    story.append(Paragraph('TECHNICAL SKILLS', section_head))
    skills = [
        '<b>Programming Languages:</b> Python, SQL, HTML5, CSS3, JavaScript',
        '<b>Data Science &amp; ML:</b> Pandas, NumPy, Matplotlib, Scikit-learn, Data Analysis',
        '<b>Web Development:</b> Flask, Jinja2, Bootstrap, RESTful APIs, Responsive Design',
        '<b>Tools &amp; Platforms:</b> Git, GitHub, Linux, Visual Studio Code',
        '<b>Creative &amp; Design:</b> Graphic Design, UI/UX Prototyping, Brand Identity, Visual Arts'
    ]
    for s in skills:
        story.append(Paragraph('&bull; ' + s, body_text))

    # Selected Projects
    story.append(Paragraph('SELECTED PROJECTS', section_head))
    projects = [
        ('Movie Recommendation System', 'Python, Machine Learning, Scikit-learn', 'Developed a content-based recommendation system that evaluates film similarities and delivers tailored movie suggestions.'),
        ('Health Score Predictor', 'Python, Machine Learning, Data Modeling', 'Created a predictive health index model estimating individual wellness metrics based on multi-factor demographic and biometric data.'),
        ('Quora Question Pair Prediction', 'Python, NLP, Machine Learning', 'Engineered an NLP model to classify duplicate question pairs, employing feature engineering, cosine similarity, and TF-IDF.'),
        ('Fitness Tracker Web Application', 'Python, Flask, SQLite', 'Built a responsive fitness tracking web app allowing users to monitor workouts, calorie intake, and visualize progress.'),
        ('Weather Forecast Application', 'Python, Flask, OpenWeather API', 'Implemented a real-time weather portal providing accurate multi-city weather statistics, humidity, and forecasts.'),
        ('Graphic Design Portfolio', 'Adobe Suite, Digital Design, Typography', 'Designed a diverse collection of marketing graphics, logos, posters, social media kits, and brand collateral.')
    ]
    for title, tech, desc in projects:
        story.append(Paragraph(f'<b>{title}</b> &nbsp;|&nbsp; <font color="#059669"><i>{tech}</i></font>', body_bold))
        story.append(Paragraph(desc, body_text))
        story.append(Spacer(1, 3))

    doc.build(story)
    print(f'CV generated successfully at: {output_path}')

if __name__ == '__main__':
    generate_cv()
