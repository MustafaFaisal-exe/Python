import pygame
import random

pygame.init()

screen = pygame.display.set_mode((1280, 650), pygame.RESIZABLE)
pygame.display.set_caption("Ludo Stars")
icon = pygame.image.load('ludo.jpeg')
pygame.display.set_icon(icon)
screen.fill("white")

# ── Center diamond ──────────────────────────────────────────────
COLORS = ["green", "yellow", "blue", "red"]
diamond_pts = [
    [[530, 250], [530, 400], [605, 325]],
    [[530, 250], [680, 250], [605, 325]],
    [[680, 400], [680, 250], [605, 325]],
    [[530, 400], [680, 400], [605, 325]],
]
for color, pts in zip(COLORS, diamond_pts):
    pygame.draw.polygon(screen, color, pts)

# ── Corner home bases (colored borders) ─────────────────────────
home_rects = [
    ("green",  [370, 90,  160, 160]),
    ("red",    [370, 400, 160, 160]),
    ("yellow", [680, 90,  160, 160]),
    ("blue",   [680, 400, 160, 160]),
]
for color, rect in home_rects:
    pygame.draw.rect(screen, color, rect, 20)

# ── Tokens: 4 per corner, 2 rows × 2 cols ───────────────────────
token_data = [
    # (fill_color, dark_color, base_x, base_y)
    ("green",  (0, 100, 0),   420, 140),
    ("red",    (139, 0, 0),   420, 450),
    ("yellow", (139, 128, 0), 730, 140),
    ("blue",   (0, 0, 139),   730, 450),
]
for fill, dark, bx, by in token_data:
    for row in range(2):
        for col in range(2):
            cx = bx + col * 60
            cy = by + row * 60
            pygame.draw.circle(screen, fill, [cx, cy], 20)
            # eye highlight
            pygame.draw.circle(screen, dark, [cx, cy - 5], 5)
            # nose triangle
            pygame.draw.polygon(screen, dark, [[cx, cy - 5], [cx - 10, cy + 10], [cx + 10, cy + 10]])

# ── Top path (yellow columns) ────────────────────────────────────
# 3 cols × 6 rows starting at (530, 90), cell 50×(160/6)
cell_h = 160 / 6
for row in range(6):
    for col in range(3):
        x = 530 + col * 50
        y = 90 + row * cell_h
        # middle column is yellow; first col row1 is grey; others are outline only
        if col == 1:
            pygame.draw.rect(screen, "yellow", [x, y, 50, cell_h])
        elif col == 0 and row == 2:
            pygame.draw.rect(screen, "grey", [x, y, 50, cell_h])
        else:
            pygame.draw.rect(screen, "black", [x, y, 50, cell_h], 2)

# ── Bottom path (red columns) ────────────────────────────────────
for row in range(6):
    for col in range(3):
        x = 530 + col * 50
        y = 400 + row * cell_h
        if col == 1:
            pygame.draw.rect(screen, "red", [x, y, 50, cell_h])
        elif col == 2 and row == 3:
            pygame.draw.rect(screen, "grey", [x, y, 50, cell_h])
        elif col == 0 and row == 4:
            pygame.draw.rect(screen, "red", [x, y, 50, cell_h])
        else:
            pygame.draw.rect(screen, "black", [x, y, 50, cell_h], 2)

# ── Left path (green rows) ───────────────────────────────────────
cell_w = 160 / 6
for row in range(3):
    for col in range(6):
        x = 370 + col * cell_w
        y = 250 + row * 50
        if row == 1 and col < 5:
            pygame.draw.rect(screen, "green", [x, y, cell_w, 50])
        elif row == 2 and col == 2:
            pygame.draw.rect(screen, "grey", [x, y, cell_w, 50])
        else:
            pygame.draw.rect(screen, "black", [x, y, cell_w, 50], 2)

# ── Right path (blue rows) ───────────────────────────────────────
for row in range(3):
    for col in range(6):
        x = 680 + col * cell_w
        y = 250 + row * 50
        if row == 1 and col < 5:
            pygame.draw.rect(screen, "blue", [x, y, cell_w, 50])
        elif row == 0 and col == 3:
            pygame.draw.rect(screen, "grey", [x, y, cell_w, 50])
        elif row == 2 and col == 4:
            pygame.draw.rect(screen, "blue", [x, y, cell_w, 50])
        else:
            pygame.draw.rect(screen, "black", [x, y, cell_w, 50], 2)

# ── Dice boxes ──────────────────────────────────────────────────
dice_positions = [(370, 30), (790, 30), (370, 570), (790, 570)]
dice_rects = [pygame.draw.rect(screen, "black", [x, y, 50, 50], 2)
              for x, y in dice_positions]
dice_green, dice_yellow, dice_red, dice_blue = dice_rects

pygame.display.flip()

# ── Game loop ────────────────────────────────────────────────────
roll_dice = pygame.USEREVENT + 2
# [is_turn, dice_x, dice_y]
turns = [[1, 385, 45], [0, 805, 45], [0, 385, 585], [0, 805, 585]]

running = True
dice_rolled = False
number = 0

while running:
    for event in pygame.event.get():
        if event.type == roll_dice:
            if not dice_rolled:
                number = random.randint(1, 6)
                dice_rolled = True
            font = pygame.font.Font('freesansbold.ttf', 32)
            text = font.render(str(number), True, "black", "white")
            for i, t in enumerate(turns):
                if t[0] == 1:
                    screen.blit(text, (t[1], t[2]))
                    t[0] = 0
                    turns[(i + 1) % len(turns)][0] = 1
                    break
        if event.type == pygame.QUIT:
            running = False

    mouse_pos = pygame.mouse.get_pos()
    if any(d.collidepoint(mouse_pos) for d in dice_rects):
        pygame.event.post(pygame.event.Event(roll_dice))

    pygame.display.update()

pygame.quit()