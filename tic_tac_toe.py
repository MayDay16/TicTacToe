class TicTacToe:
    def __init__(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'

    def print_board(self):
        print("   A   B   C")
        for i, row in enumerate(self.board):
            print(f"{i + 1}  " + " | ".join(row))
            if i < 2:
                print("  ---|---|---")
        print("\n")

    def check_winner(self):
        # Проверка строк
        for row in self.board:
            if all(cell == row[0] and cell != ' ' for cell in row):
                return True

        # Проверка столбцов
        for col in range(3):
            if all(self.board[row][col] == self.board[0][col] and self.board[row][col] != ' ' for row in range(3)):
                return True

        # Проверка диагоналей
        if all(self.board[i][i] == self.board[0][0] and self.board[i][i] != ' ' for i in range(3)) or \
           all(self.board[i][2 - i] == self.board[0][2] and self.board[i][2 - i] != ' ' for i in range(3)):
            return True

        return False

    def is_board_full(self):
        return all(cell != ' ' for row in self.board for cell in row)

    def convert_input(self, input_str):
        try:
            if input_str[0].isdigit():
                row = int(input_str[0]) - 1
                col = ord(input_str[1].upper()) - ord('A')
            else:
                col = ord(input_str[0].upper()) - ord('A')
                row = int(input_str[1]) - 1

            return row, col
        except (ValueError, IndexError):
            return None

    def play(self):
        while True:
            self.print_board()
            try:
                move = input(f"Игрок {self.current_player}, введите адрес клетки (например, B2): ")
                move = move.upper()  # Приводим ввод к верхнему регистру

                row_col = self.convert_input(move)

                if row_col is not None:
                    row, col = row_col
                    if 0 <= row < 3 and 0 <= col < 3 and self.board[row][col] == ' ':
                        self.board[row][col] = self.current_player

                        if self.check_winner():
                            self.print_board()
                            print(f"Игрок {self.current_player} победил!")
                            break
                        elif self.is_board_full():
                            self.print_board()
                            print("Ничья!")
                            break

                        self.current_player = 'O' if self.current_player == 'X' else 'X'
                    else:
                        print("Недопустимый ход. Попробуйте ещё раз.")
                else:
                    print("Недопустимый адрес клетки. Попробуйте ещё раз.")
            except ValueError:
                print("Введите корректный адрес клетки.")


if __name__ == "__main__":
    game = TicTacToe()
    game.play()
