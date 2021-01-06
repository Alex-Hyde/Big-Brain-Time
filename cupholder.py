import pygame
import button2 as b
import frame
import color as c
import pygameplus as pgp

pygame.init()


def cup_holder(but):
    pygame.cdrom.init()
    cd = pygame.cdrom.CD(0)
    cd.init()
    cd.eject()
    cd.quit()
    global run
    run = False


def close(but):
    global run
    run = False


win = pygame.display.set_mode((200, 100))
component = frame.Component(win, background_color=c.WHITE)

title = pgp.Label()
title.set_relative(component)
title.set_size(14)
title.set_text("Do you want a cup holder?")
title.layout.gravity = "centerx top"
title.layout.margin_top = 10

yes = b.Button()
yes.set_relative(component)
yes.layout.gravity = "bottom left"
yes.layout.margin_left = 5
yes.layout.margin_bottom = 10
yes.rect.w = 80
yes.rect.h = 50
yes.set_text("YES")
yes.on_release = cup_holder

no = b.Button()
no.set_relative(component)
no.layout.gravity = "bottom right"
no.layout.margin_right = 10
no.layout.margin_bottom = 10
no.rect.w = 80
no.rect.h = 50
no.set_text("NO")
no.on_release = close

run = True
while run:
    win.fill(c.WHITE)
    component.draw(win)
    pygame.display.update()
    click_bool = False
    release_bool = False
    events = pygame.event.get()

    for event in events:
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                click_bool = True
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                release_bool = True

    component.process(click_bool, release_bool, pygame.mouse.get_pos(), None)

pygame.quit()
