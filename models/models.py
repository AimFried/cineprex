# -*- coding: utf-8 -*-
from odoo import models, fields, api, exceptions

class Villes(models.Model):
    _name = 'cineprex.villes'

    name = fields.Char(string="Nom :", required=True)
    codePostal = fields.Integer(string="Code Postal :", required=True)


class Cinemas(models.Model):
    _name = 'cineprex.cinemas'

    name = fields.Char(string="Nom :", required=True)
    adresse = fields.Char(string="Adresse :", required=True)
    telephone = fields.Char(string="Téléphone :", required=True)
    image = fields.Binary(string="Photo :")
    ville_id = fields.Many2one('cineprex.villes', ondelete='set null', string='Ville :', index=True)

class Salles(models.Model):
    _name = 'cineprex.salles'
    
    name = fields.Char(string="Nom :",required=True)
    nb_place = fields.Integer(string = "Nombre de place :",required=True)
    cinema_id = fields.Many2one('cineprex.cinemas', ondelete='set null', string='Cinéma :', index=True)
    nb_place_rest=fields.Integer(string = "Nombre de place restant :", compute="_nb_place_rest")
    seance_id = fields.One2many('cineprex.seances', 'salle_id', string="Seances :")
    

    @api.depends('nb_place', 'seance_id.place_salle_max')
    def _nb_place_rest(self):
        for r in self:
            r.nb_place_rest = r.nb_place - r.seance_id.place_salle_max
 
    @api.constrains('nb_place')
    def _verify_nb_place(self):
        for r in self:
            if r.nb_place <= 0:
                raise exceptions.ValidationError("Le Nombre de place doit être supérieur à 0")


class Films(models.Model):
    _name = 'cineprex.films'

    name = fields.Char(string="Titre :",required=True)
    realisateur = fields.Char(string="Réalisateur :",required=True)   
    date_sortie = fields.Date(string="Date de sortie :",required=True) 
    duree = fields.Integer(string="Duree :",required=True)  
    image = fields.Binary(string="Affiche :",required=True)    
    
class Seances(models.Model):
    _name = 'cineprex.seances'

    start_date = fields.Date(string="Date de debut",default=fields.Date.today, required=True)
    duree_film = fields.Float(string="Durée du film :", compute="_set_duree_film", readonly=True)
    place_salle_max = fields.Integer(string = "Nombre de place", compute="_set_nb_place", readonly=True)
    
    affiche = fields.Binary(string="Affiche :",compute="_set_image_film", readonly=True) 

    salle_id = fields.Many2one('cineprex.salles', ondelete='cascade', string='Salle', index=True, required=True)
    film_id = fields.Many2one('cineprex.films', ondelete='cascade', string='Film', index=True, required=True)
    # event_id = fields.Many2one('event.event', string="Événement", readonly=True)
    
    @api.depends('duree_film', 'film_id.image')
    def _set_image_film(self):
        self.affiche= self.film_id.image
    
    @api.depends('duree_film', 'film_id.duree')
    def _set_duree_film(self):
        self.duree_film = self.film_id.duree
        
    @api.depends('place_salle_max', 'salle_id.nb_place')
    def _set_nb_place(self):
        self.place_salle_max = self.salle_id.nb_place

    # @api.constrains('seats', 'duration')
    # def _verify_seats(self):
    #     for r in self:
    #         if r.salle_id.nb_place - r.seats < 0 or r.seats <= 0:
    #             raise exceptions.ValidationError("=>Verifier la disponibilite des places!\n=>Le Nombre de place a reserve doit etre superieur a 0")
    #         if r.duration == 0:
    #             raise exceptions.ValidationError("La Duree doit etre sup a 0")

# class Seances(models.Model):
#     _name = 'cineprex.seances'

#     start_date = fields.Date(string="Date de debut",default=fields.Date.today)
#     duration = fields.Float(string="Duration in hours", help="Duree en heure (1,5 = 1h et 30 minutes)",required=True)
#     seats = fields.Integer(string = "Nombre de place reservees", required=True)

#     salle_id = fields.Many2one('cineprex.salles', ondelete='set null', string='Salle', index=True)
#     film_id = fields.Many2one('cineprex.films', ondelete='set null', string='Film', index=True)
#     # event_id = fields.Many2one('event.event', string="Événement", readonly=True)

#     @api.constrains('seats', 'duration')
#     def _verify_seats(self):
#         for r in self:
#             if r.salle_id.nb_place - r.seats < 0 or r.seats <= 0:
#                 raise exceptions.ValidationError("=>Verifier la disponibilite des places!\n=>Le Nombre de place a reserve doit etre superieur a 0")
#             if r.duration == 0:
#                 raise exceptions.ValidationError("La Duree doit etre sup a 0")
            

    
            

    # @api.model
    # def create(self, values):
    #     try:
    #         seance = super(Seance, self).create(values)

    #         # Créez un événement du module Événement d'Odoo
    #         event = self.env['event.event'].create({
    #             'name': 'test',
    #             'date_begin': seance.start_date,
    #             'date_end': seance.start_date,
    #             'seats_limited': False,
    #             'date_tz': 'Europe/Paris'
    #             # Ajoutez d'autres champs de l'événement ici en fonction de vos besoins
    #         })
    #         event_id = event.id
    
            

    #         return seance
    #     except Exception as e:
    #         raise exceptions.ValidationError(f"Erreur lors de la création de l'événement : {e}")
                
