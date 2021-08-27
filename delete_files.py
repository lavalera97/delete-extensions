import os
from os import listdir
from send2trash import send2trash
import tkinter as tk
from tkinter import messagebox


class StartWindow:
    def __init__(self, master):
        self.root = master
        self.root.title('Удаление ненужных файлов')
        self.canvas1 = tk.Canvas(self.root, width=400, height=400)
        self.canvas1.pack()

        self.label1 = tk.Label(self.root, text='Путь к папке для удаления файлов:', font=('helvetica', 10))
        self.canvas1.create_window(200, 100, window=self.label1)

        self.entry1 = tk.Entry(self.root, width=35)
        self.canvas1.create_window(200, 120, window=self.entry1)

        self.label2 = tk.Label(self.root, text='Расширениe файлов, которые надо удалить', font=('helvetica', 10))
        self.canvas1.create_window(200, 150, window=self.label2)

        self.entry2 = tk.Entry(self.root, width=35)
        self.canvas1.create_window(200, 170, window=self.entry2)

        self.label3 = tk.Label(self.root, text='Расширение файлов, которые не надо удалять', font=('helvetica', 10))
        self.canvas1.create_window(200, 200, window=self.label3)

        self.entry3 = tk.Entry(self.root, width=35)
        self.canvas1.create_window(200, 220, window=self.entry3)

        self.button1 = tk.Button(text='Удалить файлы', command=self.start_script, bg='brown', fg='white')
        self.canvas1.create_window(200, 255, window=self.button1)
        self.label4 = 0

    # FUNCTION TO INSERT PATH
    def start_script(self):
        if self.label4:
            self.label4.destroy()
        folder_path = self.entry1.get()
        remove_extension = self.entry2.get()
        stay_extension = self.entry3.get()
        if (os.path.exists(folder_path) and stay_extension != '') or (os.path.exists(folder_path) and remove_extension != ''):
            if (os.path.exists(folder_path) and stay_extension != '') \
                    and (os.path.exists(folder_path) and stay_extension != '' and remove_extension != ''):
                x = messagebox.askquestion(title='Удалить?', message=f'Вы действительно хотите удалить файлы без '
                                                                     f'расширения {stay_extension} в {folder_path}?')
                if x:
                    for file in listdir(folder_path):
                        if not file.endswith(stay_extension):
                            if os.path.isdir(os.path.join(folder_path, file)):
                                self.clear_folder(os.path.join(folder_path, file), stay_extension)
                            else:
                                send2trash(os.path.join(folder_path, file))
                                # print('Deleted: ' + os.path.join(folder_path, file))
                    self.label4 = tk.Label(root, text=f'{folder_path}\n'
                                                      f'Все файлы кроме расширений: {stay_extension} \n'
                                                      f'были перемещены в корзину!', fg='green', font=('helvetica', 12, 'bold'))
                    self.canvas1.create_window(200, 315, window=self.label4)
                else:
                    pass
            else:
                x = messagebox.askquestion(title='Удалить?', message=f'Вы действительно хотите удалить файлы с '
                                                                     f'расширением {remove_extension} в {folder_path}?')
                if x:
                    for file in listdir(folder_path):
                        if os.path.isdir(os.path.join(folder_path, file)):
                            self.delete_certain_extension(os.path.join(folder_path, file), remove_extension)
                        if file.endswith(remove_extension):
                            send2trash(os.path.join(folder_path, file))
                            # print('Deleted: ' + os.path.join(folder_path, file))
                    self.label4 = tk.Label(root, text=f'{folder_path}\n'
                                                      f'Все файлы с расширением: {remove_extension} \n'
                                                      f'были перемещены в корзину!', fg='green', font=('helvetica', 12, 'bold'))
                    self.canvas1.create_window(200, 315, window=self.label4)
                else:
                    pass
        elif not os.path.exists(folder_path):
            self.label4 = tk.Label(root, text=f'Указанного пути не существует:\n{folder_path}', fg='red',
                                   font=('helvetica', 12, 'bold'))
            self.canvas1.create_window(200, 305, window=self.label4)
        else:
            self.label4 = tk.Label(root, text='Не указано ни одного расширения файла\n', fg='red',
                                   font=('helvetica', 12, 'bold'))
            self.canvas1.create_window(200, 305, window=self.label4)

    # FUNCTION TO DELETE FILES FROM FOLDERS
    def clear_folder(self, new_path, extension):
        for folder_file in listdir(new_path):
            if not folder_file.endswith(extension):
                if os.path.isdir(os.path.join(new_path, folder_file)):
                    self.clear_folder(os.path.join(new_path, folder_file), extension)
                else:
                    send2trash(os.path.join(new_path, folder_file))
                    # print('Deleted: ' + os.path.join(new_path, folder_file))

    def delete_certain_extension(self, new_path, extension):
        for folder_file in listdir(new_path):
            if os.path.isdir(os.path.join(new_path, folder_file)):
                self.delete_certain_extension(os.path.join(new_path, folder_file), extension)
            if folder_file.endswith(extension):
                send2trash(os.path.join(new_path, folder_file))


root = tk.Tk()
gui = StartWindow(root)
root.mainloop()
