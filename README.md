# FeynmanCompiler
Convert feynman diagrams into machine code ,Graph objects ,and generate AST of a given diagram

# Mechanics
This code is a function that takes in a feynman diagram and returns the corresponding machine code.The compile function initializes the properties of the particles in the diagram and then iterates over the vertices and arrows in the diagram to generate the appropriate machine code instructions. The optimize function takes the generated code and applies advanced optimization techniques to improve its performance. The execute function takes the generated machine code and simulates its execution, printing the resulting particles to the console if the verbose flag is set to True.The code can also convert given diagrams to graph based objects and generate the abstarct syntax tree of the diagram or physical process.


## Diagram Usage
```python

from FeynmanCompiler.Compiler import *

# Make a basic feynman diagram using the Diagram function

diagram = Diagram(
  particles=[
    Particle(type="Proton", initial_state=(0, 0), final_state=(1, 0)),
    Particle(type="Electron", initial_state=(0, 1), final_state=(1, 1)),
  ],
  vertices=[
    Vertex(type="Annihilation", coordinates=(1, 0)),
  ],
  arrows=[
    Arrow(direction="Forward", length=1),
    Arrow(direction="Forward", length=1),
  ],
)

# Use the compiler to generate machine code for the diagram
machine_code = compile(diagram)

# Generate optimized code
optimized_code = optimize(machine_code)
execute(optimized_code,verbose=True) # Perform all the operations

print(optimized_code)
```
# Output
```bash
mov eax, 938.3
mov ebx, 1
mov ecx, 0.5
mov eax, 0.511
mov ebx, -1
mov ecx, 0.5
call ANNHILATE
add eax, 1
add eax, 1
```
# Graph usage

```python

from FeynmanCompiler.Compiler import *

# Make a basic Graph object like the following

graph = Graph(nodes=[Node("Electron"), Node("Proton"), Node("Photon")],
              edges=[Edge("Annihilation", "Forward", 5,"InitialState", "FinalState"), Edge("Creation", "Backward", 10,"InitialState", "FinalState"), Edge("Scattering", "Up", 15,"InitialState", "FinalState")])

# Convert the graph to a diagram
feynman_graph = graph_to_diagram(graph)

# compile to see if we have a diagram instead
print(compile(feynman_graph))

```

# Output
```bash
# Indeed we have a new output

mov eax, 0.511
mov ebx, -1
mov ecx, 0.5
mov eax, 938.3
mov ebx, 1
mov ecx, 0.5
mov eax, 0
mov ebx, 0
mov ecx, 1
call ANNHILATE
call CREATE
call SCATTER
add eax, 5
sub eax, 10
add ebx, 15

```

# Abstract Syntax Tree
The AST functionality takes a diagram as input and generates an abstract syntax tree (AST) for the diagram.An AST is a tree-like representation of the structure of a program. It provides a high-level overview of the program, and can be used for various purposes such as code analysis, optimization, and code generation.

```python

from FeynmanCompiler.Compiler import *

# Make a Graph

graph = Graph(nodes=[Node("Electron"), Node("Proton"), Node("Photon")],
              edges=[Edge("Annihilation", "Forward", 5,"InitialState", "FinalState"), Edge("Creation", "Backward", 10,"InitialState", "FinalState"), Edge("Scattering", "Up", 15,"InitialState", "FinalState")])

# graph to a diagram
feynman_graph = graph_to_diagram(graph)

# Generate the AST for the diagram
ast = generate_ast(feynman_graph)

# Print the AST
print(ast)

```

# Output
```bash
# AST

Diagram 
  Particle Electron
  
  Particle Proton
  
  Particle Photon
  
  Vertex Annihilation
  
  Vertex Creation
  
  Vertex Scattering
  
  Arrow Forward 5
  
  Arrow Backward 10
  
  Arrow Up 15

```
