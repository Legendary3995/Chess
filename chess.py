class chess:
  white = []
  black = []

  def __init__(self, init_pos: list, cost: int, surface, color: int,
               piece: int, number: int):
    self.init_pos = init_pos  #Stores the initial Position of the chess piece
    self.pos = init_pos  #Stores the current Position of the chess piece
    self.cost = cost  #Stores the cost of Chess piece
    self.surface = surface  #Stores the surface to blit for representing chess piece
    self.color = color  #stores color of chess piece: (-1) - White, 1 - Black
    self.piece = piece  #0 - King, 1 - Queen, 2 - Rook, 3 - Bishop, 4 - Knight, 5 - Pawn
    self.temp_pos = [
    ]  #stores the temporary position of chess, made to be used in Drag and Drop and legal move
    self.captured = False  #variable tells if the piece is captured
    self.number = number

    if self.color == -1:
      chess.white.append(self)
    else:
      chess.black.append(self)

  #returns the set of all positions of given color, else give all other position of the color given except the exception(the exception's number is given) given
  def occupied_pos(color: int, _except=None):
    if color == -1:
      return [tuple(i.pos) for i in chess.white if i.number != _except]
      #returns the list of all the white positions except the exception
    else:
      return [tuple(i.pos) for i in chess.black if i.number != _except]
      #returns the list of all the black positions except the exception

  #if type is True, it means that it is needed to check if the given position is true, else it means to return a set of legal moves
  def legal_moves(self, type: bool, position=tuple()):
    legal_moves = set()
    if self.piece == 0:  #legal move of *King*
      pass
    elif self.piece == 1:  #legal move of Queen
      pass
    elif self.piece == 2:  #legal move of Rook
      for x in range(self.pos[0] - 1, -1, -1):
        #Searching for legal moves in horizontally backward direction until a black or white piece comes in the way
        pass
      for x in range(self.pos[0] + 1, 8):
        #Searching for legal moves in horizontally forward direction until a black or white piece comes in the way
        pass
      for x in range(self.pos[1] - 1, -1, -1):
        #Searching for legal moves in vertically backward direction until a black or white piece comes in the way
        pass
      for x in range(self.pos[1] + 1, 8):
        #Searching for legal moves in vertically forward direction until a black or white piece comes in the way
        pass
    elif self.piece == 3:  #legal move of Bishop
      for x in range(self.pos[0] - 1, -1, -1):
        for y in range(self.pos[1] - 1, -1, -1):
          #Searching for legal moves in top left direction diagonally until a piece comes in the way
          pass
      for x in range(self.pos[0] - 1, -1, -1):
        for y in range(self.pos[1] + 1, 8):
          #Searching for legal moves in top right direction diagonally until a piece comes in the way
          pass
      for x in range(self.pos[0] + 1, 8):
        for y in range(self.pos[1] + 1, 8):
          #Searching for legal moves in bottom right direction diagonally until a piece comes in the way
          pass
      for x in range(self.pos[0] + 1, 8):
        for y in range(self.pos[1] - 1, -1, -1):
          #Searching for legal moves in bottom left direction diagonally until a piece comes in the way
          pass
    elif self.piece == 4:  #legal move of Knight
      for x in range(abs(self.pos[0] - 2), 8):
        for y in range(abs(self.pos[1] - 2), 8):
          if abs(self.pos[0] - x) in [1, 2] and abs(self.pos[1] - y) in [1, 2]:
            #logic for finding legal move for Knight
            if abs(self.pos[0] - x) != abs(self.pos[1] - y):
              #exception of logic
              if (x, y) not in chess.occupied_pos(self.color, self.number):
                legal_moves.add((x, y))
    elif self.piece == 5:  #legal move of Pawn
      pass
    else:
      return False

    if type == True:  #checks if the value of type is True
      #return true if the given position is a legal move else return false
      return (position in legal_moves)
    else:
      #return the set of legal moves
      return legal_moves
