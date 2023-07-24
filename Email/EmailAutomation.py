import win32com.client as win32

ol = win32.Dispatch('Outlook.application')

newmail=ol.CreateItem(0)
newmail.Subject= "Subject of the email" 
newmail.To= "email@email.com" #email address of MS teams group that would like to be updated
newmail.CC= "cc@email.com" #email that you would like to cc
newmail.Body= 'Message of the email'
attach='C:\\Users\\User\\Pictures\\Saved Pictures\\Test.png' #local path of the file/s that you would like to attach to the email
newmail.Attachments.Add(attach)

newmail.Send()

#note that email automation only works on the old version of outlook so far, the new version doesn't seem to be working