from Services.Send_Email import Send_Email
email = Send_Email()
email.send(email.conect_server())
email.disconect_server(email.conect_server())