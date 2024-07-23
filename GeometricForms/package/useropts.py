from maths.coordsystems import CartesianBoard
from data import Data
from maths.shapes2d import *
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import os

class Menu:

    def __init__(self):
        data = Data()
        self.dashboard = data.get_board()
        self.actions = {
            'Criar Forma Geométrica': self.criar,
            'Verificar as Formas Existentes': self.show_existing_shapes,
            'Sair': self.sair
        }

        # Initialize the main window
        self.root = tk.Tk()
        self.root.title("Formas Geométricas")
        self.root.geometry("700x750")  # Set the size of the window

        # Set background image
        self.set_background("background_image.jpg")  # Path to your background image

        # Create buttons for each action
        self.create_buttons()

    def set_background(self, image_path):
        try:
            # Get the absolute path of the image
            abs_image_path = os.path.join(os.path.dirname(__file__), image_path)
            print(f"Absolute image path: {abs_image_path}")  # Debug: print the absolute path

            # Load the image
            self.bg_image = Image.open(abs_image_path)
            self.bg_image = self.bg_image.resize((600, 550), Image.ANTIALIAS)  # Resize image to fit window
            self.bg_photo = ImageTk.PhotoImage(self.bg_image)
            
            # Create a label to hold the background image
            self.bg_label = tk.Label(self.root, image=self.bg_photo)
            self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        except FileNotFoundError:
            print(f"File not found: {abs_image_path}")
            messagebox.showerror("Error", f"Background image not found: {abs_image_path}")

    def create_buttons(self):
        # Create a frame to hold the buttons
        self.button_frame = tk.Frame(self.root, bg='white')
        self.button_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        
        # Create buttons with the same size and hover effect
        for action in self.actions:
            button = tk.Button(self.button_frame, text=action, command=self.actions[action], width=30, height=2, bg="white", fg="black")
            button.pack(pady=10)
            button.bind("<Enter>", lambda e, b=button: self.on_hover(b))
            button.bind("<Leave>", lambda e, b=button: self.on_leave(b))

    def on_hover(self, button):
        button.config(bg="black", fg="white")

    def on_leave(self, button):
        button.config(bg="white", fg="black")

    def criar(self):
        self.button_frame.destroy()
        self.create_shape_buttons()

    def create_shape_buttons(self):
        self.shape_frame = tk.Frame(self.root, bg='white')
        self.shape_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        shapes = ["Ponto", "Linha", "Círculo", "Triângulo", "Retângulo"]
        for shape in shapes:
            button = tk.Button(self.shape_frame, text=shape, command=lambda s=shape: self.create_shape(s), width=30, height=2, bg="white", fg="black")
            button.pack(pady=10)
            button.bind("<Enter>", lambda e, b=button: self.on_hover(b))
            button.bind("<Leave>", lambda e, b=button: self.on_leave(b))

        back_button = tk.Button(self.shape_frame, text="Voltar", command=self.back_to_main_menu, width=30, height=2, bg="white", fg="black")
        back_button.pack(pady=10)
        back_button.bind("<Enter>", lambda e, b=back_button: self.on_hover(b))
        back_button.bind("<Leave>", lambda e, b=back_button: self.on_leave(b))

        self.root.title("Escolha uma forma para criar")

    def create_shape(self, shape):
        self.shape_frame.destroy()
        self.show_shape_input_fields(shape)

    def show_shape_input_fields(self, shape):
        self.input_frame = tk.Frame(self.root, bg='white')
        self.input_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        
        tk.Label(self.input_frame, text="ID:", bg='white').pack(pady=3)
        self.id_entry = tk.Entry(self.input_frame)
        self.id_entry.pack(pady=5)

        # Labels and entry fields for point coordinates
        if shape == "Ponto":
            tk.Label(self.input_frame, text="Coordenada X:", bg='white').pack(pady=5)
            self.x_entry = tk.Entry(self.input_frame)
            self.x_entry.pack(pady=5)

            tk.Label(self.input_frame, text="Coordenada Y:", bg='white').pack(pady=5)
            self.y_entry = tk.Entry(self.input_frame)
            self.y_entry.pack(pady=5)
            
            create_button = tk.Button(self.input_frame, text="Criar", command=lambda: self.create_point(), width=30, height=2, bg="white", fg="black")
        
        if shape == "Linha":
            tk.Label(self.input_frame, text="Coordenada X1:", bg='white').pack(pady=3)
            self.x1_entry = tk.Entry(self.input_frame)
            self.x1_entry.pack(pady=5)

            tk.Label(self.input_frame, text="Coordenada Y1:", bg='white').pack(pady=3)
            self.y1_entry = tk.Entry(self.input_frame)
            self.y1_entry.pack(pady=5)

            tk.Label(self.input_frame, text="Coordenada X2:", bg='white').pack(pady=3)
            self.x2_entry = tk.Entry(self.input_frame)
            self.x2_entry.pack(pady=5)

            tk.Label(self.input_frame, text="Coordenada Y2:", bg='white').pack(pady=3)
            self.y2_entry = tk.Entry(self.input_frame)
            self.y2_entry.pack(pady=5)

            create_button = tk.Button(self.input_frame, text="Criar", command=lambda: self.create_line(), width=30, height=2, bg="white", fg="black")
        
        if shape == "Círculo":
            tk.Label(self.input_frame, text="Coordenada X:", bg='white').pack(pady=3)
            self.x_entry = tk.Entry(self.input_frame)
            self.x_entry.pack(pady=5)

            tk.Label(self.input_frame, text="Coordenada Y:", bg='white').pack(pady=3)
            self.y_entry = tk.Entry(self.input_frame)
            self.y_entry.pack(pady=5)

            tk.Label(self.input_frame, text="Raio do círculo:", bg='white').pack(pady=3)
            self._radius = tk.Entry(self.input_frame)
            self._radius.pack(pady=5)

            create_button = tk.Button(self.input_frame, text="Criar", command=lambda: self.create_circle(), width=30, height=2, bg="white", fg="black")
        
        if shape == "Triângulo":
            tk.Label(self.input_frame, text="Coordenada X1:", bg='white').pack(pady=3)
            self.x1_entry = tk.Entry(self.input_frame)
            self.x1_entry.pack(pady=5)

            tk.Label(self.input_frame, text="Coordenada Y1:", bg='white').pack(pady=3)
            self.y1_entry = tk.Entry(self.input_frame)
            self.y1_entry.pack(pady=5)

            tk.Label(self.input_frame, text="Coordenada X2:", bg='white').pack(pady=3)
            self.x2_entry = tk.Entry(self.input_frame)
            self.x2_entry.pack(pady=5)

            tk.Label(self.input_frame, text="Coordenada Y2:", bg='white').pack(pady=3)
            self.y2_entry = tk.Entry(self.input_frame)
            self.y2_entry.pack(pady=5)

            tk.Label(self.input_frame, text="Coordenada X3:", bg='white').pack(pady=3)
            self.x3_entry = tk.Entry(self.input_frame)
            self.x3_entry.pack(pady=5)

            tk.Label(self.input_frame, text="Coordenada Y3:", bg='white').pack(pady=3)
            self.y3_entry = tk.Entry(self.input_frame)
            self.y3_entry.pack(pady=5)

            create_button = tk.Button(self.input_frame, text="Criar", command=lambda: self.create_triangle(), width=30, height=2, bg="white", fg="black")
        
        if shape == "Retângulo":
            tk.Label(self.input_frame, text="Coordenada X1:", bg='white').pack(pady=3)
            self.x1_entry = tk.Entry(self.input_frame)
            self.x1_entry.pack(pady=5)

            tk.Label(self.input_frame, text="Coordenada Y1:", bg='white').pack(pady=3)
            self.y1_entry = tk.Entry(self.input_frame)
            self.y1_entry.pack(pady=5)

            tk.Label(self.input_frame, text="Coordenada X2:", bg='white').pack(pady=3)
            self.x2_entry = tk.Entry(self.input_frame)
            self.x2_entry.pack(pady=5)

            tk.Label(self.input_frame, text="Coordenada Y2:", bg='white').pack(pady=3)
            self.y2_entry = tk.Entry(self.input_frame)
            self.y2_entry.pack(pady=5)

            create_button = tk.Button(self.input_frame, text="Criar", command=lambda: self.create_rectangle(), width=30, height=2, bg="white", fg="black")
        
        create_button.pack(pady=10)
        create_button.bind("<Enter>", lambda e, b=create_button: self.on_hover(b))
        create_button.bind("<Leave>", lambda e, b=create_button: self.on_leave(b))

        back_button = tk.Button(self.input_frame, text="Voltar", command=self.back_to_shape_menu, width=30, height=2, bg="white", fg="black")
        back_button.pack(pady=10)
        back_button.bind("<Enter>", lambda e, b=back_button: self.on_hover(b))
        back_button.bind("<Leave>", lambda e, b=back_button: self.on_leave(b))

        self.root.title(f"Criar {shape}")

    def create_point(self):
        try:
            id = int(self.id_entry.get())
            x = float(self.x_entry.get())
            y = float(self.y_entry.get())
            point = Point(id, x, y)
            self.dashboard.insertShape(point)
            messagebox.showinfo("Sucesso", "Ponto criado com sucesso!")
            self.back_to_shape_menu()
        except ValueError:
            messagebox.showerror("Erro", "Por favor, insira valores válidos.")

    def create_line(self):
        try:
            id = int(self.id_entry.get())
            x1 = float(self.x1_entry.get())
            y1 = float(self.y1_entry.get())
            x2 = float(self.x2_entry.get())
            y2 = float(self.y2_entry.get())
            line = Line(id, x1, y1, x2, y2)
            self.dashboard.insertShape(line)
            messagebox.showinfo("Sucesso", "Linha criada com sucesso!")
            self.back_to_shape_menu()
        except ValueError:
            messagebox.showerror("Erro", "Por favor, insira valores válidos.")

    def create_circle(self):
        try:
            id = int(self.id_entry.get())
            x = float(self.x_entry.get())
            y = float(self.y_entry.get())
            radius = float(self._radius.get())
            circle = Circle(id, x, y, radius)
            self.dashboard.insertShape(circle)
            messagebox.showinfo("Sucesso", "Círculo criado com sucesso!")
            self.back_to_shape_menu()
        except ValueError:
            messagebox.showerror("Erro", "Por favor, insira valores válidos.")
    
    def create_rectangle(self):
        try:
            id = int(self.id_entry.get())
            x1 = float(self.x1_entry.get())
            y1 = float(self.y1_entry.get())
            x2 = float(self.x2_entry.get())
            y2 = float(self.y2_entry.get())
            retangulo = Rectangle(id, x1, y1, x2, y2)
            self.dashboard.insertShape(retangulo)
            messagebox.showinfo("Sucesso", "Retângulo criado com sucesso!")
            self.back_to_shape_menu()
        except ValueError:
            messagebox.showerror("Erro", "Por favor, insira valores válidos.")
    
    def create_triangle(self):
        try:
            id = int(self.id_entry.get())
            x1 = float(self.x1_entry.get())
            y1 = float(self.y1_entry.get())
            x2 = float(self.x2_entry.get())
            y2 = float(self.y2_entry.get())
            x3 = float(self.x3_entry.get())
            y3 = float(self.y3_entry.get())
            triangulo = Triangle(id, x1, y1, x2, y2, x3, y3)
            self.dashboard.insertShape(triangulo)
            messagebox.showinfo("Sucesso", "Triângulo criado com sucesso!")
            self.back_to_shape_menu()
        except ValueError:
            messagebox.showerror("Erro", "Por favor, insira valores válidos.")

    def show_existing_shapes(self):
        self.button_frame.destroy()

        # Destroy any existing voltar_button_frame to avoid overlap
        if hasattr(self, 'voltar_button_frame'):
            self.voltar_button_frame.destroy()

        self.existing_shapes_frame = tk.Frame(self.root, bg='white')
        self.existing_shapes_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        # Create a canvas widget
        canvas = tk.Canvas(self.existing_shapes_frame, bg='white', width=500, height=350)
        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Create a scrollbar widget
        scrollbar = tk.Scrollbar(self.existing_shapes_frame, orient="vertical", command=canvas.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Configure the canvas
        canvas.configure(yscrollcommand=scrollbar.set)
        canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

        # Create a frame inside the canvas
        shape_frame = tk.Frame(canvas, bg='white')
        canvas.create_window((0, 0), window=shape_frame, anchor="nw")

        # Add shapes to the frame, two per line
        shapes = list(self.dashboard.shapes.keys())
        for i in range(0, len(shapes), 2):
            row_frame = tk.Frame(shape_frame, bg='white')
            row_frame.pack(fill=tk.X, pady=5)
            button1 = tk.Button(row_frame, text=shapes[i], command=lambda s=shapes[i]: self.show_shape_details(s), width=20, height=2, bg="white", fg="black")
            button1.pack(side=tk.LEFT, padx=10)
            button1.bind("<Enter>", lambda e, b=button1: self.on_hover(b))
            button1.bind("<Leave>", lambda e, b=button1: self.on_leave(b))
            if i + 1 < len(shapes):
                button2 = tk.Button(row_frame, text=shapes[i + 1], command=lambda s=shapes[i + 1]: self.show_shape_details(s), width=20, height=2, bg="white", fg="black")
                button2.pack(side=tk.LEFT, padx=10)
                button2.bind("<Enter>", lambda e, b=button2: self.on_hover(b))
                button2.bind("<Leave>", lambda e, b=button2: self.on_leave(b))

        # Add the "Voltar" button outside the scrollable area, at the bottom of the main window
        self.voltar_button_frame = tk.Frame(self.root, bg='white')
        self.voltar_button_frame.place(relx=0.5, rely=1.0, anchor=tk.S)
        back_button = tk.Button(self.voltar_button_frame, text="Voltar", command=self.back_to_main_menu, width=30, height=2, bg="white", fg="black")
        back_button.pack(pady=10)
        back_button.bind("<Enter>", lambda e, b=back_button: self.on_hover(b))
        back_button.bind("<Leave>", lambda e, b=back_button: self.on_leave(b))

        self.root.title("Formas Existentes")
        self.details_frame_line.destroy()
        self.details_frame_point.destroy()
        self.details_frame_circle.destroy()

    def show_shape_details(self, shape_key):
        shape = self.dashboard.getShape(shape_key)
        self.existing_shapes_frame.destroy()
        self.voltar_button_frame.destroy()
        if isinstance(shape, Circle):
            self._show_circle_details(shape)
        if isinstance(shape, Point):
            self._show_point_details(shape)
        if isinstance(shape, Line):
            self._show_line_details(shape)
        if isinstance(shape, Rectangle):
            self._show_rectangle_details(shape)
        if isinstance(shape, Triangle):
            self._show_triangle_details(shape)
        
    def _show_point_details(self, point):
        # Create a new frame for point details
        self.details_frame_point = tk.Frame(self.root, bg='white')
        self.details_frame_point.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        # Display point coordinates
        tk.Label(self.details_frame_point, text=f"Ponto {point.getNumber()}", bg='white', font=('Helvetica', 14)).pack(pady=10)
        tk.Label(self.details_frame_point, text=f"Coordenadas: ({point._x}, {point._y})", bg='white').pack(pady=5)

        # Frame for actions
        action_frame = tk.Frame(self.details_frame_point, bg='white')
        action_frame.pack(pady=10)

        # Edit coordinates
        tk.Label(action_frame, text="Editar Coordenadas", bg='white').grid(row=0, column=0, padx=10)
        tk.Label(action_frame, text="Novo X:", bg='white').grid(row=1, column=0, pady=5)
        self.new_x_entry = tk.Entry(action_frame)
        self.new_x_entry.grid(row=2, column=0, pady=5)
        tk.Label(action_frame, text="Novo Y:", bg='white').grid(row=3, column=0, pady=5)
        self.new_y_entry = tk.Entry(action_frame)
        self.new_y_entry.grid(row=4, column=0, pady=5)
        tk.Button(action_frame, text="Atualizar Ponto", command=lambda: self.update_point(point), width=20, bg="white", fg="black").grid(row=5, column=0, pady=10)

        # Create selection bars for other points
        tk.Label(action_frame, text="Calcular Distância", bg='white').grid(row=0, column=1, padx=10)
        tk.Label(action_frame, text="Selecionar Outro Ponto:", bg='white').grid(row=1, column=1, pady=5)
        self.distance_point_var = tk.StringVar(action_frame)
        self.distance_point_var.set("Selecione um ponto")  # Default value
        self.distance_point_menu = tk.OptionMenu(action_frame, self.distance_point_var, *self.get_point_ids())
        self.distance_point_menu.grid(row=2, column=1, pady=5)
        tk.Button(action_frame, text="Calcular Distância", command=lambda: self.calculate_distance(point), width=20, bg="white", fg="black").grid(row=3, column=1, pady=10)

        # Midpoint calculation
        tk.Label(action_frame, text="Calcular Ponto Médio", bg='white').grid(row=0, column=2, padx=10)
        tk.Label(action_frame, text="Selecionar Outro Ponto:", bg='white').grid(row=1, column=2, pady=5)
        self.midpoint_point_var = tk.StringVar(action_frame)
        self.midpoint_point_var.set("Selecione um ponto")  # Default value
        self.midpoint_point_menu = tk.OptionMenu(action_frame, self.midpoint_point_var, *self.get_point_ids())
        self.midpoint_point_menu.grid(row=2, column=2, pady=5)
        tk.Button(action_frame, text="Calcular Ponto Médio", command=lambda: self.calculate_midpoint(point), width=20, bg="white", fg="black").grid(row=3, column=2, pady=10)

        # Back button
        tk.Button(self.details_frame_point, text="Voltar", command=self.show_existing_shapes, width=20, bg="white", fg="black").pack(pady=10)

        self.root.title(f"Detalhes do Ponto {point.getNumber()}")

    def get_point_ids(self):
        """ Returns a list of point IDs for the selection bars, excluding circles. """
        return [shape.getType() + str(shape.getNumber()) 
                for shape in self.dashboard.shapes.values() 
                if isinstance(shape, Point) and not isinstance(shape, Circle)]

    def update_point(self, point):
        try:
            new_x = float(self.new_x_entry.get())
            new_y = float(self.new_y_entry.get())
            point.updateCoord(new_x, new_y)
            messagebox.showinfo("Atualização", "Ponto atualizado com sucesso!")
            self.details_frame_point.destroy()
            self.show_existing_shapes()
        except ValueError:
            messagebox.showerror("Erro", "Por favor, insira valores válidos.")

    def calculate_distance(self, point):
        try:
            other_id = self.distance_point_var.get()
            if other_id == "Selecione um ponto":
                raise ValueError("Por favor, selecione um ponto válido.")
            
            other_point = self.dashboard.getShape(other_id)
            
            if not isinstance(other_point, Point):
                raise ValueError("A forma selecionada não é um ponto.")
            
            distance = point.distanceTo(other_point)
            messagebox.showinfo("Distância", f"A distância é {distance:.2f} cm")
            
        except KeyError:
            messagebox.showerror("Erro", f"Ponto com ID {other_id} não encontrado.")
        except ValueError as e:
            messagebox.showerror("Erro", str(e))
        except Exception as e:
            messagebox.showerror("Erro", f"Ocorreu um erro: {str(e)}")

    def calculate_midpoint(self, point):
        try:
            other_id = self.midpoint_point_var.get()
            if other_id == "Selecione um ponto":
                raise ValueError("Por favor, selecione um ponto válido.")
            
            other_point = self.dashboard.getShape(other_id)
            
            if not isinstance(other_point, Point):
                raise ValueError("A forma selecionada não é um ponto.")
            
            midpoint = point.midpoint(other_point)
            messagebox.showinfo("Ponto Médio", f"O ponto médio é ({midpoint._x}, {midpoint._y})")
            
        except ValueError as e:
            messagebox.showerror("Erro", str(e))
        except Exception as e:
            messagebox.showerror("Erro", f"Ocorreu um erro: {str(e)}")

    def _show_line_details(self, line):
        # Create a new frame for line details
        self.details_frame_line = tk.Frame(self.root, bg='white')
        self.details_frame_line.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        # Display line coordinates and other information
        tk.Label(self.details_frame_line, text=f"Linha {line.getNumber()}", bg='white', font=('Helvetica', 14)).pack(pady=10)
        tk.Label(self.details_frame_line, text=f"Coordenadas: ({line._p1._x:.2f}, {line._p1._y:.2f}) e ({line._p2._x:.2f}, {line._p2._y:.2f})", bg='white').pack(pady=5)
        tk.Label(self.details_frame_line, text=f"Comprimento: {line.length():.2f} cm", bg='white').pack(pady=5)
        tk.Label(self.details_frame_line, text=f"Inclinação: {line.slope() if not line.verifyVertical() else 'Vertical'}", bg='white').pack(pady=5)

        # Frame for actions
        action_frame = tk.Frame(self.details_frame_line, bg='white')
        action_frame.pack(pady=10)

        # Edit coordinates
        tk.Label(action_frame, text="Editar Coordenadas", bg='white').grid(row=0, column=0, padx=10)
        tk.Label(action_frame, text="Novo X1:", bg='white').grid(row=1, column=0, pady=5)
        self.new_x1_entry = tk.Entry(action_frame)
        self.new_x1_entry.grid(row=2, column=0, pady=5)
        tk.Label(action_frame, text="Novo Y1:", bg='white').grid(row=3, column=0, pady=5)
        self.new_y1_entry = tk.Entry(action_frame)
        self.new_y1_entry.grid(row=4, column=0, pady=5)
        tk.Label(action_frame, text="Novo X2:", bg='white').grid(row=5, column=0, pady=5)
        self.new_x2_entry = tk.Entry(action_frame)
        self.new_x2_entry.grid(row=6, column=0, pady=5)
        tk.Label(action_frame, text="Novo Y2:", bg='white').grid(row=7, column=0, pady=5)
        self.new_y2_entry = tk.Entry(action_frame)
        self.new_y2_entry.grid(row=8, column=0, pady=5)
        tk.Button(action_frame, text="Atualizar Linha", command=lambda: self.update_line(line), width=20, bg="white", fg="black").grid(row=9, column=0, pady=10)

        # Check if a point is on the line
        tk.Label(action_frame, text="Verificar Ponto na Linha", bg='white').grid(row=0, column=1, padx=10)
        tk.Label(action_frame, text="Selecionar Ponto:", bg='white').grid(row=1, column=1, pady=5)
        self.point_on_line_var = tk.StringVar(action_frame)
        self.point_on_line_var.set("Selecione um ponto")  # Default value
        self.point_on_line_menu = tk.OptionMenu(action_frame, self.point_on_line_var, *self.get_point_ids())
        self.point_on_line_menu.grid(row=2, column=1, pady=5)
        tk.Button(action_frame, text="Verificar Ponto", command=lambda: self.check_point_on_line(line), width=20, bg="white", fg="black").grid(row=3, column=1, pady=10)

        # Check if a line is parallel to another line
        tk.Label(action_frame, text="Verificar Paralelismo", bg='white').grid(row=0, column=2, padx=10)
        tk.Label(action_frame, text="Selecionar Linha:", bg='white').grid(row=1, column=2, pady=5)
        self.line_parallel_var = tk.StringVar(action_frame)
        self.line_parallel_var.set("Selecione uma linha")  # Default value
        self.line_parallel_menu = tk.OptionMenu(action_frame, self.line_parallel_var, *self.get_line_ids())
        self.line_parallel_menu.grid(row=2, column=2, pady=5)
        tk.Button(action_frame, text="Verificar Paralelismo", command=lambda: self.check_line_parallel(line), width=20, bg="white", fg="black").grid(row=3, column=2, pady=10)

        # Back button
        tk.Button(self.details_frame_line, text="Voltar", command=self.show_existing_shapes, width=20, bg="white", fg="black").pack(pady=10)

        self.root.title(f"Detalhes da Linha {line.getNumber()}")
    
    def get_line_ids(self):
        """ Returns a list of line IDs for the selection bars. """
        return [shape.getType() + str(shape.getNumber()) 
                for shape in self.dashboard.shapes.values() 
                if isinstance(shape, Line)]

    def check_point_on_line(self, line):
        try:
            point_id = self.point_on_line_var.get()
            if point_id == "Selecione um ponto":
                raise ValueError("Por favor, selecione um ponto válido.")
            
            point = self.dashboard.getShape(point_id)
            
            if not isinstance(point, Point):
                raise ValueError("A forma selecionada não é um ponto.")
            
            if line.pointOnLine(point):
                messagebox.showinfo("Verificação de Ponto", f"O ponto {point_id} está na linha {line.getNumber()}.")
            else:
                messagebox.showinfo("Verificação de Ponto", f"O ponto {point_id} não está na linha {line.getNumber()}.")
                
        except KeyError:
            messagebox.showerror("Erro", f"Ponto com ID {point_id} não encontrado.")
        except ValueError as e:
            messagebox.showerror("Erro", str(e))
        except Exception as e:
            messagebox.showerror("Erro", f"Ocorreu um erro: {str(e)}")

    def check_line_parallel(self, line):
        try:
            line_id = self.line_parallel_var.get()
            if line_id == "Selecione uma linha":
                raise ValueError("Por favor, selecione uma linha válida.")
            
            other_line = self.dashboard.getShape(line_id)
            
            if not isinstance(other_line, Line):
                raise ValueError("A forma selecionada não é uma linha.")
            
            if line.isParallel(other_line):
                messagebox.showinfo("Verificação de Paralelismo entre linhas", f"A linha {line.getNumber()} é paralela à linha {other_line.getNumber()}.")
            else:
                messagebox.showinfo("Verificação de Paralelismo entre linhas", f"A linha {line.getNumber()} não é paralela à linha {other_line.getNumber()}.")
                
        except KeyError:
            messagebox.showerror("Erro", f"Linha com ID {line_id} não encontrada.")
        except ValueError as e:
            messagebox.showerror("Erro", str(e))
        except Exception as e:
            messagebox.showerror("Erro", f"Ocorreu um erro: {str(e)}")
    
    def update_line(self, line):
        try:
            x1 = float(self.new_x1_entry.get())
            y1 = float(self.new_y1_entry.get())
            x2 = float(self.new_x2_entry.get())
            y2 = float(self.new_y2_entry.get())
            
            line.updateCoord(x1, y1, x2, y2)
            messagebox.showinfo("Atualizar Linha", f"A linha {line.getNumber()} foi atualizada para as novas coordenadas ({x1}, {y1}) e ({x2}, {y2}).")
            self.details_frame_line.destroy()
            self.show_existing_shapes()
            
        except ValueError:
            messagebox.showerror("Erro", "Por favor, insira valores válidos para as coordenadas.")
        

    def _show_circle_details(self, circle):
        # Create a new frame for circle details
        self.details_frame_circle = tk.Frame(self.root, bg='white')
        self.details_frame_circle.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        # Display circle details
        tk.Label(self.details_frame_circle, text=f"Círculo {circle.getNumber()}", bg='white', font=('Helvetica', 14), anchor='w').pack(pady=10)
        tk.Label(self.details_frame_circle, text=f"Centro: ({circle._x}, {circle._y})", bg='white', anchor='w').pack(pady=5)
        tk.Label(self.details_frame_circle, text=f"Raio: {circle._radius} cm", bg='white', anchor='w').pack(pady=5)
        tk.Label(self.details_frame_circle, text=f"Área: {circle.area():.2f} cm²", bg='white', anchor='w').pack(pady=5)
        tk.Label(self.details_frame_circle, text=f"Perímetro: {circle.perimeter():.2f} cm", bg='white', anchor='w').pack(pady=5)
        tk.Label(self.details_frame_circle, text=f"Diâmetro: {circle.diameter():.2f} cm", bg='white', anchor='w').pack(pady=5)
        tk.Label(self.details_frame_circle, text=f"Circunferência: {circle.circumference():.2f} cm", bg='white', anchor='w').pack(pady=5)

        # Frame for actions
        action_frame = tk.Frame(self.details_frame_circle, bg='white')
        action_frame.pack(pady=10)

        # Update coordinates
        tk.Label(action_frame, text="Editar Coordenadas", bg='white', anchor='w').grid(row=0, column=0, padx=10, sticky='w')
        tk.Label(action_frame, text="Novo X:", bg='white', anchor='w').grid(row=1, column=0, pady=5, sticky='w')
        self.new_x_entry = tk.Entry(action_frame)
        self.new_x_entry.grid(row=2, column=0, pady=5, sticky='w')
        tk.Label(action_frame, text="Novo Y:", bg='white', anchor='w').grid(row=3, column=0, pady=5, sticky='w')
        self.new_y_entry = tk.Entry(action_frame)
        self.new_y_entry.grid(row=4, column=0, pady=5, sticky='w')
        tk.Label(action_frame, text="Novo Raio:", bg='white', anchor='w').grid(row=5, column=0, pady=5, sticky='w')
        self.new_radius_entry = tk.Entry(action_frame)
        self.new_radius_entry.grid(row=6, column=0, pady=5, sticky='w')
        tk.Button(action_frame, text="Atualizar Círculo", command=lambda: self.update_circle(circle), width=20, bg="white", fg="black").grid(row=7, column=0, pady=10, sticky='w')

        # Translate circle
        tk.Label(action_frame, text="Transladar Círculo", bg='white', anchor='w').grid(row=0, column=1, padx=10, sticky='w')
        tk.Label(action_frame, text="Delta X:", bg='white', anchor='w').grid(row=1, column=1, pady=5, sticky='w')
        self.dx_entry = tk.Entry(action_frame)
        self.dx_entry.grid(row=2, column=1, pady=5, sticky='w')
        tk.Label(action_frame, text="Delta Y:", bg='white', anchor='w').grid(row=3, column=1, pady=5, sticky='w')
        self.dy_entry = tk.Entry(action_frame)
        self.dy_entry.grid(row=4, column=1, pady=5, sticky='w')
        tk.Button(action_frame, text="Transladar", command=lambda: self.translate_circle(circle), width=20, bg="white", fg="black").grid(row=5, column=1, pady=10, sticky='w')

        # Scale circle
        tk.Label(action_frame, text="Escalar Círculo", bg='white', anchor='w').grid(row=0, column=2, padx=10, sticky='w')
        tk.Label(action_frame, text="Fator de Escala:", bg='white', anchor='w').grid(row=1, column=2, pady=5, sticky='w')
        self.scale_factor_entry = tk.Entry(action_frame)
        self.scale_factor_entry.grid(row=2, column=2, pady=5, sticky='w')
        tk.Button(action_frame, text="Escalar", command=lambda: self.scale_circle(circle), width=20, bg="white", fg="black").grid(row=3, column=2, pady=10, sticky='w')

        # Check if concentric and tangent
        check_frame = tk.Frame(self.details_frame_circle, bg='white')
        check_frame.pack(pady=10)

        # Check if concentric
        tk.Label(check_frame, text="Verificar Concentricidade", bg='white', anchor='w').grid(row=0, column=0, padx=10, sticky='w')
        tk.Label(check_frame, text="Selecionar Círculo:", bg='white', anchor='w').grid(row=1, column=0, pady=5, sticky='w')
        self.concentric_var = tk.StringVar(check_frame)
        self.concentric_var.set("Selecione um círculo")  # Default value
        self.concentric_menu = tk.OptionMenu(check_frame, self.concentric_var, *self.get_circle_ids())
        self.concentric_menu.grid(row=2, column=0, pady=5, sticky='w')
        tk.Button(check_frame, text="Verificar", command=lambda: self.check_concentric(circle), width=20, bg="white", fg="black").grid(row=3, column=0, pady=10, sticky='w')

        # Check if tangent
        tk.Label(check_frame, text="Verificar Tangência", bg='white', anchor='w').grid(row=0, column=1, padx=10, sticky='w')
        tk.Label(check_frame, text="Selecionar Círculo:", bg='white', anchor='w').grid(row=1, column=1, pady=5, sticky='w')
        self.tangent_var = tk.StringVar(check_frame)
        self.tangent_var.set("Selecione um círculo")  # Default value
        self.tangent_menu = tk.OptionMenu(check_frame, self.tangent_var, *self.get_circle_ids())
        self.tangent_menu.grid(row=2, column=1, pady=5, sticky='w')
        tk.Button(check_frame, text="Verificar", command=lambda: self.check_tangent(circle), width=20, bg="white", fg="black").grid(row=3, column=1, pady=10, sticky='w')

        # Back button
        tk.Button(self.details_frame_circle, text="Voltar", command=self.back_to_main_menu, width=20, bg="white", fg="black").pack(pady=10)

        # Update window title
        self.root.title(f"Detalhes do Círculo {circle.getNumber()}")
        self.details_frame_point.destroy()

    def get_circle_ids(self):
        """ Returns a list of circle IDs """
        return [shape.getType() + str(shape.getNumber()) 
                for shape in self.dashboard.shapes.values() 
                if isinstance(shape, Circle)]

    def update_circle(self, circle):
        try:
            x = float(self.new_x_entry.get())
            y = float(self.new_y_entry.get())
            radius = float(self.new_radius_entry.get())
            
            circle.updateCoord(x, y, radius)
            messagebox.showinfo("Atualizar Círculo", f"O círculo {circle.getNumber()} foi atualizado para o centro ({x}, {y}) e raio {radius} cm.")
            self.details_frame_circle.destroy()
            self.show_existing_shapes()  # Refresh the shapes list
            
        except ValueError:
            messagebox.showerror("Erro", "Por favor, insira valores válidos para as coordenadas e o raio.")

    def translate_circle(self, circle):
        try:
            dx = float(self.dx_entry.get())
            dy = float(self.dy_entry.get())
            
            circle.translate(dx, dy)
            messagebox.showinfo("Transladar Círculo", f"O círculo {circle.getNumber()} foi transladado para ({circle._x}, {circle._y}).")
            self.show_existing_shapes()  # Refresh the shapes list
            
        except ValueError:
            messagebox.showerror("Erro", "Por favor, insira valores válidos para delta X e delta Y.")

    def scale_circle(self, circle):
        try:
            factor = float(self.scale_factor_entry.get())
            
            circle.scale(factor)
            messagebox.showinfo("Escalar Círculo", f"O círculo {circle.getNumber()} foi escalado para o raio {circle._radius:.2f} cm.")
            self.show_existing_shapes()  # Refresh the shapes list
            
        except ValueError:
            messagebox.showerror("Erro", "Por favor, insira um valor válido para o fator de escala.")

    def check_concentric(self, circle):
        try:
            circle_id = self.concentric_var.get()
            if circle_id == "Selecione um círculo":
                raise ValueError("Por favor, selecione um círculo válido.")
            
            other_circle = self.dashboard.getShape(circle_id)
            
            if not isinstance(other_circle, Circle):
                raise ValueError("A forma selecionada não é um círculo.")
            
            if circle.isConcentric(other_circle):
                messagebox.showinfo("Verificação de Concentricidade", f"O círculo {circle.getNumber()} é concêntrico com o círculo {other_circle.getNumber()}.")
            else:
                messagebox.showinfo("Verificação de Concentricidade", f"O círculo {circle.getNumber()} não é concêntrico com o círculo {other_circle.getNumber()}.")
                
        except KeyError:
            messagebox.showerror("Erro", f"Círculo com ID {circle_id} não encontrado.")
        except Exception as e:
            messagebox.showerror("Erro", f"Ocorreu um erro: {str(e)}")

    def check_tangent(self, circle):
        try:
            circle_id = self.tangent_var.get()
            if circle_id == "Selecione um círculo":
                raise ValueError("Por favor, selecione um círculo válido.")
            
            other_circle = self.dashboard.getShape(circle_id)
            
            if not isinstance(other_circle, Circle):
                raise ValueError("A forma selecionada não é um círculo.")
            
            if circle.isTangent(other_circle):
                messagebox.showinfo("Verificação de Tangência", f"O círculo {circle.getNumber()} é tangente ao círculo {other_circle.getNumber()}.")
            else:
                messagebox.showinfo("Verificação de Tangência", f"O círculo {circle.getNumber()} não é tangente ao círculo {other_circle.getNumber()}.")
                
        except KeyError:
            messagebox.showerror("Erro", f"Círculo com ID {circle_id} não encontrado.")
        except Exception as e:
            messagebox.showerror("Erro", f"Ocorreu um erro: {str(e)}")

    def _show_rectangle_details(self, rectangle):
        # Create a new frame for rectangle details
        self.details_frame_rectangle = tk.Frame(self.root, bg='white')
        self.details_frame_rectangle.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        
        tk.Label(self.details_frame_rectangle, text=f"Retângulo {rectangle.getNumber()}", bg='white', font=('Helvetica', 14)).grid(row=0, column=0, columnspan=2, pady=10)
        tk.Label(self.details_frame_rectangle, text=f"Coordenadas: Ponto 1 ({rectangle._p1._x:.2f}, {rectangle._p1._y:.2f}) e Ponto 2 ({rectangle._p2._x:.2f}, {rectangle._p2._y:.2f})", bg='white').grid(row=1, column=0, columnspan=2, pady=5)
        tk.Label(self.details_frame_rectangle, text=f"Área: {rectangle.area():.2f} cm²", bg='white').grid(row=2, column=0, columnspan=2, pady=5)
        tk.Label(self.details_frame_rectangle, text=f"Perímetro: {rectangle.perimeter():.2f} cm", bg='white').grid(row=3, column=0, columnspan=2, pady=5)
        tk.Label(self.details_frame_rectangle, text=f"Diagonal: {rectangle.diagonal():.2f} cm", bg='white').grid(row=4, column=0, columnspan=2, pady=5)
        tk.Label(self.details_frame_rectangle, text=f"É um quadrado: {'Sim' if rectangle.isSquare() else 'Não'}", bg='white').grid(row=5, column=0, columnspan=2, pady=5)

        action_frame = tk.Frame(self.details_frame_rectangle, bg='white')
        action_frame.grid(row=6, column=0, columnspan=2, pady=10, sticky='ew')

        # Update coordinates
        tk.Label(action_frame, text="Editar Coordenadas", bg='white').grid(row=0, column=0, padx=10, sticky='w')
        tk.Label(action_frame, text="Novo X1:", bg='white').grid(row=1, column=0, pady=5, sticky='w')
        self.new_x1_entry = tk.Entry(action_frame)
        self.new_x1_entry.grid(row=2, column=0, pady=5, sticky='w')
        tk.Label(action_frame, text="Novo Y1:", bg='white').grid(row=3, column=0, pady=5, sticky='w')
        self.new_y1_entry = tk.Entry(action_frame)
        self.new_y1_entry.grid(row=4, column=0, pady=5, sticky='w')
        tk.Label(action_frame, text="Novo X2:", bg='white').grid(row=5, column=0, pady=5, sticky='w')
        self.new_x2_entry = tk.Entry(action_frame)
        self.new_x2_entry.grid(row=6, column=0, pady=5, sticky='w')
        tk.Label(action_frame, text="Novo Y2:", bg='white').grid(row=7, column=0, pady=5, sticky='w')
        self.new_y2_entry = tk.Entry(action_frame)
        self.new_y2_entry.grid(row=8, column=0, pady=5, sticky='w')
        tk.Button(action_frame, text="Atualizar Retângulo", command=lambda: self.update_rectangle(rectangle), width=20, bg="white").grid(row=9, column=0, pady=10, sticky='w')

        # Translate
        tk.Label(action_frame, text="Transladar Retângulo", bg='white').grid(row=0, column=1, padx=10, sticky='w')
        tk.Label(action_frame, text="Delta X:", bg='white').grid(row=1, column=1, pady=5, sticky='w')
        self.dx_entry = tk.Entry(action_frame)
        self.dx_entry.grid(row=2, column=1, pady=5, sticky='w')
        tk.Label(action_frame, text="Delta Y:", bg='white').grid(row=3, column=1, pady=5, sticky='w')
        self.dy_entry = tk.Entry(action_frame)
        self.dy_entry.grid(row=4, column=1, pady=5, sticky='w')
        tk.Button(action_frame, text="Transladar", command=lambda: self.translate_rectangle(rectangle), width=20, bg="white").grid(row=5, column=1, pady=10, sticky='w')

        # Scale
        tk.Label(action_frame, text="Escalar Retângulo", bg='white').grid(row=0, column=2, padx=10, sticky='w')
        tk.Label(action_frame, text="Fator de Escala:", bg='white').grid(row=1, column=2, pady=5, sticky='w')
        self.scale_factor_entry = tk.Entry(action_frame)
        self.scale_factor_entry.grid(row=2, column=2, pady=5, sticky='w')
        tk.Button(action_frame, text="Escalar", command=lambda: self.scale_rectangle(rectangle), width=20, bg="white").grid(row=3, column=2, pady=10, sticky='w')

        # Rotate
        tk.Label(action_frame, text="Rotacionar Retângulo", bg='white').grid(row=0, column=3, padx=10, sticky='w')
        tk.Label(action_frame, text="Ângulo:", bg='white').grid(row=1, column=3, pady=5, sticky='w')
        self.angle_entry = tk.Entry(action_frame)
        self.angle_entry.grid(row=2, column=3, pady=5, sticky='w')
        tk.Button(action_frame, text="Rotacionar", command=lambda: self.rotate_rectangle(rectangle), width=20, bg="white").grid(row=3, column=3, pady=10, sticky='w')

        # Back button
        tk.Button(self.details_frame_rectangle, text="Voltar", command=self.back_to_main_menu, width=20, bg="white").grid(row=8, column=0, columnspan=2, pady=10)
        
        # Update window title
        self.root.title(f"Detalhes do Retângulo {rectangle.getNumber()}")

    def update_rectangle(self, rectangle):
        x1 = float(self.new_x1_entry.get())
        y1 = float(self.new_y1_entry.get())
        x2 = float(self.new_x2_entry.get())
        y2 = float(self.new_y2_entry.get())
        rectangle.updateCoord(x1, y1, x2, y2)
        self._show_rectangle_details(rectangle)

    def translate_rectangle(self, rectangle):
        dx = float(self.dx_entry.get())
        dy = float(self.dy_entry.get())
        rectangle.translate(dx, dy)
        self._show_rectangle_details(rectangle)

    def scale_rectangle(self, rectangle):
        factor = float(self.scale_factor_entry.get())
        rectangle.scale(factor)
        self._show_rectangle_details(rectangle)

    def rotate_rectangle(self, rectangle):
        angle = float(self.angle_entry.get())
        rectangle.rotate(angle)
        self._show_rectangle_details(rectangle)

    def _show_triangle_details(self, triangle):
        # Create a new frame for triangle details
        self.details_frame = tk.Frame(self.root, bg='white')
        self.details_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        # Back button
        tk.Button(self.details_frame, text="Voltar", command=self.show_existing_shapes, width=20, bg="white").grid(row=14, column=0, columnspan=2, pady=10)
        
        # Update window title
        self.root.title(f"Detalhes do Triângulo {triangle.getNumber()}")

    def back_to_main_menu(self):
        try:
            self.input_frame.destroy()
        except AttributeError:
            pass
        try:
            self.shape_frame.destroy()
        except AttributeError:
            pass
        try:
            self.details_frame_rectangle.destroy()
        except AttributeError:
            pass
        try:
            self.details_frame_line.destroy()
        except AttributeError:
            pass
        try:
            self.details_frame_point.destroy()
        except AttributeError:
            pass
        try:
            self.details_frame_circle.destroy()
        except AttributeError:
            pass
        try:
            self.voltar_button_frame.destroy()
        except AttributeError:
            pass
        try:
            self.existing_shapes_frame.destroy()
        except AttributeError:
            pass
        self.create_buttons()
        self.root.title("Formas Geométricas")

    def sair(self):
        self.root.quit()

    def run(self):
        self.root.mainloop()

# Run the interactive menu
if __name__ == "__main__":
    menu = Menu()
    menu.run()