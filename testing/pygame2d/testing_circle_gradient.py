import pygame
import colorsys

pygame.init()

screen = pygame.display.set_mode((600,600))

#--------------------------------------
# circles positions and transparency (x,y, alpha)

circles = []

for x in range(100):
    circles.append( [100+x, x , round(x*2/1.2),x] )

#--------------------------------------

white = True # background color

#--------------------------------------

running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:

            if event.key == pygame.K_ESCAPE:
                running = False

            elif event.key == pygame.K_SPACE:
                white = not white

    #--------------------------------------

    if white:
        screen.fill((255,255,255))
    else:
        screen.fill((0,0,0))

    #--------------------------------------
    # first

    circle_img = pygame.Surface((20,20))
    pygame.draw.circle(circle_img, (255,0,0), (10,10), 10)
    circle_img.set_colorkey(0)

    for x in circles:

        circle_img.set_alpha(x[2])

        screen.blit(circle_img, (x[0],40))

    #--------------------------------------
    # second

    circle_img = pygame.Surface((20,20))

    for x in circles:

        pygame.draw.circle(circle_img, (255,255-x[2],255-x[2]), (10,10), 10)
        circle_img.set_colorkey(0)

        screen.blit(circle_img, (x[0],90))

    #--------------------------------------
    # third

    circle_img = pygame.Surface((20,20))

    for x in circles:

        pygame.draw.circle(circle_img, (255,x[2],x[2]), (10,10), 10)
        circle_img.set_colorkey(0)
        circle_img.set_alpha(x[2])

        screen.blit(circle_img, (x[0],140))

    #--------------------------------------
    # last

    circle_img = pygame.Surface((300,300))

    hsv_color=colorsys.rgb_to_hls(255,0,0)
    rgb_color=colorsys.hls_to_rgb(*hsv_color)
    print(hsv_color)
    print(rgb_color)
    #print(22+"22")
    for x in circles:
        print(255, x[2], x[2])
        hsv_color = colorsys.rgb_to_hls(255, x[2], x[2])
        hsv_color = [hsv_color[0], hsv_color[1], min(hsv_color[2] + x[1] / 900, 1)]
        rgb_color = colorsys.hls_to_rgb(*hsv_color)
        print([*hsv_color])
        print([*rgb_color])
        rgb_color=[min(round(i),255) for i in rgb_color]
        #pygame.draw.circle(circle_img, (255,10+x[2],10+x[2]), (150,100+(x[0])//2), 100-x[3])
        y=0
        while abs(y) < min([60,x[3]]):
            #print(-min(y,x[3]), min((round((y)**(2))),x[3])-2,x[3])

            pygame.draw.circle(circle_img, ([*rgb_color]), (round(150-min(y,x[3])), 100 + ((x[0]) // 1.1)-min((round((y/10)**(2))),x[3])-2), 100 - x[3])
            y+=1

        y = 0
        while abs(y) < min([20,x[3]]):
            print(-min(y,x[3]), min((round((y/9)**(2))),x[3])-2,x[3])
            pygame.draw.circle(circle_img, ([*rgb_color]), (round(150-min(y,x[3])), 100 + ((x[0]) // 1.1)-min((round((y/10)**(2))),x[3])-2), 100 - x[3])
            y-=1

        circle_img.set_colorkey(0)
        circle_img2 = pygame.transform.scale(circle_img, (50, 50))
        #circle_img.set_alpha(x[2])

        screen.blit(circle_img2, (300,300))
        #screen.blit(circle_img, (x[0],190))
    #print(22+"22")
    #--------------------------------------

    pygame.display.flip()


pygame.quit()