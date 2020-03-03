import tkinter as tk
import sys
import webbrowser
chromepath = r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'
webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chromepath))
window = tk.Tk() #初始化視窗
# 設定視窗標題、大小和背景顏色
window.title('網頁快速瀏覽器')
window.geometry('200x100')
window.configure(background='white')

header_label = tk.Label(window, text='數字快速瀏覽器')
header_label.pack()



e = tk.Entry(window, show = None)#顯示成明文形式
e.pack()

def nhentai():
    number = str(e.get())
    print(number)
    print("hi")
    url = ("nhentai.net/g/" + number)
    webbrowser.get('chrome').open(url)
    



# 以下為 weight_frame 群組



calculate_btn = tk.Button(window, text='馬上前往', command=nhentai)
calculate_btn.pack()





    
window.mainloop()