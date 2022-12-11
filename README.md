# FeynmanCompiler
Convert feynman diagrams into machine code ,Graph objects ,and generate AST of a given diagram

# Mechanics
This code is a function that takes in a feynman diagram and returns the corresponding machine code.The compile function initializes the properties of the particles in the diagram and then iterates over the vertices and arrows in the diagram to generate the appropriate machine code instructions. The optimize function takes the generated code and applies advanced optimization techniques to improve its performance. The execute function takes the generated machine code and simulates its execution, printing the resulting particles to the console if the verbose flag is set to True.The code can also convert given diagrams to graph based objects and generate the abstarct syntax tree of the diagram or physical process.
