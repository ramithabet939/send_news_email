import smtplib, ssl                                                                                                    
                                                                                                                       
def send_email(message):                                                                                                
    host = 'smtp.gmail.com'                                                                                            
    port = 465                                                                                                         
                                                                                                                       
                                                                                                                       
    username = 'YOUR_EMAIL'                                                                                
    password = 'YOUR_GMAIL_PASSWORD'                                                                                      
                                                                                                                       
                                                                                                                       
    receiver = "RECIEVER_EMAIL"                                                                                
    context = ssl.create_default_context()                                                                             
                                                                                                                       
    with smtplib.SMTP_SSL(host, port, context=context) as server:                                                      
        server.login(username, password)                                                                               
        server.sendmail(username, receiver, message)                                                                   
                                                                                                                       
