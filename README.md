# google-mobility-filtering
### Executing
No Python installation is necessary, you just need to ensure that you have the "dist" folder on your system.

Download by going to the green "Code" button on this page and "Download as ZIP". Unpack the zipped folder onto any system. You will only need the "dist" folder, the rest of the files can be ignored/removed.

Place the CSV inside the "dist" folder and ensure that it is named "Global_Mobility_Report.csv" and then double click google_mobility_filtering.exe.

A new CSV named "Global_Mobility_Report_Filtered.csv" will be created with the filtered fields.


### Installation (only needed if you want to run with pure Python)
Install latest version of [Python](https://www.python.org/downloads/) 

Navigate to the folder of the google-mobility-filtering in command line/terminal

```sh
$ cd "C:\Users\folder-path-to\google-mobility-filtering"
```

Install dependencies from requirement.txt

```sh
$ pip install -r requirements.txt
```

Run the following command to execute script

```sh
$ py google_mobility_filtering.py
```
