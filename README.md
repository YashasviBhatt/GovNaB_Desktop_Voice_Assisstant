# GovNaB Desktop Voice Assisstant

## To run this Project please follow these steps

### A. Pre-Requisites
1. Open _command prompt_ or _powershell window_.
2. Type this command<br>`git clone https://github.com/YashasviBhatt/GovNaB_Desktop_Voice_Assisstant`<br>and press enter.
3. Go inside the _Cloned Repository_ folder and open _command-prompt_ or _powershell window_.

### B. Executing the Project
#### Recommended Method
1. Make sure the location where your _terminal_ is open should be inside the _Cloned repository_ Folder.
2. Type<br>`pip install virtualenv`<br>and press enter.
3. Now, type<br>`.\GovNaB\Scripts\activate`<br>and press enter.
    - if you are having Error while _activating virtual environment_ then open _command prompt_ or _powershell window_ as _administrator_.
    - now type<br>`set-executionpolicy remotesigned`<br>press enter and repeat _step 3_.
4. After activating _virtual environment_, the _path_ should look like this<br>```(GovNaB) .\<your-path>\GovNaB_Desktop_Voice_Assisstant```.
5. Run the Project using this<br>`python GovNaB.py`.
6. If you would like to see the _commands_ which works properly then open **workingCommands.csv** file.

#### Alternate Method
In case you don't want to use _virtual environment_ which has all the required _libraries_ installed then follow these steps:<br>
1. Make sure the location where your _terminal_ is open should be inside the _Cloned repository_ Folder.
2. Type<br>`pip install -r requirements.txt`<br> and press enter in either _command_prompt_ or _powershell window_ as _administrator_.
3. Now _install_ **PyAudio** using following commands,
    - `pip install pipwin`
    - `pipwin install pyaudio`
This will install PyAudio in your system.
4. After Installing all the required _libraries_ execute the program<br>`python GovNaB.py`.