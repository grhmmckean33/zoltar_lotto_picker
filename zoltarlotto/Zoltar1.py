import pygame
import sys
import random
import time
import math

pygame.init()

# Generates random numbers for each ball
number_list = [12,28,29,37,45,17,24,9,34,10,43,25,35,30,42,44,49,47,31,11,33,27,40,38,23,39,]
numbers = random.sample(number_list, 6)

# Constants
WIDTH, HEIGHT = 1000, 1000
BALL_RADIUS = 30
BALL_COLORS = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 0, 255),
               (0, 255, 255)]
AUDIO_FILE = "carnival1.mp3"  # Replace with your audio file path
AUDIO_FILE_2 = "laugh.mp3" # Replace with your audio file path
AUDIO_FILE_3 = "voice.mp3"
width, height = 800, 600
center_x, center_y = width // 2.2, height // 2.2
radius = 200
num_balls = 20
ball_radius = 35
speed = 20
stop_after_frames = 90  # Number of frames before stopping

# Colors
red = (255, 0, 0)

clock = pygame.time.Clock()

numbers = random.sample(range(1, 61), 6)

# Initialize pygame window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Growing Balls")

clock = pygame.time.Clock()

# Load background image
background_image = pygame.image.load("zoltar.jpg")
background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))

# Initialize pygame mixer
pygame.mixer.init()
# Load the first background music
sound1 = pygame.mixer.Sound(AUDIO_FILE_2)
sound2 = pygame.mixer.Sound(AUDIO_FILE_3)
# Load the second background music
pygame.mixer.music.load(AUDIO_FILE)
pygame.mixer.music.play(-1)  # -1 means play indefinitely


# Ball class
class Ball_s:
    def __init__(self, angle):
        self.x = center_x
        self.y = center_y
        self.radius = ball_radius
        self.angle = angle

    def move(self):
        self.x += int(speed * math.cos(math.radians(self.angle)))
        self.y += int(speed * math.sin(math.radians(self.angle)))

        if self.x - self.radius < 10 or self.x + self.radius > WIDTH:
            self.angle = 180 - self.angle
        if self.y - self.radius < 10 or self.y + self.radius > HEIGHT:
            self.angle = -self.angle


# Create the bouncing balls
balls_s = [Ball_s(angle) for angle in range(0, 360, 60)]

# Main loop for bouncing balls
running = True
frame_count = 0
stopped = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # Play both audio files simultaneously
        sound2.play()
        sound1.play()
    screen.blit(background_image, (0, 0))

    if not stopped:
        for ball in balls_s:
            ball.move()
            pygame.draw.circle(screen, red, (ball.x, ball.y), ball.radius)
        frame_count += 1

        if frame_count >= stop_after_frames:
            stopped = True

        pygame.display.flip()
        clock.tick(30)

    if stopped:
        pygame.time.delay(1000)  # Delay for a smooth transition

        # Create the balls with numbers
        class Ball:
            def __init__(self, x, y, radius, number):
                self.x = x
                self.y = y
                self.radius = radius
                self.number = number
                self.appear_time = time.time() + number * 0.005

            def draw(self):
                current_time = time.time()
                if current_time >= self.appear_time:
                    pygame.draw.circle(screen, BALL_COLORS[self.number % 6], (self.x, self.y),
                                       self.radius)
                    font = pygame.font.Font(
        'papyrus-let-plain_1.0.ttf', 30)
                    text = font.render(str(self.number), True, (0, 0, 0))
                    text_rect = text.get_rect(center=(self.x, self.y))
                    screen.blit(text, text_rect)

                    self.radius += 40

                    if self.radius > 1:
                        self.radius = 40

        # Create Ball objects with equally spaced positions
        ball_positions = [(i + 1) * (WIDTH // 8) for i in range(6)]
        balls = [Ball(pos, HEIGHT // 1.2, BALL_RADIUS, numbers[i]) for
                 i, pos in enumerate(ball_positions)]

# Main loop for balls with numbers
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            # Play both audio files simultaneously
            sound1.play()
            # Blit the background image onto the screen
            screen.blit(background_image, (0, 0))

            all_balls_finished = all(ball.radius == 40 for ball in balls)

            for ball in balls:
                ball.draw()

            pygame.display.flip()
            clock.tick(30)

            if all_balls_finished:
                pygame.time.delay(1000)  # Delay for a smooth transition

                # Show prompt for rolling again
                font = pygame.font.Font('papyrus-let-plain_1.0.ttf', 30)
                prompt_text = font.render("Do you want to roll again? Select Y for Yes or N for No",
                    True, (255, 255, 255))
                prompt_rect = prompt_text.get_rect(center=(WIDTH // 2, HEIGHT // 1.4))
                pygame.draw.rect(screen, (0, 0, 0, 100), (0, 690, WIDTH, 50))  # Opaque layer
                screen.blit(prompt_text, prompt_rect)

                rolling_again = True
                while rolling_again:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            running = False
                            rolling_again = False
                        elif event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_y:
                                numbers = random.sample(number_list, 6)
                                balls = [Ball((i + 1) * (WIDTH // 8), HEIGHT // 1.2,
                                              BALL_RADIUS,
                                              numbers[i]) for i in range(6)]
                                rolling_again = False
                                sound2.play()
                            elif event.key == pygame.K_n:
                                running = False
                                rolling_again = False

                    pygame.display.flip()
                    clock.tick(30)
# Stop the background music when exiting
pygame.mixer.music.stop()


pygame.quit()
sys.exit()
