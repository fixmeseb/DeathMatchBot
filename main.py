import json
import random
import time
import discord
from discord import app_commands
import os
from typing import Optional


from embeds import createPlaceEmbed
from embeds import createWeaponEmbed
from embeds import createAdjectiveEmbed
from embeds import createPlaceEmbed
from embeds import createCompetitionEmbed
from embeds import createPersonEmbed


from generation import generatePerson
from generation import generateWeapon
from generation import generatePlace
from generation import generateAdjective
from generation import generateContest
from objects import Person

# Replace with your actual token and guild ID
tokenFile = open("token.txt", "r", encoding='utf-8-sig')
tokenString = tokenFile.read()
tokens = tokenString.split('\n')
TOKEN = tokens[0]

testToken = tokens[1]
userID = int(tokens[2])
GUILD_ID = 889564564365127751  # Your guild ID as integer

intents = discord.Intents.default()
intents.message_content = True  # Make sure this is enabled
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

discordEmojiList = ["test server", "1DiscordEmoji", "2DiscordEmojis", "3DiscordEmojis", "4DiscordEmojis", "5DiscordEmojis", "6EmojiServer", "7EmojiServer", "8EmojiServer", "9EmojiServer", "10DiscordEmojis", "11DiscordEmojis", "12DiscordEmojis", "13DiscordEmojis", "CA Teacher Emojis", "2CA Teacher Emojis"]
#List of servers with the Discord Emojis. 

@tree.command(
        name="place", 
        description="Generate a random place!", 
)
async def place(interaction: discord.Interaction):
    place = generatePlace()
    await interaction.response.send_message(f"{place.name}!")

@tree.command(
    name="weapon",
    description="Get a random weapon!",
)
async def weaponMe(interaction: discord.Interaction):
    weapon = generateWeapon()
    await interaction.response.send_message(f"{weapon.tagline.capitalize()}!")

@tree.command(
    name="adjective",
    description="Get a random adjective!",
)
async def adjectiveMe(interaction: discord.Interaction):
    adjective = generateAdjective()
    await interaction.response.send_message(f"{adjective.name.capitalize()}!")

@tree.command(
    name="person",
    description="Get a random person!",
)
async def peopleMe(interaction: discord.Interaction):
    with open(f"people.json", "r", encoding='utf-8') as f:
        data = json.load(f)
    person = generatePerson(data)
    await interaction.response.send_message(f"{person.name}!")

@tree.command(
    name="contestant",
    description="Gets a random person, arms them, and gives them a power!",
)
async def contestant(interaction: discord.Interaction):
    with open(f"people.json", "r", encoding='utf-8') as f:
        data = json.load(f)
    person = generatePerson(data)
    human = person
    adjective = generateAdjective()
    weapon = generateWeapon()

    await interaction.response.send_message(f"{adjective.tagline.capitalize()}{human.name} with {weapon.tagline}!")

@tree.command(
    name="powerup",
    description="Give yourself a weapon and a power!",
)
async def powerUp(interaction: discord.Interaction, recipient: Optional[str] = None):
    if recipient == None:
        adjective = generateAdjective().strip()
        weapon = generateWeapon()
        await interaction.response.send_message(f"You are {adjective} and you have {weapon.name}!")
    else:
        adjective = generateAdjective().capitalize()
        weapon = generateWeapon()
        await interaction.response.send_message(f"{adjective}{recipient} with {weapon.name}!")

@tree.command(
    name="lincoln",
    description="Get a photo of Abraham Lincoln!",
)
async def lincoln(interaction: discord.Interaction):
    global numberOfLincolnPics
    randomNum = random.randint(1,15)
    picturePath = "lincoln" + str(randomNum)
                
    numberOfLincolnPics+=1
    if os.path.exists("Pictures\\Lincoln\\" + picturePath + ".png"):
        await interaction.response.send_message(file=discord.File("Pictures\\Lincoln\\" + picturePath + ".png"))
    else:
        if os.path.exists("Pictures\\Lincoln\\" + picturePath + ".jpg"):
            await interaction.response.send_message(file=discord.File("Pictures\\Lincoln\\" + picturePath + ".jpg"))

