# Currently in progress: Combat system

Further stuff to do: creating ASCII art for levels, characters, flavor, so on, as well implementing a save mechanism

Combat system:

"For the combat, we could have 4 things to do: Attack, Magic, Heal, Flee
For attack: values based on the weapon that the character is wearing
Mana: high damage, but takes some time to recharge (after 2 battles)
Heal: if successful, heals either 5% or 10% of total character HP (not much at start, but will be quite helpful in endgame)
Flee: random chance"

"You mean similar to like the Pokémon combat system"

Player info:

"i have created a simple tester player file with the configparser lib"

"Okay, I created a player_data_injector function, that creates a player object from the players game data from the corresponding config file
Now you can either create a new player or select an existing player and load its file data into a player object"

Save game: JSON?

Levels:

Level 0: Baptism By Fire (tutorial level)
Level 1: Over The Hills
Level 2: Degenerates, Degenerates Everywhere
Level 3: The Hunt For Red Witch
Level 4: Blackburn's Revenge
Level 5: The Final Struggle

Reuse of some of enemies are allowed, but has to be consistent transition

To-do:

- [ ] Drawing of how the combat should look like
- [ ] Drawing of how the simple shop should look like

Level 1:
    - [ ] Enemies
    - [ ] Friendly Wanderer + dialogue + implementation of buying stuff
    - [ ] Zooming in the ruins of a city
    - [ ] Map
