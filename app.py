import streamlit as st
import random

# Configuration de la page
st.set_page_config(page_title="Aux Éthalchimistes !", page_icon="🧪", layout="centered")

# Style CSS pour l'ambiance Laboratoire sombre
st.markdown("""
    <style>
    .main { background-color: #0e1117; color: #e0e0e0; }
    .stButton>button {
        width: 100%;
        border-radius: 20px;
        height: 3em;
        background-color: #f39c12;
        color: white;
        font-weight: bold;
        border: none;
    }
    .stButton>button:hover { background-color: #d35400; color: white; }
    .card {
        padding: 30px;
        border-radius: 15px;
        background: rgba(255, 255, 255, 0.05);
        border: 1px solid #f39c12;
        text-align: center;
        margin-bottom: 20px;
    }
    .stade-badge {
        font-size: 0.8em;
        text-transform: uppercase;
        color: #f39c12;
        letter-spacing: 2px;
    }
    </style>
    """, unsafe_allow_html=True)

# Ta base de données de défis
defis = [
    {"titre": "Précision Optique", "texte": "Décontamination immédiate des verres ! Buvez autant de gorgées qu'il y a de binoclards aux lunettes sales autour de la table. Les malpropres, nettoyez vos lunettes.", "stade": "Filtration", "icone": "👓"},
    {"titre": "Le Cobaye", "texte": "Désignez celui qui serait le premier à boire une potion louche. Il boit 2 gorgées.", "stade": "Filtration", "icone": "🧪"},
    {"titre": "Analyse de Matière", "texte": "Tous ceux qui portent du noir doivent vider le fond de leur éprouvette.", "stade": "Filtration", "icone": "⚗️"},
    {"titre": "L'Infiltré", "texte": "Cite 3 pays commençant par B en 5 sec, sinon tu sers tout le monde pendant 10 min.", "stade": "Filtration", "icone": "🔍"},
    {"titre": "Affinité Élective", "texte": "Si tu as déjà envoyé un message à ton ex après une séance d'alchimie, bois 3 gorgées.", "stade": "Filtration", "icone": "💌"},
    {"titre": "L'Équilibre Instable", "texte": "Tiens sur une jambe pendant 20 sec. Si tu tombes, bois la différence.", "stade": "Ébullition", "icone": "⚖️"},
    {"titre": "Transmutation", "texte": "Échange ton verre avec celui du joueur à ta gauche.", "stade": "Ébullition", "icone": "🔄"},
    {"titre": "Le Maître du Silence", "texte": "Interdiction de parler jusqu'au prochain tour. 2 gorgées par mot prononcé.", "stade": "Ébullition", "icone": "🤫"},
    {"titre": "Duel de Regard", "texte": "Premier qui cligne des yeux boit le mélange concocté par les autres.", "stade": "Ébullition", "icone": "👀"},
    {"titre": "Le Grimoire des Secrets", "texte": "Raconte ta pire honte. Si c'est jugé 'petit', bois 4 gorgées.", "stade": "Distillation", "icone": "📜"},
    {"titre": "Test de Pureté", "texte": "Je n'ai jamais été arrêté par la police. Les coupables boivent.", "stade": "Distillation", "icone": "👮"},
    {"titre": "Vapeurs de Vérité", "texte": "Quel joueur appellerais-tu pour enterrer un corps ? Le désigné boit.", "stade": "Distillation", "icone": "💀"},
    {"titre": "Synapse Brisée", "texte": "Récite l'alphabet à l'envers depuis Z. Chaque erreur = 1 gorgée.", "stade": "Distillation", "icone": "🧠"},
    {"titre": "Loi de Lavoisier", "texte": "Interdiction de poser son verre sur la table. Sinon 2 gorgées.", "stade": "Fusion", "icone": "☢️"},
    {"titre": "L'Isotope", "texte": "Choisis un binôme. Quand l'un boit, l'autre boit aussi.", "stade": "Fusion", "icone": "⛓️"},
    {"titre": "Éruption Volcanique", "texte": "Tous les garçons/filles finissent leur verre.", "stade": "Fusion", "icone": "🌋"}
]

# Interface
st.title("🧪 Aux Éthalchimistes !")
st.write("*La science exacte de la dérive entre amis.*")

# Initialisation de la session pour garder le défi affiché
if 'current_defi' not in st.session_state:
    st.session_state.current_defi = random.choice(defis)

# Bouton pour piocher
if st.button("MÉLANGER LES POTIONS"):
    st.session_state.current_defi = random.choice(defis)

# Affichage du défi
d = st.session_state.current_defi
st.markdown(f"""
    <div class="card">
        <div class="stade-badge">{d['stade']} {d['icone']}</div>
        <h2 style="color: #f39c12;">{d['titre']}</h2>
        <p style="font-size: 1.2em;">{d['texte']}</p>
    </div>
    """, unsafe_allow_html=True)
