def total_price2_1(liste_art):
    """_summary Somme totale des prix des artciles d'une liste d'article

    Args:
        liste_art (tuple): liste des article du magasin contenant la ref le nom le prix 

    Returns:
        int: total des prix des articles du magasin
    """    
    total_euro = 0
    for art in liste_art:
        total_euro =total_euro + art[2]
    return total_euro

def test_total_price2_1():
    assert total_price2_1([(152,"chaussures",37.5),(145,"Veste",87.5),(147,"T-shirt",25.3),(165,"Bonnet",11.0)]) == 161.3
    assert total_price2_1([]) == 0
    assert total_price2_1([(152,"chaussures",10.0),(145,"Veste",10.0),(147,"T-shirt",10.0),(165,"Bonnet",10.0)]) == 40.0
    assert total_price2_1([(152,"chaussures",37.5),(145,"Veste",87.5),(147,"T-shirt",25.3),(165,"Bonnet",11.0),(165,"Bonnet",87.5)]) == 248.8


def name_of_first_top_price2_2(liste_art):
    """_summary_ Déterminer l'article le plus cher d'une liste d'articles s'il y en a plusieur : ne garder que le premier trouvé

    Args:
        liste_art (list): liste des articles 

    Returns:
        str: Nom du premier article qui coute le plus cher trouvé
    """
    prec=0
    max_price=0
    nom_article = ""
    for elem in liste_art:
        if elem[2] > prec and elem[2] > max_price:
            nom_article = elem[1]
            max_price=elem[2]
        prec = elem[2]
    return nom_article

def test_name_of_first_top_price2_2():
    assert name_of_first_top_price2_2([(152,"chaussures",37.5),(145,"Veste",87.5),(147,"T-shirt",25.3),(165,"Bonnet",11.0)]) == "Veste"
    assert name_of_first_top_price2_2([]) == ""
    assert name_of_first_top_price2_2([(152,"chaussures",10.0),(145,"Veste",10.0),(147,"T-shirt",10.0),(165,"Bonnet",10.0)]) == "chaussures"
    assert name_of_first_top_price2_2([(152,"chaussures",37.5),(145,"Veste",87.5),(147,"T-shirt",25.3),(165,"Bonnet",11.0),(165,"Bonnet",87.5)]) == "Veste"
