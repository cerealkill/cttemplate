"""
Copyright (C) 2018  Justin Searle

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

import argh
from prompt_toolkit.shortcuts import prompt
from prompt_toolkit.history import InMemoryHistory
from prompt_toolkit.contrib.completers import WordCompleter

try:
    import better_exceptions
except ImportError as err:
    pass

import logging
logging.basicConfig()
log = logging.getLogger()
log.setLevel(logging.WARNING)

from . import __version__ as VERSION


def greet(name, greeting='Hello'):
    """Greets the user with given name. The greeting is customizable."""
    return greeting + ', ' + name


def connect(file):
    """Connect to a file to modify a file."""

    log.debug('Entering connect fuction')

    history = InMemoryHistory()
    completer = WordCompleter(['read', 'write <data>'], ignore_case=True)

    with open(file, 'r+') as f:
        print('file opened')
        while True:
            text = prompt('modbus> ', completer=completer, history=history)
            command = text.split()
            if command[0] == 'read':
                f.seek(0)
                print(f.read())
            elif command[0] == 'write':
                f.write(command[1])
            elif command[0] == 'exit':
                break
            else:
                Print('Bad command')
    return


def main():
    """Main CLI entrypoint."""
    parser = argh.ArghParser()
    parser.add_commands([greet, connect])
    parser.dispatch()
