
#DEFINIR CLASEE DE LA MAQUINA DE TURING
class TuringMachine:
    def __init__(self, states, alphabet, transitions, initial_state, final_state):
        #INICIALIZAMOS LOS ATRIBUTPS DE LA MAQUINA
        self.states = states
        self.alphabet = alphabet
        self.transitions = transitions
        self.current_state = initial_state
        self.final_state = final_state
        self.tape = ['_'] # Inicializar la cinta con un espacio en blanco al principio

    def move(self, direction):
      # Mover la cabeza de lectura/escritura en la cinta
        if direction == 'left':
            if self.head_position > 0:
                self.head_position -= 1
            else:
                self.tape.insert(0, '_')  #Insertar un espacio en blanco al principio si llegamos al borde izquierdo
        elif direction == 'right':
            self.head_position += 1
            if self.head_position == len(self.tape):
                self.tape.append('_') # Agregar un espacio en blanco al final si llegamos al borde derecho

    def run(self, input_string):
      # Configurar la cinta con la entrada proporcionada
        self.tape += list(input_string)
        self.head_position = 1 # Posición inicial de la cabeza de lectura/escritura

        print("Iniciando Máquina de Turing...")
        print("Estado inicial de la cinta:", "".join(self.tape))
        # Ejecutar la Máquina de Turing hasta alcanzar el estado final
        while self.current_state != self.final_state:
            current_symbol = self.tape[self.head_position]
            if (self.current_state, current_symbol) in self.transitions:
                # Obtener la transición correspondiente
                new_state, write_symbol, move_direction = self.transitions[(self.current_state, current_symbol)]
                 # Actualizar la cinta, mover la cabeza y cambiar al nuevo estado
                self.tape[self.head_position] = write_symbol
                self.move(move_direction)
                self.current_state = new_state

                # Imprimir el estado actual de la cinta de manera ordenada
                print(f"Nuevo estado: {new_state}, Símbolo escrito: {write_symbol}, Dirección: {move_direction}")
                print("Estado actual de la cinta:", "".join(self.tape))

            else:
                return "No se encontró una transición válida."
        # Mostrar mensaje de finalización y devolver el resultado
        print("Máquina de Turing completada.")
        return "".join(self.tape).replace('_', '')


        while self.current_state != self.final_state:
            current_symbol = self.tape[self.head_position]
            if (self.current_state, current_symbol) in self.transitions:
                new_state, write_symbol, move_direction = self.transitions[(self.current_state, current_symbol)]
                self.tape[self.head_position] = write_symbol
                self.move(move_direction)
                self.current_state = new_state
            else:
                return "No valid transition found."

        return "".join(self.tape).replace('_', '')

# Definir la Máquina de Turing según las instrucciones
# (Estados, alfabeto, transiciones, estado inicial, estado final)
# Las transiciones son especificadas como un diccionario
states = {'q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8', 'q9', 'q10', 'q11'}
alphabet = {'0', '1', '_'}
transitions = {
    ('q0', '_'): ('q1', '_', 'left'),
    ('q0', '0'): ('q0', '0', 'right'),
    ('q0', '1'): ('q0', '1', 'right'),

    ('q1', '1'): ('q2', '0', 'left'),
    ('q1', '0'): ('q1', '0', 'left'),
    ('q1', '_'): ('q4', '_', 'right'),

    ('q2', '0'): ('q1', '1', 'left'),
    ('q2', '1'): ('q2', '1', 'left'),
    ('q2', '_'): ('q3', '1', 'left'),

    ('q3', '_'): ('q4', '_', 'right'),

    ('q4', '0'): ('q4', '0', 'right'),
    ('q4', '1'): ('q4', '1', 'right'),
    ('q4', '_'): ('q5', '_', 'left'),

    ('q5', '1'): ('q6', '0', 'left'),
    ('q5', '0'): ('q5', '0', 'left'),
    ('q5', '_'): ('q8', '_', 'right'),

    ('q6', '0'): ('q5', '1', 'left'),
    ('q6', '1'): ('q6', '1', 'left'),
    ('q6', '_'): ('q7', '1', 'left'),

    ('q7', '_'): ('q8', '_', 'right'),

    ('q8', '0'): ('q8', '0', 'right'),
    ('q8', '1'): ('q8', '1', 'right'),
    ('q8', '_'): ('q9', '_', 'left'),

    ('q9', '0'): ('q10', '1', 'left'),
    ('q9', '1'): ('q11', '0', 'left'),

    ('q10', '0'): ('q10', '0', 'left'),
    ('q11', '1'): ('q11', '0', 'left'),

    ('q10', '1'): ('q10', '1', 'left'),
    ('q10', '0'): ('q10', '_', 'stay')
}
initial_state = 'q0'
final_state = 'q10'

# Crear la máquina de Turing
tm = TuringMachine(states, alphabet, transitions, initial_state, final_state)

# Probar la máquina de Turing con un número binario de entrada
input_number = input("Ingresa un numero binario: ")
result = tm.run(input_number)
# Mostrar el resultado
print(f"Resultado para el número binario {input_number}: {result}")
