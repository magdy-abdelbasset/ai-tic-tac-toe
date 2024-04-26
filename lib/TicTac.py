from enum import Enum
from lib.PrintChar import PrintChar
# الحالة الخاصة بحقل اللعية
class SquareStatus(Enum):
    EMPTY  = 0
    XCHAR  = 1
    OCHAR  = 2
# الاعبين
class Player(Enum):
    PlayerX  = 1
    PlayerO  = 2
class ToySquare:
    # ضبط مربع اللعبة على فارغ
    status = SquareStatus.EMPTY
    def __init__(self ,status: SquareStatus = SquareStatus.EMPTY ):
        self.status
    def playHere(self,status : SquareStatus ):
        if status == SquareStatus.EMPTY :
            print("Can't Set Empty")
            return False
        elif self.status != SquareStatus.EMPTY :
            print("Sorry Square is't Empty")
            return False
        else:
            self.status = status
            return True
        
class TicTac :
    squares :list[ToySquare] = []
    avalible_squares :list[ToySquare] = []
    print_char = PrintChar()
    player_turn = Player.PlayerX
    winner :Player= None
    def __init__(self):
        self.new_game()
        pass
    def new_game(self):
        self.squares = []
        self.player_turn = Player.PlayerX
        self.winner = None
        for i in range(1,10) :
            self.squares.append(ToySquare())
        self.printGame()
        self.updateAvalabileSquares()        
        self.newTurn()
    def get_player_name(self ,player:Player):
        p = "O"
        p2 = "2"
        if(player == Player.PlayerX):
            p=  "X" 
            p2 = "1"
        return {"name":p,"number":p2}
    def newTurn(self):
        
        # self.printGame()
        
        validatin_msg = "Input Must Be Int And Between 1 And 9 "
        try:
            player = self.get_player_name(self.player_turn)
            print("If You Wan Close Game write: exit and press Enter ")
            print("Now Player Turn In The Toy Is Player "+str(player["name"])+" ( Number "+str(player["number"])+" )")
            input_1 = input("Enter Square Number \n")
            if(  input_1 == "exit" ):
                return
            SquareNumber = int(input_1)
        except:
            print(validatin_msg)
            self.newTurn()
            # return
        if(SquareNumber > 9 or SquareNumber <= 0):
            print(validatin_msg)
            self.newTurn()
            # return
        else:
            if self.player_turn == Player.PlayerX :
                statusS = SquareStatus.XCHAR
            else :
                statusS = SquareStatus.OCHAR
            squareAvalible = self.squares[SquareNumber-1].playHere(statusS)
            if(squareAvalible):
                self.updateAvalabileSquares()
                self.changePlayer()
                self.printGame()
                if(self.checkGame()):
                    self.newTurn()
            else:
                self.printGame()
                print("Square is not Empty select Empty Square")
                self.newTurn()
    def changePlayer(self):
        if self.player_turn == Player.PlayerX :
            self.player_turn = Player.PlayerO 
        else:
            self.player_turn = Player.PlayerX
        
    def updateAvalabileSquares(self):
        self.avalible_squares = []
        for key ,square in enumerate(self.squares) :
            if(square.status == SquareStatus.EMPTY):
                self.avalible_squares.append(key + 1)
         
    def printGame(self):
        # for i in self.squares :
            # print(i.status)
        for i in range(1,4):
            cell_1 = self.squares[(i *3)-3].status
            cell_2 = self.squares[(i *3)-2].status
            cell_3 = self.squares[(i *3)-1].status
            for row in range(1,14):
                if(i == 2):
                    self.print_row(cell_1,cell_2,cell_3,row,i,False,False)
                else:
                    self.print_row(cell_1,cell_2,cell_3,row,i)
                

    def checkGame(self):
        if(len(self.avalible_squares) == 0 and not self.thereIsWiner()):
            print("Game Is End And No Player Win")
            new_g = input("if you want play again press Y")
            if(new_g == "y" or new_g == "Y"):
                return self.new_game()
            else:
                return False
                
        elif(not self.thereIsWiner()):
            return True
        else :
            player = self.get_player_name(self.winner)
            print("Game Is End Player {player} Winer".format(player=player["name"]))
            self.print_char.print_congrate()
            if(self.winner == Player.PlayerX):
                self.print_char.print_win("x")
            else:
                self.print_char.print_win("o")
            new_g = input("if you want play again press Y")
            if(new_g == "y" or new_g == "Y"):
                return self.new_game()
            return False
             
    def thereIsWiner(self):
        winerValues = [[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]
        for val in winerValues :
            if(self.squares[val[0] - 1 ].status == self.squares[val[1] - 1 ].status and \
                self.squares[val[0] - 1 ].status == self.squares[val[2] - 1 ].status and \
                self.squares[val[0] - 1 ].status != SquareStatus.EMPTY    ):
                if(self.squares[val[0] - 1 ].status == SquareStatus.OCHAR) :
                    self.winner = Player.PlayerO
                else :
                    self.winner = Player.PlayerX
                return True
        return False

    def print_row(self,square_1:SquareStatus , square_2 :SquareStatus , square_3 :SquareStatus,numRow:int,\
                  MainRow:int,start:bool = True, end :bool = True):
        row_str = ""
        str_start_end = "||"
        str_margin = " "
        border_top_bottom = "="
        if((numRow == 1 and start) or (numRow == 13 and end)):
            for i in range(1,4):
                row_str += self.print_char.print_full_char(border_top_bottom,7)
                num = 0
                if(numRow == 1 and MainRow == 1):
                    num = i
                elif (numRow == 13 and MainRow == 1):
                    num = i +3
                elif (numRow == 1 and MainRow == 3):
                    num = i +6
                elif(numRow == 13 and MainRow == 3):
                    print(self.print_char.print_full_char(border_top_bottom,18*3))
                    return
                row_str += "({num})".format(num=num)
                # row_str += str_start_end
                row_str += self.print_char.print_full_char(border_top_bottom,8)

            print(row_str)
            return
        if(numRow == 1 or numRow == 13 ):
            return
        if(numRow == 2 or numRow == 3 or numRow == 11 or numRow == 12):
            for i in range(1,4):
                if(i != 2 and i != 3):
                    row_str += str_start_end
                row_str += self.print_char.print_full_char(str_margin,15)
                # if(i != 3):
                row_str += str_start_end

            print(row_str)
            return
        num_with_out_margin = numRow -  3
        
        # row_str += str_start_end
        squares = [square_1,square_2,square_3]
        for k ,square in enumerate(squares):
            if(k != 1 and k != 2):
                row_str += str_start_end
            match square:
                case SquareStatus.EMPTY :
                    row_str += self.print_char.print_full_char(" ",15)
                case SquareStatus.XCHAR :
                    row_str += self.print_char.print_x(num_with_out_margin)
                case SquareStatus.OCHAR :
                    row_str += self.print_char.print_o(num_with_out_margin)
            if(k != 2):
                row_str += str_start_end
        row_str += str_start_end
        print(row_str)
