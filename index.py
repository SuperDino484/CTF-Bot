@bot.command(pass_context = True)
async def createteam(ctx, teamName=None):
    admin = ctx.message.author
    if admin.server_permissions.administrator:
        if teamName==None:
            await bot.say('`!createteam <teamName>`')
        else:
            f = open(teamName.upper()+'.txt', 'w')
            f.close()
            await bot.say('Team `{}` has been created!'.format(teamName.capitalize()))
    else:
        await bot.say('\U0000274C Invalid Permissions! \U0000274C')

        
@bot.command(pass_context = True)
async def disbandteam(ctx, teamName=None):
    admin = ctx.message.author
    if admin.server_permissions.administrator:
        if teamName==None:
            await bot.say('`!disbandteam <teamName>`')
        else:
            if os.path.exists(teamName.upper()+'.txt'):
                os.remove(teamName.upper()+'.txt')
                await bot.say('The team `{}` does not exist anymore. `GG`'.format(teamName.capitalize()))
            else:
                await bot.say('The team `{}` does not exist.'.format(teamName.capitalize()))
            
    else:
        await bot.say('\U0000274C Invalid Permissions! \U0000274C')
@bot.command()
async def roster(teamName=None, teamName2=''):
    if teamName==None:
        await bot.say('`!roster <team>`')
    else:
        try:
            with open(teamName.upper()+teamName2+'.txt') as f:
                f.seek(0)
                await bot.say('\`\`\`\n\t{}\n{}\`\`\`'.format(teamName.capitalize(),f.read()))
        except:
            await bot.say('The team `{}` does not exist.'.format(teamName.capitalize()))
