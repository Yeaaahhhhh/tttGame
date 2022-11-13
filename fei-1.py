import pygame,random

# User-defined functions

def main():
    pygame.init()
    pygame.display.set_mode((500, 400))
    pygame.display.set_caption('Alien Invasion')
    w_surface = pygame.display.get_surface()
    game = Game(w_surface)
    game.play()
    pygame.quit()


# User-defined classes

class Game:
    # An object in this class represents a complete game.

    def __init__(self, surface):
    # Initialize a Game.
    # - self is the Game to initialize
    # - surface is the display window surface object
        self.surface = surface
        self.FPS = 60
        self.game_Clock = pygame.time.Clock()
        self.bg_color = pygame.Color('black')
        self.close_clicked = False
        self.continue_game = True
        self.alien_list = []
        self.max_count = 10
        self.score = 0
        self.border_colors = ['red','blue','green']
        self.speed = [2,4,6]
        Alien.set_surface(surface)
        self.create_alien_list()


    def create_alien_list(self):
    # - self is the Game
    # Creates Alien objects and appends them to the list of Alien objects
        for count in range(0,self.max_count):
            color_string = random.choice(self.border_colors)
            color = pygame.Color(color_string)
            speed = random.choice(self.speed)
            alien = Alien(color,speed)
            self.alien_list.append(alien)


    def play(self):
    # Play the game until the player presses the close box.
    # - self is the Game that should be continued or not.
        while not self.close_clicked: # until player clicks close box
            # play frame
            self.handle_event()
            self.draw()
            if self.continue_game:
                self.update()
            self.decide_continue()
            self.game_Clock.tick(self.FPS) # run at most with FPS Frames Per Second



    def handle_event(self):
        # Handle each user event by changing the game state appropriately.
        # - self is the Game whose events will be handled.
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    self.close_clicked = True
                elif event.type == pygame.MOUSEBUTTONUP and self.continue_game:
                    self.handle_mouse_up(event)
    

    def handle_mouse_up(self,event):
    # Removes object from list if Alien object is selected
        for alien in self.alien_list:
            if alien.select(event.pos):
                self.alien_list.remove(alien)
            self.score = self.score + 1


    def draw(self):
    # Draw all Game objects.
    # - self is the Game to draw
        self.surface.fill(self.bg_color) # clear the display surface first
        for alien in self.alien_list:
            alien.draw()
        self.draw_score()
        if self.continue_game == False:
            self.draw_mission_over()
        pygame.display.update() # make the updated surface appear on the display


    def draw_mission_over(self):
    # draws Mission Over at bottom left corner of the window
        game_over_string = 'Mission Over'
        game_over_font = pygame.font.SysFont('', 70)
        game_over_image = game_over_font.render(game_over_string, True, pygame.Color('red'), self.bg_color)
        height = self.surface.get_height() - game_over_image.get_height()
        game_over_top_left_corner = (0, height)
        self.surface.blit(game_over_image, game_over_top_left_corner)


    def draw_score(self):
        # draws the score at the top left corner of the window
        score_string = 'Score:' + str(self.score)
        score_font = pygame.font.SysFont('', 50)
        score_image = score_font.render(score_string, True, pygame.Color('white'), self.bg_color)
        score_top_left_corner = (0, 0)
        self.surface.blit(score_image, score_top_left_corner)


    def update(self):
    # Update the game objects.
    # - self is the Game to update
        for alien in self.alien_list:
            alien.move()
            if alien.cross_center():
                alien.change_color()
            alien.reduce_speed()
            if alien.collide_window_edge():
                self.alien_list.remove(alien)


    def decide_continue(self):
        # Check and remember if the game should continue
        # - self is the Game to check
            if len(self.alien_list) == 0:
                self.continue_game = False


class Alien:
    #an object of this class is an Alien ship
    #Class Attributes
    width = 70
    height = 30
    surface = None
    low_power_mode_color = 'orange'
    border_size = 10

    @classmethod
    def set_surface(cls, surface):
        cls.surface = surface

    def __init__(self,color,speed):
        # initialize the alien ship with color,speed and surface
        self.color = color
        self.speed = speed
        x = random.randint(0,Alien.surface.get_width()-Alien.width)
        y = 0
        self.rect = pygame.Rect(x,y,Alien.width,Alien.height)

    def draw(self):
    # draws an alien ship
    # -self is the Alien ship
        pygame.draw.ellipse(Alien.surface,self.color,self.rect,Alien.border_size)

    def move(self):
    #moves the alien ship in the vertical direction using its speed
    # -self is the Alien ship
        self.rect.move_ip(0,self.speed)

    def collide_window_edge(self):
    # Return True if alien ship collides with bottom edge of window
    # False otherwise
    # -self is the Alien ship
        return self.rect.bottom > Alien.surface.get_height()

    def select(self,position):
        # Returns True if position collides alien ship
        # False otherwise
        # -self is the Alien ship
        # -position is the (x,y) location of the click
        return self.rect.collidepoint(position)

    def change_color(self):
        # change color to orange
        # -self is the Alien ship
        self.color = pygame.Color(Alien.low_power_mode_color)

    def cross_center(self):
        # has the ship crossed the center of the window?
        # - self is the Alien ship
        return self.rect.center[1] > Alien.surface.get_height()//2

    def reduce_speed(self):
        # reduces the speed by half but speed never falls below 1
        # -self is the Alien ship
        if self.speed <= 1:
            self.speed = 1
        else:
            self.speed = self.speed//2
    

main()

