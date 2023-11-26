# Mandatory
from odoo import api, models, fields

class Publisher(models.Model):
  _name = 'library_system.publisher' 
  _description = 'Master Data Penerbit' 
  _rec_name = 'publisher_name'

  publisher_id = fields.Char(string='Penerbit ID', readonly= True) 
  publisher_name = fields.Char(string='Nama Penerbit', required= True) 