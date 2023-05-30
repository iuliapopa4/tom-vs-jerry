# tom-vs-jerry
  

This project is a simple game called "Tom vs Jerry" implemented using the Pygame library. The objective of the game is to hit the opponent character while avoiding their attacks. Each character has their own image representation (Tom and Jerry) and can move within their respective boundaries. The characters can perform attacks by pressing specific keys:
    Tom:
    W - up
    A - left
    S - down
    D - right
    left_CTRL - attack
    
    Jerry:
    K_UP - up
    K_LEFT - left
    K_DOWN - down
    K_RIGHT - right
    right_CTRL - attack

The game includes health bars for both characters. When a character is hit by an attack, their health decreases. The game ends when one of the characters' health reaches zero. The winner of the game is displayed on the screen with a corresponding image (Tom or Jerry), and the game pauses for a few seconds before restarting.
