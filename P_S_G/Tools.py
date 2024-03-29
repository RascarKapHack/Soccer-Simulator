#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 28 13:43:02 2019

@author: root
"""
import random
import math
from soccersimulator import Strategy, SoccerAction, Vector2D, SoccerTeam, Simulation, show_simu
from soccersimulator import PLAYER_RADIUS, BALL_RADIUS, GAME_HEIGHT, GAME_WIDTH, GAME_GOAL_HEIGHT


class SuperState(object):
    def __init__(self, state, id_team, id_player):
        self.state = state
        self.id_team = id_team
        self.id_player = id_player
    
    """Tout ce qui est relatif a la position"""
    
    @property
    def ball(self):
        return self.state.ball.position

    @property
    def anticiper_ball_position(self):
        return self.state.ball.position + 5*self.state.ball.vitesse
    
    @property
    def ball_targetzoneA(self):
        if(self.ball.x > 40 and self.ball.x < 110 and self.ball.y <= 90 and self.ball.y > 55.8):
            return True
        return False
    
    @property
    def ball_targetzoneB(self):
        if(self.ball.x > 40 and self.ball.x < 110 and self.ball.y <= 34.2 and self.ball.y > 0):
            return True
        return False
    
    @property
    def ball_targetzoneC(self):
        if self.id_team == 1:
            if(self.ball.x > 75 and self.ball.y >= 34.2 and self.ball.y <= 55.8): #52.75 pour x
                return True
        if self.id_team == 2:
            if(self.ball.x < 75 and self.ball.y >= 34.2 and self.ball.y <= 55.8):
                return True            
        return False

    @property
    def ball_targetzoneD(self):
        if self.id_team == 1:
            if(self.ball.x > 42.75 and self.ball.x < 75 and self.ball.y > 34.2 and self.ball.y < 55.8):
                return True
        if self.id_team == 2:
            if(self.ball.x <107.25 and self.ball.x > 75 and self.ball.y > 34.2 and self.ball.y < 55.8):
                return True
        return False
    
    @property
    def ball_targetgoal(self):
        if self.id_team==1:
            if(self.ball.y > 30 and self.ball.y < 60 and self.ball.x < GAME_HEIGHT/2):
                return True
        if self.id_team==2:
            if(self.ball.y > 30 and self.ball.y < 60 and self.ball.x < GAME_HEIGHT - GAME_HEIGHT/2):
                return True
        return False
     
    @property
    def ball_target_goal_1_alerte_rouge(self):
        if self.id_team==1:
            if self.ball.x<40:
                return True
        if self.id_team==2:
            if self.ball.x>110:
                return True
        return False
    """
    @property
    def anticiper_ball_positionv2(self, distance):
    """
    
    @property
    def player(self):
        return self.state.player_state(self.id_team, self.id_player).position

    @property
    def but(self):
        if(self.id_team == 2):
            position_but = Vector2D(0,(GAME_HEIGHT/2.)) #+random.randint(-GAME_GOAL_HEIGHT/2,GAME_GOAL_HEIGHT/2)
        elif(self.id_team == 1):
            position_but = Vector2D(GAME_WIDTH,(GAME_HEIGHT/2.)) #+random.randint(-GAME_GOAL_HEIGHT/2,GAME_GOAL_HEIGHT/2)
        return position_but
    
    @property
    def je_suis_zone_goal_4_players(self):
        if self.id_team==1:
            if self.player.x < 40 and self.player.y < 65 and self.player.y > 25:
                return True
        if self.id_team==2:
            if self.player.x > 110 and self.player.y < 65 and self.player.y > 25:
                return True
        return False
    
    @property
    def gros_malaise_proche_goal_4_players(self):
        if self.id_team==1:
            if self.ball.x < 20 and self.ball.y > 65 and self.ball.y < 25:
                return True
        if self.id_team==2:
            if self.ball.x > 130 and self.ball.y > 65 and self.ball.y < 25:
                return True
        return False
    
    @property
    def position_goal_depart(self):
        if self.id_team==1:
            return Vector2D(20,45)
        if self.id_team==2:
            return Vector2D(130,45)
    
    @property
    def zone_allie(self):
        if(self.id_team==1):
            if((Vector2D(0,GAME_HEIGHT/2.) - self.state.ball.position).norm < (Vector2D(GAME_WIDTH,GAME_HEIGHT/2.) - self.state.ball.position).norm):
                return True
            else:
                return False
        if(self.id_team==2):
            if((Vector2D(0,GAME_HEIGHT/2.) - self.state.ball.position).norm > (Vector2D(GAME_WIDTH,GAME_HEIGHT/2.) - self.state.ball.position).norm):
                return True
            else:
                return False
    
    @property
    def zone_goal(self):
        if self.id_team==1:
            if(self.player.y > 30 and self.player.y < 60 and self.player.x < GAME_HEIGHT/4):
                return True
        if self.id_team==2:
            if(self.player.y > 30 and self.player.y < 60 and self.player.x < GAME_HEIGHT - GAME_HEIGHT/4):
                return True
        return False
    
    @property
    def zone_millieu_A(self):
        if(self.state.player_state(self.id_team, self.id_player).position.x > 42.75 and self.state.player_state(self.id_team, self.id_player).position.x < 107.25):
            if(self.state.player_state(self.id_team, self.id_player).position.y <= 90 and self.state.player_state(self.id_team, self.id_player).position.y > 55.8):
                return True
            return False
        return False
    
    @property
    def position_milieu_zone_Aretranche(self):
        if self.id_team == 1:
            return Vector2D(58,67.2)
        if self.id_team == 2:
            return Vector2D(92,67.2)
    
    @property
    def zone_millieu_B(self):
        if(self.state.player_state(self.id_team, self.id_player).position.x > 42.75 and self.state.player_state(self.id_team, self.id_player).position.x < 107.25):
            if(self.state.player_state(self.id_team, self.id_player).position.y <= 34.2 and self.state.player_state(self.id_team, self.id_player).position.y > 0):
                return True
            return False
        return False
    
    @property
    def position_milieu_zone_Bretranche(self):
        if self.id_team == 1:
            return Vector2D(92,22.8) #22.8
        if self.id_team == 2:
            return Vector2D(58,22.8)
    
    @property
    def zone_attaquant_C(self):
        if(self.state.player_state(self.id_team, self.id_player).position.x > 52.75):
            if(self.state.player_state(self.id_team, self.id_player).position.y >= 34.2 and self.state.player_state(self.id_team, self.id_player).position.y <= 55.8):
                return True
            return False
        return False        

    @property
    def position_attaquant_zone_C_depart(self):
        if self.id_team == 1:
            return Vector2D(118,45) #x=110/115
        if self.id_team == 2:
            return Vector2D(32,45) # avant 40/35
        
    @property
    def zone_attaque(self):
        if self.allie_2 or self.zone_ennemi:
            return True
        return False
    
    @property
    def zone_ennemi(self):
        return not self.zone_allie 
    
    @property
    def allie_1(self):
        if(self.id_team == 1):
            if(self.state.player_state(self.id_team, self.id_player).position.x < GAME_WIDTH/4):
                return True
        if(self.id_team == 2):
            if(self.state.player_state(self.id_team, self.id_player).position.x > 3*GAME_WIDTH/4):
                return True
        return False
    
    @property
    def ennemi_1(self):
        if(self.id_team == 2):
            if(self.state.player_state(self.id_team, self.id_player).position.x < GAME_WIDTH/4):
                return True
        if(self.id_team == 1):
            if(self.state.player_state(self.id_team, self.id_player).position.x > 3*GAME_WIDTH/4):
                return True
        return False 
    
    @property
    def allie_2(self):
        if(self.zone_allie and self.allie_1):
            return False
        if(self.zone_allie):
            return True
        return False
    
    @property
    def ennemi_2(self):
        if(self.zone_allie):
            return False
        if(self.zone_ennemi_1):
            return False
        return True
    @property
    def reste(self):
        if(self.id_team == 2):
            positiondef = Vector2D(140.0, self.anticiper_ball_position.y)
        else:
            positiondef = Vector2D(20.0, self.anticiper_ball_position.y)
        return positiondef
            
    @property
    def but_allie(self):
        if(self.id_team == 1):
            position_but = Vector2D(10,GAME_HEIGHT/2.)
        elif(self.id_team == 2):
            position_but = Vector2D(GAME_WIDTH-10,GAME_HEIGHT/2.)
        return position_but
    
    @property
    def but_ennemi(self):
        if(self.id_team == 2):
            position_but = Vector2D(0,GAME_HEIGHT/2.)
        elif(self.id_team == 1):
            position_but = Vector2D(GAME_WIDTH,GAME_HEIGHT/2.)
        return position_but        
    
    @property
    def distance_but_ennemi(self):
        """distance du but
            utile pour augmenter sa puissance si proche du but"""
        return (self.but-self.player).norm
            
    @property
    def liste_joueur(self):
        return self.state.players
    
    @property
    def liste_joueur_equipe_allie(self):
        """retourne liste[tuple(equipe,joueur)]"""
        L = list()
        cpt = 0
        if(self.id_team == 1):
            for i in self.liste_joueur:
                a,b = i
                if (a == 1):
                    L.append(self.liste_joueur[cpt])
                cpt+=1
        if(self.id_team == 2):
            for i in self.liste_joueur:
                a,b = i
                if(a == 2):
                    L.append(self.liste_joueur[cpt])
                cpt+=1
        return L      
    
    @property
    def liste_joueur_ennemis(self):
        """retourne liste[tuple(equipe,joueur)]"""
        L = list()
        cpt = 0
        if(self.id_team == 1):
            for i in self.liste_joueur:
                a,b = i
                if (a == 2):
                    L.append(self.liste_joueur[cpt])
                cpt+=1
        if(self.id_team == 2):
            for i in self.liste_joueur:
                a,b = i
                if(a == 1):
                    L.append(self.liste_joueur[cpt])
                cpt+=1
        return L
    
    @property
    def liste_des_positions_joueurs_equipe_allie(self):
        L = list()
        for i in self.liste_joueur_equipe_allie:
            numero_equipe,numero_joueur = i
            L.append((self.state.player_state(numero_equipe, numero_joueur)).position)
        return L       
    
    @property
    def liste_des_positions_joueurs_ennemis(self):
        L = list()
        for i in self.liste_joueur_ennemis:
            numero_equipe,numero_joueur = i
            L.append((self.state.player_state(numero_equipe, numero_joueur)).position)
        return L
    
    @property
    def joueur_ennemi_le_plus_proche(self):
        minimum = (self.player-self.liste_des_positions_joueurs_ennemis[0]).norm
        position = self.liste_des_positions_joueurs_ennemis[0]
        for i in self.liste_des_positions_joueurs_ennemis:
            if((self.player-i).norm < minimum):
                minimum = (self.player-i).norm
                position = i
        return position
    
    @property
    def position_joueur_allier_le_plus_proche(self):
        minimum = (self.player-self.liste_des_positions_joueurs_equipe_allie[0]).norm
        position = self.liste_des_positions_joueurs_equipe_allie[0]
        for i in self.liste_des_positions_joueurs_equipe_allie:
            if((self.player-i).norm > minimum):
                minimum = (self.player-i).norm
                position = i
        return position
        
    @property
    def distance_entre_joueur_allier_proche(self):
        """renvoie la distance entre self joueur et son ami le plus proche"""
        return self.player.distance(self.position_joueur_allier_le_plus_proche)
    
    @property
    def distance_entre_joueur_ennemi_proche(self):
        """renvoie la distance entre self joueur et son ami le plus proche"""
        return self.player.distance(self.joueur_ennemi_le_plus_proche)
    
    @property
    def tout_le_monde_est_sur_le_ballon(self):
        if((self.player - self.ball).norm < PLAYER_RADIUS + BALL_RADIUS):
            if((self.joueur_ennemi_le_plus_proche - self.ball).norm < 3*(PLAYER_RADIUS + BALL_RADIUS)):
                return True
        return False
    
    @property
    def impasse(self):
        if self.distance_entre_joueur_ennemi_proche<5:
            return True
        return False
    
    @property
    def allier_plus_proche_du_ballon(self):
        minimum = self.ball - self.liste_des_positions_joueurs_equipe_allie[0]
        pos = self.liste_des_positions_joueurs_equipe_allie[0]
        for position in self.liste_des_positions_joueurs_equipe_allie:
            if((self.liste_des_positions_joueurs_equipe_allie[position]).norm<minimum.norm):
                minimum = self.ball - self.liste_des_positions_joueurs_equipe_allie[position]
                pos = self.liste_des_positions_joueurs_equipe_allie[position]
        return pos

    def personne_entre_self_et_cible(self, position_cible):
        for position in self.liste_des_positions_joueurs_ennemis:
            if self.angle_de_degagement(self.player-position_cible, self.player-position) > 2:
                return True
            return False
        
    @property
    def position_joueur_ennemi_plus_proche_de_attaquant(self):
        minimum = self.position_attaquant - self.liste_des_positions_joueurs_ennemis[0]
        pos = self.liste_des_positions_joueurs_ennemis[0]
        i = 0
        for position in self.liste_des_positions_joueurs_ennemis:
            if (self.liste_des_positions_joueurs_ennemis[i]).norm < minimum.norm:
                minimum = self.position_attaquant - self.liste_des_positions_joueurs_ennemis[i]
                pos = self.liste_des_positions_joueurs_ennemis[i]
            i+=1
        return pos
        
        
    @property
    def position_joueur_ennemi_plus_proche_de_milieuA(self):
        minimum = self.position_milieu_A - self.liste_des_positions_joueurs_ennemis[0]
        pos = self.liste_des_positions_joueurs_ennemis[0]
        i = 0
        for position in self.liste_des_positions_joueurs_ennemis:
            if (self.liste_des_positions_joueurs_ennemis[i]).norm < minimum.norm:
                minimum = self.position_milieu_A - self.liste_des_positions_joueurs_ennemis[i]
                pos = self.liste_des_positions_joueurs_ennemis[i]
            i+=1
        return pos
  
    @property
    def position_joueur_ennemi_plus_proche_de_milieuB(self):
        minimum = self.position_milieu_B - self.liste_des_positions_joueurs_ennemis[0]
        pos = self.liste_des_positions_joueurs_ennemis[0]
        i = 0
        for position in self.liste_des_positions_joueurs_ennemis:
            if (self.liste_des_positions_joueurs_ennemis[i]).norm < minimum.norm:
                minimum = self.position_milieu_B - self.liste_des_positions_joueurs_ennemis[i]
                pos = self.liste_des_positions_joueurs_ennemis[i]
            i+=1
        return pos

    @property
    def position_joueur_ennemi_plus_proche_du_but_ennemi(self):
        minimum = self.but_ennemi - self.liste_des_positions_joueurs_ennemis[0]
        pos = self.liste_des_positions_joueurs_ennemis[0]
        i = 0
        for position in self.liste_des_positions_joueurs_ennemis:
            if (self.liste_des_positions_joueurs_ennemis[i]).norm < minimum.norm:
                minimum = self.but_ennemi - self.liste_des_positions_joueurs_ennemis[i]
                pos = self.liste_des_positions_joueurs_ennemis[i]
            i+=1
        return pos

        
        
    """
    @property
    def liste_opposants(self):
        return [self.state.player_state(id_team, id_player).position for (id_team,id_player) in self.state.players if id_team != self.id_team]
    
    @property
    def opposant_plus_proche(self):
        return [min(self.player.distance(player), player) for player in self.liste_opposants]
    """
    
    @property
    def g_le_ballon(self):
        """return bool"""
        if((self.player -self.ball).norm < PLAYER_RADIUS + BALL_RADIUS):
            return True
        return False
    
    @property
    def si_ballon_proche_zone_def(self):
        if((self.player - self.ball).norm <35):
            return True
        return False
    
    @property
    def champ_libre(self):
        if self.g_le_ballon:
            for i in self.liste_des_positions_joueurs_ennemis:
                if self.but_ennemi.distance(self.player) < self.but_ennemi.distance(i):
                    return True
        return False
    
    @property
    def suis_je_le_plus_proche_du_ballon(self):
        minimum = self.player-self.ball
        iterant = self.player-self.ball
        for i in self.liste_des_positions_joueurs_equipe_allie:
            for j in self.liste_des_positions_joueurs_ennemis:
                if (i-self.ball).norm < minimum.norm:
                    iterant = i
                if (j-self.ball).norm < minimum.norm:
                    iterant = j
        if minimum==iterant:
            return True
        return False
    
    """pour ma fonction degagement"""
    def angle_de_degagement(self, Vecteur_1, Vecteur_2):
        return math.acos((Vecteur_1.dot(Vecteur_2))/(Vecteur_1.norm*Vecteur_2.norm+1))*(180/math.pi)
    
   
    @property
    def si_joueur_ennemi_plus_proche_de_moi_plus_proche_ballon(self):
        if (self.ball-self.joueur_ennemi_le_plus_proche).norm > (self.ball-self.player).norm:
            return True
        return False
    
    @property
    def si_un_joueur_ennemi_a_ballon(self):
        for position in self.liste_des_positions_joueurs_ennemis:
            for pos_all in self.liste_des_positions_joueurs_equipe_allie:
                if (self.ball-position).norm < (PLAYER_RADIUS + BALL_RADIUS)*5 and (self.ball-pos_all).norm > (PLAYER_RADIUS + BALL_RADIUS)*5:
                    return True
        return False
    
    
    #############################################################################################################################
    #dans le cas ou 4 joueurs
    
    @property
    def position_goal(self):
        if self.id_team == 1:
            for idteam, numplayer in self.liste_joueur_equipe_allie:    
                return self.state.player_state(self.id_team, 0).position
        if self.id_team == 2:
            for idteam, numplayer in self.liste_joueur_ennemis:
                return self.state.player_state(self.id_team,0).position    
    @property
    def position_attaquant(self):
        if self.id_team == 1:
            for idteam, numplayer in self.liste_joueur_equipe_allie:    
                return self.state.player_state(self.id_team, 3).position
        if self.id_team == 2:
            for idteam, numplayer in self.liste_joueur_ennemis:
                return self.state.player_state(self.id_team,3).position

    @property 
    def position_milieu_A(self):
        if self.id_team == 1:
            for idteam, numplayer in self.liste_joueur_equipe_allie:
                return self.state.player_state(self.id_team, 1).position
        if self.id_team == 2:
            for idteam, numplayer in self.liste_joueur_ennemis:
                return self.state.player_state(self.id_team,1).position

    @property 
    def position_milieu_B(self):
        if self.id_team == 1:
            for idteam, numplayer in self.liste_joueur_equipe_allie:
                return self.state.player_state(self.id_team, 2).position
        if self.id_team == 2:
            for idteam, numplayer in self.liste_joueur_ennemis:
                return self.state.player_state(self.id_team,2).position
    
    
    
    ####################################################
    #nouveau test
    
    @property
    def position_moyenne_A_pourshoot(self):
        return (self.position_milieu_zone_Aretranche + self.position_milieu_A)/2
    @property
    def position_moyenne_B_pourshoot(self):
        return (self.position_milieu_zone_Bretranche + self.position_milieu_B)/2
    @property
    def position_moyenne_C_pourshoot(self):
        return (self.position_attaquant_zone_C_depart + self.position_attaquant)/2
    
    
    
    ########################################################
    def distance_pointA_droiteD(self, pointA, pointD1, pointD2):
        X0 = pointA.x
        Y0 = pointA.y
        X1 = pointD1.x
        Y1 = pointD1.y
        X2 = pointD2.x
        Y2 = pointD2.y
        return abs(((Y1-Y2)*X0+(X2-X1)*Y0+(X1*Y2-X2*Y1))/(math.sqrt(((Y1-Y2)**2)+(X2-X1)**2)))
    
    

    @property
    def passe_intelligente_goal(self):
       """A qui je donne entre defenseur, milieu, ou degagement intelligent"""
              
       if self.position_joueur_ennemi_plus_proche_de_milieuA.norm < 10 and\
           self.distance_pointA_droiteD(self.position_joueur_ennemi_plus_proche_de_milieuA,self.position_milieu_A, self.position_goal)<8 and\
           (self.but_ennemi- self.position_goal).norm > 1.05*(self.but_ennemi - self.position_milieu_A).norm:
           return self.position_milieu_A
       elif self.position_joueur_ennemi_plus_proche_de_milieuB.norm < 10 and \
           self.distance_pointA_droiteD(self.position_joueur_ennemi_plus_proche_de_milieuB,self.position_milieu_B, self.position_goal)<8 and\
           (self.but_ennemi- self.position_goal).norm > 1.05*(self.but_ennemi - self.position_milieu_B).norm:
           return self.position_milieu_B
       else:
           return self.but_ennemi
        
    @property
    def passe_intelligente_MilieuA(self):
       """A qui je donne entre defenseur, milieu, ou degagement intelligent"""
       #CAS MILIEU A
       
       if self.position_joueur_ennemi_plus_proche_de_attaquant.norm < 10 and\
           self.distance_pointA_droiteD(self.position_joueur_ennemi_plus_proche_de_attaquant,self.position_attaquant, self.position_milieu_A)<8 and\
           (self.but_ennemi- self.position_milieu_A).norm > 1.05*(self.but_ennemi - self.position_attaquant).norm:
           return self.position_attaquant
       elif self.position_joueur_ennemi_plus_proche_de_milieuB.norm < 10 and \
           self.distance_pointA_droiteD(self.position_joueur_ennemi_plus_proche_de_milieuB,self.position_milieu_B, self.position_milieu_A)<8 and\
           (self.but_ennemi- self.position_milieu_A).norm > 1.05*(self.but_ennemi - self.position_milieu_B).norm:
           return self.position_milieu_B
       else:
           return self.position_attaquant
    
    @property
    def passe_intelligente_MilieuB(self):
       #CAS MILIEU A
       
       if self.position_joueur_ennemi_plus_proche_du_but_ennemi.norm < 10 and\
           self.distance_pointA_droiteD(self.position_joueur_ennemi_plus_proche_du_but_ennemi,self.position_milieu_B, self.but_ennemi)<8 and\
           (self.but_ennemi- self.but_ennemi).norm > 1.05*(self.but_ennemi - self.position_milieu_B).norm:
           return self.but_ennemi
       elif self.position_joueur_ennemi_plus_proche_de_attaquant.norm < 10 and\
           self.distance_pointA_droiteD(self.position_joueur_ennemi_plus_proche_de_attaquant,self.position_attaquant, self.position_milieu_B)<8 and\
           (self.but_ennemi- self.position_milieu_B).norm > 1.05*(self.but_ennemi - self.position_attaquant).norm:
           return self.position_attaquant
       else:
           return self.position_attaquant
    
    
    def __getattr__(self, attr):
        return getattr(self.state, attr)
    
    
    