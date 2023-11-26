from odoo import api, fields, models
from odoo.exceptions import ValidationError
import datetime
import requests
import urllib

class Pengembalian(models.Model):
  _name = 'library_system.pengembalian' 
  _description = 'Data Pengembalian' 
  _rec_name = 'doc_pinjam'
  _inherit = ['mail.thread', 'mail.activity.mixin']

  doc_pinjam = fields.Char(string="Dokumen Pinjam")
  admin_perpus = fields.Many2one(comodel_name='res.users', string='Nama Admin', default=lambda self: self.default_admin())
  member = fields.Char("Anggota")
  book = fields.Char(string='Nama Buku') 
  tgl_pinjam = fields.Date(string="Tanggal Pinjam")
  deadline = fields.Char(string="Deadline Pengembalian")
  status_pengembalian = fields.Selection([
      ('rancangan', 'Rancangan'),
      ('selesai', 'Selesai')
  ], default="rancangan", string='Status', tracking=True)
  cover = fields.Binary(string="Cover Buku")
  ket_deadline = fields.Boolean(string="Pengembalian Sesuai Deadline", default=False)
  ket_fisik = fields.Boolean(string="Ada Kerusakan Buku", default=False)
  ket_denda = fields.Char(string="Denda", placeholder="Jika tidak ada Kosongkan")
  
  def default_admin(self):
    pengaju = self.env['res.users'].search([('user_ids.id', '=', self.env.user.id)])
    return pengaju


  def rancangan_button(self):
      self.status_pengembalian = 'rancangan'

  def selesai_button(self):
      self.status_pengembalian = 'selesai'



 