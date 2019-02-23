#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  7 16:14:40 2019

@author: root
"""
import math
from soccersimulator import Strategy, SoccerAction, Vector2D, SoccerTeam, Simulation, show_simu
from soccersimulator import PLAYER_RADIUS, BALL_RADIUS, GAME_HEIGHT, GAME_WIDTH
from .Tools import *
from .Actions import Shoot, Move

class Defenseur(Strategy):
        def __init__(self):
            Strategy.__init__(self, "Defenseur")
        def compute_strategy(self, state, id_team, id_player):
            s = SuperState(state, id_team, id_player)
            shoot = Shoot(s)
            move = Move(s)
            
            while s.zone_allie:
                
                if s.g_le_ballon and s.player.distance(s.but_ennemi) < s.joueur_ennemi_le_plus_proche.distance(s.but_allie):
                    return SoccerAction(move.aller_vers_anticiper_ballon, shoot.tire_au_but_si_peut_tirer)
                elif s.player.distance(s.ball) < s.joueur_ennemi_le_plus_proche.distance(s.ball):
                    return SoccerAction(move.aller_vers_anticiper_ballon, shoot.tire_au_but_si_peut_tirer)
                else:
                    return SoccerAction(move.aller_vers_anticiper_ballon, shoot.degagement)
            
            while s.zone_ennemi:
                if s.g_le_ballon and s.player.distance(s.but_ennemi) < s.joueur_ennemi_le_plus_proche.distance(s.but_allie):
                    return SoccerAction(move.aller_vers_anticiper_ballon, shoot.tire_au_but_si_peut_tirer)
                elif s.player.distance(s.ball) < s.joueur_ennemi_le_plus_proche.distance(s.ball):
                    return SoccerAction(move.aller_vers_anticiper_ballon, shoot.tire_au_but_si_peut_tirer)
                else:
                    return SoccerAction(move.aller_vers_but_allie, None)



class Strategy_Defense(Strategy):
    def __init__(self):
        Strategy.__init__(self, "Attaque")

    def compute_strategy(self, state, id_team, id_player):
        s = SuperState(state, id_team, id_player)
        shoot = Shoot(s)
        move = Move(s)
        
        if(id_player == 0):
            if(s.distance_but_ennemi < GAME_HEIGHT/3.2):
                return SoccerAction(move.aller_vers_ballon,shoot.tire_au_but_si_peut_tirer_violent)
            if s.tout_le_monde_est_sur_le_ballon:
                return SoccerAction(move.aller_vers_ballon,shoot.passe_joueur_allier_forte)
            else:
                return SoccerAction(move.aller_vers_ballon,shoot.tire_au_but_si_peut_tirer)
            
        if(id_player == 1):
            
            if s.champ_libre:
                return SoccerAction(move.aller_vers_ballon, shoot.tire_au_but_si_peut_tirer)
            
            if(s.g_le_ballon):
                    """
                    if(s.distance_entre_joueur_ennemi_proche<30 and s.distance_entre_joueur_ennemi_proche>15):
                        return SoccerAction(move.aller_vers_ballon,shoot.passe_joueur_allier_faible)"""
                    if(s.distance_but_ennemi < GAME_HEIGHT/3.2):
                        return SoccerAction(move.aller_vers_ballon,shoot.tire_au_but_si_peut_tirer_violent)
                    else:
                        if s.tout_le_monde_est_sur_le_ballon:
                            return SoccerAction(move.aller_vers_ballon,shoot.tire_au_but_si_peut_tirer_violent)
                        else:
                            return SoccerAction(move.aller_vers_ballon,shoot.tire_au_but_si_peut_tirer)
            else:
                if(s.zone_allie):
                    return SoccerAction(move.aller_vers_anticiper_ballon, shoot.tire_au_but_si_peut_tirer_violent)
                
                if(s.distance_entre_joueur_allier_proche<20):
                    if s.champ_libre:
                        return SoccerAction(move.aller_vers_ballon, shoot.tire_au_but_si_peut_tirer)
                    else:
                        return SoccerAction(move.aller_vers_ballon/2, None)
                else:
                    return SoccerAction(move.aller_vers_but_allie,None)