from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import Terminal256Formatter


def isplit(gen):
    started = False
    collected = []
    for line in gen:
        if line.startswith('# START'):
            started = True
            continue
        if not started:
            continue

        if line.startswith('next_()'):
            yield collected
            collected = []
        else:
            collected.append(line.rstrip())
    if len(collected):
        yield collected


def main():
    with open('1-0.py') as f:
        for group in isplit(f):
            code = "\n".join([line for line in group if line != "\n"])
            yield highlight(code, PythonLexer(), Terminal256Formatter())
