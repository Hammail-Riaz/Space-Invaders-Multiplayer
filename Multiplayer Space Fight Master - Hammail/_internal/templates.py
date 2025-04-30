"""
Template classes for Blue and yellow Red Space Spaceships.
Credits : Hammail...
"""

#importing requried module
import pygame as pg
import os


class Red_Spaceship:
    """Red Spaceship template..."""
        
    def __init__(self,screen_height, screen_width, spaceship_width, spaceship_height,rocket_width , rocket_height, jumbo_rocket_widht, jumbo_rocket_height, spaceship_vel_val):
        """Initializes Few important variables:
            screen_width , screen_height, spaceship_width,
            spaceship_height, spaceship_rect, rocket_vel, rocket_width, rocket_height,
            spaceship_vel
        """
        
        self.screen_height = screen_height 
        self.screen_width =  screen_width
        self.spaceship_height = spaceship_height
        self.spaceship_width = spaceship_width
        
        self.rocket_width = rocket_width
        self.rocket_height = rocket_height
        self.rocket_vel = 20
        
        self.jumbo_rocket_width = jumbo_rocket_widht
        self.jumbo_rocket_height = jumbo_rocket_height
        
        self.spaceship_img = pg.transform.rotate(pg.transform.scale(pg.image.load(os.path.join("assets", "game_items", "red_spaceship.png")), (spaceship_width, spaceship_height) ).convert(), 90)
        self.spaceship_img.set_colorkey((255,255,255))
        
        self.spaceship_rect = pg.Rect(self.screen_width - self.spaceship_width , self.screen_height // 2 - self.spaceship_height, self.spaceship_height, self.spaceship_width)
        
        self.spaceship_vel = spaceship_vel_val
        
        self.jumbo_rocket_img = pg.transform.rotate(pg.transform.scale(pg.image.load(os.path.join("assets", "game_items", "jumbo_red_rocket.png")), (self.jumbo_rocket_width, self.jumbo_rocket_height) ).convert(), 90)
        self.jumbo_rocket_img.set_colorkey((255,255,255))
        
        self.red_rocket_img = pg.transform.rotate(pg.transform.scale(pg.image.load(os.path.join("assets", "game_items", "red_rocket.png")), (self.rocket_width ,self.rocket_height) ).convert(), 90)
        self.red_rocket_img.set_colorkey((255,255,255))
        
        
   
    def generate_upperwing_rocket(self):
        """Generate the upper wing firing rocket for the red spaceship and return it."""
        rocket_rect = pg.Rect(self.spaceship_rect.x + (self.spaceship_img.get_width() // 2), self.spaceship_rect.y + 7, self.rocket_height, self.rocket_width)
        return rocket_rect
        
    def generate_lowerwing_rocket(self):
        """Generate the lower wing firing rocket for the red spaceship and return it."""
        rocket_rect = pg.Rect(self.spaceship_rect.x + (self.spaceship_img.get_width() // 2), self.spaceship_rect.y + (self.spaceship_img.get_width()) - 7, self.rocket_height, self.rocket_width)
        return  rocket_rect
       
    def generate_jumbo_rocket(self):
        """Generate the Jumbo firing rocket for the red spaceship and return it."""
        rocket_rect = pg.Rect(self.spaceship_rect.x, self.spaceship_rect.y + (self.spaceship_img.get_width() // 2), self.rocket_height, self.rocket_width)
        return  rocket_rect
    
    def draw_jumbo_rocket(self,surface,  rockets):
        """Draw the Jumbo rockets of red spaceship on window."""        
        for rocket in rockets:
            surface.blit(self.jumbo_rocket_img, (rocket.x, rocket.y))
    
    def move_jumbo_rocket(self, rockets):
        """Move the jumbo rockets of red spaceship toward enemy."""
        for rocket in rockets:
            rocket.x -= self.rocket_vel
        
    
    def remove_jumbo_rocket(self, rockets):
        """Remove jumbo red spaceship rockets if they are outside the screen."""
        for rocket in rockets[:]:
            if rocket.x <= 0:
                rockets.remove(rocket)
        
    
    def draw_rockets(self, surface, rockets):
        """Draw the rockets of red spaceship on window."""        
        for rocket in rockets:
            surface.blit(self.red_rocket_img, (rocket.x, rocket.y))
           
    def move_rockets(self, rockets):
        """Move the rockets of red spaceship toward enemy."""
        for rocket in rockets:
            rocket.x -= self.rocket_vel
            
    def remove_rockets(self, rockets):
        """Remove red spaceship rockets if they are outside the screen."""
        for rocket in rockets[:]:
            if rocket.x <= 0:
                rockets.remove(rocket)
                
    def check_rocket_collision(self, blue_rockets, hit_sfx, health):
        """Check collision for the rocket of enemy (blue spaceship) with the red spaceship"""
        for rocket in blue_rockets[:]:
            if rocket.colliderect(self.spaceship_rect):
                blue_rockets.remove(rocket)
                
                hit_sfx.play()
               
                health -= 1
                
                
        return health
    
    def jumbo_check_rocket_collision(self, blue_rockets, hit_sfx, health):
        """Check collision for the jumbo rocket of enemy (blue spaceship) with the red spaceship"""
        for rocket in blue_rockets[:]:
            if rocket.colliderect(self.spaceship_rect):
                blue_rockets.remove(rocket)

                hit_sfx.play()
                health -= 5
                
                
        return health
    
    def draw_spaceship(self, surface):
        """Draw the red spaceship on window."""
        surface.blit(self.spaceship_img, (self.spaceship_rect.x,self.spaceship_rect.y))
        
    def spaceship_movement_control(self, key_press):
        """Check for the Movement of red spaceship.
            *Controls:
                ->Up arrow key : Up movement
                ->Down arrow key : Down movement
                ->Left arrow key : Left movement
                ->Right arrow key : Right movement
                
            *Additional :
                ->Spaceship can only move in Specified area. (half of screen)
        """
        #Right movement
        if key_press[pg.K_RIGHT] and self.spaceship_rect.x < self.screen_width - self.spaceship_width + 15:
            self.spaceship_rect.x += self.spaceship_vel
            
        #Left movement            
        if key_press[pg.K_LEFT] and self.spaceship_rect.x > self.screen_width // 2:
            self.spaceship_rect.x -= self.spaceship_vel
            
        #Up movement
        if key_press[pg.K_UP] and self.spaceship_rect.y > 0:
            self.spaceship_rect.y -= self.spaceship_vel
        
        #Down movement
        if key_press[pg.K_DOWN] and self.spaceship_rect.y + self.spaceship_vel < self.screen_height - self.spaceship_height - 15:
            self.spaceship_rect.y += self.spaceship_vel
            
            
class Blue_Spaceship:
    """Blue Spaceship template..."""
        
    def __init__(self,screen_height, screen_width, spaceship_width, spaceship_height, rocket_width , rocket_height , jumbo_rocket_width, jumbo_rocket_height, spaceship_vel_val):
        """Initializes Few important variables:
            screen_width , screen_height, spaceship_width,
            spaceship_height, spaceship_rect, rocket_vel, rocket_width, rocket_height,
            spaceship_vel
        """
        
        self.screen_height = screen_height 
        self.screen_width =  screen_width
        self.spaceship_height = spaceship_height
        self.spaceship_width = spaceship_width
        
        self.rocket_width = rocket_width
        self.rocket_height = rocket_height
        self.rocket_vel = 20
        
        self.jumbo_rocket_width = jumbo_rocket_width
        self.jumbo_rocket_height = jumbo_rocket_height
        
        self.spaceship_img = pg.transform.rotate(pg.transform.scale(pg.image.load(os.path.join("assets", "game_items", "blue_spaceship.png")), (spaceship_width, spaceship_height) ).convert(), 270)
        self.spaceship_img.set_colorkey((255,255,255))
        
        self.spaceship_rect = pg.Rect(0, self.screen_height // 2 - self.spaceship_height, self.spaceship_height, self.spaceship_width)
        
        self.spaceship_vel = spaceship_vel_val
        
        self.jumbo_blue_rocket_img = pg.transform.rotate(pg.transform.scale(pg.image.load(os.path.join("assets", "game_items", "jumbo_blue_rocket.png")), (self.jumbo_rocket_width, self.jumbo_rocket_height) ).convert(), -90)
        self.jumbo_blue_rocket_img.set_colorkey((255,255,255))
        
        self.blue_rocket_img = pg.transform.rotate(pg.transform.scale(pg.image.load(os.path.join("assets", "game_items", "blue_rocket.png")), (self.rocket_width, self.rocket_height) ).convert(), -90)
        self.blue_rocket_img.set_colorkey((255,255,255))

        
        self.rocket_width = 5
        self.rocket_height = 10
        self.rocket_vel = 20
        
    def generate_upperwing_rocket(self):
        """Generate the upper wing firing rocket for the blue spaceship and return it."""    
        rocket_rect = pg.Rect(self.spaceship_rect.x + self.spaceship_img.get_width() // 2 - 35, self.spaceship_rect.y + 10, self.rocket_height, self.rocket_width)
        return rocket_rect
    
    def generate_lowerwing_rocket(self):
        """Generate the lower wing firing rocket for the blue spaceship and return it."""    
        rocket_rect = pg.Rect(self.spaceship_rect.x,self.spaceship_rect.y + (self.spaceship_img.get_width()) - 7, self.rocket_height, self.rocket_width)
        return rocket_rect
    
    def generate_jumbo_rocket(self):
        """Generate the jumbo blue rocket of blue spaceship"""
        rocket_rect = pg.Rect(self.spaceship_rect.x + self.spaceship_img.get_width() // 2, self.spaceship_rect.y + self.spaceship_img.get_height() // 2 - 10, self.rocket_height, self.rocket_width)
        return  rocket_rect
    
    def draw_jumbo_rocket(self,surface, rockets):
        """draw the jumbo blue rocket of blue spaceship on the window."""
        for rocket in rockets:
            surface.blit(self.jumbo_blue_rocket_img, (rocket.x, rocket.y))
    
    def remove_jumbo_rocket(self, rockets):
        """remove the jumbo blue rocket for the blue spaceship if they are out of sight."""
        for rocket in rockets[:]:
            if rocket.x >= self.screen_width:
                rockets.remove(rocket)
                
    def move_jumbo_rockets(self, rockets):
        """Move the  jumbo rockets of blue spaceship toward enemy."""
        for rocket in rockets:
            rocket.x += self.rocket_vel
        
        
    def draw_rockets(self, surface, rockets):
        """Draw the rockets of blue spaceship on window."""        
        for rocket in rockets:
            surface.blit(self.blue_rocket_img, (rocket.x, rocket.y))
           
    def move_rockets(self, rockets):
        """Move the rockets of blue spaceship toward enemy."""
        for rocket in rockets:
            rocket.x += self.rocket_vel
            
    def remove_rockets(self, rockets):
        """Remove blue spaceship rockets if they are outside the screen."""
        for rocket in rockets[:]:
            if rocket.x >= self.screen_width:
                rockets.remove(rocket)
                
    def check_rocket_collision(self, red_rockets, hit_sfx, health):
        """Check collision for the rocket of enemy (red spaceship) with the blue spaceship"""
        for rocket in red_rockets[:]:
            if rocket.colliderect(self.spaceship_rect):
                
                red_rockets.remove(rocket)
                
                hit_sfx.play()
                
                health -=1
        return health
    
    def jumbo_check_rocket_collision(self, red_rockets, hit_sfx, health):
        """Check collision for the jumbo rocket of enemy (red spaceship) with the blue spaceship"""
        for rocket in red_rockets[:]:
            if rocket.colliderect(self.spaceship_rect):
                
                red_rockets.remove(rocket)

                hit_sfx.play()
                health -= 5
        return health
    
    
    def draw_spaceship(self, surface):
        """Draw the blue spaceship on window."""
        surface.blit(self.spaceship_img, (self.spaceship_rect.x,self.spaceship_rect.y))
        
    def spaceship_movement_control(self, key_press):
        """Check for the Movement of blue spaceship.
            *Controls:
                ->W key : Up movement
                ->S key : Down movement
                ->A arrow key : Left movement
                ->D arrow key : Right movement
                
            *Additional :
                ->Spaceship can only move in Specified area. (half of screen)
        """
        #Right movement
        if key_press[pg.K_d] and self.spaceship_rect.x + self.spaceship_vel < self.screen_width // 2 - self.spaceship_width + 25:
            self.spaceship_rect.x += self.spaceship_vel
            
        #Left movement            
        if key_press[pg.K_a] and self.spaceship_rect.x - self.spaceship_vel + 10 > 0:
            self.spaceship_rect.x -= self.spaceship_vel
            
        #Up movement
        if key_press[pg.K_w] and self.spaceship_rect.y > 0:
            self.spaceship_rect.y -= self.spaceship_vel
        
        #Down movement
        if key_press[pg.K_s] and self.spaceship_rect.y + self.spaceship_vel < self.screen_height - self.spaceship_height - 15:
            self.spaceship_rect.y += self.spaceship_vel
            