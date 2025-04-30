#create start menu/screen
start_menu_background = Rect(0, 0, 400, 400, fill = 'purple')
start_button = Rect(120, 200, 160, 80, fill = 'gold')
label1 = Label('Start Game', 200, 240, fill = 'red', size = 30, font = 'arial')
label2 = Label('Welcome to Tic Tac Toe!', 200, 120, fill = 'gold', size = 30, font = 'arial')

def onMousePress(mouseX, mouseY):
    
    global start_button
    
    if start_button.hits(mouseX, mouseY):
        start_menu_background.visible = False
        start_button.visible = False
        label1.visible = False
        label2.visible = False
    

        #create design/background of game
        player_tracker = Rect(0, 0, 400, 120, fill = 'pink')
        board = Rect(0, 120, 400, 280, fill = 'lightGrey')

        #create actual grid for tic tac toe
        Line(120, 120, 120, 360, fill = 'black', lineWidth = 5)
        Line(240, 120, 240, 360, fill = 'black', lineWidth = 5)
        Line(0, 200, 360, 200, fill = 'black', lineWidth = 5)
        Line(0, 280, 360, 280, fill = 'black', lineWidth = 5)
        Line(0, 360, 360, 360, fill = 'black', lineWidth = 5)
        Line(360, 360, 360, 120, fill = 'black', lineWidth = 5)
        
        def onMousePress(mouseX, MouseY):
             Label('X', mouseX, mouseY, fill = 'red', size = 30, font = 'arial')
            
        
        Label('Player_1 make your move!', 180, 60, fill = 'blue', size = 30, font = 'arial')
