import pygame
from time import time
from rope import Rope, Vec, Collider

#region pygame init
pygame.init()
size = (600, 600)
screen = pygame.display.set_mode(size)
screen.fill([255, 255, 255])
pygame.display.set_icon(screen)
clock, fps = pygame.time.Clock(), 0

delta_time = 0 ; frame_start_time = 0
#endregion

rope = Rope(
    x=size[0]/2, y=10,
    length=500, resolution=50
)

mouse_collider = Collider(0, 0)
mouse_collider.size = 50

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    frame_start_time = time()
    screen.fill(0)

    mpos = Vec(pygame.mouse.get_pos())
    mouse_collider.pos.linear_interpolate(mpos, t=delta_time)

    pygame.draw.circle(screen, [10, 10, 10], mouse_collider.pos.get(), mouse_collider.size)

    rope.update([mouse_collider], delta_time=delta_time)
    rope.draw(screen)

    pygame.display.update()
    clock.tick(fps)
    delta_time = time() - frame_start_time
    pygame.display.set_caption(f'Framerate: {int(clock.get_fps())}')






