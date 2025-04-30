"""Credits : Hammail"""
#Importing required modules
import pygame as pg
from templates import Red_Spaceship, Blue_Spaceship
import time
import os

pg.init()
pg.mixer.init()
pg.font.init()

#Game specific Variable and constants
SCREEN_WIDTH, SCREEN_HEIGHT = 1000 , 800
SPACESHIP_HEIGHT, SPACESHIP_WIDTH = 80, 100
ROCKET_HEIGHT, ROCKET_WIDTH = 22, 10
JUMBO_ROCKET_WIDTH, JUMBO_ROCKET_HEIGHT = ROCKET_WIDTH, ROCKET_HEIGHT + 10
FPS = 60

WHITE = (255,255,255) 
CLOCK = pg.time.Clock()
FONT = pg.font.SysFont(None, 45)
WINNER_FONT = pg.font.SysFont("impact", 70)

#Game window settings
window = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pg.display.set_caption("Space Fight - Hammail")
pg.display.set_icon(pg.image.load(os.path.join("assets", "game_items", "icon.png")))


#Assets loading and paths
bg_img = pg.transform.scale(pg.image.load(os.path.join("assets", "game_items", "space.jpg")), (SCREEN_WIDTH, SCREEN_HEIGHT))

game_controls = pg.transform.scale(pg.image.load(os.path.join("assets", "game_items", "game_controls.png")), (SCREEN_WIDTH, SCREEN_HEIGHT))

background_sfx = pg.mixer.Sound(os.path.join("assets", "game_sounds", "background.wav"))

winning_sfx = pg.mixer.Sound(os.path.join("assets", "game_sounds", "winning_effect.mp3"))

hit_sfx = pg.mixer.Sound(os.path.join("assets", "game_sounds", "jumbo_hit.wav"))

jumbo_rocket_fire_sfx = pg.mixer.Sound(os.path.join("assets", "game_sounds", "rocket fire.wav"))

rocket_fire_red_sfx = pg.mixer.Sound(os.path.join("assets", "game_sounds", "red_rocket_fire.wav"))

rocket_fire_blue_sfx = pg.mixer.Sound(os.path.join("assets", "game_sounds", "blue_rocket_fire.wav"))

jumbo_hit_sfx = pg.mixer.Sound(os.path.join("assets", "game_sounds", "rocket_hit.wav"))


def add_timer(elasped_time):
    """draw the timer on the game window."""
    text = FONT.render(f"Time : {elasped_time}s", 1 , "white")
    window.blit(text, ( 10 ,SCREEN_HEIGHT - 40))

def add_blue_health(blue_health):
    """draw the health of blue spaceship on the game window."""
    text = FONT.render(f"Health : {blue_health}", 1 , " sky blue")
    window.blit(text, ( 10 , 10))
    

def add_red_health(red_health):
    """draw the health of the red spaceship on the game window."""
    text = FONT.render(f"Health : {red_health}", 1 , "red")
    window.blit(text, ( SCREEN_WIDTH - text.get_width() - 10,10))
    
    
