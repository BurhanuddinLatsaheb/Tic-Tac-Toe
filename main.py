import pygame, sys, numpy as np

screen_w = 600
screen_h = 600
pygame.init()
screen = pygame.display.set_mode((screen_w, screen_h))
icon = pygame.image.load('tic-tac-toe.png')
pygame.display.set_icon(icon)
pygame.display.set_caption("Tic - Tac - Toe")

screen.fill((92, 219, 149))



class Draw:
    def __init__(self):
        self.player=1
        self.COLS = 3
        self.ROWS = 3
        self.circle_radius = 60
        self.circle_width = 15
        self.O_color = (239, 231, 200)
        self.X_color = (50, 50, 50)
        self.linecolor=(23, 170, 156)
        self.board = np.zeros((self.ROWS, self.COLS))

    def draw_grid(self):
        pygame.draw.line(screen,self.linecolor , (0, 200), (600, 200), 10)
        pygame.draw.line(screen, self.linecolor, (0, 400), (600, 400), 10)
        pygame.draw.line(screen, self.linecolor, (200, 0), (200, 600), 10)
        pygame.draw.line(screen, self.linecolor, (400, 0), (400, 600), 10)

    def draw_X_O(self):
        for row in range(self.ROWS):
            for col in range(self.COLS):
                if self.board[row][col] == 1:
                    pygame.draw.circle(screen, self.O_color,
                                       (int(col * screen_w / 3 + screen_w / 6), int(row * screen_h / 3 + screen_h / 6)),
                                       self.circle_radius,
                                    self.circle_width)
                elif self.board[row][col] == 2:
                    pygame.draw.line(screen, self.X_color, (col * 200 + 60, row * 200 + 140),
                                     (col * 200 + 140, row * 200 + 60),
                                     15)
                    pygame.draw.line(screen, self.X_color, (col * 200 + 60, row * 200 + 60),
                                     (col * 200 + 140, row * 200 + 140),
                                     15)
    def draw_vertical_line(self,col, player):
        posX = col * 200 + 100
        if player == 1:
            color = self.O_color
        elif player == 2:
            color = self.X_color
        pygame.draw.line(screen, color, (posX, 15), (posX, screen_h - 15), 15)

    def draw_horizontal_line(self,row, player):
        posY = row * 200 + 100
        if player == 1:
            color = self.O_color
        elif player == 2:
            color = self.X_color
        pygame.draw.line(screen, color, (15, posY), (screen_w - 15, posY), 15)

    def draw_ascending_line(self,player):
        if player == 1:
            color = self.O_color
        elif player == 2:
            color = self.X_color
        pygame.draw.line(screen, color, (15, screen_h - 15), (screen_w - 15, 15), 15)

    def draw_descending_line(self,player):
        if player == 1:
            color = self.O_color
        elif player == 2:
            color = self.X_color
        pygame.draw.line(screen, color, (15, 15), (screen_w - 15, screen_h - 15), 15)



class Game:
    def __init__(self):
        self.draw=Draw()
        self.draw.draw_grid()
        self.gameover = False

    def mark_cell(self,row, col, player):
        self.draw.board[row][col] = player

    def availible_cell(self,row, col):
        if self.draw.board[row][col] == 0:
            return True
        return False

    def check_full(self):
        for row in range(self.draw.ROWS):
            for col in range(self.draw.COLS):
                if self.draw.board[row][col] == 0:
                    return False
        return True

    def check_win(self,player):
        for col in range(self.draw.COLS):
            if self.draw.board[0][col] == player and self.draw.board[1][col] == player and self.draw.board[2][col] == player:
                self.draw.draw_vertical_line(col, player)
                return True
        for row in range(self.draw.ROWS):
            if self.draw.board[row][0] == player and self.draw.board[row][1] == player and self.draw.board[row][2] == player:
                self.draw.draw_horizontal_line(row, player)
                return True
        if self.draw.board[0][0] == player and self.draw.board[1][1] == player and self.draw.board[2][2] == player:
            self.draw.draw_descending_line(player)
            return True
        if self.draw.board[0][2] == player and self.draw.board[1][1] == player and self.draw.board[2][0] == player:
            self.draw.draw_ascending_line(player)
            return True

    def restart(self):
        screen.fill((92, 219, 149))
        run = Game()
        self.draw.player = 1
        for row in range(self.draw.ROWS):
            for col in range(self.draw.COLS):
                self.draw.board[row][col] = 0






run=Game()
running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN and not run.gameover:
            col = event.pos[0] // 200
            row = event.pos[1] // 200
            if run.availible_cell(row, col) and run.draw.player == 1:
                run.mark_cell(row, col, run.draw.player)
                if run.check_win(run.draw.player):
                    run.gameover = True

                run.draw.player = 2
            if run.availible_cell(row, col) and run.draw.player == 2:
                run.mark_cell(row, col, run.draw.player)
                if run.check_win(run.draw.player):
                    run.gameover = True
                run.draw.player = 1
            run.draw.draw_X_O()
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_r:
                run.restart()
                run.gameover=False




    pygame.display.update()
