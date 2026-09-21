import plotly.express as px
import pandas as pd

# Importation de la BDD
données = pd.read_csv('https://docs.google.com/spreadsheets/d/e/2PACX-1vSC4KusfFzvOsr8WJRgozzsCxrELW4G4PopUkiDbvrrV2lg0S19-zeryp02MC9WYSVBuzGCUtn8ucZW/pub?output=csv')

# Générer le graphique (type tarte/pie) de la quantité vendue par région avec plotly
figure = px.pie(données, values='qte', names='region', title='quantité vendue par région')

# Générer le fichier HTML avec le graphique visualisable.
figure.write_html('ventes-par-region.html')
print('ventes-par-région.html généré avec succès !')


# Agrégation : Calcul du nombre de ventes et du chiffre d'affaires
grp_données = données.groupby('produit').agg(
    nombre_ventes=('prix', 'count'),
    chiffre_affaires=('prix', 'sum')
).reset_index()

# Génération du graphique des ventes par produit
fig_ventes = px.bar(
    grp_données, 
    x='produit', 
    y='nombre_ventes', 
    title='Nombre de ventes par produit',
    labels={'nombre_ventes': 'Volume de ventes', 'produit': 'Produit'},
    text_auto=True
)
fig_ventes.write_html('ventes-par-produit.html')
print('ventes-par-produit.html généré avec succès !')

# Génération du graphique du chiffre d'affaires par produit
fig_ca = px.bar(
    grp_données, 
    x='produit', 
    y='chiffre_affaires',
    title="Chiffre d'affaires par produit",
    labels={'chiffre_affaires': "Chiffre d'affaires (€)", 'produit': 'Produit'},
    text_auto=True
)

fig_ca.write_html('ca-par-produit.html')
print('ca-par-produit.html généré avec succès !')