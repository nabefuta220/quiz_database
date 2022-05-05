import django
import sqlite3

class CHECK_ANSWER():
    def __init__(self, answer, Qnumber):
        #answer = 入力された答え, Qnumber = 問題番号
        self.answer = answer
        self.Qnumber = Qnumber

        self.CHECK()

    def CHECK(answer):
        if self.answer.get() == char("answer.db"):　#クイズデータの対応する模範解答
            print("正解!〇")
        else:
         print("はずれ…×")
    