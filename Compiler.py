def compile(diagram):
  machine_code = ""
  
  # Define the particle types and their properties
  particle_types = {
    "Electron": {"Mass": 0.511, "Charge": -1, "Spin": 1/2},
    "Proton": {"Mass": 938.3, "Charge": 1, "Spin": 1/2},
    "Photon": {"Mass": 0, "Charge": 0, "Spin": 1},
    "Higgs": {"Mass": 126, "Charge": 0, "Spin": 0},
  }
  
  # Iterate over the particles in the diagram
  for particle in diagram.particles:
    # Initialize the particle's properties
    machine_code += "INIT_PARTICLE {} {} {}\n".format(particle_types[particle.type]["Mass"], particle_types[particle.type]["Charge"], particle_types[particle.type]["Spin"])
  
  # Iterate over the vertices in the diagram
  for vertex in diagram.vertices:
    # Perform the appropriate type of interaction at the vertex
    if vertex.type == "Annihilation":
      machine_code += "ANNHILATE\n"
    elif vertex.type == "Creation":
      machine_code += "CREATE\n"
    elif vertex.type == "Scattering":
      machine_code += "SCATTER\n"
  
  # Iterate over the arrows in the diagram
  for arrow in diagram.arrows:
    # Move the particle along the arrow's path
    if arrow.direction == "Forward":
      machine_code += "MOVE_FORWARD {}\n".format(arrow.length)
    elif arrow.direction == "Backward":
      machine_code += "MOVE_BACKWARD {}\n".format(arrow.length)
    elif arrow.direction == "Up":
      machine_code += "MOVE_UP {}\n".format(arrow.length)
    elif arrow.direction == "Down":
      machine_code += "MOVE_DOWN {}\n".format(arrow.length)

  
  # Optimize the generated machine code for performance
  machine_code = optimize(machine_code)
  
  return machine_code

def optimize(code):
  # Use advanced code optimization techniques to improve the performance of the generated code
  optimized_code = ""
  
  # Split the code into individual lines
  lines = code.split("\n")
  
  # Iterate over the lines of code
  for line in lines:
    # Skip empty lines
    if line == "":
      continue
      
    # Split the line into the instruction and its arguments
    parts = line.split(" ")
    instruction = parts[0]
    args = parts[1:]
    
    # Check if the instruction is a movement instruction
    if instruction in ["MOVE_FORWARD", "MOVE_BACKWARD", "MOVE_UP", "MOVE_DOWN"]:
      # Check if the previous instruction was also a movement instruction
      if optimized_code.strip().split(" ")[0] in ["MOVE_FORWARD", "MOVE_BACKWARD", "MOVE_UP", "MOVE_DOWN"]:
        # If so, combine the two instructions into a single instruction with the sum of their arguments
        prev_parts = optimized_code.strip().split(" ")
        optimized_code = "{} {}\n".format(prev_parts[0], int(prev_parts[1]) + int(args[0]))
      else:
        # If not, add the instruction to the optimized code as is
        optimized_code += "{} {}\n".format(instruction, args[0])
    else:
      # If the instruction is not a movement instruction, add it to the optimized code as is
      optimized_code += "{}\n".format(line)
      
  return optimized_code

def execute(code,verbose:bool):
    # Define a list to store the particles
    particles = []

    # Define the functions that correspond to the instructions
    def init_particle(mass, charge, spin):
        # Initialize a particle with the given properties
        particle = Particle(mass, charge, spin)
        particles.append(particle)

    def annihilate():

        #Perform an annihilation interaction
        # Get the two particles involved in the interaction
        particle1 = particles[-1]
        particle2 = particles[-2]

        # Condition I imposed becuase of sharkov condition
        if particle1.charge != -1 * particle2.charge:
            raise ValueError("Cannot annihilate particles with non-opposite charges")

        # Remove the particles from the list of particles
        particles.remove(particle1)
        particles.remove(particle2)

    def create():

        #Perform a creation interaction
        # Get the two particles involved in the interaction
        particle1 = particles[-1]
        particle2 = particles[-2]

        # Remove the particles from the list of particles
        particles.remove(particle1)
        particles.remove(particle2)

        # Create a new particle
        new_particle = create_particle(particle1, particle2)
        particles.append(new_particle)

    def scatter():

        #Perform a scattering interaction
        # Get the three particles involved in the interaction
        particle1 = particles[-1]
        particle2 = particles[-2]
        particle3 = particles[-3]

        # Remove the particles from the list of particles
        particles.remove(particle1)
        particles.remove(particle2)
        particles.remove(particle3)

        # Scatter the particles
        scattered_particles = scatter_particles(particle1, particle2, particle3)
        particles.extend(scattered_particles)

    def move_forward(distance):

        #Move the last particle in the list of particles forward by the given distance
        particle = particles[-1]
        move_particle(particle, "forward", distance)

    def move_backward(distance):

        #Move the last particle in the list of particles backward by the given distance
        particle = particles[-1]
        move_particle(particle, "backward", distance)

    def move_up(distance):

        #Move the last particle in the list of particles up by the given distance
        particle = particles[-1]
        move_particle(particle, "up", distance)

    def move_down(distance):

        #Move the last particle in the list of particles down by the given distance
        particle = particles[-1]
        move_particle(particle, "down", distance)


    if verbose == True:
        for particle in particles:
          print(particle)

    # Define a dictionary of instructions and their corresponding functions
    instructions = {
      "INIT_PARTICLE": init_particle,
      "ANNHILATE": annihilate,
      "CREATE": create,
      "SCATTER": scatter,
      "MOVE_FORWARD": move_forward,
      "MOVE_BACKWARD": move_backward,
      "MOVE_UP": move_up,
      "MOVE_DOWN": move_down}

