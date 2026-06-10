
import pygame #Here we import pygame.

import random #Here we import random.


pygame.init() #Here we have pygame call the initalize function to set up pygames features.

screen = pygame.display.set_mode( (800, 600) ) #Here we make a screen variable and inside of it we have pygame create a screen that is 800 pixels wide, and 600 pixels tall.
pygame.display.set_caption("System Savior Araga") #Here we have pygame create a caption for when the window pops up, and the title of the window will be System Savior Araga.

clock = pygame.time.Clock() #Here we make a clock variable and inside it we have pygame create a clock that controls how fast the game loop runs by putting a number in its parameters/ parenteses when the clock calls the tick function.
font = pygame.font.SysFont(None, 36) #Here we make a font variable and inside it have pygame use the font module and call the sysfont function to make the font size for the game.
playing = True #Here we make a playing variable and have it store the condition True.

enemy_bullets = [] #Here we make an enemy_bullets variable and have it hold an empty list which will be used to hold the enemy bullet patterns.
enemy_shoot_timer = 0 # Here we make an enemy_shoot_timer variable and have it store the number zero.
enemy_shoot_rate = 100 # Here we make an enemy_shoot_rate variable and have it store the number 100, which is a slow rate the enemies will be firing.   

araga_img = pygame.image.load("Araga image.png") #Here we make a araga_img variable and inside it have pygame call the load function to load the araga image thats in the folder.
araga_img = pygame.transform.rotate(araga_img, -90) #Here we have the araga_img variable have pygame call the rotate function to rotate the araga image by -90 degrees.
araga_img = pygame.transform.scale(araga_img, (60, 120)) #Here we have the araga_img variable point to pygame and have pygame call the scale function to set the size of the Araga image, and this is the version that will be used since we set the variable to it. 

Ravager_class_scout_img = pygame.image.load("Ravager class scout ship.png") #Here we make a shredder_class_corvette_img variable and inside it have pygame call the load function to load the araga image thats in the folder.
Ravager_class_scout_img = pygame.transform.rotate(Ravager_class_scout_img, 90) #Here we have the shredder_class_corvette_img variable point to pygame and have pygame call the rotate function to rotate the araga image by 90 degrees.
Ravager_class_scout_img = pygame.transform.scale(Ravager_class_scout_img, (50, 40)) #Here we have the shredder_class_corvette_img variable point to pygame and have pygame call the scale function to set the size of the Shredder corvettes image, and this is the version that will be used since we set the variable to it. 

asteroid_img = pygame.image.load("Asteroid image.png") #Here we make an asteroid image variable and inside it have pygame use its image module and its load function to load the asteroid image.
asteroid_img = pygame.transform.scale(asteroid_img, (30, 30))

pygame.mixer.init() #Here we have pygame use its mixer module and call the init function to load all of the sound files.

shoot_sound = pygame.mixer.Sound("mixkit-game-gun-shot-1662.mp3") #Here we make a shoot_sound variable and inside it we have pygame use mixer and call the sound function to use the game gun shot sound file.
explosion_sound = pygame.mixer.Sound("mixkit-8-bit-bomb-explosion-2811.wav") #Here we make a explosion_sound variable and inside it we have pygame use mixer and call the sound function to use the 8 bit bomb explosion sound file.
enemy_shoot_sound = pygame.mixer.Sound("mixkit-short-laser-gun-shot-1670.wav") #Here we make a enemy_shoot_sound variable and inside it we have pygame use mixer and call the sound function to use the laser gun shot sound file.
gameover_sound = pygame.mixer.Sound("mixkit-explosion-in-battle-2809.wav") #Here we make a gameover_sound variable and inside it we have pygame use mixer and call the sound function to use the explosion in battle sound file.

title_stars = [] #Here we make a title_stars variable and have it store an empty list which will beused for the movement pattens of the stars.

#This for loop helps with adding 100 the stars to the empty list that the title_stars variable is holding. 
for i in range(100):
    #Here we have the title_stars variable use the append function to add this specific dictionary into the list its storing.
    title_stars.append({
    "x":random.randint(0, 800),
    "y":random.randint(0, 600),
    "speed": random.randint(1, 3),
    "size": random.randint(1,2)  
    })

title_screen = True #Here we make a title_screen variable and have it store the condition true.
 #This while loop helps with the functionality of the title screen.
