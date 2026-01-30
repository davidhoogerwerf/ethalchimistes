import streamlit as st
import random
from PIL import Image

# Charger l'image
try:
    img = Image.open("Ethalchimistes_Logo.png")
except:
    img = "🧪"

# Configuration de la page
st.set_page_config(page_title="Aux Éthalchimistes !", page_icon=img, layout="centered")

# Style CSS
st.markdown("""
    <style>
    .main { background-color: #0e1117; color: #e0e0e0; }
    .stButton>button {
        width: 100%; border-radius: 20px; height: 3em;
        background-color: #f39c12; color: white; font-weight: bold; border: none;
    }
    .card {
        padding: 30px; border-radius: 15px; background: rgba(255, 255, 255, 0.05);
        border: 1px solid #f39c12; text-align: center; margin-bottom: 20px;
    }
    .stade-badge { font-size: 0.8em; text-transform: uppercase; color: #f39c12; letter-spacing: 2px; }
    .title { text-align: center }
    </style>
    """, unsafe_allow_html=True)

# Base de données
defis = [
    {"titre": "Précision Optique", "texte": "Décontamination immédiate des verres ! Buvez autant de gorgées qu'il y a de binoclards. Les malpropres, nettoyez vos lunettes.", "stade": "Filtration", "icone": "👓"},
    {"titre": "L'Écho d'Istanbul", "texte": "Qui dit Istanbul ?! Les perdants boivent autant de gorgées qu'il y a de cobayes lents.", "stade": "Ébullition", "icone": "🕌"},
    {"titre": "Le Fournisseur de l'Ombre", "texte": "Qui dit l'homme au bureau de tabac ?! Les perdants boivent autant de gorgées qu'il y a de lents.", "stade": "Ébullition", "icone": "🚬"},
    {"titre": "Manque de Rigueur", "texte": "Le premier qui fait un éffort distribuera 3 pénalités.", "stade": "Fusion", "icone": "👨‍🏫"},
    {"titre": "Le Cobaye", "texte": "Désignez celui qui serait le premier à boire une potion louche (Loann). Il boit 2 gorgées.", "stade": "Filtration", "icone": "🧪"},
    {"titre": "Le Cavalier Solitaire", "texte": "Le premier qui trouve une photo de Trump sur un cheval peut distribuer 4 pénalités.", "stade": "Distillation", "icone": "🐎"},
    {"titre": "La Torture", "texte": "Le premier qui sort une photo d'Océane avec une tortue peut distribuer 3 pénalités.", "stade": "Distillation", "icone": "🐢"},
    
    {"titre": "Analyse de Matière", "texte": "Tous ceux qui portent du noir doivent vider le fond de leur éprouvette.", "stade": "Filtration", "icone": "⚗️"},
    {"titre": "L'Infiltré", "texte": "Cite 3 pays commençant par B en 5 sec, sinon tu sers tout le monde pendant 10 min.", "stade": "Filtration", "icone": "🔍"},
    {"titre": "Affinité Élective", "texte": "Si tu as déjà envoyé un message à ton ex après une séance d'alchimie, bois 3 gorgées.", "stade": "Filtration", "icone": "💌"},
    {"titre": "L'Équilibre Instable", "texte": "Tiens sur une jambe pendant 20 sec. Si tu tombes, bois la différence.", "stade": "Ébullition", "icone": "⚖️"},
    {"titre": "Transmutation", "texte": "Échange ton verre avec celui du joueur à ta gauche.", "stade": "Ébullition", "icone": "🔄"},
    {"titre": "Le Maître du Silence", "texte": "Interdiction de parler jusqu'au prochain 'Ébullition'. 2 gorgées par mot.", "stade": "Ébullition", "icone": "🤫"},
    {"titre": "Duel de Regard", "texte": "Premier qui cligne des yeux boit le mélange concocté par les autres.", "stade": "Ébullition", "icone": "👀"},
    {"titre": "Le Grimoire des Secrets", "texte": "Raconte ta pire honte. Si c'est jugé 'petit', bois 4 gorgées.", "stade": "Distillation", "icone": "📜"},
    {"titre": "Test de Pureté", "texte": "Je n'ai jamais été arrêté par la police. Les coupables boivent.", "stade": "Distillation", "icone": "👮"},
    {"titre": "Vapeurs de Vérité", "texte": "Quel joueur appellerais-tu pour enterrer un corps ? Le désigné boit.", "stade": "Distillation", "icone": "💀"},
    {"titre": "Synapse Brisée", "texte": "Récite l'alphabet à l'envers depuis Z. Chaque erreur = 1 gorgée.", "stade": "Distillation", "icone": "🧠"},
    {"titre": "Loi de Lavoisier", "texte": "Interdiction de poser son verre sur la table. Sinon 2 gorgées.", "stade": "Fusion", "icone": "☢️"},
    {"titre": "L'Isotope", "texte": "Choisis un binôme. Quand l'un boit, l'autre boit aussi.", "stade": "Fusion", "icone": "⛓️"},
    {"titre": "Éruption Volcanique", "texte": "Tous les garçons/filles finissent leur verre.", "stade": "Fusion", "icone": "🌋"}
]

