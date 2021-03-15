from odoo import models


class PatientCardXLS(models.AbstractModel):
    _name = 'report.om_hospital.report_patient_xls'
    _inherit = 'report.odoo_report_xlsx.abstract'

    def generate_xlsx_report(self, workbook, data, lines):
        # for obj in lines:
        #     report_name = obj.name
        #     # One sheet by partner
        model = self.env.context.get('active_model')
        print('model', model)
        print('workbook', workbook)
        print('data', data)
        print('lines', lines, 'types', type(lines))

        docs = self.env['hospital.appointment'].search([])
        print('docs', docs, 'types', type(docs))
        format1 = workbook.add_format({'font_size': 14, 'align': 'center', 'bold': True})
        format2 = workbook.add_format({'font_size': 10, 'align': 'center'})

        sheet = workbook.add_worksheet("Patient Card")
        # sheet.write(2, 2, 'Name', format1)
        # sheet.write(2, 3, lines.patient_name, format2)
        # sheet.write(3, 2, 'age', format1)
        # sheet.write(3, 3, lines.patient_age, format2)
        # bold = workbook.add_format({'bold': True})
        # sheet.write(0, 0, obj.name, bold)
        sheet.write(0, 0, 'patient_id', format1)
        sheet.write(0, 1, 'age', format1)
        sheet.write(0, 2, 'date ', format1)
        sheet.write(0, 3, 'note', format1)
        # sheet.write(2, 3, docs.patient_id.patient_name, format2)

        for idx, doc in enumerate(docs, start=1):
            # for j in range(0, 4):
            # print(idx, j)
            sheet.write(idx, 0, doc.patient_id.id, format2)
            sheet.write(idx, 1, doc.patient_age, format2)
            sheet.write(idx, 2, doc.appointment_date, format2)
            sheet.write(idx, 3, doc.notes, format2)
