import re
from datetime import datetime
import matplotlib.pyplot as plt

def count_emoji_occurrences(file_path, emoji):
    # Ouvrir le fichier en mode lecture
    with open(file_path, 'r', encoding='utf-8') as file:
        # Lire le contenu du fichier
        content = file.read()

    # Utiliser une expression régulière pour trouver tous les emojis dans le texte
    emojis = re.findall(emoji, content)

    # Retourner le nombre total d'occurrences d'emoji
    return len(emojis)

def count_member_emoji_occurrences(file_path, member, emoji):
    # Ouvrir le fichier en mode lecture
    with open(file_path, 'r', encoding='utf-8') as file:
        # Lire le contenu du fichier
        content = file.read()

    # Utiliser une expression régulière pour extraire les messages du membre spécifié
    member_messages = re.findall(f'{member}: (.*?)\n', content)

    # Concaténer les messages du membre en une seule chaîne
    member_messages_text = ' '.join(member_messages)

    # Utiliser une expression régulière pour trouver tous les emojis dans les messages du membre
    emojis_in_member_messages = re.findall(emoji, member_messages_text)

    # Retourner le nombre d'occurrences d'emoji pour le membre spécifié
    return len(emojis_in_member_messages)

def count_days():
#     Compte le nombre de jours entre le premier et le dernier message
    with open('Discussion WhatsApp avec La communauté.txt', 'r', encoding='utf-8') as file:
        content = file.read()
    dates = re.findall(r'\d+/\d+/\d+', content)
    date_format = '%d/%m/%Y'
    dates = [datetime.strptime(date, date_format) for date in dates]
    return (dates[-1] - dates[0]).days + 1

def count_each_day(member, emoji_to_count):
    #pour un member donné, cette fonction va inspecter le fichier et toutes ses lignes et si l'emoji emoji_to_count
    # est présent, elle va récupérer la date du message qu'elle va stocker dans une liste list_dates et ajouter 1 à un
    # compteur dans une liste compte_cacas. Si la date est déjà dans list_dates, on ajoute 1 au compteur correspondant
    # dans compte_cacas. A la fin, on affiche les dates et le nombre de cacas pour chaque date.
    with open('Discussion WhatsApp avec La communauté.txt', 'r', encoding='utf-8') as file:
        content = file.readlines()
    list_dates = []
    compte_cacas = []
    for line in content:
        if member in line:
            if emoji_to_count in line:
                date = line.split(' ')[0]
                if date in list_dates:
                    compte_cacas[list_dates.index(date)] += 1
                else:
                    list_dates.append(date)
                    compte_cacas.append(1)
    for i in range(len(list_dates)):
        print(f"{list_dates[i]}: {compte_cacas[i]} cacas")
    plt.plot(list_dates, compte_cacas)
    # ajoute en pointillés la moyenne de cacas par jour
    plt.plot(list_dates, [sum(compte_cacas)/len(compte_cacas)]*len(compte_cacas), linestyle='--', color='green')




    plt.subplots_adjust(bottom=0.25)
    plt.gca().xaxis.set_major_locator(plt.MaxNLocator(10))
    plt.xticks(rotation=45)

    # Ajoute sur l'axe des ordonnées secondaire le nombre accumulé de cacas
    ax2 = plt.gca().twinx()
    ax2.plot(list_dates, [sum(compte_cacas[:i+1]) for i in range(len(compte_cacas))], color='red')
    ax2.set_ylabel('Nombre accumulé de cacas')
    ax2.tick_params(axis='y', labelcolor='red')
    ax2.set_ylim(bottom=0)

    plt.xlabel('Dates')
    plt.ylabel('Nombre de cacas')
    plt.title(f"Nombre de cacas par jour pour {member}")

    # enregistrer le graphe dans un fichier png avec le nom du membre
    plt.savefig(member+".png")
    plt.show()
    plt.close()

    print('caca')





# Exemple d'utilisation
file_path = 'Discussion WhatsApp avec La communauté.txt'
# # enlève les deux premières lignes de la discussion
# with open(file_path, 'r', encoding='utf-8') as file:
#     content = file.readlines()
# with open(file_path, 'w', encoding='utf-8') as file:
#     file.writelines(content[2:])

emoji_to_count = '💩'
member_to_count = ['Jordan Litaud', 'Xavier Sidambarompoulé', 'Maxime Picard', 'Kévin Champeroux', 'Florian']

days_difference = count_days()
total_occurrences = count_emoji_occurrences(file_path, emoji_to_count)

member_dict = {}
for member in member_to_count:
    member_occurrences = count_member_emoji_occurrences(file_path, member, emoji_to_count)
    member_dict[member]=member_occurrences
    count_each_day(member, emoji_to_count)
    print(f"Nombre d'occurrences de {emoji_to_count} pour {member}: {member_occurrences}, soit {member_occurrences / days_difference :.2f} cacas par jour")

print(f"Nombre total d'occurrences de {emoji_to_count}: {total_occurrences}")
print(member_dict)



