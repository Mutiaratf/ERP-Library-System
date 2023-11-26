from odoo import api, fields, models
from odoo.exceptions import ValidationError
import datetime
import urllib
import requests

class Book(models.Model):
  _name = 'library_system.book' 
  _description = 'Master Data Buku' 
  _rec_name = 'title_book'

  number_inventaris = fields.Char(string='No Inventaris', required= True) 
  title_book = fields.Char(string='Judul Buku', required= True) 
  author = fields.Many2one(comodel_name='library_system.author',string='Penulis', required= True) 
  tahun_terbit = fields.Char(string='Tahun Terbit', required= True) 
  publisher = fields.Many2one(comodel_name='library_system.publisher', string='Penerbit', required= True)
  isbn = fields.Char(string="ISBN", required= True)
  image = fields.Binary(string="Cover Buku")
  teacher_name = fields.Many2one(comodel_name='school_management.teacher',string='Nama Guru')
