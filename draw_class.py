import pygame

class Shape:
    def __init__(self, screen, color):
        self.screen = screen
        self.color  = color


class Rectangle(Shape):
    
    def __init__(self, screen, color, x_pos, y_pos, width, height):
        super().__init__(screen, color)
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.width = width
        self.height = height

    def draw(self):
        """
        pygame.draw.rect(
            surface/screen, 
            color,
            pygame.Rect(x_pos, y_pos, width, height),
            fill = 0, line thickness > 0,

            )
        """
        pygame.draw.rect(
            self.screen, 
            self.color, 
            pygame.Rect(
                self.x_pos,
                self.y_pos,
                self.width,
                self.height
                )
            )
        pass
    
    pass