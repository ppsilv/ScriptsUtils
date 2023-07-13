import smtplib 

try: 

    #Create your SMTP session 

    smtp = smtplib.SMTP('smtp.gmail.com', 587) 


   #Use TLS to add security 

    smtp.starttls() 


    #User Authentication 

    smtp.login("ppsilv@gmail.com","acme@2018")


    #Defining The Message 

    message = "Eu gosto muito de mim" 


    #Sending the Email

    smtp.sendmail("ppsilv@gmail.com", "ppsilv@gmail.com",message) 


    #Terminating the session 

    smtp.quit() 

    print ("Email sent successfully!") 


except Exception as ex: 

    print("Something went wrong....",ex)
