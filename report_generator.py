from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas


def generate_report(
    disease,
    confidence,
    risk_level,
    description,
    medication,
    diet,
    workout,
    doctor,
    precautions
):

    pdf_file = "Health_Report.pdf"

    c = canvas.Canvas(
        pdf_file,
        pagesize=letter
    )

    c.setFont(
        "Helvetica-Bold",
        16
    )

    c.drawString(
        50,
        750,
        "Healthcare AI Report"
    )

    c.setFont(
        "Helvetica",
        12
    )

    y = 710

    report_data = [

        f"Disease: {disease}",
        f"Confidence: {confidence:.2f}%",
        f"Risk Level: {risk_level}",
        "",
        f"Description: {description}",
        "",
        f"Medication: {medication}",
        "",
        f"Diet: {diet}",
        "",
        f"Workout: {workout}",
        "",
        f"Doctor: {doctor}",
        "",
        "Precautions:"

    ]

    for item in report_data:

        c.drawString(
            50,
            y,
            str(item)
        )

        y -= 20

    for precaution in precautions:

        c.drawString(
            70,
            y,
            f"- {precaution}"
        )

        y -= 20

    c.save()

    return pdf_file