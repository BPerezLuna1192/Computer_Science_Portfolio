#create design/background of game
player_tracker = Rect(0, 0, 400, 120, fill = 'pink')
board = Rect(0, 120, 400, 280, fill = 'lightGrey')

#create actual grid for tic tac toe
Line(120, 120, 120, 360, fill = 'black', lineWidth = 5)
Line(240, 120, 240, 360, fill = 'black', lineWidth = 5)
Line(0, 200, 360, 200, fill = 'black', lineWidth = 5)
Line(0, 280, 360, 280, fill = 'black', lineWidth = 5)