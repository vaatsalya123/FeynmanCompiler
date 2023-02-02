import re

class GraphParser:
    def __init__(self, input_string):
        self.input_string = input_string
        self.tokenizer = re.compile(r"\s*([A-Za-z0-9_.-]+)")
        self.tokens = None
        self.next_token = None
        self.particle_types = {
            "e-": {"Mass": 0.511, "Charge": -1, "Spin": 1/2},
            "e": {"Mass": 0.511 , "Charge": 1 ,"Spin":1/2},
            "Proton": {"Mass": 938.3, "Charge": 1, "Spin": 1/2},
            "Photon": {"Mass": 0, "Charge": 0, "Spin": 1},
            "Higgs": {"Mass": 126, "Charge": 0, "Spin": 0},
            "Neutrino": {"Mass": 0, "Charge": 0, "Spin": 1/2},
            "Muon": {"Mass": 105.66, "Charge": -1, "Spin": 1/2},
            "Pion": {"Mass": 139.57, "Charge": 1, "Spin": 0},
            "Gluon": {"Mass": 0, "Charge": 0, "Spin": 1},
            "Quark": {"Mass": 0, "Charge": 1/3, "Spin": 1/2},
            "Antiquark": {"Mass": 0, "Charge": -1/3, "Spin": 1/2},
        }

    def parse(self):
        self.tokens = self.tokenizer.findall(self.input_string)
        self.next_token = 0
        return self.parse_graph()

    def parse_graph(self):
        vertices = []
        edges = []
        while self.next_token < len(self.tokens)-1:
            particle_type1 = self.tokens[self.next_token]
            self.next_token += 1
            particle_type2 = self.tokens[self.next_token]
            self.next_token += 1
            if particle_type1 not in vertices:
                vertices.append(particle_type1)
            if particle_type2 not in vertices:
                vertices.append(particle_type2)
            edges.append((particle_type1, particle_type2))
        return {
        "vertices": [self.particle_types[vertex] for vertex in vertices],
        "edges": edges
        }


input_string = "(e-,e+) =>=> (e+ e-)"
feynman_parser = GraphParser(input_string)
feynman_graph = feynman_parser.parse()
print(feynman_graph)