def draw_winner(winner):
    """
    Add the winning text on the window.
    Additional*
    -> add the text in appropriate color if red wins winner text will be red in color
    else in the blue color

    """
    text = WINNER_FONT.render(f"The Winner is {winner}", 1 , f"{'sky blue' if winner.lower() == 'blue' else 'red'} ")
    window.blit(text, (SCREEN_WIDTH // 2 - text.get_width() // 2,  SCREEN_HEIGHT // 2 - text.get_height()))

def show_controls_screen():
    showing = True
    while showing:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                raise SystemExit  # Correct way to quit everything cleanly

            if event.type == pg.KEYDOWN:
                showing = False

        if not pg.display.get_init():  # If display is quit externally, break safely
            return

        window.blit(game_controls, (0, 0))
        pg.display.update()


def main():
  
    """Main game logic."""
    try:
        show_controls_screen()
    except SystemExit:
        return False  # In case window is closed during controls screen
    background_sfx.play(1)
    background_sfx.set_volume(0.4)  # 50% volume
    
    red_spaceship = Red_Spaceship(SCREEN_HEIGHT, SCREEN_WIDTH, SPACESHIP_WIDTH, SPACESHIP_HEIGHT,ROCKET_WIDTH, ROCKET_HEIGHT ,JUMBO_ROCKET_WIDTH , JUMBO_ROCKET_HEIGHT, 10)
    blue_spaceship = Blue_Spaceship(SCREEN_HEIGHT, SCREEN_WIDTH, SPACESHIP_WIDTH, SPACESHIP_HEIGHT, ROCKET_WIDTH, ROCKET_HEIGHT ,JUMBO_ROCKET_WIDTH , JUMBO_ROCKET_HEIGHT, 10)
    
    red_rockets = []
    blue_rockets = []
    red_jumbo_rockets = []
    blue_jumbo_rockets = []

    red_health = 20
    blue_health = 20
    
    run = True
    start_time = time.time()
    elasped_time = 0
    
    #Main game loop
    while run:
        
        elasped_time = round( (time.time() - start_time) , 1)
        
        #Setting FPS of the game
        CLOCK.tick(FPS)
                
        #Event Hander of game
        for event in pg.event.get():
        
            
            #Handling the quit event
            if event.type == pg.QUIT:
                run = False
                
            #Handling the rocket fire
            if event.type == pg.KEYDOWN:
                
                #Handling the rocket fire event of red spaceship
                if event.key == pg.K_RCTRL and len(red_rockets) < 4:
                    # pg.mixer.music.load(rocket_fire_red_sfx)
                    rocket_fire_red_sfx.play()
                    
                    rocket = red_spaceship.generate_lowerwing_rocket()
                    red_rockets.append(rocket)
                    
                if event.key == pg.K_RSHIFT and len(red_rockets) < 4:
                    # pg.mixer.music.load(rocket_fire_red_sfx)
                    rocket_fire_red_sfx.play()
                    
                    rocket = red_spaceship.generate_upperwing_rocket()
                    red_rockets.append(rocket)
                    
                if event.key == pg.K_RALT and len(red_jumbo_rockets) == 0:
                    # pg.mixer.music.load(jumbo_rocket_fire_sfx)
                    jumbo_rocket_fire_sfx.play()
                    
                    rocket = red_spaceship.generate_jumbo_rocket()
                    red_jumbo_rockets.append(rocket)
                    
                #Handling the rocket fire event of blue spaceship
                if event.key == pg.K_LCTRL and len(blue_rockets) < 4:
                    # pg.mixer.music.load(rocket_fire_blue_sfx)
                    rocket_fire_blue_sfx.play()
                    
                    
                    rocket = blue_spaceship.generate_lowerwing_rocket()
                    blue_rockets.append(rocket)
                    
                if event.key == pg.K_LSHIFT and len(blue_rockets) < 4:
                    # pg.mixer.music.load(rocket_fire_blue_sfx)
                    rocket_fire_blue_sfx.play()
                    
                    
                    rocket = blue_spaceship.generate_upperwing_rocket()
                    blue_rockets.append(rocket)
                    
                if event.key == pg.K_LALT and len(blue_jumbo_rockets) == 0:
                    # pg.mixer.music.load(jumbo_rocket_fire_sfx)
                    jumbo_rocket_fire_sfx.play()
                    
                    
                    rocket = blue_spaceship.generate_jumbo_rocket()
                    blue_jumbo_rockets.append(rocket)

        #Drawing the Background
        window.fill(WHITE)
        window.blit(bg_img, (0,0))

        
        
        #Adding the Game timer & Players Health
        add_timer(elasped_time)
        add_blue_health(blue_health)
        add_red_health(red_health)
        
        #getting the key pressed on key_board
        key_pressed = pg.key.get_pressed()
        
        #Drawing and  movement control of red spaceship
        red_spaceship.draw_spaceship(window)
        red_spaceship.spaceship_movement_control(key_press=key_pressed)
        
        #Drawing , Moving and removing rockets of Red spaceship
        red_spaceship.move_rockets(red_rockets)
        red_spaceship.draw_rockets(window, red_rockets)
        red_spaceship.remove_rockets(red_rockets)
        
        red_spaceship.move_jumbo_rocket(red_jumbo_rockets)
        red_spaceship.draw_jumbo_rocket(window, red_jumbo_rockets)
        red_spaceship.remove_jumbo_rocket(red_jumbo_rockets)
        
        
        #Adding border (white line)
        pg.draw.line(window, WHITE, (SCREEN_WIDTH // 2, 0), (SCREEN_WIDTH // 2, SCREEN_HEIGHT), width = 2)
        
        #Drawing, and movement control of blue spaceship
        blue_spaceship.draw_spaceship(window)
        blue_spaceship.spaceship_movement_control(key_pressed)
        
        #Drawing , Moving and removing rockets of blue spaceship
        blue_spaceship.move_rockets(blue_rockets)
        blue_spaceship.draw_rockets(window, blue_rockets)
        blue_spaceship.remove_rockets(blue_rockets)
        
        blue_spaceship.move_jumbo_rockets(blue_jumbo_rockets)
        blue_spaceship.draw_jumbo_rocket(window, blue_jumbo_rockets)
        blue_spaceship.remove_jumbo_rocket(blue_jumbo_rockets)
        
        #Checking blue rockets collision with red spaceship
        red_health = red_spaceship.check_rocket_collision(blue_rockets, hit_sfx, red_health)
        blue_health = blue_spaceship.check_rocket_collision(red_rockets, hit_sfx, blue_health)
        
        red_health = red_spaceship.jumbo_check_rocket_collision(blue_jumbo_rockets, jumbo_hit_sfx, red_health)
        blue_health = blue_spaceship.jumbo_check_rocket_collision(red_jumbo_rockets, jumbo_hit_sfx, blue_health)
        #Finding the winner
        if red_health <= 0 and blue_health > 0:
            
            #Red spaceship winning condition
            draw_winner("Blue")
            # pg.mixer.music.load(winning_sfx)
            winning_sfx.play()
            pg.display.flip()
            pg.time.delay(3000)
            
            run = False
            
        if blue_health <=0 and red_health > 0:
            
            #blue spaceship winning condition
            draw_winner("Red")
            # pg.mixer.music.load(winning_sfx)
            winning_sfx.play()
            pg.display.flip()
            pg.time.delay(3000)
         
            run = False

        #Updating the whole window of game
        pg.display.flip()
        
    background_sfx.stop()
    



if __name__ == "__main__":
    
    while True:
        try:
            main()
        except SystemExit:
            break  # Exit the loop if sys.exit() or pg.quit() was called
        except pg.error:
            break  # Safeguard for display surface quit error

