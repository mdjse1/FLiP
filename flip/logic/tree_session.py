 #Copyright (C) 2009, 2010, 2011 Jonathan Jacky
 
 # This program is free software: you can redistribute it and/or modify
 # it under the terms of the GNU General Public License as published by
 # the Free Software Foundation, either version 3 of the License, or
 # (at your option) any later version.

 # This program is distributed in the hope that it will be useful,
 # but WITHOUT ANY WARRANTY; without even the implied warranty of
 # MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 # GNU General Public License for more details.

 # You should have received a copy of the GNU General Public License
 # along with this program.  If not, see <https://www.gnu.org/licenses/>.
 

# Logic module for tree logic from Kaye ch 3

import tree

# Put logics etc. in checker nd

import nd

nd.add_rule_names(tree._rule_names)

nd.add_rules(tree._rules)

# used by save function
nd.add_imports(tree._imports)

# Import all the identifiers that might be used in the interactive session

from common import *
from tree import *

from nd import *  # prover commands

from pprint import pprint
