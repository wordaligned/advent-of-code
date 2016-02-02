from collections import namedtuple

# Inputs
boss_damage = 9  # The boss' attacks inflict this much damage
boss_points = 58 # The boss starts with this many points

# A representation of the state at some point in the game
game_state = namedtuple('game_state',
    ['turn',                    # Whose turn to attack?
     'spent',                   # Mana spent by the player
     'points', 'armour', 'mana',# Points, armour and mana the player has
     'effects',                 # Dict mapping active effects to durations
     'boss_points'])            # Points the boss has


# Each spell accepts a game state and returns a new game state
def missile(g):    return g._replace(boss_points=g.boss_points - 4)
def drain(g):      return g._replace(points=g.points + 2, boss_points=g.boss_points - 2)
# Poison and recharge have the same effect each turn they are active
def poison(g,_):   return g._replace(boss_points=g.boss_points - 3)
def recharge(g,_): return g._replace(mana=g.mana + 101)
# The shield affects turns 6 and 1
def shield(g,d):   return g._replace(armour=g.armour + {1:-7, 6:7}.get(d, 0))

spell  = namedtuple('spell', 'effect cost duration')
spells = (spell(missile,   53, 0),
          spell(drain,     73, 0),
          spell(shield,   113, 6),
          spell(poison,   173, 6),
          spell(recharge, 229, 5))

def process_effects(g):
    ' Process active effects and return the resulting game state. '
    for effect, duration in g.effects.items():
        g = effect(g, duration)
    # Reduce the effect durations, removing expired effects
    return g._replace(effects={e:d-1 for e,d in g.effects.items() if d > 1})

def cast(g, spell):
    ' Cast a spell and return the resulting game state. '
    g = g._replace(turn=boss,
                   spent=g.spent + spell.cost,
                   mana=g.mana - spell.cost,
                   effects=dict(g.effects)) # Note: copy the effects so the
                                            # input g's effects are not modified 
    if spell.duration == 0:
        g = spell.effect(g)
    else:
        g.effects[spell.effect] = spell.duration
    return g

def player(g):
    ' The player takes a turn, yielding possible new game states. '
    for spell in spells:
        if spell.cost <= g.mana and spell.effect not in g.effects:
            yield cast(g, spell)

def boss(g):
    ' The boss takes a turn, yielding the new game state. '
    damage = max(1, boss_damage - g.armour) # At least 1 damage done
    yield g._replace(turn=player, points=g.points - damage)

def play(game):
    ' Play the game, returning the least amount of mana spent to win. '
    cheap_win = 1000000

    def won(g):
        ' Return True if this game state is a win for the player. '
        nonlocal cheap_win
        if g.boss_points <= 0:
            cheap_win = min(cheap_win, g.spent)
            return True

    def lost(g):
        ' Return True if the player has lost. ' 
        return g.points <= 0

    def prune(g):
        ' Return True if this game state can be pruned from the search. '
        nonlocal cheap_win
        return g.spent >= cheap_win # Don't continue if we've overspent

    while game:
        g = process_effects(game.pop())
        if not won(g):
            game.extend(g for g in g.turn(g)
                        if not any((won(g), lost(g), prune(g))))
    return cheap_win

print(play([game_state(turn=player,
                       spent=0,
                       points=50,
                       armour=0,
                       mana=500,
                       boss_points=boss_points,
                       effects={})]))
