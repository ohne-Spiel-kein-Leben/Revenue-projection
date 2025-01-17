import pandas as pd
import xgboost as xgb
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt
import seaborn as sns
import tkinter as tk
from tkinter import filedialog, messagebox
import xlwings as xw

# 常量定义
RETAIN_COLUMNS = ['次留', '3留', '7留', '14留', '30留']
FEATURES = ['留存降幅', '次留', '3留', '7留', '14留', '30留', 'ARPU', '模拟每日活跃人数']


class PredictionApp:
    def __init__(self, master):
        self.master = master
        master.title("流水预估工具")

        self.label = tk.Label(master, text="请选择数据文件:")
        self.label.pack()

        self.file_button = tk.Button(master, text="导入文件", command=self.load_file)
        self.file_button.pack()

        self.predict_button = tk.Button(master, text="开始预测", command=self.predict)
        self.predict_button.pack()

        self.export_button = tk.Button(master, text="导出数据", command=self.export_data)
        self.export_button.pack()

        self.data = None
        
def load_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx;*.xls")])
        if file_path:
            self.data = pd.read_excel(file_path)
            messagebox.showinfo("信息", "文件导入成功!")
            
def predict(self):
        if self.data is None:
            messagebox.showwarning("警告", "请先导入数据文件!")
            return
    
        self.preprocess_data()
        features = self.data[FEATURES]
        target = self.data['充值金额']
        
        X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)
        
        model = xgb.XGBRegressor(objective='reg:squarederror')
        model.fit(X_train, y_train)