@tree.command(
    name="ranked",
    description="Launches ranked matches for HDM. Moderators only!",
)
@discord.app_commands.checks.has_permissions(administrator=True)
async def ranked(interaction: discord.Interaction):
    print("Launching a ranked match!")
    numberOfMatches = 5

    validServers = {
        889564564365127751: [1466213635004301372, 1466212235897475194],
        1173402242989166702: [1466213379051094183, 1466213354308894895]
    }
    for serverID in validServers.keys():
        print(f"HDM Time in {serverID}!")
        data = None
        if os.path.exists(f"Current Brackets\\{serverID}_bracket.json"):
            with open(f"Current Brackets\\{serverID}_bracket.json", "r", encoding='utf-8') as f:
                data = json.load(f)
        else:
            with open("people.json", "r", encoding='utf-8') as f:
                data = json.load(f)
            with open(f"Current Brackets\\{serverID}_bracket.json", "w", encoding='utf-8') as json_file:
                json.dump(data, json_file, indent=2, ensure_ascii=False)
                match_file = open(f"match_nums\\matchNum{serverID}.txt", "w")
                match_file.write(f"{1}\n{1}\n{1}")
        if data:
            if len(data) >= numberOfMatches*2:
                print(f"\tNumber of matches is good.")
            else:
                print(f"\tDecreasing number of matches.")
                numberOfMatches = round(len(data)/2)
            print(f"Generating fighters for {numberOfMatches} matches:")
            matches = []
            print(f"Starting with {len(data)} people in bracket")
            #print(f"Keys at start: {list(data.keys())}")
            for i in range(numberOfMatches):
                print(f"\n=== Creating match {i + 1} ===")
                fighters = []
                for j in range(2):
                    print(f"Before selection: {len(data)} people available")
                    current_fighter = generatePerson(data)
                    if current_fighter.key in data:
                        print(f"\tFound {current_fighter.key} in data, removing...")
                        data.pop(current_fighter.key, None)
                    fighters.append(current_fighter)
                    print(f"\t{current_fighter.name} was chosen!")
                match = generateContest(fighters)
                matches.append(match)
            
            print(f"Ending with {len(data)} people in bracket")
            server = client.get_guild(serverID)

            poll_channel = server.get_channel(validServers[serverID][0])
            info_channel = server.get_channel(validServers[serverID][1])
            match_num = int(open(f"match_nums\\matchNum{serverID}.txt", "r", encoding='utf-8-sig').read().split("\n")[0])
            round_num = int(open(f"match_nums\\matchNum{serverID}.txt", "r", encoding='utf-8-sig').read().split("\n")[1])
            total_match_num = int(open(f"match_nums\\matchNum{serverID}.txt", "r", encoding='utf-8-sig').read().split("\n")[2])

            for match in matches:
                match_string = ""
                fighter_strings = []
                for fighter in match.fighters:
                    person_embed = createPersonEmbed(fighter)
                    person_embed.add_field(name="Return to Match", value=f"{poll_channel.jump_url}", inline=False)
                    fighter.info_id = await info_channel.send(embed=person_embed)
                    fighter_string = f"[{fighter.name}]({fighter.info_id.jump_url})"
                    if fighter.adjective != None:
                        adjective_embed = createAdjectiveEmbed(fighter.adjective)
                        adjective_embed.add_field(name="Return to Match", value=f"{poll_channel.jump_url}", inline=False)
                        fighter.adjective.info_id = await info_channel.send(embed=adjective_embed)
                        fighter_string = f"[{fighter.adjective.tagline}]({fighter.adjective.info_id.jump_url}){fighter_string}"
                    if fighter.weapon != None:
                        weapon_embed = createWeaponEmbed(fighter.weapon)
                        weapon_embed.add_field(name="Return to Match", value=f"{poll_channel.jump_url}", inline=False)
                        fighter.weapon.info_id = await info_channel.send(embed=weapon_embed)
                        fighter_string = f"{fighter_string} with [{fighter.weapon.tagline}]({fighter.weapon.info_id.jump_url})"
                    fighter_strings.append(fighter_string)
                match_embed = createCompetitionEmbed(match)
                match_embed.add_field(name="Return to Match", value=f"{poll_channel.jump_url}", inline=False)
                match.info_id = await info_channel.send(embed=match_embed)
                match_string = f"{fighter_strings[0]} versus {fighter_strings[1]} in [{match.tagline}]({match.info_id.jump_url})"
                if match.place != None:
                    place_embed = createPlaceEmbed(match.place)
                    place_embed.add_field(name="Return to Match", value=f"{poll_channel.jump_url}", inline=False)
                    match.place.info_id = await info_channel.send(embed=place_embed)
                    match_string = f"{match_string}[{match.place.tagline}]({match.place.info_id.jump_url})"
                match_string = f"{match_string}!"
                embed = discord.Embed(title=f"Round #{round_num} Match #{match_num} (Total Match #{total_match_num})", description=f"{match_string[0]+match_string[1].upper()+match_string[2:]}", color=0xFF9900)
                match_id = await poll_channel.send(embed=embed)
                for fighter in match.fighters:
                    emoji = client.get_emoji(fighter.emoji_id)
                    await match_id.add_reaction(emoji)
                match_num+=1
                total_match_num+=1
                print("Completed match.")
            
            match_file = open(f"match_nums\\matchNum{serverID}.txt", "w")
            match_file.write(f"{match_num}\n{round_num}\n{total_match_num}")
            print(f"Completing Game with {len(data)} people remaining.")
            with open(f"Current Brackets\\{serverID}_bracket.json", "w", encoding='utf-8') as json_file:
                json.dump(data, json_file, indent=2, ensure_ascii=False)
            
@client.event
async def on_ready():
    print(f'Logged in as {client.user}')
    print(f"Guild object: {discord.Object(GUILD_ID)}")
        
    # Try syncing
    try:
        synced = await tree.sync()
        print(f"Synced {len(synced)} command(s)")
        for cmd in synced:
            print(f"  - {cmd.name}")
    except Exception as e:
        print(f"Error syncing: {e}")

client.run(TOKEN)