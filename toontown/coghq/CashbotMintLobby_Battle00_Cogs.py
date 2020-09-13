from SpecImports import *
import random
from toontown.toonbase import ToontownGlobals
CogParent = 10000
MidCogParent = 10022
FrontCogParent = 10060
BattleCellId = 0
MidBattleCellId = 1
FrontBattleCellId = 2
BattleCells = {BattleCellId: {'parentEntId': CogParent,
                'pos': Point3(0, 0, 0)},
 MidBattleCellId: {'parentEntId': MidCogParent,
                   'pos': Point3(0, 0, 0)},
 FrontBattleCellId: {'parentEntId': FrontCogParent,
                     'pos': Point3(0, 0, 0)}}
CogData = [{'parentEntId': CogParent,
  'boss': 0,
  'level': random.choice([8, 9, 10]),
  'battleCell': BattleCellId,
  'pos': Point3(-6, 0, 0),
  'h': 180,
  'behavior': 'stand',
  'revives': random.choice([0, 1, 2]),
  'path': None,
  'skeleton': 0},
 {'parentEntId': CogParent,
  'boss': 0,
  'level': random.choice([8, 9, 10]),
  'battleCell': BattleCellId,
  'pos': Point3(-2, 0, 0),
  'h': 180,
  'behavior': 'stand',
  'revives': random.choice([0, 1, 2]),
  'path': None,
  'skeleton': 0},
 {'parentEntId': CogParent,
  'boss': 0,
  'level': random.choice([8, 9, 10]),
  'battleCell': BattleCellId,
  'pos': Point3(2, 0, 0),
  'h': 180,
  'behavior': 'stand',
  'revives': random.choice([0, 1, 2]),
  'path': None,
  'skeleton': 0},
 {'parentEntId': CogParent,
  'boss': 0,
  'level': random.choice([8, 9, 10]),
  'battleCell': BattleCellId,
  'pos': Point3(6, 0, 0),
  'h': 180,
  'behavior': 'stand',
  'revives': random.choice([0, 1, 2]),
  'path': None,
  'skeleton': 0},
 {'parentEntId': MidCogParent,
  'boss': 0,
  'level': random.choice([8, 9, 10]),
  'battleCell': MidBattleCellId,
  'pos': Point3(-6, 0, 0),
  'h': 180,
  'behavior': 'stand',
  'revives': random.choice([0, 1, 2]),
  'path': None,
  'skeleton': 0},
 {'parentEntId': MidCogParent,
  'boss': 0,
  'level': random.choice([8, 9, 10]),
  'battleCell': MidBattleCellId,
  'pos': Point3(-2, 0, 0),
  'h': 180,
  'behavior': 'stand',
  'revives': random.choice([0, 1, 2]),
  'path': None,
  'skeleton': 0},
 {'parentEntId': MidCogParent,
  'boss': 0,
  'level': random.choice([8, 9, 10]),
  'battleCell': MidBattleCellId,
  'pos': Point3(2, 0, 0),
  'h': 180,
  'behavior': 'stand',
  'revives': random.choice([0, 1, 2]),
  'path': None,
  'skeleton': 0},
 {'parentEntId': MidCogParent,
  'boss': 0,
  'level': random.choice([8, 9, 10]),
  'battleCell': MidBattleCellId,
  'pos': Point3(6, 0, 0),
  'h': 180,
  'behavior': 'stand',
  'revives': random.choice([0, 1, 2]),
  'path': None,
  'skeleton': 0},
 {'parentEntId': FrontCogParent,
  'boss': 0,
  'level': random.choice([8, 9, 10]),
  'battleCell': FrontBattleCellId,
  'pos': Point3(-6, 0, 0),
  'h': 180,
  'behavior': 'stand',
  'revives': random.choice([0, 1, 2]),
  'path': None,
  'skeleton': 0},
 {'parentEntId': FrontCogParent,
  'boss': 0,
  'level': random.choice([8, 9, 10]),
  'battleCell': FrontBattleCellId,
  'pos': Point3(-2, 0, 0),
  'h': 180,
  'behavior': 'stand',
  'revives': random.choice([0, 1, 2]),
  'path': None,
  'skeleton': 0},
 {'parentEntId': FrontCogParent,
  'boss': 0,
  'level': random.choice([8, 9, 10]),
  'battleCell': FrontBattleCellId,
  'pos': Point3(2, 0, 0),
  'h': 180,
  'behavior': 'stand',
  'revives': random.choice([0, 1, 2]),
  'path': None,
  'skeleton': 0},
 {'parentEntId': FrontCogParent,
  'boss': 0,
  'level': random.choice([8, 9, 10]),
  'battleCell': FrontBattleCellId,
  'pos': Point3(6, 0, 0),
  'h': 180,
  'behavior': 'stand',
  'revives': random.choice([0, 1, 2]),
  'path': None,
  'skeleton': 0}]
ReserveCogData = []
