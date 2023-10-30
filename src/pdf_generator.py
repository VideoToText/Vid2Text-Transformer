from fpdf import FPDF

def generate_pdf_from_text(text, output_path):
    """
    Convert given structured text into a PDF document.
    """
    class PDF(FPDF):
        def header(self):
            # Select Arial bold 15
            self.set_font('Arial', 'B', 15)
            # Move to the right
            self.cell(80)
            # Framed title
            self.cell(30, 10, 'Text Document', 1, 0, 'C')
            # Line break
            self.ln(20)

        def footer(self):
            # Position at 1.5 cm from bottom
            self.set_y(-15)
            # Select Arial italic 8
            self.set_font('Arial', 'I', 8)
            # Page number
            self.cell(0, 10, 'Page ' + str(self.page_no()), 0, 0, 'C')

    # Create instance of PDF class
    pdf = PDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, text)

    # Save the pdf with name .pdf
    pdf.output(output_path)

# # Example usage:
# text_content = """
# Video Content:

# Title: Learn Basic Korean Greetings - (Hello)
# Duration: 2 minutes and 30 seconds

# ... (and so on)
# """

# generate_pdf_from_text(text_content, "output.pdf")
