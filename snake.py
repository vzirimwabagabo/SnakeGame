import pygame
import random
import tkinter as tk  # Import tkinter for creating pop-up message window
from tkinter import messagebox

pygame.init()

window_x = 900
window_y = 500
window = pygame.display.set_mode((window_x, window_y))
pygame.display.set_caption("Snake Game")

snake_speed = 15
snake_block = 10
snake_position = [100, 50]
snake_body = [[100, 50], [90, 50], [80, 50]]  # Initial snake body
fruit_position = [random.randrange(1, (window_x // 10)) * 10, random.randrange(1, (window_y // 10)) * 10]

score = 0
paused = False  # Flag to track if the game is paused

def display_score(score):
    font = pygame.font.SysFont("comicsansms", 35)
    text = font.render("Score: " + str(score), True, (255, 255, 255))
    window.blit(text, [0, 0])

def draw_snake(snake_block, snake_body):
    for pos in snake_body:
        pygame.draw.rect(window, (0, 255, 0), pygame.Rect(pos[0], pos[1], snake_block, snake_block))

def draw_fruit(fruit_position):
    pygame.draw.rect(window, (255, 0, 0), pygame.Rect(fruit_position[0], fruit_position[1], snake_block, snake_block))

def show_message(title, message):
    root = tk.Tk()
    root.withdraw()  # Hide the main tkinter window
    tk.messagebox.showinfo(title, message)
    root.destroy()

running = True
direction = 'RIGHT'

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != 'DOWN':
                direction = 'UP'
            elif event.key == pygame.K_DOWN and direction != 'UP':
                direction = 'DOWN'
            elif event.key == pygame.K_LEFT and direction != 'RIGHT':
                direction = 'LEFT'
            elif event.key == pygame.K_RIGHT and direction != 'LEFT':
                direction = 'RIGHT'
            elif event.key == pygame.K_SPACE:  # Pause the game when spacebar is pressed
                paused = not paused  # Toggle the paused state

    if not paused:  # If the game is not paused
        if direction == 'UP':
            snake_position[1] -= snake_block
        elif direction == 'DOWN':
            snake_position[1] += snake_block
        elif direction == 'LEFT':
            snake_position[0] -= snake_block
        elif direction == 'RIGHT':
            snake_position[0] += snake_block

        snake_head = list(snake_position)
        snake_body.insert(0, snake_head)
        if snake_position[0] == fruit_position[0] and snake_position[1] == fruit_position[1]:
            score += 1
            fruit_position = [random.randrange(1, (window_x // 10)) * 10, random.randrange(1, (window_y // 10)) * 10]
        else:
            snake_body.pop()

    window.fill((0, 0, 0))
    draw_snake(snake_block, snake_body)
    draw_fruit(fruit_position)
    display_score(score)

    if snake_position[0] < 0 or snake_position[0] >= window_x or snake_position[1] < 0 or snake_position[1] >= window_y:
        show_message("Game Over", "You collided with the window boundaries!")  # Display pop-up message
        running = False

    pygame.display.update()
    pygame.time.Clock().tick(snake_speed)

pygame.quit()
