import tkinter

# 画面作成
tki = tkinter.Tk()
tki.geometry('300x200')
tki.title('ンソ変換')

# clickイベント
def btn_click():
    txt_2.delete(0,tkinter.END)
    # テキスト取得
    num = str(txt_1.get())
    ans = ''
    aft = ''
    # ンソ変換
    for nso in num :
        aft = nso
        if nso == 'ン':
            aft = 'ソ'
        if nso == 'ソ':
            aft = 'ン'
        if nso == 'ツ':
            aft = 'シ'
        if nso == 'シ':
            aft = 'ツ'
        if nso == 'ゾ':
            aft = 'ン゛'
        if nso == 'ジ':
            aft = 'ヅ'
        ans = ans + aft
    txt_2.insert(0,ans)

# ラベル
lbl_1 = tkinter.Label(text='変換したい文字')
lbl_1.place(x=30, y=70)
lbl_2 = tkinter.Label(text='変換後')
lbl_2.place(x=30, y=100)

# テキストボックス
txt_1 = tkinter.Entry(width=20)
txt_1.place(x=140, y=70)
txt_2 = tkinter.Entry(width=20)
txt_2.place(x=140, y=100)

# ボタン
btn = tkinter.Button(tki, text='ンソ変換!', command=btn_click)
btn.place(x=140, y=170)

# 画面をそのまま表示
tki.mainloop()
