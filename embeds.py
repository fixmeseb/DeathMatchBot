# The file for creating the Discord embeds that HDM sends.
import discord

def createPersonEmbed(person):
    print(f"Person Embed: {person.name}")
    embed = discord.Embed(title=person.name.title(), description=person.description, color=0xFF9900)
    embed.add_field(name="Link", value=person.link, inline=False)
    embed.set_image(url=person.image)
    embed.set_footer(text="Created by The Invisible Man", icon_url="https://i.imgur.com/tce0LOa.jpg")
    return embed
#Returns an embed object created from the inputed person.
def createWeaponEmbed(weapon):
    print(f"Weapon Embed: {weapon.name}")
    embed = discord.Embed(title=weapon.name.title(), description=weapon.description, color=0xFF9900)
    embed.add_field(name="Link", value=weapon.link, inline=False)
    embed.set_image(url=weapon.image)
    embed.set_footer(text="Created by The Invisible Man", icon_url="https://i.imgur.com/tce0LOa.jpg")
    return embed
#Returns an embed object from the weapon inputed. 
def createPlaceEmbed(place):
    print(f"Place Embed: {place.name}")
    embed = discord.Embed(title=place.name.title(), description=place.description, color=0xFF9900)
    embed.add_field(name="Link", value=place.link, inline=False)
    embed.set_image(url=place.image)
    embed.set_footer(text="Created by The Invisible Man", icon_url="https://i.imgur.com/tce0LOa.jpg")
    return embed
#Returns an embed with the place inputed. 
def createAdjectiveEmbed(adjective):
    print(f"Adjective: {adjective.name}")
    embed = discord.Embed(title=adjective.name.title(), description=adjective.description.capitalize(), color=0xFF9900)
    embed.add_field(name="Link",value=adjective.link, inline=False)
    embed.set_footer(text="Created by The Invisible Man", icon_url="https://i.imgur.com/tce0LOa.jpg")
    return embed
#Create an adjective embed
def createCompetitionEmbed(contest):
    print(f"Contest Embed: {contest.type}")
    embed = discord.Embed(title=f"{contest.type.title()}", description=contest.description, color=0xFF9900)
    embed.add_field(name="Rules",value=contest.rules, inline=False)
    embed.add_field(name="Link",value=contest.link, inline=False)
    embed.set_footer(text="Created by The Invisible Man", icon_url="https://i.imgur.com/tce0LOa.jpg")
    return embed
#Creates an embed for the competition.