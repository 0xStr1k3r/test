# Task 1     Introduction
#### Welcome to the team, kid. I have something for you to get your feet wet.

#### Our client has a newly hired employee who saw a suspicious-looking janitor exiting his office as he was about to return from lunch.  

I want you to investigate if there was user activity while the user was away **between** **12:05 PM to 12:45 PM on the 19th of November 2022**. If there are, figure out what files were accessed and exfiltrated externally.

You'll be accessing a live system, but use the disk image already exported to the `C:\Users\THM-RFedora\Desktop\kape-results\C` directory for your investigation. The link to the tools that you'll need is in `C:\Users\THM-RFedora\Desktop\tools` 

Finally, I want to remind you that you signed an NDA, so avoid viewing any files classified as top secret. I don't want us to get into trouble.

## Connecting to the machine

Start the virtual machine in split-screen view by clicking on the green "Start Machine" button on the upper right section of this task. If the VM is not visible, use the blue "Show Split View" button at the top-right of the page. Alternatively, you can connect to the VM using the credentials below via "Remote Desktop".



|   |   |
|---|---|
|**Username**|THM-RFedora|
|**Password**|Passw0rd!|
|**IP**|MACHINE_IP|

_**Note:** Once the VM is fully running, please run Registry Explorer immediately, as this tool may take a few minutes to fully start up when executing the program for the first time._

##### Answer the questions below

##### Connect to the machine and continue to the next task
```
No answer needed
```

# Task 2    Windows Forensics review
## Pre-requisites

This room is based on the [Windows Forensics 1](https://tryhackme.com/room/windowsforensics1) and [Windows Forensics 2](https://tryhackme.com/room/windowsforensics2) rooms. A cheat sheet is attached below, which you can also download by clicking on the blue `Download Task Files` button on the right.

# Task 3    Snooping around

Initial investigations reveal that someone accessed the user's computer during the previously specified timeframe.

Whoever this someone is, it is evident they already know what to search for. Hmm. Curious.

##### Answer the questions below

##### What file type was searched for using the search bar in Windows Explorer?
use the tool registry explorer , open the file C:\Users\THM-RFedora\Desktop\kape-results\C\Users\THM-RFedora\NTUSER.DAT 
then go to the folder Software\Microsoft\Windows\CurrentVersion\Explorer\WordWheelQuery

![[Pasted image 20251021113014.png]]
```
.pdf
```
##### What top-secret keyword was searched for using the search bar in Windows Explorer?
same for this one also see the value of the data at the last 
![[Pasted image 20251021113113.png]]
```
continental
```

# Task 4    Can't simply open it
Not surprisingly, they quickly found what they are looking for in a matter of minutes.

Ha! They seem to have hit a snag! They needed something first before they could continue.

_**Note:**  W__hen using the Autopsy Tool, you can speed up the load times by only selecting "Recent Activity" when configuring the Ingest settings._

![Configuring the Ingest setting in Autopsy](https://tryhackme-images.s3.amazonaws.com/user-uploads/63588b5ef586912c7d03c4f0/room-content/fda88f43a1c03a9959249945f061094a.png)

##### Answer the questions below

##### What is the name of the downloaded file to the Downloads folder?
use autopsy to recover the  download history , 
create new case , enter the details , it will create database ,proceed further , while selecting the data source type select the logical files , select the path 
```
 C:\Users\THM-RFedora\Desktop\kape-results\C
```
as the data source 
![[Pasted image 20251021114903.png]]
then 
deselect all in the configure ingest , only select recent activity 
after opening , data artifacts-> web downloads , search for the file according time given in the question  in task-1 
![[Pasted image 20251021120634.png]]
```
7z2201-x64.exe
```

##### When was the file from the previous question downloaded? (YYYY-MM-DD HH:MM:SS UTC)  
It is very simple 
```
2022-11-19 12:09:19 UTC
```

##### Thanks to the previously downloaded file, a PNG file was opened. When was this file opened? (YYYY-MM-DD HH:MM:SS)
use registry explorer , load the hives which we did in the task task-3 , and open the path 
```
Software\Microsoft\Windows\CurrentVersion\Explorer\RecentDocs\.png
```

![[Pasted image 20251021122145.png]]
```
2022-11-19 12:10:21
```

# Task 5    Sending it outside

Uh oh. They've hit the jackpot and are now preparing to exfiltrate data outside the network.

There is no way to do it via USB. So what's their other option?  

##### Answer the questions below

##### A text file was created in the Desktop folder. How many times was this file opened?
the activities are recorded in the file `C:\Users\<username>\AppData\Roaming\Microsoft\Windows\Recent\AutomaticDestinations` 
so open the folder 
```
C:\Users\THM-RFedora\Desktop\kape-results\C\Users\THMRFedora\AppData\Roaming\Microsoft\Windows\Recent\AutomaticDestinations

```
using the tool JLECmd.exe to retrieve the data using command prompt 
```
JLECmd.exe -d "C:\Users\THM-RFedora\Desktop\kape-results\C\Users\THM-RFedora\AppData\Roaming\Microsoft\Windows\Recent\AutomaticDestinations" --csv JLECMD-OUTPUT
```

after running the command i found only one text file on the desktop 
![[Pasted image 20251021124709.png]]
```

```

##### When was the text file from the previous question last modified? (MM/DD/YYYY HH:MM)  
We can see the value in the above screen shot , just change the format according to the requirement
```
11/19/2022 12:12
```

##### The contents of the file were exfiltrated to pastebin.com. What is the generated URL of the exfiltrated data?  
we need to use the autopsy , open the last case that we did previously , go the data artifacts -> webhistory 
check for pastebin.com in the time link **between** **12:05 PM to 12:45 PM on the 19th of November 2022** which is mentioned in the task-1
![[Pasted image 20251021125608.png]]
```
https://pastebin.com/1FQASAav
```
##### What is the string that was copied to the pastebin URL?
which is available from the previous question 
![[Pasted image 20251021130027.png]]
```
ne7AIRhi3PdESy9RnOrN
```

# Task 6    Conclusion
At this point, we already have a good idea of what happened. The malicious threat actor was able to successfully find and exfiltrate data. While we could not determine who this person is, it is clear that they knew what they wanted and how to get it.

I wonder what's so important that they risked accessing the machine in-person... I guess we'll never know.

Anyways, you did good, kid. I guess it was too easy for you, huh?

##### Answer the questions below

##### Let's see if you can handle the next one.
```
No answer needed
```

