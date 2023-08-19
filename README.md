# Whatsapp-Blast

Whatsapp Blasting automates sending of messages via Whatsapp Web. The tool can you used to send whatsapp message. Program uses runs through a list of numbers provided in phone.xlsx and then tries to send a prediefined (but templated) message to each number in the list. It can also read other columns from the number xslx to populate template specific words and then send out a personalized message to the number and name.

This current program is limited to sending only TEXT message

# Requirements

*  Python >= 3.6
*  Chrome Driver (your chrome version)

# Setup

1. Install python - >=v3.6
2. Install Chrome Driver as same with your Google Chrome. And move to your repo. In my project I'm using 116 version.If your chrome version is different, this program might be not working. So make sure that your chrome driver and remove my chromedriver first.
3. Run `pip install -r requirements.txt`


# Steps

1. Enter the message you want to send inside `message.txt` file.
2. Filled list of phone number and name in `phone.xlsx` file.
3. Run `python blast_wa.py`.
4. Once the program starts, you'll see the message in message.txt and count of numbers in the numbers.Excel file.
5. After a while, Chrome should pop-up and open web.whatsapp.com.
6. Scan the QR code to login into whatsapp.
7. Press `Enter` to start sending out messages.
8. Enjoy and Watch this program works.

