from odoo import models, fields

class Employee(models.Model):
    _name = 'my_employee.employee'
    _description = 'Thông tin cá nhân nhân viên'

    name = fields.Char(string='Tên nhân viên')
    contact_info = fields.Text(string='Thông tin liên hệ')
    address = fields.Text(string='Hộ tịch')
    work_experience = fields.Text(string='Lý lịch công việc')
    education = fields.Text(string='Học vấn')
    family_info = fields.Text(string='Thông tin gia đình')
    skills = fields.Text(string='Kỹ năng và sở thích')
    medical_records = fields.Text(string='Thông tin khám chữa bệnh')
    attachments = fields.Many2many('ir.attachment', string='Hồ sơ đính kèm')
class MyEmployee(models.Model):
    _name = 'my_employee.myemployee'
    _description = 'Thông tin công việc của nhân viên'
    
    name = fields.Many2one('my_employee.employee',string='Tên nhân viên')
    job_position = fields.Char(string='Vị trí công việc')
    job_title = fields.Char(string='Chức danh')
    job_level = fields.Char(string='Cấp bậc')
    department = fields.Char(string='Phòng ban')
    workplace = fields.Char(string='Nơi làm việc')
    employee_group = fields.Char(string='Nhóm nhân viên')
    manager = fields.Char( string='Người quản lý')
    work_contact_phone = fields.Char(string='Điện thoại liên hệ công việc')
    work_contact_email = fields.Char(string='Email công ty')
    hire_date = fields.Date(string='Ngày vào công ty')
    birthday = fields.Date(string='Sinh nhật')
class IncomeInformation(models.Model):
    _name = 'income.information'
    _description = 'Thông tin liên quan thu nhập'

    contract_id = fields.Many2one('hr.contract', string='Hợp đồng lao động')
    contract_appendix_ids = fields.One2many('contract.appendix', 'income_information_id', string='Phụ lục hợp đồng')
    salary_adjustment_ids = fields.One2many('salary.adjustment', 'income_information_id', string='Phụ lục điều chỉnh lương')


class ContractAppendix(models.Model):
    _name = 'contract.appendix'
    _description = 'Phụ lục hợp đồng'

    name = fields.Char(string='Tên phụ lục')
    income_information_id = fields.Many2one('income.information', string='Thông tin liên quan thu nhập')


class SalaryAdjustment(models.Model):
    _name = 'salary.adjustment'
    _description = 'Phụ lục điều chỉnh lương'

    name = fields.Char(string='Tên phụ lục')
    income_information_id = fields.Many2one('income.information', string='Thông tin liên quan thu nhập')    
    
    