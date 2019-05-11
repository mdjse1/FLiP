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
 
from formula import Letter, Variable, InfixRelation, FormulaPlaceholder, VariablePlaceholder

# F is just a propositional letter that appears in inference rules

F = Letter('F')

class lt(InfixRelation):
  """
  lt(a,b) means a < b in Kaye
  """
  def __init__(self, *args):
    InfixRelation.__init__(self, *args)
    self.symbol = '<'

class nlt(InfixRelation):
  """
  nlt(a,b) means a /< b in Kaye
  """
  def __init__(self, *args):
    InfixRelation.__init__(self, *args)
    self.symbol = '/<'

# Define a symbol for each rule, chosen for easy typing
# Rule symbols are self-evaluating, used to write proof in save file format

(assume, trans, irref, contra, raa) = \
  ('assume', 'trans', 'irref', 'contra', 'raa')

# Pretty-print names for rules.
# Each logic module merges its own rule_names with checker.rule_names
# Note _ prefix on _rule_name here makes it private

_rule_names = { assume: 'Assumption',
                trans: 'Transitivity', irref : 'Irreflexivity',
                contra : 'Contradiction', raa: 'Reductio Ad Absurdum' 
              }

# Inference rules, dictionary of rule symbol and list of patterns:
#  list of premises, then conclusion last
# Subproofs in inference rules are nested lists

# Placeholders used in rules
m1 = FormulaPlaceholder('m1')

# Kaye's 'poset elements' (p. 38) are like fol variables
v1,v2,v3 = map(VariablePlaceholder, ['v1','v2','v3'])

_rules = { assume: [[ m1 ]],  # subproof, assumer
           trans:  [ lt(v1,v2), lt(v2,v3), lt(v1,v3) ],
           irref:  [ lt(v1,v1), F ],
           contra: [ lt(v1,v2), nlt(v1,v2), F ], 
           raa:    [[ lt(v1,v2), F ], nlt(v1,v2) ]  # subproof, discharger
         }

# variables used in proofs.  Kaye calls these 'poset elements' (p. 38)
a,b,c,d = map(Variable, 'abcd')    # a.name = 'a' etc.

# Import statement to write to save file, so it in turn can be imported 
_imports = 'from flip.logic.poset import *'
