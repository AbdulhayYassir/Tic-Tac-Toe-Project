import time
from IPython.display import clear_output

##########################################################################################################################
def clear_screen():
    clear_output(wait=True)

##########################################################################################################################
class Player:
    def __init__(self):
        self.name = ""
        self.symbol = ""

    def choose_name(self):
        while True:
            name = input("Enter Player Name (letters only): ").strip()
            if name.isalpha():
                self.name = name
                break
            print("Invalid Name! Please use letters only.")

    def choose_symbol(self):
        while True:
            symbol = input(f"{self.name}, choose your symbol (X or O): ").strip().upper()
            if symbol in ['X', 'O']:
                self.symbol = symbol
                break
            print("Invalid Symbol! Please choose 'X' or 'O' only.")

##########################################################################################################################
class Menu:
    def _get_choice(self):
        while True:
            try:
                choose = int(input("Enter your choice (1 or 2): "))
                if choose in [1, 2]:
                    return choose
                else:
                    print("Invalid choice! Please enter 1 or 2.")
            except ValueError:
                print("Invalid input! Please enter a number (1 or 2).")

    def display_main_menu(self):
        print("--- Welcome to Tic Tac Toe ---")
        print("1. Start Game")
        print("2. Quit")
        return self._get_choice()

    def display_endgame_menu(self):
        print("\n--- Game Over ---")
        print("1. Play Again")
        print("2. Quit")
        return self._get_choice()

##########################################################################################################################
class Board:
    def __init__(self):
        self.board = [str(i) for i in range(1, 10)]

    def display_board(self):
        print(f"\n {self.board[0]} | {self.board[1]} | {self.board[2]} ")
        print("-----------")
        print(f" {self.board[3]} | {self.board[4]} | {self.board[5]} ")
        print("-----------")
        print(f" {self.board[6]} | {self.board[7]} | {self.board[8]} \n")

    def update_board(self, choice, symbol):
        if self.is_valid_move(choice):
            self.board[choice - 1] = symbol
            return True
        return False

    def is_valid_move(self, choice):
        return self.board[choice - 1].isdigit()

    def reset_board(self):
        self.board = [str(i) for i in range(1, 10)]

    def check_win(self):
        win_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8], # صفوف
            [0, 3, 6], [1, 4, 7], [2, 5, 8], # أعمدة
            [0, 4, 8], [2, 4, 6]             # أقطار
        ]
        for combo in win_combinations:
            if self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]]:
                return True
        return False

    def check_draw(self):
        return all(not cell.isdigit() for cell in self.board)

##########################################################################################################################
class Game:
    def __init__(self):
        self.player = [Player(), Player()]
        self.board = Board()
        self.menu = Menu()
        self.current_player_index = 0

    def start_game(self):
        clear_screen()
        choice = self.menu.display_main_menu()
        if choice == 1:
            self.setup_player()
            self.play_game()
        else:
            self.quit_game()

    def setup_player(self):
        for num, player in enumerate(self.player, start=1):
            clear_screen()
            print(f"--- Player {num} Setup ---")
            player.choose_name()
            if num == 1:
                player.choose_symbol()
            else:
                player.symbol = "O" if self.player[0].symbol == "X" else "X"
                print(f"\n[!] {player.name}, your symbol is automatically assigned to: {player.symbol}")
                # وقفة لمدة ثانيتين عشان اللاعب التاني يلحق يشوف الرمز بتاعه
                time.sleep(2) 

    def play_game(self):
        while True:
            self.play_turn()
            
            # فحص حالة الفوز
            if self.board.check_win():
                clear_screen()
                self.board.display_board()
                print(f"🎉 Winner! Congratulations {self.player[self.current_player_index].name}! 🎉")
                if self.menu.display_endgame_menu() == 1:
                    self.board.reset_board()
                    self.current_player_index = 0
                    continue # إعادة اللعب بشكل نظيف بدل الـ Recursion
                else:
                    self.quit_game()
                    break

            # فحص حالة التعادل
            if self.board.check_draw():
                clear_screen()
                self.board.display_board()
                print("🤝 It's a Draw! 🤝")
                if self.menu.display_endgame_menu() == 1:
                    self.board.reset_board()
                    self.current_player_index = 0
                    continue
                else:
                    self.quit_game()
                    break

            self.switch_player()

    def play_turn(self):
        player = self.player[self.current_player_index]
        
        while True:
            # مسح الشاشة جوه اللوب عشان لو دخل رقم غلط، الخلية متكبرش
            clear_screen()
            self.board.display_board()
            print(f"{player.name}'s Turn ({player.symbol})")
            
            try:
                choice = int(input("Enter cell number (1-9): "))
                if 1 <= choice <= 9:
                    if self.board.update_board(choice, player.symbol):
                        break 
                    else:
                        print("Invalid move! This cell is already taken.")
                        time.sleep(1.5) # عرض رسالة الخطأ شوية قبل ما الشاشة تتمسح
                else:
                    print("Invalid choice! Please choose a number between 1 and 9.")
                    time.sleep(1.5)
            except ValueError:
                print("Please enter a valid number.")
                time.sleep(1.5)

    def switch_player(self):
        self.current_player_index = 1 - self.current_player_index

    def quit_game(self):
        clear_screen()
        print("Thank you for playing Tic Tac Toe! See you next time.")

##########################################################################################################################
# تشغيل اللعبة
if __name__ == "__main__":
    game = Game()
    game.start_game()