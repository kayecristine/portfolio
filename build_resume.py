from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, HRFlowable, ListFlowable, ListItem
)
from reportlab.lib.enums import TA_LEFT, TA_CENTER

import os

OUTPUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Resume_Kaye Cristine Tolentino (v2).pdf")

# ── Color palette (minimal / professional) ──────────────────────────────────
BLACK      = colors.HexColor("#111111")
DARK_GRAY  = colors.HexColor("#333333")
MID_GRAY   = colors.HexColor("#555555")
LIGHT_GRAY = colors.HexColor("#888888")
RULE_COLOR = colors.HexColor("#CCCCCC")
WHITE      = colors.white

def build_pdf():
    doc = SimpleDocTemplate(
        OUTPUT,
        pagesize=letter,
        rightMargin=0.65 * inch,
        leftMargin=0.65 * inch,
        topMargin=0.55 * inch,
        bottomMargin=0.55 * inch,
    )

    # ── Styles ───────────────────────────────────────────────────────────────
    def S(name, parent="Normal", **kwargs):
        base = getSampleStyleSheet()[parent]
        return ParagraphStyle(name, parent=base, **kwargs)

    name_style = S("Name",
        fontSize=22, leading=26, textColor=BLACK,
        fontName="Helvetica-Bold", spaceAfter=2, alignment=TA_CENTER)

    contact_style = S("Contact",
        fontSize=9, leading=13, textColor=MID_GRAY,
        fontName="Helvetica", alignment=TA_CENTER, spaceAfter=6)

    summary_style = S("Summary",
        fontSize=9.5, leading=14, textColor=DARK_GRAY,
        fontName="Helvetica", spaceAfter=4)

    section_heading = S("SectionHeading",
        fontSize=10.5, leading=14, textColor=BLACK,
        fontName="Helvetica-Bold", spaceBefore=8, spaceAfter=3,
        textTransform="uppercase", letterSpacing=0.8)

    job_title_style = S("JobTitle",
        fontSize=10.5, leading=13, textColor=BLACK,
        fontName="Helvetica-Bold", spaceBefore=6, spaceAfter=0)

    company_date_style = S("CompanyDate",
        fontSize=9.5, leading=13, textColor=MID_GRAY,
        fontName="Helvetica-Oblique", spaceAfter=3)

    bullet_style = S("Bullet",
        fontSize=9.5, leading=13.5, textColor=DARK_GRAY,
        fontName="Helvetica", leftIndent=12, spaceAfter=0)

    label_style = S("Label",
        fontSize=9.5, leading=13, textColor=BLACK,
        fontName="Helvetica-Bold", spaceAfter=2)

    plain_style = S("Plain",
        fontSize=9.5, leading=13, textColor=DARK_GRAY,
        fontName="Helvetica", spaceAfter=2)

    def rule():
        return HRFlowable(width="100%", thickness=0.5,
                          color=RULE_COLOR, spaceAfter=4, spaceBefore=4)

    def section(title):
        return [
            Spacer(1, 4),
            rule(),
            Paragraph(title, section_heading),
        ]

    def job(title, company, dates, bullets):
        items = [
            Paragraph(title, job_title_style),
            Paragraph(f"{company} &nbsp;&nbsp;|&nbsp;&nbsp; {dates}", company_date_style),
        ]
        for b in bullets:
            items.append(Paragraph(f"• &nbsp;{b}", bullet_style))
        return items

    # ── Content ──────────────────────────────────────────────────────────────
    story = []

    # Header
    story.append(Paragraph("KAYE CRISTINE TOLENTINO", name_style))
    story.append(Paragraph(
        "Taguig City, Philippines &nbsp;|&nbsp; +63 977 316 6317 &nbsp;|&nbsp; "
        "kayecristine.tolentino@gmail.com &nbsp;|&nbsp; "
        "www.linkedin.com/in/kayecristine",
        contact_style))

    # Summary
    story += section("Professional Summary")
    story.append(Paragraph(
        "Technical professional specializing in cloud infrastructure, AWS services, and automation. "
        "Proven ability to design and implement cloud solutions including serverless architectures, "
        "container orchestration, and automated systems. Strong background in technical instruction "
        "with expertise in translating complex concepts into practical applications. Seeking to "
        "leverage cloud knowledge and operational experience in site reliability engineering and "
        "AI operations.",
        summary_style))

    # Experience
    story += section("Work Experience")

    story += job(
        "Site Reliability Engineer",
        "Cambridge University Press and Assessment",
        "February 2026 – Present",
        [
            "Manage and optimize mission-critical cloud infrastructure across AWS and Kubernetes environments, ensuring high availability, system reliability, and SLA adherence.",
            "Implement AI-driven operations (AIOps) workflows, automated telemetry analysis, and proactive incident detection to minimize system downtime.",
            "Develop automated remediation pipelines, CI/CD deployment guardrails, and infrastructure as code (IaC) to streamline global assessment platform operations.",
            "Enhance system observability through distributed tracing, log aggregation, and real-time alert monitoring to reduce Mean Time to Resolution (MTTR).",
        ]
    )

    story += job(
        "Cloud Engineer Technical Trainer",
        "Apper Digital Inc.",
        "November 2024 – February 2026",
        [
            "Built automated assessment system using AWS Lambda, DynamoDB, and Step Functions for real-time student evaluation and grading.",
            "Designed AWS hands-on labs covering EC2, ECS, S3, VPC, IAM, and serverless architectures for enterprise training programs.",
            "Developed AI-powered Study Bot using n8n workflow automation to generate cloud certification practice questions with automated answers.",
            "Delivered cloud computing and Kubernetes training to enterprise clients including DLSU-Taft, SageSoft, and GCash.",
            "Created CKAD assessment labs using Amazon ECS for container orchestration and deployment testing.",
            "Conducted InfoSecOps training sessions covering AWS security services and DevOps security practices.",
            "Trained professionals for KCNA certification, covering Kubernetes and cloud-native technologies.",
        ]
    )

    story += job(
        "AWS BuildHers+ Mentor",
        "AWS Community",          # ← CORRECTED
        "October 2025 – January 2026",
        [
            "Provide biweekly professional mentorship to women in technology, supporting AWS cloud learning and career development.",
            "Part of a structured program focused on fostering inclusive growth in cloud computing.",
        ]
    )

    story += job(
        "Engineering Board Exam Instructor",
        "Excel Review Center",
        "June 2019 – November 2024",
        [
            "Trained 10,000+ engineering students through online (300 participants/session) and in-person (150 participants/session) review programs.",
            "Delivered training programs across the Philippines and internationally in Qatar, Saudi Arabia, and UAE.",
            "Partnered with leading universities: Mapua University, Malayan Colleges, Saint Louis University, LPU-L, FAITH, USLT, and PUP.",
            "Served as panelist and quiz master for national and regional Electronics Engineering competitions.",
        ]
    )

    story += job(
        "Content Creator",
        "Alterguru Ph",
        "August 2020 – March 2023",
        [
            "Created educational science content for high school students and video series on technical problem-solving.",
        ]
    )

    story += job(
        "Academic Tutor",
        "Course Hero",
        "May 2020 – July 2020",
        [
            "Provided solutions and tutoring for Mathematics and Electronics engineering subjects.",
        ]
    )

    # Key Technical Projects
    story += section("Key Technical Projects")

    story += job(
        "Momentum OS & Companion Creator Studio",
        "Full-Stack Desktop & Web Applications",
        "2026",
        [
            "Built desktop productivity command center using Electron, React 19, and Firebase featuring 8 Life Pillars, energy-based task selection, and Google Calendar sync.",
            "Developed companion AI Creator Studio web app featuring algorithmic 2-second hook retention scoring and multi-night music release pipelines.",
        ]
    )

    story += job(
        "Momentum Finance & Venice Vista Lodge",
        "Full-Stack Web & Native Mobile Applications",
        "2025 – 2026",
        [
            "Created cross-platform personal finance app with Google Gemini AI agent for autonomous natural language transaction logging (Web + iOS with FaceID).",
            "Shipped property management PWA featuring live Google Calendar booking synchronization, automated concierge email notifications, and role-based access control.",
        ]
    )

    # Education
    story += section("Education")
    story.append(Paragraph("Bachelor of Science in Electronics Engineering", job_title_style))
    story.append(Paragraph("Lyceum of the Philippines University – Laguna &nbsp;|&nbsp; 2013 – 2018", company_date_style))
    story.append(Paragraph("• &nbsp;Cum Laude", bullet_style))
    story.append(Paragraph("• &nbsp;Consistent Dean's List (2013–2018)", bullet_style))
    story.append(Paragraph("• &nbsp;Top 1 Academic Excellence Awardee – College of Engineering", bullet_style))

    # Certifications
    story += section("Certifications & Licenses")

    cert_groups = [
        ("Professional Licenses", [
            "Electronics Engineer | Professional Regulation Commission (2018)",
            "Electronics Technician | Professional Regulation Commission (2018)",
        ]),
        ("AWS Certifications", [
            "AWS Certified Solutions Architect – Associate (2024)",
            "AWS Certified AI Practitioner (2024)",
            "AWS Certified Cloud Practitioner (2023)",
        ]),
        ("Kubernetes & Cloud Native", [
            "Kubernetes and Cloud Native Associate (KCNA) | CNCF (2024)",
        ]),
        ("Data Analytics", [
            "Google Data Analytics Professional Certificate | Coursera (2023)",
            "Introduction to Data Science | CISCO (2023)",
            "Data Analytics Essentials | CISCO (2023)",
        ]),
    ]

    for group_label, certs in cert_groups:
        story.append(Paragraph(group_label, label_style))
        for c in certs:
            story.append(Paragraph(f"• &nbsp;{c}", bullet_style))
        story.append(Spacer(1, 4))

    # Technical Skills
    story += section("Technical Skills")

    skill_groups = [
        ("Cloud & Infrastructure",
         "AWS (Lambda, DynamoDB, Step Functions, ECS/Fargate, EC2, S3, VPC, IAM, CloudFormation, CloudWatch), "
         "Kubernetes, Docker, Infrastructure as Code"),
        ("AI & Automation",
         "n8n workflow automation, LLMs, Generative AI, AWS Bedrock, Prompt Engineering, Observability"),
        ("Development",
         "Python, SQL, R, C++, Git, CI/CD pipelines, Agile methodology"),
        ("Security",
         "InfoSecOps, AWS security services, IAM, data protection"),
        ("Data & Analytics",
         "Tableau, MS Excel, data visualization"),
    ]

    for label, content in skill_groups:
        story.append(Paragraph(f"<b>{label}:</b> {content}", plain_style))

    # Key Strengths
    story += section("Key Strengths")
    strengths = [
        "Cloud infrastructure design and automation using AWS services",
        "Experience with AI workflow automation and n8n platform",
        "Container orchestration with Kubernetes and Amazon ECS",
        "Strong technical communication and training delivery skills",
        "Cross-functional collaboration with development and operations teams",
        "Self-directed learning and continuous improvement mindset",
    ]
    for s in strengths:
        story.append(Paragraph(f"• &nbsp;{s}", bullet_style))

    # Reference
    story += section("Reference")
    story.append(Paragraph("Marnie Tolosa", job_title_style))
    story.append(Paragraph(
        "Partner Enablement Manager – Philippines, Training and Certification, AWS Philippines",
        company_date_style))
    story.append(Paragraph("marniest@amazon.ph", plain_style))

    doc.build(story)
    print(f"✅ PDF saved to: {OUTPUT}")

build_pdf()
