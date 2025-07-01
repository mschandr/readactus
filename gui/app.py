import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import mysql.connector
from mysql.connector import Error
import json
import os
from cryptography.fernet import Fernet

CONFIG_FILE = "readactus_config.json"
KEY_FILE = "readactus.key"

class ReadactusApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Readactus - Database Obfuscation Tool")
        self.root.geometry("900x500")

        self.left_db = {}
        self.right_db = {}

        self.key = self.load_or_create_key()
        self.cipher = Fernet(self.key)

        self.create_widgets()
        self.load_config()

    def load_or_create_key(self):
        if os.path.exists(KEY_FILE):
            with open(KEY_FILE, 'rb') as f:
                return f.read()
        key = Fernet.generate_key()
        with open(KEY_FILE, 'wb') as f:
            f.write(key)
        return key

    def create_widgets(self):
        main_frame = ttk.Frame(self.root, padding=10)
        main_frame.pack(fill=tk.BOTH, expand=True)

        # Left panel - Remote DB
        left_frame = ttk.LabelFrame(main_frame, text="Remote (Source) MySQL")
        left_frame.grid(row=0, column=0, padx=10, sticky="nsew")

        self.left_db['host'] = self._add_labeled_entry(left_frame, "MySQL Host:", 0)
        self.left_db['user'] = self._add_labeled_entry(left_frame, "MySQL User:", 1)
        self.left_db['password'] = self._add_labeled_entry(left_frame, "MySQL Password:", 2, show="*")
        self.left_db['port'] = self._add_labeled_entry(left_frame, "MySQL Port:", 3, default="3306")
        self.left_db['database'] = self._add_labeled_entry(left_frame, "MySQL DB:", 4)

        test_left_btn = ttk.Button(left_frame, text="Test Connection", command=lambda: self.test_connection(self.left_db))
        test_left_btn.grid(row=5, column=0, columnspan=2, pady=10)

        # Right panel - Local DB
        right_frame = ttk.LabelFrame(main_frame, text="Local (Target) MySQL")
        right_frame.grid(row=0, column=1, padx=10, sticky="nsew")

        self.right_db['host'] = self._add_labeled_entry(right_frame, "MySQL Host:", 0)
        self.right_db['user'] = self._add_labeled_entry(right_frame, "MySQL User:", 1)
        self.right_db['password'] = self._add_labeled_entry(right_frame, "MySQL Password:", 2, show="*")
        self.right_db['port'] = self._add_labeled_entry(right_frame, "MySQL Port:", 3, default="3306")
        self.right_db['database'] = self._add_labeled_entry(right_frame, "MySQL DB:", 4)

        test_right_btn = ttk.Button(right_frame, text="Test Connection", command=lambda: self.test_connection(self.right_db))
        test_right_btn.grid(row=5, column=0, columnspan=2, pady=10)

        # Save/Load config buttons
        config_frame = ttk.Frame(self.root)
        config_frame.pack(fill=tk.X, padx=10, pady=5)
        save_btn = ttk.Button(config_frame, text="Save Config", command=self.save_config)
        load_btn = ttk.Button(config_frame, text="Load Config", command=self.load_config)
        save_btn.pack(side=tk.LEFT, padx=5)
        load_btn.pack(side=tk.LEFT, padx=5)

        # Expand layout
        main_frame.columnconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)
        main_frame.rowconfigure(0, weight=1)

    def _add_labeled_entry(self, parent, label, row, show=None, default=""):
        ttk.Label(parent, text=label).grid(row=row, column=0, sticky="w", pady=5)
        entry = ttk.Entry(parent, show=show) if show else ttk.Entry(parent)
        entry.insert(0, default)
        entry.grid(row=row, column=1, sticky="ew", padx=5, pady=5)
        parent.columnconfigure(1, weight=1)
        return entry

    def test_connection(self, db_fields):
        host = db_fields['host'].get()
        port = db_fields['port'].get()
        user = db_fields['user'].get()
        password = db_fields['password'].get()
        database = db_fields['database'].get()
        try:
            connection = mysql.connector.connect(
                host=host,
                port=port,
                user=user,
                password=password,
                database=database
            )
            if connection.is_connected():
                messagebox.showinfo("Connection Test", "Connection successful!")
                connection.close()
        except Error as e:
            messagebox.showerror("Connection Test Failed", f"Error: {str(e)}")

    def save_config(self):
        config = {
            'left': {key: (self.cipher.encrypt(field.get().encode()).decode() if key == 'password' else field.get())
                     for key, field in self.left_db.items()},
            'right': {key: (self.cipher.encrypt(field.get().encode()).decode() if key == 'password' else field.get())
                      for key, field in self.right_db.items()}
        }
        with open(CONFIG_FILE, 'w') as f:
            json.dump(config, f, indent=4)
        messagebox.showinfo("Save Config", f"Configuration saved to {CONFIG_FILE}")

    def load_config(self):
        if not os.path.exists(CONFIG_FILE):
            return
        try:
            with open(CONFIG_FILE, 'r') as f:
                config = json.load(f)
            for key, field in self.left_db.items():
                field.delete(0, tk.END)
                value = config.get('left', {}).get(key, '')
                if key == 'password' and value:
                    try:
                        value = self.cipher.decrypt(value.encode()).decode()
                    except Exception:
                        value = ''
                field.insert(0, value)
            for key, field in self.right_db.items():
                field.delete(0, tk.END)
                value = config.get('right', {}).get(key, '')
                if key == 'password' and value:
                    try:
                        value = self.cipher.decrypt(value.encode()).decode()
                    except Exception:
                        value = ''
                field.insert(0, value)
            messagebox.showinfo("Load Config", f"Configuration loaded from {CONFIG_FILE}")
        except Exception as e:
            messagebox.showerror("Load Config Failed", f"Error: {str(e)}")

if __name__ == '__main__':
    root = tk.Tk()
    app = ReadactusApp(root)
    root.mainloop()

