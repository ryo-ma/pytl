import ast
import argparse


class LineText:

    def __init__(self, node, indent):
        self.node = node
        self.name = node.name
        self.indent = indent

    def get_line_number(self):
        if hasattr(self.node, 'lineno'):
            return self.node.lineno

    def get_indent_text(self):
        indent_text = ' ' * self.indent
        if self.indent != 0:
            indent_text += '|_'
        return indent_text


class ClassDefLineText(LineText):

    def __init__(self, class_node, indent):
        if not isinstance(class_node, ast.ClassDef):
            raise ValueError('node type is not ClassDef.')
        super(ClassDefLineText, self).__init__(class_node, indent)

    def __str__(self):
        return '{}: {}class {}'.format(self.get_line_number(), self.get_indent_text(), self.name)


class FunctionDefLineText(LineText):

    def __init__(self, def_node, indent):
        if not isinstance(def_node, ast.FunctionDef):
            raise ValueError('node type is not FunctionDef.')
        super(FunctionDefLineText, self).__init__(def_node, indent)
        try:
            self.args = ', '.join([a.arg for a in def_node.args.args])
        except AttributeError:
            # Support to python2
            self.args = ', '.join([a.id for a in def_node.args.args])

    def __str__(self):
        return '{}: {}def {}({})'.format(self.get_line_number(), self.get_indent_text(), self.name, self.args)


INDENT_NUM = 2


class Parser:

    def __init__(self, file_text, class_only=False, def_only=False):
        self.text_list = []
        self.class_only = class_only
        self.def_only = def_only
        self.tree = ast.parse(file_text)
        self.walk(self.tree)

    def walk(self, node, indent=0):
        next_indent = indent + INDENT_NUM
        if isinstance(node, ast.ClassDef) and not self.def_only:
            self.text_list.append(ClassDefLineText(node, indent))
        elif isinstance(node, ast.FunctionDef) and not self.class_only:
            self.text_list.append(FunctionDefLineText(node, indent))
        else:
            next_indent = indent

        for child in ast.iter_child_nodes(node):
            self.walk(child, indent=next_indent)

    def max_line_number_length(self):
        return len(str(max([x.get_line_number() for x in self.text_list])))

    def print(self):
        for line in self.text_list:
            left_space = self.max_line_number_length() - len(str(line.get_line_number()))
            print('{}{}'.format(' ' * left_space, line))


def main():
    parser = argparse.ArgumentParser(add_help=True)
    parser.add_argument('python_file_path', type=str, help='Specify target python file path')
    parser.add_argument('-c', '--class-only', action='store_true', default=False, help='Show only the class line')
    parser.add_argument('-d', '--def-only', action='store_true', default=False, help='Show only the def line')
    parse_args = parser.parse_args()
    with open(parse_args.python_file_path, 'r') as f:
        Parser(f.read(), parse_args.class_only, parse_args.def_only).print()


if __name__ == '__main__':
    main()
