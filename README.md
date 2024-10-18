[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?style=flat)](https://github.com/ellerbrock/open-source-badges/)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg?logo=github&color=%23F7DF1E)](https://opensource.org/licenses/MIT)
![GitHub last commit](https://img.shields.io/github/last-commit/cakraawijaya/Bot-Inventaris-Tugas-Berbasis-Python?logo=Codeforces&logoColor=white&color=%23F7DF1E)
![Project](https://img.shields.io/badge/Project-Multi-%2DPlatform-light.svg?style=flat&logo=googlechrome&logoColor=white&color=%23F7DF1E)
![Type](https://img.shields.io/badge/Type-Campus%20Assignment-light.svg?style=flat&logo=gitbook&logoColor=white&color=%23F7DF1E)

# Bot-Telegram-Python-Inventaris-Tugas
<strong>2nd Final Project in API Programming</strong><br>

This project is closely related to telegram bots, which themselves have an important role in teaching and learning activities in a classroom. This bot can perform task inventory periodically. This bot is built with the help of a platform called ``` pythonanywhere ```. In this project, the program creator uses ``` python version 3.6 ``` because it is known to have advantages in syntax. The purpose of this project is to help lecturers or teachers in taking inventory of their students' assignments and anticipate errors that might occur, namely forgetting to recap, this is due to the busy messaging activities in a class social media group, in this case telegram.

<br><br>

## Project Requirements
| Part | Description |
| --- | --- |
| Features | Reply Keyboard, Inline Keyboard, Error Handling, Inventory, User Log Activity |
| Platform | Pythonanywhere |
| Library | telebot, datetime |
| Code | Python 3.6 |

<br><br>

## Bot Capabilities
1. There are menu options that can be accessed by clicking or typing.<br><br>
   
2. It can also detect incoming files or documents and notify the sender directly.<br><br>
   
3. Another ability of this bot is that it can provide notification to the bot owner that someone has accessed a certain menu, so that the bot owner can monitor the movements that occur directly.<br><br>
   
4. This bot can address both group users and non-group users.<br><br>
   
5. There is problem control in the system, if the message does not match the command it will be redirected to the ``` /help ``` command.

<br><br>

## Get Started
1. Download this repository and extract it.<br><br>
   
2. Register for a ``` pythonanywhere account ``` :

   <table><tr><td width="810">

   ```
   https://www.pythonanywhere.com/registration/register/beginner/
   ```

   </td></tr></table><br>
   
3. Login to ``` pythonanywhere account ```.<br><br>
   
4. Create a new directory on the ``` pythonanywhere platform ``` by clicking on ``` Files ``` at the top -> Type in the ``` Directories ``` section: ``` KelasApi ``` -> Click ``` New directory ```.<br><br>

5. Then upload ``` Bot-InventarisTugas.py ``` by clicking the ``` Upload a file ``` button.<br><br>

6. Return to the previous page, which is at ``` /home/[pythonanywhere username] ``` -> Click on ``` Open Bash console here ```.<br><br>
  
7. Then type this in the console in rotation:

   <table><tr><td width="810">

   ```python
   mkvirtualenv myvirtualenv --python=/usr/bin/python3
   ```   

   <img width="810" src="Documentation/Bash-1.jpg" alt="bash-1">
   
   </td></tr></table><br>
   <table><tr><td width="810">
      
   ```python
   pip install pytelegrambotapi
   ```

   <img width="810" src="Documentation/Bash-2.jpg" alt="bash-2">

   </td></tr></table><br>
   <table><tr><td width="810">
      
   ```python
   pip install datetime
   ```

   <img width="810" src="Documentation/Bash-3.jpg" alt="bash-3">
   
   </td></tr></table><br>
   <table><tr><td width="810">
      
   ```python
   cd KelasApi
   ```

   <img width="810" src="Documentation/Bash-4.jpg" alt="bash-4">
   
   </td></tr></table><br>
   <table><tr><td width="810">

   ```bash
   python3 Bot-InventarisTugas.py
   ```

   <img width="810" src="Documentation/Bash-5.jpg" alt="bash-5">
   
   </td></tr></table><br>

8. Enjoy [Done].

<br><br>

## Reminder
• Pay attention to writing good and correct syntax because python is case sensitive.

• Make sure your PC/Laptop is connected to the internet.

<br><br>

## Highlights
<table>
<tr>
<th colspan="5">Telegram Bot</th>
<th>Pythonanywhere</th>
</tr>
<tr>
<td width="140"><img height="238" src="Documentation/Telegram Bot View-1.jpg" alt="telegram-bot-1"></td>
<td width="140"><img height="238" src="Documentation/Telegram Bot View-2.jpg" alt="telegram-bot-2"></td>
<td width="140"><img height="238" src="Documentation/Telegram Bot View-3.jpg" alt="telegram-bot-3"></td>
<td width="140"><img height="238" src="Documentation/Telegram Bot View-4.jpg" alt="telegram-bot-4"></td>
<td width="140"><img height="238" src="Documentation/Telegram Bot View-5.jpg" alt="telegram-bot-5"></td>
<td width="140"><img height="235" src="Documentation/Pythonanywhere.jpg" alt="pythonanywhere"></td></td>
</tr>
</table>

<br><br>

## Demonstration of Application
Via Telegram: <a href="http://t.me/inventaristugas_bot">@inventaristugas_bot</a>

<br><br>

## Appreciation
If this work is useful to you, then support this work as a form of appreciation to the author by clicking the ``` ⭐Star ``` button at the top of the repository.

<br><br>

## Disclaimer
This application is my own work and is not the result of plagiarism from other people's research or work, except those related to third party services which include: libraries, frameworks, and so on.

<br><br>

## LICENSE
MIT License - Copyright © 2020 - Devan C. M. Wijaya

Permission is hereby granted without charge to any person obtaining a copy of this software and the software-related documentation files to deal in them without restriction, including without limitation the right to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons receiving the Software to be furnished therewith on the following terms:

The above copyright notice and this permission notice must accompany all copies or substantial portions of the Software.

IN ANY EVENT, THE AUTHOR OR COPYRIGHT HOLDER HEREIN RETAINS FULL OWNERSHIP RIGHTS. THE SOFTWARE IS PROVIDED AS IS, WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESS OR IMPLIED, THEREFORE IF ANY DAMAGE, LOSS, OR OTHERWISE ARISES FROM THE USE OR OTHER DEALINGS IN THE SOFTWARE, THE AUTHOR OR COPYRIGHT HOLDER SHALL NOT BE LIABLE, AS THE USE OF THE SOFTWARE IS NOT COMPELLED AT ALL, SO THE RISK IS YOUR OWN.