def graph_to_diagram(graph):
  # Define the particles, vertices, and arrows for the diagram
  particles = []
  vertices = []
  arrows = []
  
  # Iterate over the nodes in the graph
  for node in graph.nodes:
    # Add the node's type as a particle in the diagram
    # Provide the initial_state and final_state arguments
    particles.append(Particle(node.type, (0, 0), (1, 0)))
  
  # Iterate over the edges in the graph
  for edge in graph.edges:
    # Add the edge's type as a vertex in the diagram
    # Provide the coordinates argument
    vertices.append(Vertex(edge.type, (1, 0)))
    
    # Add the edge's direction and length as an arrow in the diagram
    arrows.append(Arrow(edge.direction, edge.length))
  
  # Return the diagram
  return Diagram(particles, vertices, arrows)


class Diagram:
  def __init__(self, particles, vertices, arrows):
    self.particles = particles
    self.vertices = vertices
    self.arrows = arrows
    
class Particle:
  def __init__(self, type, initial_state, final_state):
    self.type = type
    self.initial_state = initial_state
    self.final_state = final_state
    
class Vertex:
  def __init__(self, type, coordinates):
    self.type = type
    self.coordinates = coordinates
    
class Arrow:
  def __init__(self, direction, length):
    self.direction = direction
    self.length = length

class Node:
  def __init__(self, type):
    self.type = type

class Edge:
  def __init__(self, type, direction, length, initial_state, final_state):
    self.type = type
    self.direction = direction
    self.length = length
    self.initial_state = initial_state
    self.final_state = final_state

class Graph:
  def __init__(self, nodes, edges):
    self.nodes = nodes
    self.edges = edges

class AstNode:
    def __init__(self, type, *values):
      self.type = type
      self.values = values
      self.children = []
  
    def add_child(self, child):
        self.children.append(child)

    def __str__(self):
        # Convert the node's values to a string
        values_str = " ".join([str(v) for v in self.values])
        # Create a string representation of the node
        node_str = "{} {}".format(self.type, values_str)
    
        # Create a string representation of the node's children
        children_str = ""
        for child in self.children:
          # Use recursion to get the string representation of the child node
          child_str = str(child)
          # Indent the child node's string representation to show its hierarchy in the AST
          child_str = "  " + child_str.replace("\n", "\n  ")
          # Add the child node's string representation to the string for the node's children
          children_str += child_str + "\n"
    
        # Return the string representation of the node and its children
        return "{}\n{}".format(node_str, children_str)
    
def generate_ast(diagram):
    # Create the root node of the AST
    ast = AstNode("Diagram")
  
    # Iterate over the particles in the diagram
    for particle in diagram.particles:
      # Create a node for the particle
      particle_node = AstNode("Particle", particle.type)
      # Add the particle node to the AST
      ast.add_child(particle_node)
  
    # Iterate over the vertices in the diagram
    for vertex in diagram.vertices:
      # Create a node for the vertex
      vertex_node = AstNode("Vertex", vertex.type)
      # Add the vertex node to the AST
      ast.add_child(vertex_node)
  
    # Iterate over the arrows in the diagram
    for arrow in diagram.arrows:
      # Create a node for the arrow
      arrow_node = AstNode("Arrow", arrow.direction, arrow.length)
      # Add the arrow node to the AST
      ast.add_child(arrow_node)
  
    return ast

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
optimized_code = optimize(machine_code)
print(machine_code)
print(optimized_code)
# Execute the generated machine code
a =execute(optimized_code,verbose=True)
print(a)

# Define the graph
graph = Graph(nodes=[Node("Electron"), Node("Proton"), Node("Photon")],
              edges=[Edge("Annihilation", "Forward", 5,"InitialState", "FinalState"), Edge("Creation", "Backward", 10,"InitialState", "FinalState"), Edge("Scattering", "Up", 15,"InitialState", "FinalState")])

# Convert the graph to a diagram
State_graph = graph_to_diagram(graph)

print(compile(State_graph))

# Generate the AST for the diagram
ast = generate_ast(diagram)

# Print the AST
print(ast)
