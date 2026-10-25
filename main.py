def decompression_lzw(codes):
    if not codes:
        return "", {}

    # 1. Initialisation du dictionnaire avec l'alphabet de base
    # Pour la décompression : code (int) -> chaîne (str)
    dictionnaire = {
        0: 'a',
        1: 'b',
        2: 'c'
    }
    next_code = 3

    # 2. Traitement du premier code
    premier_code = codes[0]
    chaine_precedente = dictionnaire[premier_code]
    resultat = [chaine_precedente]

    # 3. Traitement des codes suivants
    for code in codes[1:]:
        # Cas standard : le code est déjà présent dans le dictionnaire
        if code in dictionnaire:
            chaine_courante = dictionnaire[code]
        # Cas particulier LZW (code non encore présent) : prev + prev[0]
        elif code == next_code:
            chaine_courante = chaine_precedente + chaine_precedente[0]
        else:
            raise ValueError(f"Code LZW invalide détecté : {code}")

        # Ajout du texte décodé
        resultat.append(chaine_courante)

        # Mise à jour dynamique du dictionnaire
        dictionnaire[next_code] = chaine_precedente + chaine_courante[0]
        next_code += 1

        # Mise à jour de la chaîne précédente
        chaine_precedente = chaine_courante

    chaine_finale = "".join(resultat)
    return chaine_finale, dictionnaire


def main():
    print("=== Projet n°3 : Décompression LZW ===")

    # Lecture de la séquence de codes en entrée
    entree = input("Entrez les codes séparés par des espaces (ex: 0 1 3 2) : ").strip()

    if not entree:
        print("Aucun code fourni.")
        return

    try:
        codes = [int(x) for x in entree.split()]
    except ValueError:
        print("Erreur : Tous les éléments doivent être des entiers.")
        return

    # Décompression
    texte_reconstruit, dictionnaire_final = decompression_lzw(codes)

    # Affichage du résultat
    print("\nChaîne de caractères décompressée :")
    print(texte_reconstruit)

    # Visualisation du dictionnaire reconstruit
    print("\n--- Dictionnaire généré lors de la décompression ---")
    print(f"{'Code':<8} | {'Sous-chaîne':<15}")
    print("-" * 26)
    for code, motif in dictionnaire_final.items():
        print(f"{code:<8} | {motif:<15}")


if __name__ == "__main__":
    main()