while title_screen:
     for event in pygame.event.get():
         if event.type == pygame.QUIT:
             title_screen = False
             playing = False
         if event.type == pygame.KEYDOWN: #THis if statement checks to see if a specific key is pressed.
             if event.key == pygame.K_RETURN: # This if nessted inside checks to see if the player restarted the game so that the game does not go back to the title screen.
                 title_screen = False 
     screen.fill((0, 0, 0))
     #This for loop helps with crating the stars on the title screen.
     for star in title_stars:
         star["y"] += star["speed"]
         if star["y"] > 600:
             star["y"] = 0 
             star["x"] = random.randint(0, 800)
         pygame.draw.circle(screen, (255, 255, 255), (star["x"], star["y"]), star["size"])
         title_text = font.render("SYSTEM SAVIOR ARAGA", True, (255, 255, 255))
         subtitle_text = font.render("Press Enter to begin", True, (22, 226, 255))
         controls_text = font.render("left and right Arrow Keys to move, Spacebar to fire", True, (180, 180, 180))
     screen.blit(title_text, (800//2 - title_text.get_width()//2, 250))
     screen.blit(subtitle_text, (800//2 - subtitle_text.get_width()//2, 320))
     screen.blit(controls_text, (800//2 - controls_text.get_width()//2, 400))
     pygame.display.flip()
     clock.tick(60)


#This while loop will help with reseting eveery variable back to thier original values after a game over.
while playing:
 x = 400 #Here we make a x variable and have it store the number 400 which will serve as the Aragas horiziontal position on the windows grid.
 y = 400 #Here we make a y variable and have it store the number 500 which will serve as the Aragas vertical position on the windows grid.
 speed = 5 #Here we make a speed variable and have it store the number 5 which will serve as the speed the Araga will move each frame.
 health = 3 #Here we make a health variable and have it store the number 3, which will serve as the players health.
 fire_rate = 500 #Here we make a fire_rate variable and have it store the number 300.
 score = 0 #Here we make a score variable and have it store the number zero.
 bullets = [] #Here we make a bullets variable and have it store an empty list so that it will be used to add in bullet patterns.
 enemies = [] #Here we make an enemies variable and have it store an epty list which will be used to hold the spawn time of enemies aswell as the enemies bullet and movement patterns. 
 last_shot = 0 #Here we make a last_shot variable and have it store the number zero.
 enemy_spawn_timer = 0 #Here we make a enemy spawn timer variable and have it store the number 0.
 enemy_spawn_rate = 90 #Here we make a enemy_spawn_rate variable and have it store the number 90.
 running = True #Here we make a running variable and have it store the condition True.
 debris = [] #Here we make a debris variable and have it store an empyty list which will be used to hold the movement pattern of the debris in the backround.
 stars = [] #Here we make a stars variable and have it store an empty list which will be used to store the movement patterns of the stars in the backround. 
 pygame.mixer.music.load("mixkit-unforgiven-890.mp3") #Here we have pygame use the load function to load the unforgiven music file.
 pygame.mixer.music.play(-1) #Here we have pygame use the play function to have the music loop forever.
 

 #This for loop helps with creatng the stars movement patterns by adding them to the empty list that the star variable is holding.
 for i in range(100):
   stars.append({
     "x":random.randint(0, 800),
     "y":random.randint(0, 600),
     "speed":random.randint(1,3),
     "size":random.randint(1,3)
   })
 #This for loop helps to create the debris and thier movement patterns that will appear on screen by adding them to the debris list.
 for i in range(20):
   debris.append({
     "x": random.randint(0, 780),
     "y": random.randint(-600, -30),
     "width": random.randint(10, 40),
     "height": random.randint(5, 20),
     "speed": random.randint(1, 3),
     "color": random.choice([(80,80,80), (60,60,60), (100,90,80)])

   })
   
  #This while loop helps with the functionality of the windows x button for when a player wants to close the window while the game is running.
 while running:
   #This for loop helps with the functionality of the x button when the player presses the x to close the window.
   for event in pygame.event.get():
     if event.type == pygame.QUIT:
       running = False
       playing = False

   keys = pygame.key.get_pressed()
   #This if statement helps with player movement and speed when the player pushes the left key.
   if keys[pygame.K_LEFT]:
    x -= speed
    #This if statement sets the boundriey for how far the player can move left.
    if x < 0:
      x = 0
   #This if statement helps with player movement and speed when the player pushes the right key.
   if keys[pygame.K_RIGHT]:
    x += speed
    #This if statement sets the boundriey for how far the player can checks move right.
    if x > 740:
      x = 740
   
   current_time = pygame.time.get_ticks() #Here we make a current_time variable and inside of it we have pygame use the time module and call get_ticks so that it gets the frames persecond.
   #This if statement helps with setting the bullets functionality and travel speed.
   if keys[pygame.K_SPACE] and current_time - last_shot > fire_rate:
     bullet = {"x": x + 25, "y": y} #Here we make a bullet variable and have it store a dictionary of the bullets coordinates for where on the grid the bullet should travel.
     bullets.append(bullet) #Here we have the bullets list add the dictionary the bullet variable is holding into the list.
     last_shot = current_time #Here we have the last shot variable equel the current_time variable so that as the game timer is increasing and if the last shot fired is greater then 300 on grid a bullet will fire.
     shoot_sound.play() #Here we have the shoot_sound variable call the play function so that it plays the sound file it is storing.
   
   screen.fill((0, 0, 0)) #Here we have the screen variable call the fill function to make the screen fully black using the RGB values 0,0,0.
   #This for loop helps with crating the stars on the title screen.
   

   #This for loop helps with crating the stars and getting rid of them when they reach a certain y axis on the grid.
   for star in stars:
    star["y"] += star["speed"]
    if star["y"] > 600:
     star["y"] = 0
     star["x"] = random.randint(0,800)
    pygame.draw.circle(screen, (255, 255, 255), (star["x"], star["y"]), star["size"]) #Here we have pygame use the draw module and call the circle function to make the circle, which is what the stars will be represented as.
   

#This for loop helps with the movement and creation of the debri and to have them show up on random coordinates.
   for debri in debris:
    debri["y"] += debri["speed"]
    if debri["y"] > 600:
     debri["y"] = random.randint(-100, -10)
     debri["x"] = random.randint(0,780)
   screen.blit(asteroid_img, (debri["x"], debri["y"]))


   #This for loop goes through the bullet list and removes it from the list when it leaves the screen.
   for bullet in bullets:
    bullet["y"] -= 8
    #This if statement helps with removing a bullet from the screen and a bullet pattern from the bullets list once it reaches a certain y cordinate which is 8, this ia also at the top of the window.
    if bullet["y"] < 0:
      bullets.remove(bullet)
    pygame.draw.rect(screen, (255, 165, 0), (bullet["x"], bullet["y"], 6, 16)) #Here we have pygame use the draw module and cal the rect function to create the bullet itself which will be orange.
   
   enemy_spawn_timer += 1
   #This if statement helps with the generation of the enemies
   if enemy_spawn_timer >= enemy_spawn_rate:
     enemy = {"x": random.randint(0, 740), "y": -30, "shoot_timer": 0, "health": 2} #Here we make an enemy variable and have it store a dictionary with a random x and a specific y coordinate for where the enemies will show up. We also include inside the dictionary a shoot_timer key which has the number 0, and a health key with the number 2. 
     enemies.append(enemy) #Here we add the enemy dictionary the enemy variable is holding into the enemies variables list.
     enemy_spawn_timer = 0 #Here we make an enemy spawn timer variable and have it store the number zero.
   
   #This for loop goes through the enemies list and removes an enemy when it leaves the screen.
   for enemy in enemies:
     enemy["y"] += 1 #Here we have the enemy variable use the y key in the dictionary it is storing and have it increase the number the y key is holding by 1.
     #This if statement helps with removing an enemy from the enemies list if they go below a certain y coordinate.
     if enemy["y"] > 600:
       enemies.remove(enemy)
     screen.blit(Ravager_class_scout_img, (enemy["x"], enemy["y"])) #Here we have the screen variable call the blit function to display the ravager class scout ships and hhave it use the same coordinates as the enemy
     

     enemy["shoot_timer"] += 1 #Here we have the enemy_shoot_timer variable increse the nuber its storing by one.
     #This is statement helps with the functionality of the enemies bullets by adding the enemy bullet pattern to the enemy_bullets variables empty list.
     if enemy["shoot_timer"] >= enemy_shoot_rate:
       enemy_bullet = {"x": enemy["x"] + 20, "y": enemy["y"] + 30}
       enemy_bullets.append(enemy_bullet)
       enemy["shoot_timer"] = 0 
       enemy_shoot_sound.play() #Here we have the enemy_shoot_sound variable call the play function so that it uses the sound file it is storing inside of itself.
 
       
     #This for loop helps with drawing the enemy bullets and removing them once they reach a certain y coordinate.
     for enemy_bullet in enemy_bullets:
       enemy_bullet["y"] += 5 
       pygame.draw.rect(screen, (255, 0, 0), (enemy_bullet["x"], enemy_bullet["y"], 4, 10))
       #This if statement helps with removing an enemys bullet when it raches a certain y coordinate.
       if enemy_bullet["y"] > 600:
         enemy_bullets.remove(enemy_bullet)
       
       #This if statement helps with the collision detection of the enemy bullets to ensure that they hit and interact with all sides of the Araga.
       if enemy_bullet["x"] > x and \
       enemy_bullet["x"] < x + 60 and \
       enemy_bullet["y"] > y and \
       enemy_bullet["y"] < y + 140:
        enemy_bullets.remove(enemy_bullet)
        health -= 1
       
       
      

   #This if statement helps with the functionality of the health and if its zero the running variables condition will be set to false.
   if health <= 0:
    running = False
   
   #This for loop helpes with the collision detection of the bullets, ensuring the bullets will get rid of the enemies upon contact regardless of where it hits it.
   for bullet in bullets[:]:
     #This for loop nested inside here, checks to see if a bullets x and y values are greater or less then
     for enemy in enemies[:]:
       if bullet["x"] > enemy["x"] and \
          bullet["x"] < enemy["x"] + 40 and \
          bullet["y"] > enemy["y"] and \
          bullet["y"] < enemy["y"] + 30:
         bullets.remove(bullet)
         enemy["health"] -= 1
         #This if statement helps with checking to see if the enemies health is less then or equal to zero before finally being removed from play, and the enemy dictionary is also removed from the empty list the enemies variable is holding.
         if enemy["health"] <= 0:
          enemies.remove(enemy)
          score += 1 #Here we have the score variable increase the number it is storing by one.
          explosion_sound.play() #Here we have the explosion_sound variable call the play function so that it uses the sound file that was store within itself.
   

   screen.blit(araga_img, (x, y)) #Here we have screen call the blit function and inside its argument have the araga_img variable so that the araga can be placed on the screen.
   


   score_text = font.render("Score: " + str(score), True, (255, 255, 255)) #Here we make a score_text variable and inside it we have the font variable call the render function to create the score text. 
   screen.blit(score_text, (10, 10))
   health_text = font.render("Health : " + str(health), True, (255, 0, 0))
   screen.blit(health_text, (10, 50))
   
   pygame.display.flip()
   clock.tick(60)


#This if statement helps with the functionality of the game over screen and text when the player gets a game over.
 if playing:
  screen.fill((0, 0, 0)) #Here we have the screen variable call the fill function to set the screens RGB values to black which is 0,0,0. 
  game_over_text = font.render("GAME OVER", True, (255, 0, 0)) #Here we make a game_over_tect variable and inside it have the font variable call the render function to make the game over text.
  final_score_text = font.render("Final Score: " + str(score), True, (255, 255, 255))
  restart_text = font.render("Press R to restart or Q to quit", True, (255, 255, 255))
  screen.blit(game_over_text, (300, 250))
  screen.blit(final_score_text, (300, 300))
  screen.blit(restart_text, (220, 350))
  pygame.display.flip()

  waiting = True

  pygame.mixer.music.stop() #Here we have pygame call the stop function to stop all of the music from playing
  gameover_sound.play() #Here we have the gameover_sound variable call the play function so that it uses the sound file that was stored inside itself.

  #This while loop helps with the functionality of the restart and quit options while the player is still playing the game.
  while waiting:
    
    for event in pygame.event.get():
      #This if statement helps with the functionality of the quit option if th player chooses to quit the game. 
      if event.type == pygame.QUIT:
        playing = False
        waiting = False
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_r:
          waiting = False
        if event.key == pygame.K_q:
          playing = False
          waiting = False

pygame.quit()
