import pygame
import math

# Inicjalizacja Pygame
pygame.init()

# Ustawienia okna
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('FPV Lot Dronem')

# Kolory
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (34, 139, 34)  # Kolor trawy
BROWN = (139, 69, 19)   # Kolor pnia drzewa
DARK_GREEN = (0, 100, 0)  # Kolor liści

# Parametry drona
drone_radius = 30
drone_x, drone_y = screen_width // 2, screen_height // 2
drone_angle = 0
drone_height = 100
speed = 5
movement_speed = 3  # Prędkość ruchu drona

# Czas
clock = pygame.time.Clock()

# Flaga zatrzymania
stopped = False

# Funkcja do rysowania trawy
def draw_grass():
    for i in range(0, screen_width, 10):
        pygame.draw.line(screen, GREEN, (i, screen_height - 50), (i, screen_height), 2)

# Funkcja do rysowania drzew
def draw_trees():
    tree_positions = [(100, 400), (300, 350), (500, 420), (700, 380)]
    for pos in tree_positions:
        x, y = pos
        pygame.draw.rect(screen, BROWN, (x - 10, y, 20, 50))  # Pień drzewa
        pygame.draw.circle(screen, DARK_GREEN, (x, y), 40)  # Korona drzewa

# Pętla gry
running = True
while running:
    screen.fill(WHITE)

    # Rysowanie łąki
    draw_grass()
    draw_trees()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Obsługa klawiszy
    keys = pygame.key.get_pressed()

    # Zatrzymywanie drona (Tab)
    if keys[pygame.K_TAB]:
        stopped = True
    else:
        stopped = False

    if not stopped:
        # Obracanie drona (lewo/prawo)
        if keys[pygame.K_LEFT]:
            drone_angle -= 5
        if keys[pygame.K_RIGHT]:
            drone_angle += 5

        # Zmiana wysokości (góra/dół)
        if keys[pygame.K_UP]:
            drone_y -= movement_speed  # W górę (zmniejszamy Y)
        if keys[pygame.K_DOWN]:
            drone_y += movement_speed  # W dół (zwiększamy Y)

        # Ruch do przodu (kontrola przód/tył)
        move_x = movement_speed * math.cos(math.radians(drone_angle))
        move_y = movement_speed * math.sin(math.radians(drone_angle))

        # Zaktualizowanie pozycji drona
        drone_x += move_x
        drone_y += move_y

        # Sprawdzanie, czy dron nie wyszedł poza ekran
        if drone_x < 0: drone_x = 0
        if drone_x > screen_width: drone_x = screen_width
        if drone_y < 0: drone_y = 0
        if drone_y > screen_height: drone_y = screen_height

    # Rysowanie drona na ekranie
    pygame.draw.circle(screen, BLACK, (int(drone_x), int(drone_y)), drone_radius)

    # Przekształcenie w perspektywę FPV
    view_rect = pygame.Rect(drone_x - 150, drone_y - 150, 300, 300)
    pygame.draw.rect(screen, (200, 200, 200), view_rect, 2)

    # Aktualizacja ekranu
    pygame.display.flip()

    # Ustawienie liczby klatek na sekundę
    clock.tick(60)

# Zakończenie gry
pygame.quit()
