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
 

# Logic modules for fol logic from Kaye ch 9

import prop_common
import prop_classic
import fol

# Combine logics etc. in checker nd

import nd

nd.add_rule_names(prop_common._rule_names, prop_classic._rule_names,
                  fol._rule_names)

nd.add_rules(prop_common._rules, prop_classic._rules, fol._rules)

# used by save function
nd.add_imports(prop_common._imports, prop_classic._imports, fol._imports)

# Import all the identifiers that might be used in the interactive session

from common import * 
from prop_common import *
from prop_classic import *
from fol import *

from nd import *  # prover commands

from pprint import pprint
