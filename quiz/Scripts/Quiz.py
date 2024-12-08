import random
import tkinter as tk
from tkinter import messagebox

class QuizApp:
    def __init__(self, root):
        self.root = root
        # The above code is setting the title of the root window to "Quiz App by Gaurav" in a Python
        # Tkinter application.
        self.root.title("Quiz App by Gaurav")
        # The above code is setting the window to be displayed in fullscreen mode in a Python Tkinter
        # application.
        self.root.attributes('-fullscreen', True)
        self.root.geometry("900x700")
        root.bind("<Escape>", lambda event: root.attributes("-fullscreen", False))
        self.root.resizable(True, True)

        # Variables for storing the quiz state
        self.score = 0
        self.question_number = 0
        self.selected_answer = tk.StringVar()
        self.total_questions = 8  # number of questions

        # Initialize the questions bank
        self.questions_bank = {}
        self.initialize_questions()

        # Create GUI elements
        self.setup_gui()

    def setup_gui(self):
        self.validate_alphabetic = self.root.register(self.validate_alphabetic_input)
        self.validate_numeric = self.root.register(self.validate_numeric_input)
        # Initialize widgets only if they do not exist
        if not hasattr(self, 'start_button'):
            # Category and Difficulty Selection
            self.category_label = tk.Label(self.root, text="Welcome to Quiz Center", font=("Times New Roman", 50, 'bold'), fg='Black')
            # The above code is using the `pack` method to display the `category_label` widget in a
            # Python GUI application with a vertical padding of 50 units.
            self.category_label.pack(pady=50)

            self.name_label = tk.Label(self.root, text="Name:", font=("Times New Roman", 22, 'bold'))
            self.name_label.pack(pady=2)
            self.name_entry = tk.Entry(self.root, font=("Times New Roman", 22), validate="key", validatecommand=(self.validate_alphabetic, "%S"))
            self.name_entry.pack(pady=0)

            self.mobile_label = tk.Label(self.root, text="Roll no:", font=("Times New Roman", 22, 'bold'))
            self.mobile_label.pack(pady=1)
            self.mobile_entry = tk.Entry(self.root, font=("Times New Roman", 22), validate="key", validatecommand=(self.validate_numeric, "%S"))
            self.mobile_entry.pack(pady=0)

            self.category_label = tk.Label(self.root, text="Choose Category:", font=("Times New Roman", 22, 'bold'))
            self.category_label.pack(pady=10)

            self.category_var = tk.StringVar(value="Science")
            self.category_menu = tk.OptionMenu(self.root, self.category_var, "Science", "Geography", "Literature")
            self.category_menu.pack(pady=5)

            self.difficulty_label = tk.Label(self.root, text="Choose Difficulty:", font=("Times New Roman", 22, 'bold'))
            self.difficulty_label.pack(pady=10)

            self.difficulty_var = tk.StringVar(value="Easy")
            self.difficulty_menu = tk.OptionMenu(self.root, self.difficulty_var, "Easy", "Medium", "Hard")
            self.difficulty_menu.pack(pady=5)

            # Start button
            self.start_button = tk.Button(self.root, text="Start Quiz", command=self.start_quiz, font=("Times New Roman", 22, 'bold'), bg="green", fg="white")
            self.start_button.pack(pady=20)

        # Create a message label to display messages if it does not already exist
        if not hasattr(self, 'message_label'):
            self.message_label = tk.Label(self.root, text="", font=("Times New Roman", 18, 'bold'), fg='red')
            self.message_label.pack(pady=10)
            
            
            
    def validate_alphabetic_input(self, char):
        if char.isalpha() or char == "":
            return True
        return False

    def validate_numeric_input(self, char):
        if char.isdigit() or char == "":
            return True
        return False    

    def reset_widgets(self):
        # Hide all quiz-related widgets and show the initial setup screen
        if hasattr(self, 'question_label'):
            self.question_label.pack_forget()
        if hasattr(self, 'hint_button'):
            self.hint_button.pack_forget()
        if hasattr(self, 'submit_button'):
            self.submit_button.pack_forget()
        for btn in getattr(self, 'option_buttons', []):
            btn.pack_forget()

        # Show the setup GUI elements
        
        self.name_label.pack()
        self.name_entry.pack()
        self.mobile_label.pack()
        self.mobile_entry.pack()
        self.category_label.pack()
        self.category_menu.pack()
        self.difficulty_label.pack()
        self.difficulty_menu.pack()
        self.start_button.pack()

    def update_message(self, message, color='red'):
        self.message_label.config(text=message, fg=color)

    def initialize_questions(self):
        # Add categorized questions with difficulty levels
        self.questions_bank = {
            "Science": {
                "Easy": [
                    {'text': "Which planet is known as the Red Planet?", 'options': ["A. Earth", "B. Mars", "C. Jupiter", "D. Saturn"], 'correct_option': 'B', 'hint': "It is the fourth planet from the Sun."},
                    {'text': "What is the chemical symbol for water?", 'options': ["A. CO2", "B. H2O", "C. O2", "D. NaCl"], 'correct_option': 'B', 'hint': "It's made up of hydrogen and oxygen."},
                    {'text': "How many legs do insects have?", 'options': ["A. 4", "B. 6", "C. 8", "D. 10"], 'correct_option': 'B', 'hint': "Count a spider's legs and subtract 2."},
                    {'text': "What gas do plants absorb from the atmosphere?", 'options': ["A. Oxygen", "B. Nitrogen", "C. Carbon Dioxide", "D. Hydrogen"], 'correct_option': 'C', 'hint': "It helps in photosynthesis."},
                    {'text': "What is the boiling point of water at sea level?", 'options': ["A. 0°C", "B. 50°C", "C. 100°C", "D. 200°C"], 'correct_option': 'C', 'hint': "It's a 3-digit number."},
                    {'text': "Which organ is responsible for pumping blood throughout the body?", 'options': ["A. Brain", "B. Liver", "C. Heart", "D. Lungs"], 'correct_option': 'C', 'hint': "It's often associated with love."},
                    {'text': "What is the chemical symbol for gold?", 'options': ["A. Ag", "B. Au", "C. Pb", "D. Fe"], 'correct_option': 'B', 'hint': "It's derived from the Latin word 'aurum'."},
                    {'text': "How many bones are there in the adult human body?", 'options': ["A. 206", "B. 210", "C. 215", "D. 220"], 'correct_option': 'A', 'hint': "It's the standard number used in medical references."},
                    {'text': "What planet is closest to the Sun?", 'options': ["A. Venus", "B. Earth", "C. Mercury", "D. Mars"], 'correct_option': 'C', 'hint': "It's named after the Roman messenger god."},
                    {'text': "What is the largest organ in the human body?", 'options': ["A. Brain", "B. Liver", "C. Skin", "D. Heart"], 'correct_option': 'C', 'hint': "It's the body's outer layer."},
                    {'text': "What is the hardest natural substance on Earth?", 'options': ["A. Gold", "B. Diamond", "C. Iron", "D. Platinum"], 'correct_option': 'B', 'hint': "It's used in cutting tools and jewelry."},
                    {'text': "What element is essential for respiration?", 'options': ["A. Hydrogen", "B. Nitrogen", "C. Oxygen", "D. Carbon"], 'correct_option': 'C', 'hint': "It's the same element that makes up water's second component."},
                    {'text': "What is the primary source of energy for the Earth?", 'options': ["A. Moon", "B. Wind", "C. Sun", "D. Coal"], 'correct_option': 'C', 'hint': "It's a star that provides light and warmth."},
                    {'text': "Which planet is known for its rings?", 'options': ["A. Jupiter", "B. Saturn", "C. Uranus", "D. Neptune"], 'correct_option': 'B', 'hint': "It's the second-largest planet in the Solar System."},
                    {'text': "What is the primary component of the Earth's atmosphere?", 'options': ["A. Oxygen", "B. Carbon Dioxide", "C. Nitrogen", "D. Argon"], 'correct_option': 'C', 'hint': "It's a gas that makes up about 78% of the atmosphere."},
                    {'text': "What is the process by which plants make their own food?", 'options': ["A. Respiration", "B. Digestion", "C. Photosynthesis", "D. Fermentation"], 'correct_option': 'C', 'hint': "It involves sunlight, water, and carbon dioxide."},
                    {'text': "What is the name of the force that pulls objects towards the Earth?", 'options': ["A. Magnetism", "B. Electricity", "C. Gravity", "D. Friction"], 'correct_option': 'C', 'hint': "It's the reason things fall to the ground."},
                    {'text': "Which planet is known for its Great Red Spot?", 'options': ["A. Mars", "B. Venus", "C. Jupiter", "D. Saturn"], 'correct_option': 'C', 'hint': "It's the largest planet in the Solar System."},
                    # The above code is creating a Python dictionary that represents a multiple-choice
                    # question about the chemical symbol for Sodium. The dictionary contains keys for
                    # the question text, options, correct option, and a hint for the question.
                    {'text': "What is the chemical symbol for Sodium?", 'options': ["A. Na", "B. So", "C. S", "D. Sd"], 'correct_option': 'A', 'hint': "It's derived from the Latin 'Natrium'."},
                    {'text': "What organ in the human body is primarily responsible for digestion?", 'options': ["A. Heart", "B. Stomach", "C. Liver", "D. Kidneys"], 'correct_option': 'B', 'hint': "It's where food is broken down."},
                    {'text': "What is the most common element in the Earth's crust?", 'options': ["A. Iron", "B. Oxygen", "C. Silicon", "D. Magnesium"], 'correct_option': 'B', 'hint': "It's also essential for breathing."},
                    {'text': "What type of animal is a dolphin?", 'options': ["A. Fish", "B. Mammal", "C. Reptile", "D. Bird"], 'correct_option': 'B', 'hint': "It's warm-blooded and gives live birth."}
                ],
                "Medium": [
                    {'text': "Who developed the theory of relativity?", 'options': ["A. Isaac Newton", "B. Albert Einstein", "C. Galileo Galilei", "D. Nikola Tesla"], 'correct_option': 'B', 'hint': "E=mc² is a famous equation related to him."},
                    {'text': "What is the powerhouse of the cell?", 'options': ["A. Nucleus", "B. Ribosome", "C. Mitochondria", "D. Endoplasmic Reticulum"], 'correct_option': 'C', 'hint': "It generates energy for the cell."},
                    {'text': "What is the second most abundant gas in the Earth's atmosphere?", 'options': ["A. Oxygen", "B. Carbon Dioxide", "C. Nitrogen", "D. Argon"], 'correct_option': 'D', 'hint': "It's used in light bulbs."},
                    {'text': "What is the process by which a liquid turns into a gas?", 'options': ["A. Condensation", "B. Evaporation", "C. Sublimation", "D. Freezing"], 'correct_option': 'B', 'hint': "It's the opposite of condensation."},
                    {'text': "What type of bond is found in water molecules?", 'options': ["A. Ionic Bond", "B. Covalent Bond", "C. Hydrogen Bond", "D. Metallic Bond"], 'correct_option': 'B', 'hint': "Atoms share electrons in this bond."},
                    {'text': "Which scientist is known for the laws of motion?", 'options': ["A. Isaac Newton", "B. Albert Einstein", "C. Galileo Galilei", "D. James Clerk Maxwell"], 'correct_option': 'A', 'hint': "He formulated three fundamental laws of motion."},
                    {'text': "What is the primary function of white blood cells?", 'options': ["A. Oxygen Transport", "B. Immune Defense", "C. Nutrient Transport", "D. Hormone Regulation"], 'correct_option': 'B', 'hint': "They help fight infections."},
                    {'text': "What is the name of the outermost layer of the Earth?", 'options': ["A. Mantle", "B. Crust", "C. Core", "D. Lithosphere"], 'correct_option': 'B', 'hint': "It's where we live."},
                    {'text': "What is the name of the process by which plants lose water?", 'options': ["A. Transpiration", "B. Respiration", "C. Photosynthesis", "D. Germination"], 'correct_option': 'A', 'hint': "It's the release of water vapor from plants."},
                    {'text': "What is the speed of light?", 'options': ["A. 300,000 km/s", "B. 150,000 km/s", "C. 100,000 km/s", "D. 500,000 km/s"], 'correct_option': 'A', 'hint': "It's approximately 300,000 kilometers per second."},
                    {'text': "Which scientist is known for his work on radioactivity?", 'options': ["A. Marie Curie", "B. Niels Bohr", "C. Ernest Rutherford", "D. Richard Feynman"], 'correct_option': 'A', 'hint': "She won Nobel Prizes in Physics and Chemistry."},
                    {'text': "What is the name of the effect that causes the sky to appear blue?", 'options': ["A. Scattering", "B. Reflection", "C. Refraction", "D. Absorption"], 'correct_option': 'A', 'hint': "It's caused by the scattering of sunlight by the atmosphere."},
                    {'text': "What type of cells in the human body are responsible for transmitting nerve impulses?", 'options': ["A. Epithelial Cells", "B. Muscle Cells", "C. Nerve Cells", "D. Blood Cells"], 'correct_option': 'C', 'hint': "They are also known as neurons."},
                    {'text': "What type of energy is stored in food?", 'options': ["A. Kinetic Energy", "B. Potential Energy", "C. Thermal Energy", "D. Chemical Energy"], 'correct_option': 'D', 'hint': "It's released during metabolism."},
                    {'text': "What part of the plant conducts photosynthesis?", 'options': ["A. Root", "B. Stem", "C. Leaf", "D. Flower"], 'correct_option': 'C', 'hint': "It's where chlorophyll is located."},
                    {'text': "What is the boiling point of water in Fahrenheit?", 'options': ["A. 212°F", "B. 100°F", "C. 32°F", "D. 50°F"], 'correct_option': 'A', 'hint': "It's a standard temperature for boiling water."},
                    {'text': "What is the name of the chemical reaction that breaks down glucose to release energy?", 'options': ["A. Photosynthesis", "B. Cellular Respiration", "C. Fermentation", "D. Digestion"], 'correct_option': 'B', 'hint': "It's the process used by cells to convert glucose into energy."},
                    {'text': "What is the most abundant element in the universe?", 'options': ["A. Hydrogen", "B. Helium", "C. Oxygen", "D. Carbon"], 'correct_option': 'A', 'hint': "It's the simplest and lightest element."},
                    {'text': "What is the primary gas in the air we breathe?", 'options': ["A. Carbon Dioxide", "B. Oxygen", "C. Nitrogen", "D. Argon"], 'correct_option': 'C', 'hint': "It's the most abundant gas in the Earth's atmosphere."},
                    {'text': "What is the name of the process by which plants convert light energy into chemical energy?", 'options': ["A. Respiration", "B. Photosynthesis", "C. Fermentation", "D. Glycolysis"], 'correct_option': 'B', 'hint': "It occurs in the chloroplasts of plant cells."},
                    {'text': "What is the smallest unit of matter?", 'options': ["A. Molecule", "B. Atom", "C. Proton", "D. Electron"], 'correct_option': 'B', 'hint': "It's the basic building block of elements."},
                    {'text': "What type of electromagnetic radiation is visible to the human eye?", 'options': ["A. X-rays", "B. Radio Waves", "C. Ultraviolet", "D. Light"], 'correct_option': 'D', 'hint': "It's what we see as colors."}
                ],
            
                "Hard": [
                    {'text': "What is the smallest particle of an element that retains the properties of that element?", 'options': ["A. Atom", "B. Molecule", "C. Proton", "D. Neutron"], 'correct_option': 'A', 'hint': "It's the basic unit of matter."},
                    {'text': "What is the name of the effect that causes the sky to appear red during sunset?", 'options': ["A. Rayleigh Scattering", "B. Doppler Effect", "C. Quantum Tunneling", "D. Gravitational Lensing"], 'correct_option': 'A', 'hint': "It's caused by the scattering of light."},
                    {'text': "What is the primary force responsible for holding atomic nuclei together?", 'options': ["A. Electromagnetic Force", "B. Gravitational Force", "C. Strong Nuclear Force", "D. Weak Nuclear Force"], 'correct_option': 'C', 'hint': "It's the strongest of the four fundamental forces."},
                    {'text': "What is the term for the study of the universe's origins and development?", 'options': ["A. Cosmology", "B. Astrophysics", "C. Quantum Mechanics", "D. Meteorology"], 'correct_option': 'A', 'hint': "It involves the Big Bang Theory."},
                    {'text': "What is the process called where an unstable atomic nucleus loses energy by emitting radiation?", 'options': ["A. Fusion", "B. Fission", "C. Radioactive Decay", "D. Neutron Capture"], 'correct_option': 'C', 'hint': "It's a natural process of decay."},
                    {'text': "What is the name of the phenomenon where light bends as it passes through different media?", 'options': ["A. Reflection", "B. Diffraction", "C. Refraction", "D. Polarization"], 'correct_option': 'C', 'hint': "It's what causes a straw to look bent in a glass of water."},                        {'text': "What is the term for the amount of matter in an object, typically measured in kilograms or grams?", 'options': ["A. Volume", "B. Density", "C. Mass", "D. Weight"], 'correct_option': 'C', 'hint': "It's measured by a scale."},
                    {'text': "What is the name of the force that opposes the relative motion between two surfaces in contact?", 'options': ["A. Tension", "B. Friction", "C. Normal Force", "D. Thrust"], 'correct_option': 'B', 'hint': "It acts in the opposite direction to movement."},
                    {'text': "What is the principle that states energy cannot be created or destroyed, only transformed?", 'options': ["A. First Law of Thermodynamics", "B. Second Law of Thermodynamics", "C. Law of Conservation of Mass", "D. Law of Universal Gravitation"], 'correct_option': 'A', 'hint': "It's also known as the law of energy conservation."},
                    {'text': "What type of reaction occurs when an atom gains or loses electrons?", 'options': ["A. Chemical Reaction", "B. Nuclear Reaction", "C. Redox Reaction", "D. Physical Change"], 'correct_option': 'C', 'hint': "It's also known as oxidation-reduction."},
                    {'text': "What is the name of the effect where light waves spread out when passing through a small slit?", 'options': ["A. Diffraction", "B. Reflection", "C. Refraction", "D. Interference"], 'correct_option': 'A', 'hint': "It's a behavior of light waves similar to sound waves."},
                    {'text': "What is the name of the fundamental particle of the strong nuclear force?", 'options': ["A. Proton", "B. Neutron", "C. Gluon", "D. Photon"], 'correct_option': 'C', 'hint': "It's responsible for binding quarks together."},
                    {'text': "What is the concept that describes the curvature of spacetime due to mass?", 'options': ["A. General Relativity", "B. Special Relativity", "C. Quantum Field Theory", "D. String Theory"], 'correct_option': 'A', 'hint': "It's the theory developed by Albert Einstein."},
                    {'text': "What is the term for a material that allows electricity to flow through it easily?", 'options': ["A. Insulator", "B. Conductor", "C. Semiconductor", "D. Resistor"], 'correct_option': 'B', 'hint': "Metals are good examples of this."},
                    {'text': "What is the name of the decay process where a neutron turns into a proton, an electron, and an antineutrino?", 'options': ["A. Beta Decay", "B. Alpha Decay", "C. Gamma Decay", "D. Positron Emission"], 'correct_option': 'A', 'hint': "It's a common type of radioactive decay."},
                    {'text': "What is the principle that states the total entropy of a closed system always increases over time?", 'options': ["A. First Law of Thermodynamics", "B. Second Law of Thermodynamics", "C. Third Law of Thermodynamics", "D. Zeroth Law of Thermodynamics"], 'correct_option': 'B', 'hint': "It's often referred to as the law of entropy."},
                    {'text': "What is the term for the phenomenon where light waves overlap and combine to form a new wave pattern?", 'options': ["A. Diffraction", "B. Interference", "C. Refraction", "D. Polarization"], 'correct_option': 'B', 'hint': "It can be constructive or destructive."},
                    {'text': "What is the name of the force that causes objects to move in a circular path?", 'options': ["A. Centripetal Force", "B. Gravitational Force", "C. Frictional Force", "D. Tensional Force"], 'correct_option': 'A', 'hint': "It's directed towards the center of the circular path."},
                    {'text': "What is the name of the principle that describes the behavior of gas particles at extremely low temperatures?", 'options': ["A. Bose-Einstein Condensate", "B. Fermi Gas", "C. Ideal Gas Law", "D. Van der Waals Equation"], 'correct_option': 'A', 'hint': "It's a state of matter at temperatures close to absolute zero."},
                    {'text': "What is the term for the resistance encountered by an object moving through a fluid?", 'options': ["A. Drag", "B. Lift", "C. Thrust", "D. Weight"], 'correct_option': 'A', 'hint': "It's a force that opposes motion in fluids."},
                    {'text': "What is the name of the force that causes objects to experience acceleration in a gravitational field?", 'options': ["A. Tension", "B. Normal Force", "C. Gravitational Force", "D. Centripetal Force"], 'correct_option': 'C', 'hint': "It's proportional to mass and inversely proportional to distance squared."}
                ]
            },
            "Geography": {
                "Easy": [
                    {'text': "What is the capital of France?", 'options': ["A. Paris", "B. London", "C. Berlin", "D. Madrid"], 'correct_option': 'A', 'hint': "It's also known as the city of love."}
                ],
                "Medium": [
                    {'text': "Which is the largest desert in the world?", 'options': ["A. Sahara", "B. Gobi", "C. Antarctic Desert", "D. Kalahari"], 'correct_option': 'C', 'hint': "It's located at the Earth's southern pole."}
                ],
                "Hard": [
                    {'text': "Which country has the longest coastline in the world?", 'options': ["A. Australia", "B. Russia", "C. Canada", "D. Brazil"], 'correct_option': 'C', 'hint': "It's a North American country with vast wilderness."}
                ]
            },
            "Literature": {
                "Easy": [
                    {'text': "Who wrote 'Romeo and Juliet'?", 'options': ["A. William Shakespeare", "B. Charles Dickens", "C. Mark Twain", "D. J.K. Rowling"], 'correct_option': 'A', 'hint': "He's considered the greatest English playwright."}
                ],
                "Medium": [
                    {'text': "Who wrote '1984'?", 'options': ["A. George Orwell", "B. Aldous Huxley", "C. F. Scott Fitzgerald", "D. Ernest Hemingway"], 'correct_option': 'A', 'hint': "The book is a dystopian novel about surveillance."}
                ],
                "Hard": [
                    {'text': "What is the name of the first novel by Herman Melville?", 'options': ["A. Type", "B. Moby-Dick", "C. Billy Budd", "D. Omoo"], 'correct_option': 'A', 'hint': "It's a semi-autobiographical narrative of life among cannibals."}
                ]
            }
        }

    def start_quiz(self):
        # Check if name and mobile number fields are filled
        name = self.name_entry.get().strip()
        mobile = self.mobile_entry.get().strip()

        if not name or not mobile:
            self.update_message("Please fill in both name and mobile number first!", color='red')
            return
        else:
            self.name_entry.pack_forget()
            self.name_label.pack_forget()
            self.mobile_entry.pack_forget()
            self.mobile_label.pack_forget()
            self.category = self.category_var.get()
            self.difficulty = self.difficulty_var.get()
            self.update_message("8 Questions will be asked! Please give answers carefully!!!!", color='green')
            self.reset_widgets()
            self.name_entry.pack_forget()
            self.name_label.pack_forget()
            self.category_label.pack_forget()
            self.category_menu.pack_forget()
            self.mobile_entry.pack_forget()
            self.mobile_label.pack_forget()
            self.difficulty_label.pack_forget()
            self.difficulty_menu.pack_forget()
            self.start_button.pack_forget()
            # Hide the setup screen elements
            self.permanent_name_label = tk.Label(self.root, text=f"Name: {name}", font=("Times New Roman", 16, 'bold'))
            self.permanent_name_label.place(x=10, y=10)  # Place at the top-left corner

            self.permanent_roll_label = tk.Label(self.root, text=f"Roll no: {mobile}", font=("Times New Roman", 16, 'bold'))
            self.permanent_roll_label.place(x=10, y=40)  # Place below the name label
            
            # Prepare for the quiz
            self.show_question()

    def get_random_question(self):
        category_questions = self.questions_bank.get(self.category, {}).get(self.difficulty, [])
        if not category_questions:
            return None
        return random.choice(category_questions)

    def show_question(self):
        self.question = self.get_random_question()

        if not self.question:
            self.update_message("No questions available for the selected category and difficulty.")
            return

        # Question Label

        # The above code snippet is creating a label widget in a Tkinter GUI application using Python.
        # The label will display the text from the `self.question['text']` variable. The label is
        # styled with a specific font (Times New Roman, size 22, bold) and has a wrap length of 400
        # pixels, meaning that the text will wrap to the next line if it exceeds this width.
        self.question_label = tk.Label(self.root, text=self.question['text'], font=("Times New Roman", 22, 'bold'), wraplength=400)
        self.question_label.pack(pady=2)

        # Answer options (radio buttons)
        self.selected_answer.set(None)  # Reset the selected answer
        self.option_buttons = []
        for idx, option in enumerate(self.question['options']):
            btn = tk.Radiobutton(self.root, text=option, variable=self.selected_answer, value=chr(65 + idx), font=("Times New Roman", 22, 'bold'))
            btn.pack(anchor="w", pady=5)
            self.option_buttons.append(btn)

        # Submit Button
        self.submit_button = tk.Button(self.root, text="Submit", command=self.check_answer, font=("Times New Roman", 16, 'bold'), bg="green", fg="white")
        self.submit_button.pack(pady=20,padx=5)

        # Hint Button
        self.hint_button = tk.Button(self.root, text="Hint", command=self.show_hint, font=("Times New Roman", 16, 'bold'), bg="orange", fg="white")
        self.hint_button.pack(pady=20,padx=5)

    def check_answer(self):
        if not self.selected_answer.get():
            self.update_message("Please select an option first!", color='red')
            return

        if self.selected_answer.get() == self.question['correct_option']:
            self.score += 1
            self.update_message("Well done! You got it right.", color='green')
        else:
            correct_option_text = self.question['options'][ord(self.question['correct_option']) - 65]
            self.update_message(f"Oops! The correct answer was: {correct_option_text}", color='red')

        # Move to the next question or end the quiz
        self.question_number += 1
        self.clear_question()
        if self.question_number < self.total_questions:
            self.show_question()
        else:
            self.end_quiz()

    def show_hint(self):
        self.update_message(self.question['hint'], color='blue')

    def clear_question(self):
        # Clear the current question
        if hasattr(self, 'question_label'):
            self.question_label.pack_forget()
        if hasattr(self, 'submit_button'):
            self.submit_button.pack_forget()
        if hasattr(self, 'hint_button'):
            self.hint_button.pack_forget()
        for btn in getattr(self, 'option_buttons', []):
            btn.pack_forget()

    def end_quiz(self):
        
        self.message_label.pack_forget()
        # Show the "Show Score" and "Try Again" buttons
        self.show_score_button = tk.Button(self.root, text="Show Score", command=self.show_score, font=("Times New Roman", 22, 'bold'), bg="blue", fg="white")
        self.show_score_button.pack(pady=10)

        
        self.finish_button = tk.Button(self.root, text="Finish Quiz", command=self.quit_application, font=("Times New Roman", 22, 'bold'), bg="purple", fg="white")
        self.finish_button.pack(pady=20)

    def show_score(self):
        self.message_label.pack_forget()
        self.show_score_button.pack_forget()
        self.finish_button.pack_forget()
        
        report_card_text = f"Report Card\n\nName: {self.name_entry.get()}\nRoll No: {self.mobile_entry.get()}\nScore: {self.score} / {self.total_questions}"
        self.report_card_label = tk.Label(self.root, text=report_card_text, font=("Times New Roman", 22, 'bold'))
        self.report_card_label.pack(pady=50)
        self.try_again_button = tk.Button(self.root, text="Try Again", command=self.try_again, font=("Times New Roman", 22, 'bold'), bg="red", fg="white")
        self.try_again_button.pack(pady=10)
        self.finish_button = tk.Button(self.root, text="Finish Quiz", command=self.quit_application, font=("Times New Roman", 22, 'bold'), bg="purple", fg="white")
        self.finish_button.pack(pady=20)
        
        

    def try_again(self):
        # Reset quiz state
        self.score = 0
        self.question_number = 0

        # Hide the score and try again buttons
        self.finish_button.pack_forget()
        self.report_card_label.pack_forget()
        self.try_again_button.pack_forget()
        self.show_score_button.pack_forget()
        self.try_again_button.pack_forget()
        self.message_label.pack_forget()
        

        # Show the initial setup screen again
        self.reset_widgets()
    def quit_application(self):
        self.root.quit()
    

# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()