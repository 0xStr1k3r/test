# Task 1  Introduction
Incident Scenario  

Our user "Hattori" has reported strange behavior on his computer and realized that some PDF files have been encrypted, including a critical document to the company named `important_document.pdf`. He decided to report it; since it was suspected that some credentials might have been stolen, the `DFIR` team has been involved and has captured some evidence. Join the team to investigate and learn how to get information from a memory dump in a practical scenario.

Learning Objectives  

In this room, we'll cover the following learning objectives.

- Memory Forensics’ basic concepts.  
    
- How to access and set up the environment.
- Gathering information from the compromised target.
- Search for suspicious activity using the information obtained.
- Extracting and analysing data from memory.
- Conclusion & further steps after completing the room.

In this room, we'll learn how to extract essential information and artifacts when performing a memory forensic task in a compromised machine using the Windows OS. First, we'll learn basic memory forensics concepts before setting up our working environment. Next, we'll learn how to get basic information about the compromised target and how to search for suspicious activity. Finally, we will extract interesting data that may help us identify potential malicious actors.

Learning Prerequisites

  An understanding of the following topics is recommended before starting the room:

  - [Analysing Volatile Memory](https://tryhackme.com/r/room/analysingvolatilememory)
- [Volatility](https://tryhackme.com/r/room/volatility)
- [IR Difficulties and Challenges](https://tryhackme.com/r/room/irdifficultiesandchallenges)  
    

Let's begin our task!

##### Answer the questions below

##### Click to complete the task.
```
No answer needed
```

# Task 2   Memory Forensics

Let's now recap some important concepts about memory forensics that may be useful for us while working on the scenario we are presented with.

In cyber security, `memory forensics` is a subset of computer forensics that analyzes volatile memory, usually on a compromised machine; in Windows OS, it corresponds to the Random Access Memory (RAM), and its content is flushed with every reboot or shutdown, making it one of the usual initial task to perform during an incident. The process differs from disk forensics analysis since it not only provides information about what resides on the target computer but also provides us with information about the processes or applications that were running at a particular time and detailed information on the execution flow on a system that may not be present in regular storage units or application logs. 

This memory analysis can help us with an immediate snapshot of an application's or a timestamp of an attacker's actions. This is crucial since evidence collected through memory forensics can become invaluable in creating a chronology of events.   

We can divide the tasks in a Memory forensic task into two main phases: Memory Acquisition and Memory Analysis.

During the memory acquisition phase, we'll copy the live memory to a file, commonly referred to as a dump, to perform the analysis without risking losing the data from an inadvertent reboot on the compromised system and have proof of the analysis inc as needed.

![Descriptive image of memory being copied to disk in the form of a memory dump](https://tryhackme-images.s3.amazonaws.com/user-uploads/66264cef7bba67a6bbbe7179/room-content/66264cef7bba67a6bbbe7179-1718813538019)  

Next, during the memory analysis phase, we'll analyze the obtained memory dump of the forensic data.  

##### Answer the questions below

##### What type of memory is analyzed during a forensic memory task?
```
RAM
```
##### In which phase will you create a memory dump of the target system?
```
Memory Acquisition
```

# Task 3   Environment & Setup

Using the knowledge from our previous task, we can approach the first phase of our memory forensic task, Memory Acquisition, and determine the environment and tools we will use to analyze the memory dump.

Imaging Tools

There are several ways to acquire the memory from the target machine if needed; several tools can help us, but which one to use will depend on personal preference and the OS involved in the imaging task. Some of these tools are:

|   |   |
|---|---|
|Windows|[FTK imager](https://www.exterro.com/digital-forensics-software/ftk-imager), [WinPmem](https://github.com/Velocidex/WinPmem)|
|Linux|[LIME](https://github.com/504ensicsLabs/LiME)|
|macOS|[osxpmem](https://code.google.com/archive/p/pmem/wikis/OSXPmem.wiki)|

In our scenario, FTK Imager was used to take the memory dump of the compromised machine, which was copied to the Linux machine to perform the analysis.

Accessing the Machine

Before moving forward, start the lab by clicking the Start Machine button. It will take around 2 minutes to load properly. The VM will be accessible on the right side of the split screen. In case the VM is not visible, use the blue Show Split View button at the top of the page. You can also connect directly to the machine using the following information via SSH:



|   |   |
|---|---|
|**Username**|analyst|
|**Password**|forensics|
|**IP**|10.10.61.167|

A memory dump named `memdump.mem` will be present at the home address at `/home/analyst`

To analyze the dump, we'll use `Volatility 3`, a popular choice among analysts to inspect a memory during an incident. In this case, the tool has been installed, and an alias was created for simplicity; entering the command `vol` will execute Volatiliy3 in the terminal. The `-h` switch can display the help menu, as shown below.

Volatility3

```shell-session
user@machine$ vol -h
usage: volatility [-h] [-c CONFIG] [--parallelism [{processes,threads,off}]] [-e EXTEND] [-p PLUGIN_DIRS] [-s SYMBOL_DIRS]
                  [-v] [-l LOG] [-o OUTPUT_DIR] [-q] [-r RENDERER] [-f FILE] [--write-config] [--save-config SAVE_CONFIG]
                  [--clear-cache] [--cache-path CACHE_PATH] [--offline] [--single-location SINGLE_LOCATION]
                  [--stackers [STACKERS [STACKERS ...]]]
                  [--single-swap-locations [SINGLE_SWAP_LOCATIONS [SINGLE_SWAP_LOCATIONS ...]]]
```
As we can observe from the above output, Volatility gives us several options to analyze the memory. We can list the plugins specific for each OS since, in our case, we are analyzing a memory dump from Windows; let's list the Windows plugins executing Volatility using the `windows` keyword as an argument to search for Windows plugins with the `--help` switch to list them, as shown below.

Volatility3
           `user@machine$ vol windows --help usage: volatility [-h] [-c CONFIG] [--parallelism [{processes,threads,off}]] [-e EXTEND] [-p PLUGIN_DIRS] [-s SYMBOL_DIRS] [-v] [-l LOG] [-o OUTPUT_DIR] [-q] [-r RENDERER] [-f FILE] [--write-config] [--save-config SAVE_CONFIG] [--clear-cache] [--cache-path CACHE_PATH] [--offline]                   [--single-location SINGLE_LOCATION] [--stackers [STACKERS [STACKERS ...]]] [--single-swap-locations [SINGLE_SWAP_LOCATIONS [SINGLE_SWAP_LOCATIONS ...]]]                   plugin ... volatility: error: argument plugin: plugin windows matches multiple plugins (windows.bigpools.BigPools, windows.cachedump.Cachedump, windows.callbacks.Callbacks, windows.cmdline.CmdLine, windows.crashinfo.Crashinfo, windows.devicetree.DeviceTree, windows.dlllist.DllList, windows.driverirp.DriverIrp, windows.drivermodule.DriverModule, windows.driverscan.DriverScan, windows.dumpfiles.DumpFiles, windows.envars.Envars, windows.filescan.FileScan, windows.getservicesids.GetServiceSIDs, windows.getsids.GetSIDs, windows.handles.Handles, windows.hashdump.Hashdump, windows.info.Info, windows.joblinks.JobLinks, windows.ldrmodules.LdrModules, windows.lsadump.Lsadump, windows.malfind.Malfind, windows.mbrscan.MBRScan, windows.memmap.Memmap, windows.mftscan.ADS, windows.mftscan.MFTScan, windows.modscan.ModScan, windows.modules.Modules, windows.mutantscan.MutantScan, windows.netscan.NetScan, windows.netstat.NetStat, windows.poolscanner.PoolScanner, windows.privileges.Privs, windows.pslist.PsList, windows.psscan.PsScan, windows.pstree.PsTree, windows.registry.certificates.Certificates, windows.registry.hivelist.HiveList, windows.registry.hivescan.HiveScan, windows.registry.printkey.PrintKey, windows.registry.userassist.UserAssist, windows.sessions.Sessions, windows.skeleton_key_check.Skeleton_Key_Check, windows.ssdt.SSDT, windows.statistics.Statistics, windows.strings.Strings, windows.svcscan.SvcScan, windows.symlinkscan.SymlinkScan, windows.vadinfo.VadInfo, windows.vadwalk.VadWalk, windows.vadyarascan.VadYaraScan, windows.verinfo.VerInfo, windows.virtmap.VirtMap)`

Plugins are extremely helpful during the analysis when using Volatility3 since they will quickly parse a memory dump for specific data types and sort the data according to the selected plugin. You can find a summary of some of the most relevant plugins below

|                      |                                                                                     |
| -------------------- | ----------------------------------------------------------------------------------- |
| Windows.cmdline      | Lists process command line arguments                                                |
| windows.drivermodule | Determines if any loaded drivers were hidden by a rootkit                           |
| Windows.filescan     | Scans for file objects present in a particular Windows memory image                 |
| Windows.getsids      | Print the SIDs owning each process                                                  |
| Windows.handles      | Lists process open handles                                                          |
| Windows.info         | Show OS & kernel details of the memory sample being analyzed                        |
| Windows.netscan      | Scans for network objects present in a particular Windows memory image              |
| Widnows.netstat      | Traverses network tracking structures present in a particular Windows memory image. |
| Windows.mftscan      | Scans for Alternate Data Stream                                                     |
| Windows.pslist       | Lists the processes present in a particular Windows memory image                    |
| Windows.pstree       | List processes in a tree based on their parent process ID                           |

Now that we know how to access our environment and which tools we will use, let's move to the next phase, where we'll start analyzing the data.

##### Answer the questions below

##### Which plugin can help us to get information about the OS running on the target machine?
```
Windows.info
```
##### Which tool referenced above can help us take a memory dump on a Linux OS?  
```
LIME
```
##### Which command will display the help menu using Volatility on the target machine?
```
vol -h
```


# Task 4  Gathering Target Information

Obtaining Information  

  Getting information about the target is crucial to our investigation since it ensures we're analyzing the correct context and environment of the evidence. This step helps us understand specific architecture and operating systems, ensuring our findings' accuracy, relevance, and legitimacy.

  We can get information about the target using the `-f` switch to indicate the file to analyze, in this case, `memdump.mem` followed by the plugin `windows.info`  used to get the general information, as in the example shown below.

  Volatility

           `user@machine$ vol -f memdump.mem windows.info Volatility 3 Framework 2.5.2 Progress:  100.00PDB scanning finished                         VariableValue  Kernel Base  0xf9066161c000 DTB   0x1ac000 Symbolsfile:    ///home/analyst/volatility3-2.5.2/volatility3/symbols/windows/ntkrnlmp.pdb/4DBE144182FF4156845CD3BD8B65 4E56-1.json.xz Is64Bit   False IsPAE   False layer_name   0 WindowsIntel32e memory_layer   1 FileLayer KdVersionBlock   0xf8066222a400 Major/Minor   15.19041 MachineType   34404 KeNumberProcessors   2 SystemTime   2024-02-24 22:52:52 NtSystemRoot   C:\Windows NtProductType   NtProductWinNt NtMajorVersion   7 NtMinorVersion   0 PE MajorOperatingSystemVersion   10 PE MinorOperatingSystemVersion   0 PE Machine   34404 PE TimeDateStamp   Sat Jan 13 03:45:32 2085`
        

The output above shows relevant information to identify the machine we are working on, such as architecture, number of processors, and version. All this can help us correlate information and data with other analyses performed on separate hardware of the compromised machine or the network itself while still having proof this is the machine that was compromised.  

  With this taken into consideration, navigate to the `working` directory in the VM and execute the command `vol -f memdump.mem windows.info`  to answer the next questions.

##### Answer the questions below

##### Is the architecture of the machine x64 (64bit) Y/N?
use the command 
```
vol -f memdump.mem windows.info 
```
![[Pasted image 20251021143433.png]]
```
Y
```
##### What is the Verison of the Windows OS  
![[Pasted image 20251021143551.png]]
```
10
```
##### What is the base address of the kernel?
![[Pasted image 20251021143711.png]]
```
0xf8066161b000
```

# Task 5   Searching for Suspicious Activity
Now that we have the information from the target we are working on let's try to identify any suspicious activity in the memory dump. 

Suspicious Activity

Suspicious activity refers to technical anomalies that may be present in a system, such as unexpected processes, unusual network connections, or registry modifications. These activities often signal potential security threats like malware attacks or data breaches.  

Starting the Search

We can start by observing any potential network activity. We can use the plugin `windows.netstat` to see if there's an interesting or unusual connection. At this stage, remote access connections or access to suspicious sites are something to look for.  

Let's navigate to the `/home/analyst` directory and execute the command.

`vol -f memdump.mem windows.netstat`

![The image shows the output of the command highlighting a foreign connection established on port 3389 by 2 local IPs](https://tryhackme-images.s3.amazonaws.com/user-uploads/66264cef7bba67a6bbbe7179/room-content/66264cef7bba67a6bbbe7179-1716994189281)

From the output above, we can observe a connection established on port `3389` from the IP `192.168.182.139` with timestamp `2024-02-24 22:47:52.00` ; this could indicate an attacker's initial access. 

Now that we have information about the network, let's look at the processes. A volatility plugin we can use is windows.pstree, which will display a tree of the process running on the OS.`vol -f memdump.mem windows.pstree`

![The image shows the output of the command highlighting the PID and PPID columns (process ID and Parent Process ID) and highlights services.exe with PID 636 and dlhost.exe that shows a PPID of 636](https://tryhackme-images.s3.amazonaws.com/user-uploads/66264cef7bba67a6bbbe7179/room-content/66264cef7bba67a6bbbe7179-1716994189699)

As we can observe from the above output, the command provides us with information on processes hierarchically running on the system, indicating to us the process and their respective parent process. In this case, `Services.exe` is the parent process of `dllhost.exe`

But how can we identify a suspicious process? One of the most common ways is to check the name of the process; threat actors commonly use names to try to disguise the execution. One of the ways to do this is to check that this process is not usually present. We can find a list of processes commonly used in Windows represented in the image below.

![Image showing a windows process tree with the most common services](https://tryhackme-images.s3.amazonaws.com/user-uploads/66264cef7bba67a6bbbe7179/room-content/66264cef7bba67a6bbbe7179-1718813719752)

Considering the above and looking again at the output, we can observe a process with the truncated name `critical_updat`, as shown below.

![Image displaying the output of the pstree plugin highlighting the parent process critical_update and the child process updater.exe, they can be identified since the parent PID of updater.exe is the PID of critical_update](https://tryhackme-images.s3.amazonaws.com/user-uploads/66264cef7bba67a6bbbe7179/room-content/66264cef7bba67a6bbbe7179-1718997024575)

This process does not look like it is part of the system, and observing in detail, it's the parent process of `updater.exe`, which is also not listed as a process part of the Windows OS.

Great. We identify a possible malicious process and should note the information, like timestamp, PID, PPID, and Memory offset.

##### Answer the questions below

##### Using the plugin "windows.netscan". Can you identify the destination IP address where a connection is established on port 80? 
```
vol -f memdump.mem windows.netscan
```
execute the command and look for the established connections on port 80
![[Pasted image 20251021144523.png]]
```
192.168.182.128
```
##### Using the plugin "windows.netscan," can you identify the program (owner) used to access through port 80?  
we can see the program name in from the previous command 
```
msedge.exe
```
##### Analyzing the processes present on the dump, what is the PID of the child process of critical_updat?
```
vol -f memdump.mem windows.pstree
```
after executing the command look for the process critical_updat , it's child process pid 
![[Pasted image 20251021144957.png]]
```
1612
```
##### What is the time stamp time for the process with the truncated name critical_updat?
It is available from the above question 
```
2024-02-24 22:51:50.000000
```

# Task 6  Finding Interesting Data
With the information we have collected, we can investigate the process `critical_updat`  that we identified in our previous task, which has a child process called `updater`**.** Let's investigate the child process more in-depth. Let's start by looking at where on the disk it was saved; for that, we can use the plugin `windows.filescan` which will allow us to examine the files accessed that are stored in the memory dump. This output is quite big, so to access the data in a better way, we will use the `>` character in bash to redirect the output to a file, in this case, `filescan_out`.

`vol -f memdump.mem windows.filescan > filescan_out`

After executing the command, we can inspect the data by using `cat` and filtering using the `grep` command as shown below.

`cat filescan_out |grep updater`

![The image shows the output of the command cat filescan_out |grep updater, highlighting the path to updater.exe](https://tryhackme-images.s3.amazonaws.com/user-uploads/66264cef7bba67a6bbbe7179/room-content/66264cef7bba67a6bbbe7179-1718810458883)

Above, we can observe that the files have been stored in the Directory `\Users\user01\Documents\updater.exe` or `C:\Users\user01\Documents\updater.exe`

If we want to have more detailed information like when the file was accessed or modified, we can use the plugin `windows.mftscan.MFTScan`, whose output is also quite big, so we will redirect the output to the file `mftscan_out` as shown below.

`vol -f memdump.mem windows.mftscan.MFTScan > mftscan_out`

We can then use the grep command again to parse the file for the appearance of `updater.exe`.

`cat mftscan_out | grep updater`

![The image shows the output of the command cat mftscan_out | grep updater, highlighting the process updater.exe](https://tryhackme-images.s3.amazonaws.com/user-uploads/66264cef7bba67a6bbbe7179/room-content/66264cef7bba67a6bbbe7179-1718810459624)

From the output above, we observe the last four timestamps correspond to the Created, Modified, Updated, and Accessed TimeStamps; we can take notes of those.

Getting the Goods

Let's get information on the process. There are several ways to examine memory, but we will continue using volatility. This time, we will dump the memory region corresponding to `updater.exe` , and examine it.  

 To accomplish the above, we'll use the plugin `windows.memmap`. This time, we'll specify the output dir with the `-o` switch. In this case, we will use the same directory denoted by the character " `.` "and the option `--dump` followed by the option `--pid` and the PID of the process, which in the case of updater.exe is.

`vol -f memdump.mem -o . windows.memmap --dump --pid 1612`

When the command above is finished, we will have a file with an extension `.dmp` in our working directory.

Examining the file is difficult since it contains non-printable characters, so we'll use the strings command to analyze the output better. Since we have the file strings available to us now, we could look for key patterns like `HTTP` or `key` or any pattern that can lead us quickly to an artefact. Another way to scroll the terminal is by using the `strings` command piped to `less` to navigate through the output as shown in the command output below.

`strings pid.1612.dmp |less`

![The image shows the output of the command strings pid.1612.dump |less, highlighting an URL http://key.critical-update.com/encKEY.txt](https://tryhackme-images.s3.amazonaws.com/user-uploads/66264cef7bba67a6bbbe7179/room-content/66264cef7bba67a6bbbe7179-1718811341324)

As we can observe, we immediately identified a possible key and a domain from a URL that the process may have accessed. Also, by scrolling down, we found more indications that this is a malicious process since we can find the `important_document.pdf` filename indicating an interaction with the file.

![The image display the strings output highlighting the document important_document.pdf](https://tryhackme-images.s3.amazonaws.com/user-uploads/66264cef7bba67a6bbbe7179/room-content/66264cef7bba67a6bbbe7179-1718811341816)

Great, we can infer that the process updater.exe accessed the document `important_document.pdf` and accessed a "key" at some point in the URL `http://key.critical-update.com/encKEY.txt` .

If we use the command grep to look for the HTTP request that may be stored in memory, we can do it using -B and -A to look for 10 lines above and below our match to see if we can spot something else.

`strings pid.1612.dmp |grep -B 10 -A 10 "http://key.critical-update.com/encKEY.txt"`

Scrolling up, we can observe the HTTP request, as displayed.

![The image shows the output of the command strings pid.1612.dmp |grep -B 10 -A 10 http://key.critical-update.com/encKEY.txt
highlighting the URL http://key.critical-update.com/encKEY.txt](https://tryhackme-images.s3.amazonaws.com/user-uploads/66264cef7bba67a6bbbe7179/room-content/66264cef7bba67a6bbbe7179-1718811342193)

From the above, we can observe at the end of the HTTP request the content of the file `encKey.txt`, and on the same request, we can observe data with the value `cafebabe`. This could be the key to encrypting the PDF used by the attacker that was not downloaded to disk.

![the image shows the content of the key on the HTTP transaction cafebabe](https://tryhackme-images.s3.amazonaws.com/user-uploads/66264cef7bba67a6bbbe7179/room-content/66264cef7bba67a6bbbe7179-1718811342931)  

Excellent. We collected valuable information from the memory dump, including the possible key used to encrypt the documents.

##### Answer the questions below

##### Analyzing the "windows.filescan" output, what is the full path and name for critical_updat?
use the command `vol -f memdump.mem windows.filescan` > filescan , the use grep to filter `cat filescan | grep critical_updat
![[Pasted image 20251021151046.png]]
`
```
C:\Users\user01\Documents\critical_update.exe
```
##### Analyzing the "windows.mftscan.MFTScan" what is the Timestamp for the created date of important_document.pdf?  
use the command `vol -f memdump.mem windows.mftscan.MFTScan > mftscan` to get the data about the ADS , the filter the output
![[Pasted image 20251021151504.png]]
```
2024-02-24 20:39:42.000000 
```
##### Analyzing the updater.exe memory output, can you observe the HTTP request and determine the server used by the attacker?
first dump the memory related to the malicious process of pid 1612 with the command  `vol -f memdump.mem -o . windows.memmap --dump --pid 1612` after use strings , filter the output using grep   `strings pid.1612.dmp | grep -i http `
![[Pasted image 20251021151913.png]]
```
SimpleHTTP/0.6 Python/3.10.4
```

# Task 7   Conclusion & Wrapping Up
Conclusion
In this scenario, we have put into practice the skills necessary to start digging into the world of memory forensics and practice with a tool like volatility, which is widely used among digital forensics professionals.  
We learned how to gather information about the machine the dump belongs to, search for connections, enumerate and investigate processes, and examine the content for malicious patterns in a memory dump.

  While all the information presented in his room can be used in real-life scenarios, it is possible to delve more deeply into the topic by examining more complex attacks. Some interesting material to get more into it can be the following:

- [Windows Forensics 2](https://tryhackme.com/r/room/windowsforensics2)
- [Linux Forensics](https://tryhackme.com/r/room/linuxforensics)
- [iOS Forensics](https://tryhackme.com/r/room/iosforensics)
- [Windows Applications Forensics](https://tryhackme.com/r/room/windowsapplications)

##### Answer the questions below
##### Click to complete the room.
```
No answer needed
```
