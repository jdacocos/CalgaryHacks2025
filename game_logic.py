import pygame

def switch_block(player1, player2, player1_vel_y, player2_vel_y, player1_gravity, player2_gravity, gravity_switch_block_1, gravity_switch_block_2):
    """
    switch block reverses the other player's gravity until it is flipped again
    """
    if player1.colliderect(gravity_switch_block_1):  
        player2_gravity *= -1 
        player2_vel_y = -player2_vel_y 
    
    if player2.colliderect(gravity_switch_block_2):  
        player1_gravity *= -1 
        player1_vel_y = -player1_vel_y 

    return player1_vel_y, player2_vel_y, player1_gravity, player2_gravity

def button_block(player1, player2, player1_vel_y, player2_vel_y, player1_gravity, player2_gravity, button_block_1, button_block_2):
    """
    button block reverses the other player's gravity for a couple seconds
    """
    if player1.colliderect(button_block_1):  
        player2_gravity *= -1 
        player2_vel_y = -player2_vel_y 
    
    if player2.colliderect(button_block_2):  
        player1_gravity *= -1 
        player1_vel_y = -player1_vel_y 

    return player1_vel_y, player2_vel_y, player1_gravity, player2_gravity

def pressure_plate_block(player1, player2, player1_vel_y, player2_vel_y, player1_gravity, player2_gravity, pressure_plate_1, pressure_plate_2):
    """
    pressure_plate_block reverses the other player's gravity while it is stepped on
    """
    if player1.colliderect(pressure_plate_1):  
        player2_gravity *= -1 
        player2_vel_y = -player2_vel_y 
    
    if player2.colliderect(pressure_plate_2):  
        player1_gravity *= -1 
        player1_vel_y = -player1_vel_y 

    return player1_vel_y, player2_vel_y, player1_gravity, player2_gravity

def fire_block(player1, player2, fire_block_1, fire_block_2):
    """
    fire_block quits the game
    """
    if player1.colliderect(fire_block_1):  
        pygame.quit()  # Quits the game
        quit()  # Ends the Python process
    
    if player2.colliderect(fire_block_2):  
        pygame.quit()  # Quits the game
        quit()  # Ends the Python process



