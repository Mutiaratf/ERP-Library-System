# Mandatory
from odoo import api, fields, models
from odoo.exceptions import ValidationError
import datetime
import urllib
import requests

class Pinjam(models.Model):
  _name = 'library_system.pinjam' 
  _description = 'Master Data Pinjam' 
  _rec_name = 'member'
  _inherit = ['mail.thread', 'mail.activity.mixin']

  id_pinjam = fields.Char(string='ID Pinjam') 
  member = fields.Many2one(comodel_name='library_system.member', string='Nama Peminjam')
  book_id = fields.Many2one(comodel_name='library_system.book', string='Nama Buku', required= True) 
  deadline = fields.Date(string='Tanggal Pengembalian', required=True)
  admin_perpus = fields.Many2one(comodel_name='res.users', string='Nama Admin', required=True, default=lambda self: self.default_admin())
  status_pinjam = fields.Selection([
      ('rancangan', 'Rancangan'),
      ('pinjam', 'Pinjam'),
      ('pengembalian', 'Pengembalian')
  ], default="rancangan", string='Status', tracking=True)
  cover = fields.Binary(string="Cover Buku")
  author = fields.Char("Penulis")

  @api.onchange('book_id')
  def _onchange_cover(self):
      self.cover = self.book_id.image
      self.author = self.book_id.author.author_name

  def default_admin(self):
    pengaju = self.env['res.users'].search([('user_ids.id', '=', self.env.user.id)])
    return pengaju

  def rancangan_button(self):
      self.status_pinjam = 'rancangan'

  def pinjam_button(self):
      self.status_pinjam = 'pinjam'

  def selesai_button(self):
    self.status_pinjam = 'pengembalian'


# Auto create ke Menu Pengembalian when click button "pengembalian"
  def write(self, vals):
    status_before_edit = self.status_pinjam
    res = super(Pinjam, self).write(vals)
    if 'status_pinjam' in vals and vals['status_pinjam'] == 'pengembalian':
        target_model = self.env['library_system.pengembalian']
        for pinjam in self.filtered(lambda p: p.status_pinjam == 'pengembalian'):
            target_model.create({
                'book': pinjam.book_id.title_book,
                'member': pinjam.member.full_name,
                'tgl_pinjam':pinjam.create_date,
                'cover': pinjam.book_id.image,
                'deadline': pinjam.deadline
                # Tambahkan field lainnya yang diperlukan di sini
            })
    return res

