import re

class GraphParser:
    def __init__(self, input_string):
        self.input_string = input_string
        self.tokenizer = re.compile("\s*([A-Za-z0-9_.]+)")
        self.tokens = None
        self.next_token = None

    def parse(self):
        self.tokens = self.tokenizer.findall(self.input_string)
        self.next_token = 0
        return self.parse_graph()

    def parse_graph(self):
        vertices = []
        edges = []
        while self.next_token < len(self.tokens):
            vertex1 = self.tokens[self.next_token]
            self.next_token += 1
            vertex2 = self.tokens[self.next_token]
            self.next_token += 1
            if vertex1 not in vertices:
                vertices.append(vertex1)
            if vertex2 not in vertices:
                vertices.append(vertex2)
            edges.append((vertex1, vertex2))
        return {"vertices": vertices, "edges": edges}

input_string = "(e-,e+) => (e-,e+)"
feynman_parser = GraphParser(input_string)
feynman_graph = feynman_parser.parse()

