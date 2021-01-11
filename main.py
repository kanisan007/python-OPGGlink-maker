import json

champions = {}

with open('champions.json') as f:
    champions = json.loads(f.read())

role = input('チャンピオンのロールを指定してください。[top,jg,mid,adc,sup]\n> ')

# top_list1 = ['aatrox','akali','camille','chogath','darius','fiora','gangplank','garen','gnar','gragas','heimerdunger','illaoi','irelia','jax','jayce','kalista','kayle','kennen','kled','lucian','malphite','maokai','mordekaiser','nasus','ornn','pantheon','poppy','quinn','renekton','rengar','riven','rumble','ryze','sett','shen','singed','sion','sylas','teemo','tryndamere','urgot','vayne','viktor','vladmir','volivear','warwick','wukong','yasuo','yone','yorick','zac']
# jg_list1 = ['amumu','ekko','elise','evelynn','fiddlesticks','gragas','graves','hecarim','ivern','jarvaniv','jax','karthus','kayn','khazix','kindred','leesin','lillia','masteryi','nidalee','nocturne','nunu','olaf','poppy','rammus','reksai','rengar','sejuani','shaco','shyvana','skarner','taliyah','uder','vi','volibear','werwick','wukong','xinxhao','zac']
# mid_list1 = ['ahri','akali','anivia','annie','aurelionsol','azir','cassiopeia','chogath','corki','diana','ekko','fizz','galio','garen','irelia','jayce','kassadin','katarina','leblanc','lissandra','lusian','lux','malphite','malzahar','margana','neeko','nocturne','nunu','oriana','pantheon','pyke','qiyana','renekton','rumble','ryze','sett','swain','sylas','syndra','talon','tristana','twisteddate','veigar','viktor','vladmir','xerath','yasuo','yone','zed','zoe']
# adc_list1 = ['ashe','aphelios','caitlyn','draven','ezrial','jhin','jinx','kaisa','kalista','kogmaw','lucian','missfortune','samira','senna','sivir','swain','tristana','twitch','varus','vayne','xayah','yasuo']
# sup_list1 = ['alistar','anivia','ashe','bard','blitzcrank','brand','braum','fiddlesticks','galio','gragas','janna','karma','leona','lulu','lux','maokai','missfortune','morgana','nami','nautilus','neeko','pantheon','poppy','pyke','rakan','rell','senna','seraphine','sett','shaco','shen','sona','soraka','swain','taric','thresh','twitch','velkoz','xerath','yuumi','zac zilean','zyra']

def get_role_id(role: str):
    roles = {
        'top': 'top',
        'jg': 'jungle',
        'mid': 'mid',
        'adc': 'adc',
        'sup': 'support',
    }
    if role not in roles:
        raise Exception('ロールが不正です。')
    return roles[role]

if role not in champions:
    raise Exception('ロールが不正です。')

print(champions[role])
champion = input('チャンピオン名を指定してください\n> ')

if champion not in champions[role]:
    raise Exception('チャンピオン名が不正です')

print('https://jp.op.gg/champion/' + champion + '/statistics/' + get_role_id(role))

# print('そのロールに適したチャンピオンはこれです。')

# if role=='top':
#     print(top_list1)
#     champion = input('チャンピオン名を指定してください')
#     url = 'https://jp.op.gg/champion/'+champion+'/statistics/'+role
#     print(url)

# elif role=='jg':
#     role = 'jungle'
#     print(jg_list1)
#     champion = input('チャンピオン名を指定してください')

#     url = 'https://jp.op.gg/champion/'+champion+'/statistics/'+role
#     print(url)

# elif role=='mid':
#     print(mid_list1)
#     champion = input('チャンピオン名を指定してください')

#     url = 'https://jp.op.gg/champion/'+champion+'/statistics/'+role
#     print(url)


# elif role=='adc':
#     print(adc_list1)
#     champion = input('チャンピオン名を指定してください')

#     url = 'https://jp.op.gg/champion/'+champion+'/statistics/'+role
#     print(url)

# elif role=='sup':
#     role = 'support'
#     print(sup_list1)
#     champion = input('チャンピオン名を指定してください')

#     url = 'https://jp.op.gg/champion/'+champion+'/statistics/'+role
#     print(url)

# else:
#     print('入力が不正です。もう一度やり直してください')


