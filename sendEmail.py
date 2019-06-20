import smtplib
con = smtplib.SMTP('smtp.gmail.com',587)
con.ehlo()
con.starttls()
con.login('testtry2321@gmail.com','test12321')
con.sendmail('testtry2321@gmail.com','testtry2321@gmail.com', 'Subject:Python Email send')
con.quit()