# Mandatory
from odoo import api, models, fields

class Member(models.Model):
  _name = 'library_system.member' 
  _description = 'Master Data Anggota' 
  _rec_name = 'full_name'

  nis = fields.Char(string='NIS', required= True) 
  full_name = fields.Char(string='Nama Lengkap', required= True) 
  kelas = fields.Char(string='Kelas', required= True) 
