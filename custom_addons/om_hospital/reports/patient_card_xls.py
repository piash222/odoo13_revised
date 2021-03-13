from odoo import models


class PatientCardXLS(models.AbstractModel):
    _name = 'report.om_hospital.report_patient_xls'
    _inherit = 'report.odoo_report_xlsx.abstract'

    def generate_xlsx_report(self, workbook, data, lines):
        # for obj in lines:
        #     report_name = obj.name
        #     # One sheet by partner
        format1 = workbook.add_format({'font_size': 14, 'align': 'center', 'bold': True})
        format2 = workbook.add_format({'font_size': 10, 'align': 'center'})

        sheet = workbook.add_worksheet("Patient Card")
        sheet.write(2, 2, 'Name', format1)
        sheet.write(2, 3, lines.patient_name, format2)
        sheet.write(3, 2, 'age', format1)
        sheet.write(3, 3, lines.patient_age, format2)
        # bold = workbook.add_format({'bold': True})
        # sheet.write(0, 0, obj.name, bold)
