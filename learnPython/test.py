
import os
def open_app(app_dir):
    os.startfile(app_dir) #os.startfile（）打开外部应该程序，与windows双击相同
if __name__ == "__main__":
    app_dir = r'.\dist\doit.exe'#指定应用程序目录
    open_app(app_dir)