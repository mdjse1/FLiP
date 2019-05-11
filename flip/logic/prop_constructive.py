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

from formula import FormulaPlaceholder
from prop_common import Not, Or, F

# Rules for constructive propositional logic from Bornat.
# Contradiction (constructive) here does not appear in classical logic.
# Contradiction (classical) here is similar to Kaye's Reductio Ad Absurdum.
# Bornat's not-intro, not-elim already appear in prop_common as raa, contra.
# assume_case, ore rules here also appear in prop_derived with the same names.
# contra_classic, contra_con rules here appear as pbc, fe in prop_derived

# Define symbol for each rule, short for easy typing at Python interpreter
# Rule symbols are self-evaluating, used to write proof in save file format

assume_case, ore, contra_con, contra_classic = \
  'assume_case', 'ore', 'contra_con', 'contra_classic'

# Pretty-print names for rules.
# Each logic module merges its own rule_names with checker.rule_names
# Note _ prefix on _rule_name here makes it private

_rule_names = { assume_case: 'Assumption (next case)',
                ore: 'Or-Elimination',
                contra_con: 'Contradiction (constructive)',
                contra_classic: 'Contradiction (classical)' 
              }

# Inference rules, dictionary of rule symbol and list of formulas:
#  list of premises, then conclusion last
# Subproofs in inference rules are nested lists

# Placeholders used in rules
m1, m2, m3 = map(FormulaPlaceholder, ('m1','m2','m3'))

_rules = { assume_case:  [[],[ m1 ]],  # subproof, replace top assumption
           ore: [ Or(m1,m2), [ m1,m3 ], [ m2,m3 ], m3 ], #subproofs, discharger
           contra_con:     [ F, m1 ],             # from False, infer anything!
           contra_classic: [ [ Not(m1), F], m1 ]  # subproof, discharger
         }

# Import statement to write to save file, so it in turn can be imported 

_imports = 'from flip.logic.prop_constructive import *'
