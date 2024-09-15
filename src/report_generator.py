from fpdf import FPDF

class PDFReport(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'GitHub Project Report', 0, 1, 'C')

    def project_data(self, project_name, data):
        self.set_font('Arial', '', 12)
        self.cell(0, 10, f'Project: {project_name}', 0, 1)
        for key, value in data.items():
            self.cell(0, 10, f'{key}: {value}', 0, 1)

def generate_report(project_name, data):
    pdf = PDFReport()
    pdf.add_page()
    pdf.project_data(project_name, data)
    pdf.output(f'{project_name}_report.pdf')