# --- LOGIQUE DE GESTION DU JEU ---

# Initialisation de la pioche
if 'pioche' not in st.session_state:
    st.session_state.pioche = list(defis)
    random.shuffle(st.session_state.pioche)
    st.session_state.current_defi = None # Aucun défi au début
    st.session_state.game_over = False

# --- INTERFACE ---
st.title("🌈🍷 Aux Éthalchimistes ! 🍺🌈")

# ÉCRAN DE DÉBUT
if st.session_state.current_defi is None and not st.session_state.game_over:
    st.markdown("""
        <div class="card">
            <div class="stade-badge">Accueil</div>
            <h2 style="color: #f39c12;">Bienvenue à la Taverne !🍻</h2>
            <p style="font-size: 1.2em;">Préparez vos bites et vos couteaux. <br> A vos bières bandes de tartiflettes...</p>
        </div>
        """, unsafe_allow_html=True)
    
    if st.button("LET'S GO !"):
        st.session_state.current_defi = st.session_state.pioche.pop()
        st.rerun()

# ÉCRAN DE FIN
elif st.session_state.game_over:
    st.markdown("""
        <div class="card">
            <div class="stade-badge">Fin de l'expérience</div>
            <h2 style="color: #f39c12;">Laboratoire Fermé 💀</h2>
            <p style="font-size: 1.2em;">Le grimoire est vide et vos foies sont en fusion.<br>Voulez-vous relancer une nouvelle série de tests ?</p>
        </div>
        """, unsafe_allow_html=True)
    
    if st.button("RECOMMENCER UNE PARTIE"):
        st.session_state.pioche = list(defis)
        random.shuffle(st.session_state.pioche)
        st.session_state.current_defi = None
        st.session_state.game_over = False
        st.rerun()

# ÉCRAN DE JEU (Pendant les défis)
else:
    d = st.session_state.current_defi
    restant = len(st.session_state.pioche)
    
    st.markdown(f"""
        <div class="card">
            <div class="stade-badge">{d['stade']}</div>
            <h2 style="color: #f39c12;">{d['titre']} {d['icone']}</h2>
            <p style="font-size: 1.2em;">{d['texte']}</p>
            <p style="font-size: 0.7em; color: gray; margin-top: 20px;">Potions restantes : {restant}</p>
        </div>
        """, unsafe_allow_html=True)

    if st.button("PROCHAINE POTION ⚗️"):
        if len(st.session_state.pioche) > 0:
            st.session_state.current_defi = st.session_state.pioche.pop()
            st.rerun()
        else:
            st.session_state.game_over = True
            st.rerun()
