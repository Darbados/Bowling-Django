# Delasport
Bowling emulation

Short documentation of how the bowling emulation app works.

1. By calling the 'bowling/' or 'blank' url, the home page will appear, where you'll be required to enter a name.
2. By clicking 'start game' button, the add_roll page will load, where the rolls will be made. A JS is being used for random generating the rolls results. They are stored in hidden inputs, with ids of id_attempt1-3. If you have strike or spare, the appropriate sign will be shown in the appropriate green box.
3. By clicking the 'Next frame' button the rolls from the current frame will be submit to the Add_Roll() post function which will create a Frame object with the attempts and total_score fields. Then, the next frame page will be loaded. With completing each frame, the Scoreboard will be increased with a box for the completed frame.
4. When all frames are finished, you'll be able to check your final score, by clicking on the 'total score' link. Then a 'total_score' page will be loaded with a an exteme simple table for displaying the results + 'New game' button available on the top if you want to play another game.

REST API exists by calling the 'bawling/api/<pk>' where <pk> stays for the primary key of the Game object.
  
Weakness:
1. I've couldn't make this as a total REST app. This is at least what I need to learn more about.
2. JS code is not elegant.
