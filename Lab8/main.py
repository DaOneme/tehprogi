import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# Функция для выполнения конвертации
def convert():
    try:
        value = float(entry_value.get())
        unit_from = combo_from.get()
        unit_to = combo_to.get()

        # Таблица коэффициентов для конвертации из одной единицы в другую
        units_in_meters = {
            "Метр": 1,
            "Километр": 1000,
            "Миллиметр": 0.001
        }

        # Конвертируем исходное значение в метры
        value_in_meters = value * units_in_meters[unit_from]
        # Конвертируем из метров в целевую единицу
        result = value_in_meters / units_in_meters[unit_to]

        label_result.config(text=f"Результат: {result:.6f} {unit_to}")
    except ValueError:
        messagebox.showerror("Ошибка", "Пожалуйста, введите числовое значение.")

# Создаем главное окно
root = tk.Tk()
root.title("Конвертер единиц измерения")
root.geometry("400x200")  # Размер окна

# Ввод значения
label_prompt = ttk.Label(root, text="Введите значение:")
label_prompt.pack(pady=5)

entry_value = ttk.Entry(root)
entry_value.pack(pady=5)

# Выбор исходной единицы
frame_units = ttk.Frame(root)
frame_units.pack(pady=5)

ttk.Label(frame_units, text="Из:").grid(row=0, column=0, padx=5)
combo_from = ttk.Combobox(frame_units, values=["Метр", "Километр", "Миллиметр"])
combo_from.current(0)
combo_from.grid(row=0, column=1, padx=5)

ttk.Label(frame_units, text="В:").grid(row=0, column=2, padx=5)
combo_to = ttk.Combobox(frame_units, values=["Метр", "Километр", "Миллиметр"])
combo_to.current(1)
combo_to.grid(row=0, column=3, padx=5)

# Кнопка для запуска конвертации
button_convert = ttk.Button(root, text="Конвертировать", command=convert)
button_convert.pack(pady=10)

# Метка для отображения результата
label_result = ttk.Label(root, text="Результат:")
label_result.pack()

# Запуск главного цикла
root.mainloop()