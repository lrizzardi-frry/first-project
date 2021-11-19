# -*- coding: utf-8 -*-
# =============================================================================
# Imports
# =============================================================================
import smtplib

ListaEmails = open('./emails.txt')
emails = ListaEmails.read()
print(emails)
for item in emails.split():
  ListaEmails2 = emails[0:].split()
print("\n\n\n\n")
# =============================================================================
# Informações de Login
# =============================================================================
gmail_user = '(email)'
gmail_app_password = '(senha)'
# =============================================================================
# Informações do E-Mail
# =============================================================================
sent_from = gmail_user
sent_to = ListaEmails2
sent_subject = "Email Teste"  # Título do e-mail
sent_body = (u"Gente, finalmente, gra\u00e7as a Deus.\n\n"
             u"Depois de muita a\u00e7\u00e3o\n"
             # https://unicode-table.com/pt/ | Palavras em Unicode, que estão fora da tabela ASCII.
             u"\n"
             u"a API está funcionando corretamente.\n\n"
             u"Atenciosamente,\n"
             u"Lucas, developer da API.\n")  # Corpo do e-mail

email_text = """\
From: %s
To: %s
Subject: %s

%s
""" % (sent_from, ", ".join(sent_to), sent_subject, sent_body)

email_text.encode('utf-8')

print(email_text)
# =============================================================================
# SEND EMAIL OR DIE TRYING!!! | MANDE EMAIL OU MORRA TENTANDO!!!
# Detalhes: http://www.samlogic.net/articles/smtp-commands-reference.htm
# =============================================================================

try:
  server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
  server.ehlo()
  server.login(gmail_user, gmail_app_password)
  server.sendmail(sent_from, sent_to, email_text.encode('utf-8'))
  server.close()

  print('Email enviado!')
except Exception as exception:
  print("Erro: %s!\n\n" % exception)

# Aplicação montada para o envio múltiplo e simultâneo de e-mails cadastrados no arquivo de texto de acordo com a outra aplicação montada em Flask.

# Versão do Python utilizada para o desenvolvimento da aplicação: Python 3.9