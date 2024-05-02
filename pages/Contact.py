import streamlit as st
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Titre de la page
st.title("Page de Contact")

# Adresse e-mail
st.subheader("Adresse E-mail")
st.write("agitportfolio@gmail.com")

# Lien vers LinkedIn
st.subheader("Profil LinkedIn")
st.markdown("[Lien vers mon profil LinkedIn](https://www.linkedin.com/in/agit-firat-morcicek-397499233/)")

# Formulaire de contact
st.subheader("Formulaire de Contact")
email = st.text_input("Votre adresse e-mail", "")
message = st.text_area("Votre message", "")
submit_button = st.button("Envoyer")

# Fonction d'envoi de courrier électronique
def send_email(email, message):
    sender_email = "agitportfolio@gmail.com"  # Remplacez par votre adresse e-mail
    password = "31072001Juillet"  # Remplacez par votre mot de passe

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = "agitportfolio@gmail.com"  # Adresse e-mail de réception
    msg['Subject'] = "Nouveau message de contact"

    body = message
    msg.attach(MIMEText(body, 'plain'))

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender_email, password)
    text = msg.as_string()
    server.sendmail(sender_email, "agitportfolio@gmail.com", text)
    server.quit()

if submit_button:
    if email and message:
        send_email(email, message)
        st.success("Votre message a été envoyé avec succès !")
    else:
        st.error("Veuillez remplir tous les champs du formulaire.")
