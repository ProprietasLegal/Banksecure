
import streamlit as st
import re

# Liste des principales banques belges avec leurs domaines officiels
trusted_domains = {
    "belfius": "belfius.be",
    "bnpparibasfortis": "bnpparibasfortis.be",
    "ing": "ing.be",
    "kbc": "kbc.be",
    "argenta": "argenta.be",
    "cbc": "cbc.be",
    "axa": "axa.be",
    "keytrade": "keytradebank.be"
}

st.set_page_config(page_title="BankScan", layout="centered")
st.title("🔐 BankScan Belgique")
st.markdown("Vérifiez si un site bancaire est **authentique ou frauduleux**.")

url = st.text_input("Entrez l'URL à vérifier", placeholder="ex: https://www.belfius.be")

def is_suspicious(url):
    if not url:
        return False, "Aucune URL saisie."
    for name, domain in trusted_domains.items():
        if re.search(domain.replace(".", "\."), url):
            if domain in url:
                return False, f"✅ Ce site semble authentique ({domain})"
    return True, "🚨 Ce site semble suspect ou non officiel !"

if st.button("Vérifier"):
    if not url.startswith("http"):
        st.warning("Ajoutez http:// ou https:// devant l’URL.")
    else:
        danger, message = is_suspicious(url)
        if danger:
            st.error(message)
        else:
            st.success(message)
