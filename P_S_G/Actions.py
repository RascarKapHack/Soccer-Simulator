#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 11:02:09 2019

@author: 3535014
"""
import math
from .Tools import *
from soccersimulator import Strategy, SoccerAction, Vector2D, SoccerTeam, Simulation, show_simu
from soccersimulator import PLAYER_RADIUS, BALL_RADIUS, GAME_HEIGHT, GAME_WIDTH, GAME_GOAL_HEIGHT


class Move(object):
    def __init__(self, superstate):
        self.superstate = superstate
    def move(self, acceleration=None):
        return SoccerAction(acceleration = acceleration)
    
    def aller_vers(self, Vecteur):
        if((Vecteur - self.superstate.player).norm < PLAYER_RADIUS):
            return None
        return (Vecteur - self.superstate.player).normalize()*1000

    @property
    def aller_vers_ballon(self):
        return self.aller_vers(self.superstate.ball)
    
    @property
    def aller_vers_anticiper_ballon(self):
        return (self.aller_vers(self.superstate.state.ball.position + 5*self.superstate.state.ball.vitesse))
    
    @property
    def aller_vers_but_allie(self):
        return self.aller_vers(self.superstate.but_allie)
    @property
    def aller_vers_but_ennemi(self):
        return self.aller_vers(self.superstate.but_ennemi).normalize()*1000
    @property
    def allier_plus_proche_du_ballon_y_va(self):
        return self.aller_vers_anticiper_ballon
    """
    def __getattr__(self, name):
        return getattr(self.MyState, name)
    """
    
class Shoot(object):
    def __init__(self, superstate):
        self.superstate = superstate
        
    @property
    def tire_au_but_si_peut_tirer(self):
        """Tire uniquement si il est à coté du ballon"""
        vecteur_shoot = None
        if((self.superstate.player - self.superstate.ball).norm < PLAYER_RADIUS + BALL_RADIUS):
                vecteur_shoot = ((self.superstate.but-self.superstate.ball).normalize())
        return vecteur_shoot
    
    @property
    def tire_au_but_si_peut_tirer_violent(self):
        """Tire fort uniquement si il est a côté du ballon"""
        vecteur_shoot = None
        if((self.superstate.player - self.superstate.ball).norm < PLAYER_RADIUS + BALL_RADIUS):
                vecteur_shoot = ((self.superstate.but-self.superstate.ball).normalize())*1000
        return vecteur_shoot
    
    @property
    def passe_joueur_allier_forte(self):
        """Tire fort uniquement si il est a côté du ballon a son allier"""
        vecteur_shoot = None
        if((self.superstate.player - self.superstate.ball).norm < PLAYER_RADIUS + BALL_RADIUS):
                vecteur_shoot = ((self.superstate.position_joueur_allier_le_plus_proche-self.superstate.ball).normalize())*100
        return vecteur_shoot
    
    @property
    def passe_joueur_allier_faible(self):
        """Tire fort uniquement si il est a côté du ballon a son allier"""
        vecteur_shoot = None
        if((self.superstate.player - self.superstate.ball).norm < PLAYER_RADIUS + BALL_RADIUS):
                vecteur_shoot = ((self.superstate.position_joueur_allier_le_plus_proche-self.superstate.ball).normalize())
        return vecteur_shoot
    """
    def __getattr__(self, name):
        return getattr(self.MyState, name)
    """
    @property
    def degagement(self):
        vecteur_shoot = None
        if ((self.superstate.angle_de_degagement(self.superstate.but_ennemi-self.superstate.player,self.superstate.but_ennemi-self.superstate.joueur_ennemi_le_plus_proche) < 1.0) and (self.superstate.angle_de_degagement(self.superstate.but_ennemi-self.superstate.player,self.superstate.but_ennemi-self.superstate.joueur_ennemi_le_plus_proche) > -1.0)):
            if((self.superstate.player - self.superstate.ball).norm < PLAYER_RADIUS + BALL_RADIUS):
                vecteur_shoot = Vector2D(self.superstate.joueur_ennemi_le_plus_proche.x, self.superstate.joueur_ennemi_le_plus_proche.y+10)
        else:
            vecteur_shoot = self.tire_au_but_si_peut_tirer
        return vecteur_shoot
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    