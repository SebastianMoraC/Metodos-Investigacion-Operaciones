from simplex import Simplex

if __name__ == "__main__":
    print("Solve the first solution.\n")
def levelOne():
    
    pygame.init()
    
    #Screen
    
    pygame.display.set_caption("Game")
    
    
    #Map
    img = pygame.image.load("images/worldMario.png")
    uploadMap("maps/mapGG")
    left = arrayTileSet(img)

    #Font and Text
    white = pygame.Color("#FFFFFF")
    fontOne = pygame.font.Font(None,37)
    timeAux = 1
    corner = 0

    
    
    #Player
    event = pygame.event.get()
    myPlayer = player.Xena((50,345),speed)
    players1.add(myPlayer)
    all_sprites.add(myPlayer)
    
    shot = 0
    
    while True:
        
        #Bullet
        keys = pygame.key.get_pressed()
        keys2 = pygame.key.get_focused()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        myPlayer.eventS(keys,event)
        #Colls
        colls = pygame.sprite.groupcollide(players1, bullets,False,True)
        
        for myPlayer, bullets_ in colls.items():
            myPlayer._health -= 1
            if(myPlayer._health <= 0):
                screenFinish()
        
        
        #Sprites
        if(shot == 50):
            positionX, positionY = randomPositionBullet(corner)
        
            bullet = enemy.Bullet(positionX,positionY,corner)
            all_sprites.add(bullet)
            bullets.add(bullet)
            corner += 1
            if(corner == 3):
                corner = 0
            shot = 0
        shot +=1    
        #---------------------------
        
        #---------------------------
        #Time
        timeS = pygame.time.get_ticks() //1000      #The time is miliseconds so we divide in 1000
        
        if(timeAux == timeS):
            
            timeAux += 1
        
        #Draw Map
        for i in range(MAPHEIGHT):
            for j in range(MAPWIDTH):
                numTile = MATRIZMAP[i][j]
                tileImg = left[numTile-1]
                tileImg = pygame.transform.scale(tileImg,(TILEWIDTH, TILEHEIGHT))
                screen.blit(tileImg, (j*TILEWIDTH, i*TILEHEIGHT))
        bullets.update()
       

        bullets.draw(screen)
        #screen.blit(myPlayer.clipping,(myPlayer.rectClip.x,myPlayer.rectClip.y))

        #Count
        textLifes = fontOne.render("Lifes = " + str(myPlayer._health),0,white)
        count = fontOne.render("Time left: " + str(60-timeS)+"s",0,white)    
        if (60 - timeS <= 0):
            levelTwo()
        screen.blit(textLifes,(5,5))
        screen.blit(count,(630,5)) #Show the cont in the screen
        screen.blit(myPlayer.clipping,myPlayer.rect)
        pygame.display.flip()
    t = Simplex('min', [-3, -1, -3])
    t.add_constraint([2, 1, 1], 2, "<=")
    t.add_constraint([1, 1, 3], 5, "<=")
    t.add_constraint([2, 2, 1], 6, "<=")
    t.solve()

    '''print("\n\n\nSolve the second solution.\n")
    t = Simplex("min", [-9, 12, 41])
    t.add_constraint([1, -1, -5], 17, "<=")
    t.add_constraint([1, -2, -8], -36, "<=")
    t.add_constraint([1, -2, -5], 28, "<=")
    t.solve()
    '''
    '''
    t = Simplex("min", [-3, -1, -3])
    t.add_constraint([2, 1, 1], 2, ">=")
    t.add_constraint([1, 1, 3], 5, "<=")
    t.add_constraint([2, 2, 1], 6, "=")
    t.solve()'''