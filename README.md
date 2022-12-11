# FeynmanCompiler
Convert feynman diagrams into machine code ,Graph objects ,and generate AST of a given diagram

# Mechanics
This code is a function that takes in a feynman diagram and returns the corresponding machine code.The compile function initializes the properties of the particles in the diagram and then iterates over the vertices and arrows in the diagram to generate the appropriate machine code instructions. The optimize function takes the generated code and applies advanced optimization techniques to improve its performance. The execute function takes the generated machine code and simulates its execution, printing the resulting particles to the console if the verbose flag is set to True.The code can also convert given diagrams to graph based objects and generate the abstarct syntax tree of the diagram or physical process.


## Usage
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

print(optimized_code)
```
# Output
```bash
INIT_PARTICLE 938.3 1 0.5
INIT_PARTICLE 0.511 -1 0.5
ANNHILATE
MOVE_FORWARD 1
MOVE_FORWARD 1
```

