import os
from os import listdir
from send2trash import send2trash
import tkinter as tk


class StartWindow:
    def __init__(self, master):
        self.root = master
        self.root.title('Удаление ненужных файлов')
        self.canvas1 = tk.Canvas(self.root, width=400, height=400)
        self.canvas1.pack()

        self.label1 = tk.Label(self.root, text='Путь к папке для удаления файлов:', font=('helvetica', 10))
        self.canvas1.create_window(200, 130, window=self.label1)

        self.entry1 = tk.Entry(self.root, width=35)
        self.canvas1.create_window(200, 150, window=self.entry1)

        self.label2 = tk.Label(self.root, text='Расширения файлов, которые не надо удалять', font=('helvetica', 10))
        self.canvas1.create_window(200, 180, window=self.label2)

        self.entry2 = tk.Entry(self.root, width=35)
        self.canvas1.create_window(200, 200, window=self.entry2)

        self.button1 = tk.Button(text='Удалить файлы', command=self.start_script, bg='brown', fg='white')
        self.canvas1.create_window(200, 245, window=self.button1)
        self.label3 = 0

    # FUNCTION TO INSERT PATH
    def start_script(self):
        if self.label3:
            self.label3.destroy()
        folder_path = self.entry1.get()
        extension = self.entry2.get()
        if os.path.exists(folder_path) and extension != '':
            for file in listdir(folder_path):
                if not file.endswith(extension):
                    if os.path.isdir(os.path.join(folder_path, file)):
                        self.clear_folder(os.path.join(folder_path, file), extension)
                    else:
                        send2trash(os.path.join(folder_path, file))
                        # print('Deleted: ' + os.path.join(folder_path, file))
            self.label3 = tk.Label(root, text=f'{folder_path}\n'
                                              f'Все файлы кроме расширений: {extension} \n'
                                              f'были перемещены в корзину!', fg='green', font=('helvetica', 12, 'bold'))
            self.canvas1.create_window(200, 295, window=self.label3)
        elif not os.path.exists(folder_path):
            self.label3 = tk.Label(root, text=f'Указанного пути не существует:\n{folder_path}', fg='red',
                                   font=('helvetica', 12, 'bold'))
            self.canvas1.create_window(200, 285, window=self.label3)
        else:
            self.label3 = tk.Label(root, text='Не указано ни одного расширения файла', fg='red',
                                   font=('helvetica', 12, 'bold'))
            self.canvas1.create_window(200, 285, window=self.label3)

    # FUNCTION TO DELETE FILES FROM FOLDERS
    def clear_folder(self, new_path, extension):
        for folder_file in listdir(new_path):
            if not folder_file.endswith(extension):
                if os.path.isdir(os.path.join(new_path, folder_file)):
                    self.clear_folder(os.path.join(new_path, folder_file), extension)
                else:
                    send2trash(os.path.join(new_path, folder_file))
                    # print('Deleted: ' + os.path.join(new_path, folder_file))


root = tk.Tk()
gui = StartWindow(root)
root.mainloop()
