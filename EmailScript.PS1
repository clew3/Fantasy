$SmtpClient = new-object system.net.mail.smtpClient

$MailMessage = New-Object system.net.mail.mailmessage

$SmtpClient.Host = "smtp.gmail.com"

$mailmessage.from = ("calebblew@gmail.com")

$mailmessage.To.add("calebblew@gmail.com")

$mailmessage.Subject = 'Fantasy Hockey'

$mailmessage.Attachments = \weeklyresult.txt

$mailmessage.Body = 'Alert Body with Instruction to recipients'

$smtpclient.Send($mailmessage)