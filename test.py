# ------------------------------------------------------------
# Streamlit Notenrechner (1–15 Punkte)
# Deutsches Notenpunktesystem
# Dunkles, schlichtes Design
# ------------------------------------------------------------

import streamlit as st
import random

# ------------------------------------------------------------
# Grundeinstellungen der App
# ------------------------------------------------------------
st.set_page_config(
    page_title="Notenrechner",
    page_icon="📊",
    layout="centered"
)

# ------------------------------------------------------------
# Optionales Dark-Design per CSS (ergänzend zum Streamlit-Theme)
# ------------------------------------------------------------
st.markdown(
    """
    <style>
        body {
            background-color: #0e1117;
            color: #fafafa;
        }
        .stButton>button {
            background-color: #262730;
            color: #fafafa;
            border-radius: 8px;
        }
        .stNumberInput input {
            background-color: #262730;
            color: #fafafa;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# ------------------------------------------------------------
# Session State initialisieren
# ------------------------------------------------------------
if "grades" not in st.session_state:
    st.session_state.grades = []

# ------------------------------------------------------------
# Hilfsfunktionen
# ------------------------------------------------------------
def calculate_average(grades: list[float]) -> float | None:
    """Berechnet den Durchschnitt der Notenpunkte."""
    if not grades:
        return None
    return sum(grades) / len(grades)


def get_fun_fact(avg: float) -> str:
    """Gibt einen motivierenden Hinweis basierend auf dem Durchschnitt zurück."""
    if avg >= 13:
        return "🌟 Starke Leistung! Das ist fast schon Einser-Niveau."
    elif avg >= 10:
        return "💪 Sehr gut! Du bist klar über dem Durchschnitt."
    elif avg >= 7:
        return "🙂 Solide Basis – da ist noch Luft nach oben."
    elif avg >= 5:
        return "📈 Kopf hoch! Mit etwas Übung geht da mehr."
    else:
        return "🚀 Jeder Anfang ist schwer – bleib dran!"

# ------------------------------------------------------------
# UI – Titel & Beschreibung
# ------------------------------------------------------------
st.title("📊 Notenrechner (1–15 Punkte)")
st.write(
    "Gib deine Notenpunkte ein und behalte deinen **aktuellen Durchschnitt** im Blick."
)

# ------------------------------------------------------------
# Eingabebereich
# ------------------------------------------------------------
with st.container():
    col1, col2 = st.columns([3, 1])

    with col1:
        grade_input = st.number_input(
            "Notenpunkte eingeben",
            min_value=1,
            max_value=15,
            step=1
        )

    with col2:
        add_button = st.button("➕ Hinzufügen")

# ------------------------------------------------------------
# Note zur Liste hinzufügen
# ------------------------------------------------------------
if add_button:
    st.session_state.grades.append(grade_input)

# ------------------------------------------------------------
# Anzeige der bisherigen Noten
# ------------------------------------------------------------
st.subheader("📚 Eingetragene Noten")

if st.session_state.grades:
    st.write(", ".join(str(g) for g in st.session_state.grades))
else:
    st.info("Noch keine Noten eingetragen.")

# ------------------------------------------------------------
# Durchschnitt berechnen & anzeigen (live)
# ------------------------------------------------------------
average = calculate_average(st.session_state.grades)

st.subheader("📈 Aktueller Durchschnitt")

if average is not None:
    st.metric(
        label="Durchschnitt (Punkte)",
        value=f"{average:.2f}"
    )

    # Fun Fact / Motivation
    st.success(get_fun_fact(average))
else:
    st.write("—")

# ------------------------------------------------------------
# Footer
# ------------------------------------------------------------
st.divider()
st.caption("✨ Lernfortschritt ist ein Prozess – jede Note zählt!")
