import tkinter as tk        # GUIモジュール
import tkinter.scrolledtext as tkscr  # GUI：スクロールテキストクラスモジュール
import PIL.Image as im      # Pillowの画像クラスモジュール
import PIL.ImageTk as imtk  # Pillowの写真画像クラスモジュール
import sys                  # システム用モジュール
import random as rd         # 乱数を扱うモジュール
import time
#
# ウィンドウアプリケーションの定義
#
class tkApp(tk.Frame):          # GUIモジュール tkinter を使ったアプリを定義する
                                # tk.Frameを拡張したクラスにする
    def __init__(self, master=None):
        super().__init__(master)    # 基底クラスtk.Frameの初期化を実行する
        self.pack()                 # レイアウト


        self.titleimg = im.open("title.png")# タイトルの画像を読み込む https://www.bing.com/images/search?view=detailV2&ccid=D%2F8rJFFN&id=466ADAFFEBE6FE4145BE9E0057CD0EA6A4514709&thid=OIP.D_8rJFFNFUWTBfwc6BJvpQHaFj&mediaurl=https%3A%2F%2Fstat.ameba.jp%2Fuser_images%2F20200611%2F23%2Ftelubow-26%2F5a%2Fb5%2Fj%2Fo1080081014772776614.jpg&exph=810&expw=1080&q=%e3%83%a9%e3%83%bc%e3%83%a1%e3%83%b3%e4%ba%8c%e9%83%8e%e3%80%80%e5%ba%97%e5%86%85&simid=608010079140989619&form=IRPRST&ck=265F69C6C66AC7BAC6CA41428A019C75&selectedindex=3&ajaxhist=0&ajaxserp=0&vt=0&sim=11
        self.backimg = im.open("back.png")  # 分かれ道の画像を読み込む https://www.bing.com/images/search?view=detailV2&ccid=wUchbEHs&id=21AF146E2ED09C126BFD04E2EAC685AB6D460CBC&thid=OIP.wUchbEHsZzBwQ6KwaXH6egHaNK&mediaurl=https%3A%2F%2Fdivnil.com%2Fwallpaper%2Fiphone8%2Fimg%2Fapp%2Fc%2F1%2Fc147216c41ec67307043a2b06971fa7a_a5572ab3ef1071a2cfda81384b9ba9ad_raw.jpg&exph=1920&expw=1080&q=%e3%82%b9%e3%83%a2%e3%83%bc%e3%82%af%e3%83%9b%e3%83%af%e3%82%a4%e3%83%88+%e5%a3%81%e7%b4%99&simid=608048935703160443&form=IRPRST&ck=9F942314E4068EC75CB275C195A5766C&selectedindex=0&ajaxhist=0&ajaxserp=0&vt=0&sim=11
        self.text_r = 1      # テキストの行位置

        # 初期画面表示

        self.menu_bar = tk.Menu(wnd)            # メニューバー

        # プレイメニュー
        self.play_menu = tk.Menu(self.menu_bar, tearoff=False)
        self.play_menu.add_command(label="スタート", command=self.game_start)
        self.play_menu.add_separator()
        self.play_menu.add_command(label="終了", command=self.game_exit)

        wnd.config(menu=self.menu_bar)

        self.change_image(self.titleimg) # 画像をタイトルの画像にする(初回の変更)

        # スタートボタンを作成して配置する
        self.start_btn = tk.Button(wnd, text="スタート",
                        command=self.start_btn_click,
                        width=14, height=2, bg="green", fg="white")
        self.start_btn.place(x=600, y=400)
    def change_image(self,image):       # 画像を変更する関数
        png = imtk.PhotoImage(image)    # 指定された画像を写真画像として保存する
        lab = tk.Label(wnd, image=png)  # 画像をラベルに貼り付ける
        lab.image = png                 # これをやらないと画像が消されてしまう
        lab.pack()                      # レイアウトを実行する
        lab.place(x=100, y=20)          # 配置する

    def enable_dir_button(self):                # 方向ボタンを全て有効にする関数
        self.left_btn["state"] = tk.NORMAL
        self.mid_btn["state"] = tk.NORMAL
        self.right_btn["state"] = tk.NORMAL

    def disable_dir_button(self):               # 方向ボタンを全て無効にする関数
        self.left_btn["state"] = tk.DISABLED
        self.mid_btn["state"] = tk.DISABLED
        self.right_btn["state"] = tk.DISABLED

    def game_start(self):               # ゲーム開始時の設定をする
        self.text_r = 1      # テキストの行位置
        self.enable_dir_button()            # 方向ボタンを全て有効にする

    def game_exit(self):        # ゲームを終了する関数
        sys.exit(0)

    def start_btn_click(self):  # スタートボタンがクリックされた時に呼ばれる関数
        self.game_start()

    def left_btn_click(self):   # 左ボタンがクリックされた時に呼ばれる関数
        self.choose_left()  # 左を選ぶ

    def mid_btn_click(self):    # 真ん中ボタンがクリックされた時に呼ばれる関数
        self.choose_mid()  # 真ん中を選ぶ

    def right_btn_click(self):  # 右ボタンがクリックされた時に呼ばれる関数
        self.choose_right()  # 右を選ぶ

    def game_start(self):               # ゲーム開始時の設定をする
        time.sleep(1.0)                     # チョット待つ
        self.change_image(self.backimg)
        # 左ボタンを作成して配置する
        self.left_btn = tk.Button(wnd, text="数学",
                        command=self.left_btn_click,
                        width=14, height=2, bg="sandybrown", fg="black",
                        state=tk.DISABLED)
        self.left_btn.place(x=200, y=550)

        # 真ん中ボタンを作成して配置する
        self.mid_btn = tk.Button(wnd, text="英語",
                        command=self.mid_btn_click,
                        width=14, height=2, bg="sandybrown", fg="black",
                        state=tk.DISABLED)
        self.mid_btn.place(x=600, y=550)

        # 右ボタンを作成して配置する
        self.right_btn = tk.Button(wnd, text="国語",
                        command=self.right_btn_click,
                        width=14, height=2, bg="sandybrown", fg="black",
                        state=tk.DISABLED)
        self.right_btn.place(x=1000, y=550)

        self.left_btn["state"] = tk.NORMAL
        self.mid_btn["state"] = tk.NORMAL
        self.right_btn["state"] = tk.NORMAL
    def choose_left(self):
        time.sleep(1.0)                     # チョット待つ
        self.change_image(self.backimg)
        # 左ボタンを作成して配置する
        self.left_btn = tk.Button(wnd, text="基礎数学",
                        command=self.left_btn_click,
                        width=14, height=2, bg="sandybrown", fg="black",
                        state=tk.DISABLED)
        self.left_btn.place(x=200, y=550)

        # 真ん中ボタンを作成して配置する
        self.mid_btn = tk.Button(wnd, text="解析学",
                        command=self.mid_btn_click,
                        width=14, height=2, bg="sandybrown", fg="black",
                        state=tk.DISABLED)
        self.mid_btn.place(x=600, y=550)

        # 右ボタンを作成して配置する
        self.right_btn = tk.Button(wnd, text="代数幾何",
                        command=self.right_btn_click,
                        width=14, height=2, bg="sandybrown", fg="black",
                        state=tk.DISABLED)
        self.right_btn.place(x=1000, y=550)

        self.left_btn["state"] = tk.DISABLED
        self.mid_btn["state"] = tk.DISABLED
        self.right_btn["state"] = tk.DISABLED
    def choose_mid(self):
        time.sleep(1.0)                     # チョット待つ
        self.change_image(self.backimg)
        # 左ボタンを作成して配置する
        self.left_btn = tk.Button(wnd, text="英語１",
                        command=self.left_btn_click,
                        width=14, height=2, bg="sandybrown", fg="black",
                        state=tk.DISABLED)
        self.left_btn.place(x=200, y=550)

        # 真ん中ボタンを作成して配置する
        self.mid_btn = tk.Button(wnd, text="英語２",
                        command=self.mid_btn_click,
                        width=14, height=2, bg="sandybrown", fg="black",
                        state=tk.DISABLED)
        self.mid_btn.place(x=600, y=550)

        # 右ボタンを作成して配置する
        self.right_btn = tk.Button(wnd, text="英語３",
                        command=self.right_btn_click,
                        width=14, height=2, bg="sandybrown", fg="black",
                        state=tk.DISABLED)
        self.right_btn.place(x=1000, y=550)

        self.left_btn["state"] = tk.DISABLED
        self.mid_btn["state"] = tk.DISABLED
        self.right_btn["state"] = tk.DISABLED
    def choose_right(self):
        time.sleep(1.0)                     # チョット待つ
        self.change_image(self.backimg)
        # 左ボタンを作成して配置する
        self.left_btn = tk.Button(wnd, text="国語１",
                        command=self.left_btn_click,
                        width=14, height=2, bg="sandybrown", fg="black",
                        state=tk.DISABLED)
        self.left_btn.place(x=200, y=550)

        # 真ん中ボタンを作成して配置する
        self.mid_btn = tk.Button(wnd, text="国語２",
                        command=self.mid_btn_click,
                        width=14, height=2, bg="sandybrown", fg="black",
                        state=tk.DISABLED)
        self.mid_btn.place(x=600, y=550)

        # 右ボタンを作成して配置する
        self.right_btn = tk.Button(wnd, text="国語３",
                        command=self.right_btn_click,
                        width=14, height=2, bg="sandybrown", fg="black",
                        state=tk.DISABLED)
        self.right_btn.place(x=1000, y=550)

        self.left_btn["state"] = tk.DISABLED
        self.mid_btn["state"] = tk.DISABLED
        self.right_btn["state"] = tk.DISABLED
wnd = tk.Tk()                   # ウィンドウを作成する
wnd.geometry('1200x600')         # ウィンドウサイズを500 ✕ 500ドットにする
wnd.title('クイズ')   # ウィンドウタイトルを設定する

# ウィンドウのフレームを作成する

app = tkApp(wnd)

# ウィンドウを表示してメニュー・ボタン等の待受け処理に入る
# ウィンドウを終了するまで戻ってこない無限ループ

wnd.mainloop()
