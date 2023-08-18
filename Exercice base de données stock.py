import sqlite3

conn = sqlite3.connect('Stock_objet.db')
cur = conn.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS Stock(id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE, Nom_produit TEXT, Prix FLOAT, Obj_en_stock INTEGER)")

def affichage_du_stock():
    cur.execute('SELECT * FROM Stock')
    liste_stock = cur.fetchall()
    return print(liste_stock)

def affichage_produit(Nom_produit):
    Nom = (str(Nom_produit))
    cur.execute('SELECT * FROM Stock WHERE Nom_produit = ?', Nom)
    Objet_cherché = cur.fetchall()
    conn.commit()
    return print(Objet_cherché)

def ajouter_un_produit(Nom_produit, Prix_produit, Stock_produit):
    nouveau_produit = (str(Nom_produit),float(Prix_produit),int(Stock_produit))
    cur.execute("INSERT INTO Stock(Nom_produit,Prix,Obj_en_stock) VALUES(?, ?, ?)", nouveau_produit)
    conn.commit()
    return 

def mise_a_jour_stock(Nom_produit, stock_en_plus):
    Nom = Nom_produit
    cur.execute('SELECT Obj_en_stock FROM Stock WHERE Nom_produit = ?', (Nom,))
    Ancien_stock = cur.fetchall()
    nvx_stock = int(Ancien_stock[0][0]) + int(stock_en_plus)
    nouveau_stock = (int(nvx_stock),str(Nom_produit))
    cur.execute('UPDATE Stock SET Obj_en_stock = ? WHERE Nom_produit = ?', nouveau_stock)
    conn.commit()
    return

def calcul_prix_stock(Nom_produit):
    Nom = Nom_produit
    cur.execute('SELECT Obj_en_stock, Prix FROM Stock WHERE Nom_produit = ?', (Nom,))
    Données_recupérée = cur.fetchall()
    prix_total_stock = int(Données_recupérée[0][0]) * float(Données_recupérée[0][1])
    return print(prix_total_stock)

def gestion_du_stock():
    choix = str(input("Si vous voulez affichez la liste des produits en stock tapez 1, si vous voulez chercher un produit en particulier tapez 2, si vous voulez ajoutez un produit  3, si vous voulez mettre a jour le stock d'un produit tapez 4, si vous voulez calculer la valeur total du stock d'un produit tapez 5. "))
    if choix == '1':
        affichage_du_stock()
    elif choix == '2':
        Nom_produit = input('Quel est le nom du produit que vous cherchez ?')
        affichage_produit(Nom_produit)
    elif choix == '3':
        Nom_produit = input('Quel est le nom du produit que vous voulez ajouter ?')
        Stock_produit = input('Quel est le stock de ce produit ?')
        Prix_produit = input('Quel est le prix de ce produit ?')
        ajouter_un_produit(Nom_produit, Prix_produit, Stock_produit)
    elif choix == '4' :
        Nom_produit = input('Quel est le nom du produit auquel vous voulez ajouter ou enlever du stock ?')
        stock_en_plus = input('Quel est le stock que vosu voulez ajouter ou enlever ?')
        mise_a_jour_stock(Nom_produit, stock_en_plus)
    elif choix == '5':
        Nom_produit = input('Quel est le nom du produit dont vous voulez connaitre le prix du stock total ?')
        calcul_prix_stock(Nom_produit)
    else :
        return "Le chiffre rentrée n'est en lien avec aucune requete"


gestion_du_stock()

cur.close()
conn.close()