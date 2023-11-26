from odoo import api, models, fields

class Author(models.Model):
  _name = 'library_system.author' 
  _description = 'Master Data Penulis' 
  _rec_name = 'author_name'

  author_id = fields.Char(string='ID Penulis', readonly= True) 
  author_name = fields.Char(string='Nama Penulis', required= True) 